with open ("output.txt", 'w') as f:
    user_input = input("Enter some text: ")
    writing_file = f.write(user_input)
    print(writing_file)

with open("output.txt", 'r') as f:
    reading_file = f.read()
    print(reading_file)

with open("output.txt", 'a') as f:
    f.write("\nWelcome to the GANG!")
