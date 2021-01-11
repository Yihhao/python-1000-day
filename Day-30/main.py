# try:
#     file = open("a_file.txt")
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File was close.")


height = float(input("Height:"))
weight = float(input("Weight:"))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters")

bmi = weight / height ** 2
