# get initial bill total
input_total = float(raw_input("Enter Total Amount: "))

# get integer input:
# float() convert string to floating number
tip_rate = float(raw_input("Enter Tip Rate (such as 0.15): "))

total_with_tip = input_total + (input_total * tip_rate)

# use string formatting to output result
print "You should pay: $%d" % (total_with_tip)
