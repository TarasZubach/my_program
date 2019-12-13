import json
import argparse
import os
from datetime import datetime, timedelta

parser = argparse.ArgumentParser()
parser.add_argument("-task", "--task_name", nargs=1, help="Введите задание: ")
parser.add_argument("-day_and_month", "--day_and_month", nargs=1, help="Введите дату и месяц черезе точку: ")
args = parser.parse_args()

task_name_convert_to_json = f"{''.join(args.task_name)}.json"
split_day_and_month_ = "".join(args.day_and_month)

if task_name_convert_to_json in os.listdir("../schedule_recording_program"):
    print(f"{task_name_convert_to_json}: already exists")
else:

    try:
        convert_day_and_month = datetime.strptime(split_day_and_month_, "%d.%m").strftime("%d.%m")


    except ValueError as value_error:

        if split_day_and_month_ == "tomorrow":
            scheduled_to_tomorrow = (datetime.today() + timedelta(days=1)).strftime("%d.%m")

            with open(task_name_convert_to_json, "w") as file:
                file.write(json.dumps({''.join(args.task_name): f"Scheduled to {scheduled_to_tomorrow}"},
                                      sort_keys=True, separators=(",", ": "), indent=4, ensure_ascii=False))

        elif split_day_and_month_ == "day_after_tomorrow":
            scheduled_to_day_after_tomorrow = (datetime.today() + timedelta(days=2)).strftime("%d.%m")

            with open(task_name_convert_to_json, "w") as file:

                file.write(json.dumps({''.join(args.task_name): f"Scheduled to {scheduled_to_day_after_tomorrow}"},
                                      sort_keys=True, separators=(",", ": "), indent=4, ensure_ascii=False))

    else:
        with open(task_name_convert_to_json, "w") as file:

            file.write(json.dumps({''.join(args.task_name): f"Scheduled to {split_day_and_month_}"},
                                  sort_keys=True, separators=(",", ": "), indent=4, ensure_ascii=False))