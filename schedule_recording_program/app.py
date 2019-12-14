import json
import os
import argparser
from datetime import datetime, timedelta

def write_json_file (func_arg):
    imported_function_argument = argparser.func_argparser()
    task_name_convert_to_json = f"{''.join(imported_function_argument.task_name)}.json"

    if task_name_convert_to_json in os.listdir("../schedule_recording_program"):
        print(f"{task_name_convert_to_json}: already exists")
    else:
        with open(task_name_convert_to_json, "w") as file:
            json.dump({''.join(imported_function_argument.task_name): f"Scheduled to {func_arg}"}, file,
            sort_keys=True, indent=4, ensure_ascii=False)


def schedule_recording_app():
    imported_args = argparser.func_argparser()
    split_day_and_month = "".join(imported_args.day_and_month)

    try:
        convert_day_and_month = datetime.strptime(split_day_and_month, "%d.%m").strftime("%d.%m")

    except ValueError:

        scheduled_date = ''

        if split_day_and_month == "tomorrow":
            scheduled_date = (datetime.today() + timedelta(days=1)).strftime("%d.%m")


        elif split_day_and_month == "day_after_tomorrow":
            scheduled_date = (datetime.today() + timedelta(days=2)).strftime("%d.%m")

        write_json_file(scheduled_date)

    else:

        write_json_file(convert_day_and_month)

if __name__ == "__main__":
    schedule_recording_app()