'''
Let's assume you are planning to use your Python skills to build a PBLApp for Mobile.
You decide to host your application on servers running in the cloud. You pick a hosting provider that charges $0.51 per hour. You will launch your service using one server and want to know how much it will cost to operate per day, per week, per month.
Write a Python program that displays the answers to the following questions:
How much does it cost to operate one server per day?
How much does it cost to operate one server per week?
How much does it cost to operate one server per month?
How many days can I operate one server with $918?
'''
hourly_cost = 0.51
budget = 918

daily_serve = hourly_cost * 24
print(f"Cost to operate one server per day: ${hourly_cost}")

weekly_cost = daily_serve * 7
print(f"Cost to operate one server per week: ${weekly_cost}")

monthly_cost = daily_serve * 30
print(f"Cost to operate one server per month: ${monthly_cost}")

days_operable = budget / daily_serve
print(f"Number of days you can operate one server with ${budget}:{days_operable} days")