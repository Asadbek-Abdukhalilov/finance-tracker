print("Добро пожаловать в финансовый трекер!")

history=[]
balance=0
total_income = 0
total_expense = 0

try:
    with open("finance.txt", "r", encoding="utf-8") as file:
        for line in file:
            line=line.strip()
            if line:
                history.append(line)
except FileNotFoundError:
    pass

while True:
    print("1. Добавить доход")
    print("2. Добавить расход")
    print("3. Показать баланс")
    print("4. Показать историю")
    print("5. Выйти")
    print("6. Статистика")
    choice=input("Виберите действие")


    match choice:
        
        case "1":
            amount = int(input("Введите сумму дохода: "))
            balance = balance + amount
            total_income = total_income + amount
            kat = input("Введите категорию дохода: ")
            history.append(f"Доход: +{amount} категория {kat}")
            print("Доход добавлен!")

        case "2":
            amount2 = int(input("Введите сумму расхода: "))
            if amount2 > balance:
                print("Недостаточно средств!")
            else:
                kat2 = input("Введите категорию расхода: ")
                balance = balance - amount2
                total_expense = total_expense + amount2
                history.append(f"Расход: -{amount2} Категория {kat2}")
                print("Расход добавлен!")

        case "3":
            print(f"Ваш баланс: {balance}")

        case "4":
            if history:
                for record in history:
                    print(record)
            else:
                print("История пуста")

        case "5":
            print("До свидания!")
            with open("finance.txt", "w", encoding="utf-8") as file:
                for record in history:
                    file.write(record + "\n")
            break
             
        case "6":
             print("===Cтатистика===")
             print(f"Доход: {total_income}")
             print(f"Расход: {total_expense}") 
             print(f"Количество операций: {len(history)}")
        case  _:
             print("Неверный выбор, попробуйте снова.")