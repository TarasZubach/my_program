from datetime import date, datetime
import os

def scheduled_date_file_recording():
    task_name = input("Введите задание: ")
    day_month_original = input("Введите планируемое время в виде день.месяц:")

    # Do I convert keyboard input to a file with the extension txt
    day_month_conversion_to_txt = f"{task_name}.txt"

    convert_to_num = day_month_original.split(".")

    if day_month_conversion_to_txt in os.listdir("../st_app"):
        print("This name of file are used")

    for file_name in convert_to_num:
        if file_name.isdigit():
            # I check if there is such a file in the directory
            if day_month_conversion_to_txt not in os.listdir("../st_app"):
                # Here I take only the data I need, that is, the date and month, remove the rest with a slice, and then
                # replace the hyphen with a period.
                day_month_second_version = str(datetime.strptime(day_month_original, "%d.%m"))[5:10].replace("-", ".")

                # I’m doing practically the same thing here
                today = str(datetime.strptime(f"{date.today().month}.{date.today().day}", "%d.%m"))[5:10].replace(
                "-", ".")

                with open(day_month_conversion_to_txt, "w") as file:
                    file.write(f"Scheduled from {today} to {day_month_second_version}")


        elif file_name.isalpha():
            if file_name == "завтра":
                if day_month_conversion_to_txt not in os.listdir("../st_app"):

                    today = str(datetime.strptime(f"{date.today().month}.{date.today().day}", "%d.%m"))[5:10].replace(
                    "-", ".")

                    with open(day_month_conversion_to_txt, 'w') as file:
                    # Here I do almost the same thing as above, but add + 1 day, based on the fact that i need the next
                    # day in the task, that is, tomorrow.
                        file.write(f"Scheduled on {today.replace(today[1:2], str(int(today[1:2]) + 1))}")

            elif file_name == "послезавтра":
                if day_month_conversion_to_txt not in os.listdir("../st_app"):

                    today = str(datetime.strptime(f"{date.today().month}.{date.today().day}", "%d.%m"))[5:10].replace(
                    "-", ".")

                    with open(day_month_conversion_to_txt, "w") as file:
                    # Then I do almost the same thing as above, but add + 2 day, based on the fact that I need the next day
                    #  in the task, that is, the day after tomorrow.
                        file.write(f"Scheduled on {today.replace(today[1:2], str(int(today[1:2]) + 2))}")

print(scheduled_date_file_recording())