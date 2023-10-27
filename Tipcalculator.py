#TODO: Creating a tool to calculate the tip and split the bill!.....
#?..Taking the input from the users by asking there bill value
#!....welcome message for user.....
message="Welcome to the tip calculator."
print (message)
#!......taking "F&I" inputs from the user..........
bill=float(input("What was the total bill? ₹"))
tip=int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people=int(input("How many people to split the bill? "))
#!.......Formula..........
tip_as_percentage = tip / 100
total_tip_amount = bill * tip_as_percentage
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
#!.......Now using formate function to print 2 decimal degit in output.....
final_amount = "{:.2f}".format(bill_per_person)
print (f"Each person should pay: ₹{final_amount}")
