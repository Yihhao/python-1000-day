# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

age_as_int = int(age)
left_age = 90 - age_as_int
day = left_age * 365
week = left_age * 52
month = left_age * 12
result = f"You have {day} days, {week} weeks, and {month} months left."
print(result)







