from _datetime import datetime

value = []
_value = []
flag = True

while True:
    defolt_value = 0
    if flag == True:
        d = input("ввод1 ")
    if len(d) > 3:
        _value.append(d)
    c = input("znach ")
    if len(c) < 3:
        defolt_value = c
        value.append((_value[0], defolt_value))
        flag = True
    else:
        value.append((_value[0], defolt_value))
        d = c
        flag = False


    _value.clear()

    print(value)

    # if len(_value) != 0:
    #     value.append((_value[-1], defolt_value))
    #     _value.clear()
    # if len(d) > 3:
    #     _value.append(d)
    # elif len(d) < 3:
    #     value.append((_value[-1], d))

    # if len(c) > 3:
    #     value.append(f"дк № {c}, значение {defolt_value}, время {datetime.now()}\n")
    #
    # else:
    #     value.append(f"дк № {d}, значение {c}, время {datetime.now()}\n")
