#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. 

print("Welcome to the tip calculator!")

bill = input("What was the total bill? $")
tip = input("How much tip would you like to give? 10, 12, or 15? ")
split = input("How many people to split the bill? ")

total_bill = float(bill) * (100+float(tip))/100

total_per_person = total_bill / int(split)
total_per_person_2dec = "{:.2f}".format(total_per_person)

print("Each person should pay: $" + total_per_person_2dec)
