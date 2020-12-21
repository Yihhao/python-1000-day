PLACEHOLDER = "name"
all_name = []
all_letters = []

with open("./Input/Names/invited_names.txt") as invited_names:
    names = invited_names.readlines()

with open("./Input/Letters/starting_letter.docx") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip("\n")
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.docx", "x") as send_letter:
            send_letter.write(new_letter)


