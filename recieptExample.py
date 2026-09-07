taxes : 0
prices = [12.50, 45.00, 110.00, 8.25, 65.50, 200.00, 3.00]
budgetItems = []
premiumItems = []
totalSum = 0
subTotal = 0

for price in prices:
    if price <= 50.00:
        budgetItems.append(price)
    else:
        premiumItems.append(price)
subTotal = sum(premiumItems)
totalSum = subTotal * 1.08
budgetItemSubtotal = 0

for item in budgetItems:
   budgetItemSubtotal += item


highestPrice = 0

for item in premiumItems:
    if item > highestPrice:
        highestPrice = item

lowestPrice = float("inf")

for item in budgetItems:
    if item < lowestPrice:
        lowestPrice = item




receipt = f"""
---------TRANSACTION SUMMARY---------
Budget Item List: {sorted(budgetItems)}
Premium Item List: {sorted(premiumItems)}
Subtotal (Before Tax): ${subTotal:.2f}
Total After Tax: ${totalSum:.2f}
Budget Item Subtotal: ${budgetItemSubtotal:.2f}
Lowest Priced Item: ${lowestPrice}
---------THANK YOU FOR SHOPPING HERE---------"""

print(receipt)
