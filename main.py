from datetime import datetime
time = datetime.now()
print(time)
print(datetime.utcnow())
format = "%Y-%m-%dT%H:%M:%S.%f"
print(datetime.strptime((time).strftime(format), format))
