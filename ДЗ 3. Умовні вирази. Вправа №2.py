a = input ("введіть строку \n")
while True:
    if "привіт" in a.lower() or "хай" in a.lower() or "доброго дня" in a.lower():
        print('Доброго вечора, я бот з України!')
        a = input("введіть строку \n")
    elif "як справи?" in a.lower() or "що робиш?" in a.lower() or "чим займаєшся?" in a.lower():
        print('Вчусь програмувати на Python!')
        a = input("введіть строку \n")
    elif "фільм" in a.lower() or "кінотеатр" in a.lower() or "серіал" in a.lower():
        print("Соррі що втручуюсь, не знаю про що йдеться мова, але подивіться фільм 'тринадцять життів', він просто бомба!")
        a = input("введіть строку \n")
    elif "бувай" in a.lower() or "надобраніч" in a.lower() or "гудбай" in a.lower():
        print ("Побачимось у мережі, I'll be back.")
        break
    else:
        print("Дуже цікаво, але, нажаль, ніфіга не зрозуміло :(" )
        a = input("введіть строку \n")