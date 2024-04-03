print("Welcome to the tip calculator")
total_bill = input("What was the total bill? $")
tip = input("How much tip would you like to tip? 10, 12 or 15? ")
num_people = input("How many people to split the bill? ")

pay = (int(total_bill) * (100 + int(tip))/100)/int(num_people)
print(f"Each person should pay: ${pay}")
