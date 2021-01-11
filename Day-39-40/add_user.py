import os
import requests

SHEET_USERS_ENDPOINT = os.environ.get("SHEET_USERS_ENDPOINT")
USER_NAME = os.environ.get("USER_NAME")
PASSWORD = os.environ.get("PASSWORD")

print("Welcome to Yihao's Flight club.")
print("We find the best flight deals and email you.")
first_name = input("What is your first name?\n")
second_name = input("What is your second name?\n")

double_check_email = False
while not double_check_email:
    email = input("What is your email?\n")
    if email == input("Type you email again.\n"):
        print("You're in the club!")
        double_check_email = True
    else:
        print("The email isn't match. Please input email again.")

new_data = {
    "user": {
        "firstName": first_name,
        "lastName": second_name,
        "email": email,
    }
}
response = requests.post(SHEET_USERS_ENDPOINT, json=new_data, auth=(USER_NAME, PASSWORD))
print(response.text)
