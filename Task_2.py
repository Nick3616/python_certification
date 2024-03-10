import argparse
import logging

logging.basicConfig(filename='example.log', filemode='w', encoding='utf-8',
                    format='{levelname} - {asctime} в строке {lineno} '
                           'функция "{funcName}()" : {msg}', style='{', level=logging.WARNING)

def func(a, b):
    try:
        res = a / b
    except ZeroDivisionError:
        logging.warning('Нельзя делить на ноль')
        return
    else:
        return res

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Программа деления двух чисел.")
    parser.add_argument("num1", type=float)
    parser.add_argument("num2", type=float)

    args = parser.parse_args()

    result = func(args.num1, args.num2)

    if result is not None:
        print(f"Результат: {result}")
    else:
        print("Деление не выполнено.")
# Пример ввода python Task_2.py 6 3