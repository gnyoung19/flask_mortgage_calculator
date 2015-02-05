def mortgage_afford(income, down_payment, interest_rate):
	monthly_income = income/12
	mortgage_monthly = monthly_income * 0.25
	cost_to_borrow_ten_grand = interest_rate*1000
	max_affordable_mortgage = ((mortgage_monthly/cost_to_borrow_ten_grand) * 10000) + down_payment
	print "Your maximum affordable mortgage is {}.".format(max_affordable_mortgage)

print "Welcome to the Mortgage affordability calculator!"
user_income = int(raw_input("What is your annual income? "))
user_down_payment = int(raw_input("What will be your down payment? "))
user_interest_rate = float(raw_input("What is the current interest rate? "))


mortgage_afford(user_income, user_down_payment, user_interest_rate)