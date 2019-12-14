import argparse

def func_argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-task", "--task_name", nargs=1, help="Введите задание: ")
    parser.add_argument("-day_and_month", "--day_and_month", nargs=1, help="Введите дату и месяц черезе точку: ")
    args = parser.parse_args()
    return args

