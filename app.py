
first_name = input('What is your Name? ')
last_name = input('What is your last Name? ')
age = input('How old are you? ')
print("You are ", first_name, last_name + " and you are ", age, "years old")

# Fragt sich wie Alt du bist, wie du heißt und gibt dir am Ende einen Satz mit all deinen Antworten !

Frage2 = input('How are you today? ')

if "I'm Fine" == Frage2:
    print("That's good to hear")
elif "Good" == Frage2:
    print("That's nice to hear")
elif "Very Nice" == Frage2:
    print("That's good to hear")
elif "Nice" == Frage2:
    print("That's good to hear")
elif "Fine" == Frage2:
    print("That's good to hear")

# Tells you every time the Same thing for a Different Answer !

elif "Not so Good" == Frage2:
    print("I'm sorry to hear that")
elif "Bad" == Frage2:
    print("I'm sorry to hear that")
elif "Very Bad" == Frage2:
    print("I'm sorry to hear that")
print("Here is another Question for you:")

Frage3 = input('Do you have Kids? ')
if "No" == Frage3:
    print("Okey")
elif 'Yes' == Frage3:
    print('Okey')
    Frage4 = input('and How many? ')
if '1' == Frage4:

    print("That's good to hear!")
elif '2' == Frage4:
    Frage5 = input("That's good. Boys or Girls? ")
if "1 Boy and 1 Girl" == Frage5:
    print("That's good to hear")
elif "2 Girls" == Frage5:
    print("That's good to hear!")
elif "2 Boys" == Frage5:
    print("That's good to hear!")
elif '3' == Frage4:

    Frage5 = input("That's good. Boys or Girls? ")
if "1 Boy and 1 Girl" == Frage5:
    print("That's good to hear")
elif "2 Girls" == Frage5:
    print("That's good to hear!")
elif "2 Boys" == Frage5:
    print("That's good to hear!")
elif '4' == Frage4:

    Frage5 = input("That's good. Boys or Girls? ")
if "Boys and Girls" == Frage5:
    print("That's good to hear")
elif "Only Girls" == Frage5:
    print("That's good to hear!")
elif "Only Boys" == Frage5:
    print("That's good to hear!")

elif 'More than 5' == Frage4:
    Frage5 = input("That's a lot. Boys or Girls? ")
if "Boys and Girls" == Frage5:
    print("That's good to hear")
elif "Only Girls" == Frage5:
    print("That's good to hear!")
elif "Only Boys" == Frage5:
    print("That's good to hear!")