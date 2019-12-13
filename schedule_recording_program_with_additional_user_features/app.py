''''''
'''
Вторая программа: выдает 5 следующих дел и 5 последних, которые прошли. Считается относительно текущей даты. Так же 
чтобы можно было в консоли параметром ввести на какой день считать вместо сегодняшнего.


Что тебе понадобится
1. Вынести общий код в отдельный модуль
2. Разобраться как будешь сохранять данные (json или sqlite на выбор)
3. Разобраться с аргументами командной строки (модуль Argparse)
4. Разобраться с модулем datetime.

Усложнения:
1. Использовать sqlite или json опрделеяется настройками программы 
2. Сделать UI (веб или десктоп), работающий с тем же хранилищем

'''

import json
import os
from schedule_recording_program import argparser
from datetime import datetime, timedelta

def schedule_recording_program():
    import_arg_parser = argparser.args.task_name

    task_name_convert_to_json = f"{''.join(import_arg_parser)}.json"
    split_day_and_month_ = "".join(import_arg_parser)

    if task_name_convert_to_json in os.listdir("../schedule_recording_program"):
        print(f"{task_name_convert_to_json}: already exists")
    else:

        try:
            convert_day_and_month = datetime.strptime(split_day_and_month_, "%d.%m").strftime("%d.%m")


        except ValueError :

            if split_day_and_month_ == "tomorrow":
                scheduled_to_tomorrow = (datetime.today() + timedelta(days=1)).strftime("%d.%m")

                with open(task_name_convert_to_json, "w") as file:
                    json.dump({''.join(import_arg_parser): f"Scheduled to {scheduled_to_tomorrow}"}, file,
                        sort_keys=True, separators=(",", ": "), indent=4, ensure_ascii=False)

            elif split_day_and_month_ == "day_after_tomorrow":
                scheduled_to_day_after_tomorrow = (datetime.today() + timedelta(days=2)).strftime("%d.%m")

                with open(task_name_convert_to_json, "w") as file:

                    json.dump({''.join(import_arg_parser): f"Scheduled to {scheduled_to_day_after_tomorrow}"}
                        , file, sort_keys=True, separators=(",", ": "), indent=4, ensure_ascii=False)

        else:
            with open(task_name_convert_to_json, "w") as file:

                json.dump({''.join(import_arg_parser): f"Scheduled to {convert_day_and_month}"}, file,
                    sort_keys=True, separators=(",", ": "), indent=4, ensure_ascii=False)
