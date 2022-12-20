import random

def receipt():
    
    shops = [
                {"name":"ABC_Shop",
                "Shampoo":9.9, "Canola Oil":7.5, 
                "Thai Rice":12.1, "Meji Crackers":5.7,
                "Chocolate":2.95, "Chips":1.95,
                "Soft Drink":2.05, "Coffee":4.95,
                "Tea":3.95, "Chilli Sauce":6.8,
                "Mask":19.9, "Milo Packets":14.8,
                "Tissue":3.55, "Hand Soap":3.9,
                "Toothpaste":6.9, "Milk":5.95
                },
                
                {"name":"NTUC",
                "Shampoo":9.9, "Canola Oil":7.5, 
                "Thai Rice":12.1, "Meji Crackers":5.7,
                "Chocolate":2.95, "Chips":1.95,
                "Soft Drink":2.05, "Coffee":4.95,
                "Tea":3.95, "Chilli Sauce":6.8,
                "Mask":19.9, "Milo Packets":14.8,
                "Tissue":3.55, "Hand Soap":3.9,
                "Toothpaste":6.9, "Milk":5.95
                },
                
                {"name":"Cold Storage",
                "Shampoo":9.9, "Canola Oil":7.5, 
                "Thai Rice":12.1, "Meji Crackers":5.7,
                "Chocolate":2.95, "Chips":1.95,
                "Soft Drink":2.05, "Coffee":4.95,
                "Tea":3.95, "Chilli Sauce":6.8,
                "Mask":19.9, "Milo Packets":14.8,
                "Tissue":3.55, "Hand Soap":3.9,
                "Toothpaste":6.9, "Milk":5.95
                },
                
                {"name":"Sheng Siong",
                "Shampoo":9.9, "Canola Oil":7.5, 
                "Thai Rice":12.1, "Meji Crackers":5.7,
                "Chocolate":2.95, "Chips":1.95,
                "Soft Drink":2.05, "Coffee":4.95,
                "Tea":3.95, "Chilli Sauce":6.8,
                "Mask":19.9, "Milo Packets":14.8,
                "Tissue":3.55, "Hand Soap":3.9,
                "Toothpaste":6.9, "Milk":5.95
                }
            ]
    
    i = random.randint(0,3)
    
    top = shops[i]["name"]
    top = "Welcome_to_" + top
    top = "{:^47s}".format(top)
    top = top.replace(" ","-").replace("_"," ")
    title = """{}
+---------------------------------------------+
       Item Name       |     Item Price($)     
                       |                       
""".format(top)

    keys = list(shops[i].keys())
    keys.remove("name")
    random.shuffle(keys)
    keys = keys[:random.randint(1,len(shops[i]))]

    receipt = title
    total = 0
    for k in keys:
        receipt += "{:^23s}|{:^23.2f}\n".format(k,shops[i][k])
        total += shops[i][k]

    receipt += "+---------------------------------------------+\n"
    receipt += "{:^23s}|{:^23.2f}\n".format("Total",total)
    receipt += """\nThanks for shopping with us :)
Your Total bill amount is : ${:.2f}""".format(total)
    return receipt
    
def generate_receipt():
    receipts = []
    for i in range(random.randint(1,20)):
        receipts.append(receipt())
    return receipts

#print(generate_receipt())
