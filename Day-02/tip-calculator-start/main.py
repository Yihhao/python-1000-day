#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: You might need to do some research in Google to figure out how to do this.

print("Welcome to the tip calculator")
tot_bill = float(input("What was total bill? $"))
per_tip = int(
    input("What percentage tip would you like to give? 10, 12 or 15? "))
num_pepole = int(input("How many pepole to spilt the bill? "))

person_pay = (tot_bill / num_pepole) * (1 + per_tip / 100)
round_person_pay = round(person_pay, 2)
print(f"Each person shold pay: $ {round_person_pay}")
