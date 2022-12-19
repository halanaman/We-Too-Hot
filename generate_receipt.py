import random

def receipt():
    title = """--------------WELCOME TO ABC SHOP--------------
+---------------------------------------------+
       Item Name       |     Item Price($)     
                       |                       
"""

    items = {"Shampoo":9.9, "Canola Oil":7.5, "Thai Rice":12.1, "Meji Crackers":5.7}

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
    for i in range(random.randint(1,5)):
        receipts.append(receipt())
    return receipts

#print(generate_receipt())
