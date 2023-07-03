def display_regular(variable):
    print(variable)


def display_uppercase(variable):
    print(variable.upper())


def display_lowercase(variable):
    print(variable.lower())

string = input('What is your message?: ')
display_regular(string)
display_lowercase(string)
display_uppercase(string)