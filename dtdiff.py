#!/usr/bin/env python3

import datetime as dt
import argparse

def datediff(first: str|None = None, second: str|None = None) -> str:
    today = dt.datetime.now()
    try:
        if first is None:
            return f'{today.strftime("%d.%m.%Y")}'
        elif first == 'today':
            first = today
        elif first.isdigit():
            result = today + dt.timedelta(days=int(first))
            return result.strftime('%d.%m.%Y')
        else:
            if len(first.split('.')) == 2:
                first += '.' + str(today.year)
            first = dt.datetime.strptime(first, '%d.%m.%Y')

        if second is None:
            diff = (first - today).days + 1
            return show_days(diff)
        elif second == 'today':
            second = today
        elif second.isdigit():
            result = first + dt.timedelta(days=int(second))
            return result.strftime('%d.%m.%Y')
        else:
            if len(second.split('.')) == 2:
                second += '.' + str(today.year)
            second = dt.datetime.strptime(second, '%d.%m.%Y')
    except (TypeError, ValueError):
        return (
            'Неправильний формат. Використовуйте: '
            'DD.MM, DD.MM.YYYY, "today" або число (дні).'
        )
    if first == 'today' or second == 'today':
        diff = (second - first).days + 1
    else:
        diff = (second - first).days
    return show_days(diff)

def show_days(diff: int) -> str:
    if 11 <= diff % 100 <= 14:
        return f'{diff} днів'
    elif diff % 10 == 1:
        return f'{diff} день'
    elif 2 <= diff % 10 <= 4:
        return f'{diff} дні'
    else:
        return f'{diff} днів'

def arg_parser():
    parser = argparse.ArgumentParser(description='Обчислення різниці між двома датами або обчислення дати, що настає через певну кількість днів.')
    parser.add_argument('dates',
                        type=str,
                        nargs='*',
                        help='Дата у форматі DD.MM або DD.MM.YYYY, "today", або кількість днів (ціле число).')
    return parser.parse_args()

if __name__ == '__main__':
    try:
        args = arg_parser()
        if len (args.dates) == 0:
            print(datediff())
        elif len(args.dates) == 1:
            print(datediff(args.dates[0]))
        elif len(args.dates) == 2:
            print(datediff(args.dates[0], args.dates[1]))
        else:
            print('Забагато аргументів. Вкажіть не більше двох аргументів.')
    except Exception as e:
        print(f'Виникла помилка: {e}')
