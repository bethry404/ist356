import datetime as dt


date_string = "9/8/2026"
print(dt.datetime.strptime(date_string, "%m/%d/%Y").strftime("%Y-%m-%d"))

