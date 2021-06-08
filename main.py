import datetime
year = datetime.datetime.now().year
month = datetime.datetime.now().month
dt = datetime.datetime.now().day

by = str(input("When were you born (year): "))
bm = str(input("Which month were you born (in number): "))
bd = str(input("Which date were you born (number): "))

age = int(year) - int(by)
age2 = int(month) - int(bm)
if int(bm) > int(month):
  age2 = int(bm) - int(month)
age3 = int(dt) - int(bd)
if int(bd) > int(dt):
  age3 = int(bd) - int(dt)

print("So, now you're " + str(age) + " years, " + str(age2) + " months and " + str(age3) + " days old!")