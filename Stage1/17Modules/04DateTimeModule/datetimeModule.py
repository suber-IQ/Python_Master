# 👉  Datetime Module of Python

# 🎏 He method is called strftime(),takes one parameter,format, to specify the format of the returned string:
# 🎏 %b :- Month name, short version  (Dec)
# 🎏 %B :-  Month name, Full version  (December)
# 🎏 %m :-  Month as a number 01-12  (12)
# 🎏 %y :-  Year, short version, without century (18) 
# 🎏 %Y :- Year, full version  (2018) 
# 🎏 %H :- Hour 00-23 (17) 
# 🎏 %I :- Hour 00-12 (05) 
# 🎏 %p :- AM/PM  (PM) 
# 🎏 %M :- Minute 00-59 (41) 


import datetime

# 🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠

# 👉 datetime.now() :- The date contains year, month, day, hour, minute, second and microsecond

# x = datetime.datetime.now() # 🎉 example:- 2024-04-06 15:26:32.862380
# print(x)


# 🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠

# 👉 datetime() 

# print(datetime.datetime(2024,4,8))

# 🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠

# 👉 Section 1

now = datetime.datetime.now()

# year = now.strftime('%Y') # 🎉 example:- 2024

# print("year:",year) 

# 👉 Section 2

# month = now.strftime('%B') # 🎉 example:- April

# print("month:",month)

# month = now.strftime('%b') # 🎉 example:- Apr

# print("month:",month)


# 👉 Section 3

# month = now.strftime('%m') # 🎉 example:- 04 (month as number 04 (April))

# print("month:",month)

# 👉 Section 4

# year = now.strftime('%y') # 🎉 example:- 24 (year (2024) with short form (24))

# print("year:",year)

# year = now.strftime('%Y') # 🎉 example:- 2024 (year)

# print("year:",year)


# 👉 Section 5

# Hour = now.strftime('%H') # 🎉 example:- 15 (15 clock'o => 3 pm (24 hour))

# print("Hour:",Hour)

# Hour = now.strftime('%I') # 🎉 example:- 03 (3 clock'o (12 hour))

# print("Hour:",Hour)

# 👉 Section 6

# ampm = now.strftime('%p') # 🎉 example:- AM / PM

# print("Am/Pm:",ampm)

# 👉 Section 7

minutes = now.strftime('%M') # 🎉 example:- 50 (minutes)

print("minutes:",minutes)