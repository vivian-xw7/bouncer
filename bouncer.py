
# age = input("How old are you? ")
# if int(age) >= 18 and int(age) < 21:
#     print("No drinking. Wrist band for you!")
# elif int(age) >= 21:
#     print("You can enter and drink.")
# else:
#     print("Get outta here!")



# now take advantage of falsiness...
# an empty string is inherantly False
# use   if age...  If age does not exist, run the else.

# to make the int(age) more concise you can establish the int() at top, but still within the if/else

# age = input("How old are you? ")

# if age:
#     age = int(age)
#     if age >= 18 and age < 21:
#         print("No drinking. Wrist band for you!")
#     elif age >= 21:
#         print("You can enter and drink.")
#     else:
#         print("Get outta here!")
# else:
#     print("Enter your age...")




# now make more concise...


age = input("How old are you? ")

if age:
    age = int(age)
    if age >= 21:
        print("You can enter and drink.")
        # this is first bc if negated, it just moves down
    elif age >= 18:
        print("No drinking. Wrist band for you!")
    else:
        print("Get outta here!")
else:
    print("Enter your age...")