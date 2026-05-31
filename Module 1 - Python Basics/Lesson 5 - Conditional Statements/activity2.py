# ACTIVITY 2 - PROFIT OR LOSS

cost_price = float(input("Please Enter the Actual Product Price: "))
sale_price = float(input("Please Enter the Sales Amount: "))
 
if (sale_price > cost_price):
    print("This transaction made a Profit")
    print("Total Profit = {0}".format(sale_price - cost_price))
else:
    print("This transaction made a Loss")