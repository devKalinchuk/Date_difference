#!/usr/bin/env python3

import datetime as dt
import argparse

TODAY = dt.date.today()


def parse_date(date_str: str) -> dt.date | int:
    """Перетворює вхідний рядок на дату або число - кількість днів"""
    if date_str.isdigit() or (date_str.startswith('-') and date_str[1:].isdigit()):
        return int(date_str)
    elif '.' in date_str:
        if len(date_str.split('.')) == 2:
            date_str += '.' + str(TODAY.year)
            return dt.datetime.strptime(date_str, '%d.%m.%Y').date()
        elif len(date_str.split('.')) == 3:
            return dt.datetime.strptime(date_str, '%d.%m.%Y').date()
        else:
            raise ValueError('Неправильний формат дати. Використовуйте: DD.MM або DD.MM.YYYY')
    else:
        raise ValueError('Неправильний формат. Використовуйте: '
        'DD.MM, DD.MM.YYYY або число (кількість днів).')


def parse_arguments(argv: list):
    """Парсить аргументи командного рядка"""
    if len(argv) == 2:
        return parse_date(argv[0]), parse_date(argv[1])
    elif len(argv) == 1:
        return TODAY, parse_date(argv[0])
    else:
        raise ValueError('Некоректна кількість аргументів')


def date_difference(date1: dt.date, date2: dt.date) -> str:
    """Обчислює різницю в днях між двома датами"""
    difference = (date2 - date1).days
    return show_days(difference)


def add_days(date: dt.date, days: int) -> dt.date:
    """Додає певну кількість днів до дати"""
    return date + dt.timedelta(days=days)


def show_days(diff: int) -> str:
    """Повертає рядок з правильною формою слова 'день'"""
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


def main(first, second):
    if isinstance(second, int):
        result_date = add_days(first, second)
        return f'{result_date.strftime('%d.%m.%Y')}'
    else:
        diff = date_difference(first, second)
        return diff

if __name__ == '__main__':
    try:
        args = arg_parser()
        first, second = parse_arguments(args.dates)
        print(main(first, second))
    except Exception as e:
        print(f'Виникла помилка: {e}')
