from LoadInterface import strings
from dispatcher import dp, bot
from DBrequests import *
from States import States


from aiogram.dispatcher import FSMContext

def register_handlers():
    @dp.message_handler(commands = ['start'])
    async def hello(message):

        await bot.send_message(message.chat.id, strings["Hello"])
        await States.MenuState.set()
    @dp.message_handler(state=States.MenuState)
    async def Menu(message, state: FSMContext):

        already_register = await check_existing_user(message.from_user.id)

        match(message.text):
            case '/register':

                if (already_register == False):
                    await States.RegisterState.set()
                    await bot.send_message(message.chat.id, "Введите своё имя:")
                else:
                    await bot.send_message(message.chat.id, "Вы уже зарегистрированы!")

            case '/enter_scores':
                if already_register:
                    await States.WritingResultState.set()
                    await bot.send_message(message.chat.id, "Введите предмет, результаты которого вы хотите записать:")
                else:
                    await bot.send_message(message.chat.id, "Для того, чтобы записать ответы, нужно зарегистрироваться")

            case '/view_scores':
                if already_register:
                    results = await view_scores(message.from_user.id)
                    if results == "": results = "Вы еще не записывали результаты. Запишите их сейчас!"
                    await bot.send_message(message.chat.id, results)
                else:
                    await bot.send_message(message.chat.id, "Для того, чтобы посмотреть ответы, нужно зарегистрироваться.")



    @dp.message_handler(state=States.RegisterState)
    async def register(message, state: FSMContext):
        data = await state.get_data()
        if len(data.items()) == 0:
            await state.update_data(FirstName = message.text)
            await bot.send_message(message.chat.id, "Введите фамилию:")
        else:
            FirstName = data['FirstName']
            SecondName = message.text
            await insert_user(message.from_user.id, FirstName, SecondName)
            await state.reset_data()
            await States.MenuState.set()
            await bot.send_message(message.chat.id, "Вы зарегистрированы! Теперь вы можете записать ваши результаты ЕГЭ")


    @dp.message_handler(state = States.WritingResultState)
    async def enter_scores(message, state: FSMContext):
        data = await state.get_data()
        if len(data.items()) == 0:
            await state.update_data(subject = message.text)
            await bot.send_message(message.chat.id, "Введите балл по этому предмету")
        else:
            if message.text.isdigit():
                score = int(message.text)
                if score < 0 or score > 100:
                    bot.send_message(message.chat.id, "Результат должен быть от 0 до 100.")
                    return

                subject = data.get('subject')
                await insert_score(message.from_user.id, subject, score)
                await state.reset_data()
                await States.MenuState.set()
                await bot.send_message(message.chat.id, "Результат записан!")
            else:
                States.MenuState.set()
                await bot.send_message(message.chat.id, "Результат не записан. Значение балла должно быть корректным")


    async def view_scores(telegramId: int) -> str:
        subjects = await select_score_by_ID(telegramId)
        res = ""
        for subject in subjects:
            res += subject.get('subject') + ": " + str(subject.get('score')) + "\n"
        return res



