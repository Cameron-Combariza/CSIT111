#
#

#welcomes user
print("Welcome User.")

#ask for name, major, amd credits taken
Name = input("What is your Name? ") 
Major = input("what is your intended major? ")
Taken_Credits = int(input("How Many Credits have you takens so far? "))

#Credits Needed to Graduate
CreditsNeeded = 60

#calculate remaining need credits.
needed_credits = CreditsNeeded - Taken_Credits

#
if Taken_Credits <= CreditsNeeded:
    print(Name,"you need to take", needed_credits, "to be able to graduate with", major ,"as your intended major.")
else:
    print (Name,"you have the nesseary credits to graduate with", major,"as your intended major.")
