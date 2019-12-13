import json
import os
from datetime import datetime, timedelta
from schedule_recording_program import argparser

def schedule_recording_app():
    imported_args = argparser.args


    task_name_convert_to_json = f"{''.join(imported_args.task_name)}.json"
    split_day_and_month_ = "".join(imported_args.day_and_month)

    if task_name_convert_to_json in os.listdir("../schedule_recording_program"):
        print(f"{task_name_convert_to_json}: already exists")
    else:

        try:
            convert_day_and_month = datetime.strptime(split_day_and_month_, "%d.%m").strftime("%d.%m")


        except ValueError:

            if split_day_and_month_ == "tomorrow":
                scheduled_to_tomorrow = (datetime.today() + timedelta(days=1)).strftime("%d.%m")

                with open(task_name_convert_to_json, "w") as file:
                    json.dump({''.join(imported_args.task_name): f"Scheduled to {scheduled_to_tomorrow}"}, file,
                        sort_keys=True, separators=(",", ": "), indent=4, ensure_ascii=False)

            elif split_day_and_month_ == "day_after_tomorrow":
                scheduled_to_day_after_tomorrow = (datetime.today() + timedelta(days=2)).strftime("%d.%m")

                with open(task_name_convert_to_json, "w") as file:

                    json.dump({''.join(imported_args.task_name): f"Scheduled to {scheduled_to_day_after_tomorrow}"},
                        file, sort_keys=True, separators=(",", ": "), indent=4, ensure_ascii=False)

            else:
                with open(task_name_convert_to_json, "w") as file:

                    json.dump({''.join(imported_args.task_name): f"Scheduled to {convert_day_and_month}"},
                        file, sort_keys=True, separators=(",", ": "), indent=4, ensure_ascii=False)

