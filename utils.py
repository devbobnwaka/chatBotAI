from datetime import datetime

def formatted_time(time_str):
    timestamp = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S.%f")
    return timestamp.strftime("%Y-%m-%d %I:%M %p")


# time_str = "2023-11-27 14:17:02.59700"
# t = formatted_time(time_str)
# print(t)