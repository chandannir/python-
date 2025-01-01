s = input("Do you agree? ")

s = s.lower()

if s in ["yes", "y"]:
    print("Agreed.")
elif s in ["no","n"]:
    print("Not Agreed.")