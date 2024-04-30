# Compares strings

#answer = input('Do you agree?')
#if answer == "yes":
#    print('Agreed')
#else:
#    print("Not agreed")

#//////////////////////////////
# Strips string before comparing
#answer = input("Do you agree?").strip()
#if answer == "yes":
#    print("Agreed")
#else:
#    print("Not agreed")

#////////////////
#Lowercases string before comparing
answer = input("Do you agree?").strip().lower()
if answer == "yes":
    print("Agreed")
else:
    print("Not agreed")