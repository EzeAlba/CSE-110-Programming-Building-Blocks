
# Asking the user to introduce values and they're stored
#in variables.    
child_meal = float(input(f"What is the price of a child's meal? "))
adult_meal = float(input(f"What is the price of an adult's meal? "))
children = int(input(f"How many children are there? "))
adults = int(input(f"How many adults are there? "))
tax_rate = float(input(f"What is the sales tax rate? "))
tip = float(input(f"What is the tip percentage? "))
print()

#In this part we ask the user to choose an option for it's payment method.
payment_method = ""
while True:
    payment_option = input("what is your payment method?\n1. Cash\n2. Debit Card\n3. Credit Card\nSelect your payment method: ")
    if payment_option == '1':
        payment_method = "Cash"
        break
    elif payment_option == '2':
        payment_method = "Debit Card"
        break
    elif payment_option == '3':
        payment_method = "Credit Card"
        break
    else:
        print("Incorrect option.\n")


print()


# This part is to process the values typed by the user.
subtotal = (child_meal * float(children)) + (adult_meal * float(adults))
sales_tax = (subtotal * tax_rate)/100.0
tip_amount = (tip * subtotal)/100.0 
total = subtotal + sales_tax + tip_amount


# This code lines are to prompt all the procesed values
# but with only 2 decimals. 
print(f"Subtotal: ${subtotal:.2f}")
print(f"Sales Tax: ${sales_tax:.2f}")
print(f"Your tip: ${tip_amount:.2f}")
print(f"Total: ${total:.2f}")
print(f"Payment method: {payment_method}")
print()

# Asking a payment amount to user.
# If the payment amount is less than the total check we ask to typed a new valid amount.
while True:
    payment = float(input("What is the payment amount? "))
    if payment < total:
        print("The payment amount is not enough to pay the check.\nIntroduce another amount.\n")
    else:
        change = payment - total
        print(f"Change: ${change:.2f}")
        break