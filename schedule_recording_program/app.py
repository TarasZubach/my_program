import json
import os
from schedule_recording_program import argparser
from datetime import datetime, timedelta

import_argparser_args = argparser.args


task_name_convert_to_json = f"{''.join(import_argparser_args.task_name)}.json"
split_day_and_month_ = "".join(import_argparser_args.day_and_month)

if task_name_convert_to_json in os.listdir("../schedule_recording_program"):
    print(f"{task_name_convert_to_json}: already exists")
else:

    try:
        convert_day_and_month = datetime.strptime(split_day_and_month_, "%d.%m").strftime("%d.%m")


    except ValueError as value_error:

        if split_day_and_month_ == "tomorrow":
            scheduled_to_tomorrow = (datetime.today() + timedelta(days=1)).strftime("%d.%m")

            with open(task_name_convert_to_json, "w") as file:
                json.dump({''.join(import_argparser_args.task_name): f"Scheduled to {scheduled_to_tomorrow}"}, file,
                                      sort_keys=True, separators=(",", ": "), indent=4, ensure_ascii=False)

        elif split_day_and_month_ == "day_after_tomorrow":
            scheduled_to_day_after_tomorrow = (datetime.today() + timedelta(days=2)).strftime("%d.%m")

            with open(task_name_convert_to_json, "w") as file:

                json.dump({''.join(import_argparser_args.task_name): f"Scheduled to {scheduled_to_day_after_tomorrow}"},
                    file, sort_keys=True, separators=(",", ": "), indent=4, ensure_ascii=False)

    else:
        with open(task_name_convert_to_json, "w") as file:

            json.dump({''.join(import_argparser_args.task_name): f"Scheduled to {split_day_and_month_}"},
                file, sort_keys=True, separators=(",", ": "), indent=4, ensure_ascii=False)