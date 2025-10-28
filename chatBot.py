def chat_bot():
    print("Сәлем! Мен қарапайым чат-ботпын. Маған сұрақ қой немесе '/exit' не 'шығу' деп жазып, шығуға болады.")

    while True:
        user_input = input("Сіз: ").lower()  

        if user_input in ["/exit", "шығу"]:
            print("Бот: Сау болыңыз!")
            break

        elif "сәлем" in user_input or "салем" in user_input:
            print("Бот: Сәлеметсіз бе! Қалыңыз қалай?")
        elif "қалың қалай" in user_input or "қал қалай" in user_input:
            print("Бот: Жақсы, рахмет! Өзіміз ше?")
        elif "не істеп жатырсың" in user_input:
            print("Бот: Мен сізбен сөйлесіп отырмын 🙂")
        elif "рахмет" in user_input:
            print("Бот: Әрқашан дайынмын!")
        else:
            print("Бот: Кешіріңіз, мен бұл сұраққа жауап бере алмаймын.")

chat_bot()
