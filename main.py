# Welcome message
print("Welcome to the tip calculator.")

total_bill = float(input("What was the total bill? $"))

percentage_tip = float(input("What percentage tip would you like to give? 10, 12, or 15? "))

number_of_people = int(input("How many people to split the bill? "))

total_bill = round((total_bill * (1 + percentage_tip / 100)) / number_of_people, 2)

print(f"Each person should pay: ${total_bill}")
