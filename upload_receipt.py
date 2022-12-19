from get_rfid import *
from firebase import *
from generate_receipt import *

while True:
    rfid,name = get_values()
    if rfid != "":
        userdata = {"User":name, "Receipts":generate_receipt()}
        set_receipt(rfid,userdata)
        
        val = dict(get_receipt(rfid))
        print("User: ",val["User"])
        print("Receipts:", len(val["Receipts"]))
        for ele in val["Receipts"]:
            print("\n",ele,"\n")
