import io, os, json
from datetime import date, datetime

def scheduled_date_file_recording():
    task_name = input("Введите задание: ")
    day_month_original = input("Введите планируемое время в виде день.месяц(просьба прописать через точку):")

    # Do I convert keyboard input to a file with the extension txt
    task_name_conversion_to_json = f"{task_name}.json"

    # I broke the date and month into separate elements so that you can work with them
    day_month_original_conversion_to_num = day_month_original.split('.')

    count_days_and_month = 0

    for day_and_month in day_month_original_conversion_to_num:
        try:
            day_and_month = int(day_and_month)
        except ValueError:
            pass
        if isinstance(day_and_month, int):
            count_days_and_month += 1

    if task_name_conversion_to_json in os.listdir("../schedule_recording_program"):
        print("This name of file are used")

    if count_days_and_month > 0:
            # I check if there is such a file in the directory
        if task_name_conversion_to_json not in os.listdir("../schedule_recording_program"):
            # Here I take only the data I need, that is, the date and month, remove the rest with a slice, and then
            # replace the hyphen with a period.
            day_month_second_version = str(datetime.strptime(day_month_original, "%d.%m"))[5:10].replace("-", ".")

            # I’m doing practically the same thing here
            today = str(datetime.strptime(f"{date.today().month}.{date.today().day}", "%d.%m"))[5:10].replace(
            "-", ".")

            with io.open(task_name_conversion_to_json, "w", encoding='utf8') as file:
                #file.write(f"Scheduled from {today} to {day_month_second_version}")
                file.write(json.dumps({task_name: f"Scheduled from {today} to {day_month_second_version}"}, sort_keys=True,
                           separators=(",", ": "), indent=4, ensure_ascii=False))


    elif count_days_and_month == 0:
        if day_month_original == "завтра":
            if task_name_conversion_to_json not in os.listdir("../schedule_recording_program"):

                today = str(datetime.strptime(f"{date.today().month}.{date.today().day}", "%d.%m"))[5:10].replace(
                "-", ".")

                with io.open(task_name_conversion_to_json, "w", encoding="utf8") as file:
                # Here I do almost the same thing as above, but add + 1 day, based on the fact that i need the next
                # day in the task, that is, tomorrow.
                    file.write(json.dumps({task_name : f"Scheduled on {today.replace(today[1:2], str(int(today[1:2]) + 1))}"},
                    sort_keys=True, separators=(",", ": "), indent=4, ensure_ascii=False))


        elif task_name == "послезавтра":

            if task_name_conversion_to_json not in os.listdir("../schedule_recording_program"):

                today = str(datetime.strptime(f"{date.today().month}.{date.today().day}", "%d.%m"))[5:10].replace(
                "-", ".")

                with io.open(task_name_conversion_to_json, "w", encoding="utf8") as file:
                # Then I do almost the same thing as above, but add + 2 day, based on the fact that I need the next day
                #  in the task, that is, the day after tomorrow.
                    file.write(json.dumps({task_name : f"Scheduled on {today.replace(today[1:2], str(int(today[1:2]) + 2))}"},
                    sort_keys = True, separators=(",", ": "), indent=4, ensure_ascii=False))

print(scheduled_date_file_recording())