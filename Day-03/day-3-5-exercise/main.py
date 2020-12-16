# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combine_name = name1 + name2
lower_case_name = combine_name.lower()

first_count = 0
second_count = 0

first_count += lower_case_name.count('t')
first_count += lower_case_name.count('u')
first_count += lower_case_name.count('r')
first_count += lower_case_name.count('e')

second_count += lower_case_name.count('l')
second_count += lower_case_name.count('o')
second_count += lower_case_name.count('v')
second_count += lower_case_name.count('e')

score = int(str(first_count) + str(second_count))

if score >= 10 or score <= 90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score <= 50 and score >= 40:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")