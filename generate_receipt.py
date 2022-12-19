import random

def receipt():
    title = """--------------WELCOME TO ABC SHOP--------------
+---------------------------------------------+
       Item Name       |     Item Price($)     
                       |                       
"""

    items = {
            "Shampoo":9.9, "Canola Oil":7.5, 
            "Thai Rice":12.1, "Meji Crackers":5.7,
            "Chocolate":2.95, "Chips":1.95,
            "Soft Drink":2.05, "Coffee":4.95,
            "Tea":3.95, "Chilli Sauce":6.8,
            "Mask":19.9, "Milo Packets":14.8,
            "Tissue":3.55, "Hand Soap":3.9,
            "Toothpaste":6.9, "Milk":5.95
            }

    keys = list(items.keys())
    random.shuffle(keys)
    keys = keys[:random.randint(1,len(items))]

    receipt = title
    total = 0
    for k in keys:
        receipt += "{:^23s}|{:^23.2f}\n".format(k,items[k])
        total += items[k]

    receipt += "+---------------------------------------------+\n"
    receipt += "{:^23s}|{:^23.2f}\n".format("Total",total)
    receipt += """\nThanks for shopping with us :)
Your Total bill amount is Total: ${:.2f}""".format(total)
    return receipt
    
def generate_receipt():
    receipts = []
    for i in range(random.randint(1,20)):
        receipts.append(receipt())
    return receipts

#print(generate_receipt())
