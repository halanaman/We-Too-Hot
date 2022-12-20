# Tkinter GUI Interface
from tkinter import *
from tkinter import messagebox

from get_rfid import *
from firebase import *

val = {"User":"Tap Your Card", "Receipts":[]}

def filtering(mode):
    if mode == "e-receipts":
        display()

# Create frame_display which is destroyable for updating the informations to display
# Display all the information as individual buttons after filtering
def display():
    global frame2, frame_display, val

    frame_display.destroy()
    frame_display = Frame(frame2)
    frame_display.pack()

    # Using canvas to use scrollbar
    canvas = Canvas(frame_display, width=235, height=500)

    vsb = Scrollbar(frame_display, orient="vertical", command=canvas.yview)
    hsb = Scrollbar(frame_display, orient="horizontal", command=canvas.xview)

    frame_display.grid_rowconfigure(0, weight=1)
    frame_display.grid_columnconfigure(0, weight=1)
    canvas.configure(xscrollcommand=hsb.set, yscrollcommand=vsb.set)
    canvas.grid(row=0, column=0, sticky="nsew")
    vsb.grid(row=0, column=1, sticky="ns")
    hsb.grid(row=1, column=0, sticky="ew")

    label_display = Label(frame_display, text="Transaction History", font=("Arial", 8, "bold"))
    canvas.create_window(50, 0, anchor="nw", window=label_display)

    # Initialize positions
    i = 10
    j = 25
    dict_btn = {}

    # For each dictionary in dict_show, show each item as a button
    for key in range(len(val["Receipts"])):

        # This function is used to keep track of each key as every button has its own unique key
        def func(x=key):
            return display2(x)

        t = val["Receipts"][key].split("\n")
        shop_name = t[0].strip(" -Welcome to")
        shop_total = t[len(t)-1].strip("Your Total bill amount is :")

        dict_btn[key] = Button(canvas, text=shop_name+"   "+shop_total, width=30, height=2, command=func)
        #dict_btn[key].bind('<FocusIn>', lambda event: (dict_btn[key].configure(bg="cyan")))

        # Place each button into its positions assigned
        canvas.create_window(i, j, anchor="nw", window=dict_btn[key])
        j+=45

    canvas.bind("<Configure>", lambda event: canvas.configure(scrollregion=canvas.bbox("all")))

def display2(key):
    global window3, frame_display2, val
    frame_display2.destroy()
    frame_display2 = Frame(window3)
    frame_display2.pack()

    t = val["Receipts"][key].split("\n")
    shop_name = t[0].strip(" -Welcome to")
    shop_total = t[len(t)-1].strip("Your Total bill amount is :")

    # Display more information about the planning
    label_30 = Label(frame_display2, text=shop_name+"   "+shop_total, font=("Arial", 8, "bold"))
    label_31 = Label(frame_display2, text=val["Receipts"][key], font=("Arial", 8, "bold"))
    label_30.grid(row=0, column=0, padx=5, pady=5, sticky='w')
    label_31.grid(row=1, column=0, padx=5, pady=5, sticky='w')

def reload():
    global val, label_filtering, frame_display, frame_display2
    rfid,name = get_values()
    if rfid != "":
        #userdata = {"User":name, "Receipts":generate_receipt()}
        #set_receipt(rfid,userdata)
        try:
            val = dict(get_receipt(rfid))
            label_filtering['text'] = "Hello,\n"+val["User"]
            frame_display.destroy()
            frame_display2.destroy()
        except:
            messagebox.showwarning("Warning", "Unknown User has no History")

    window.after(100, reload)

##### App Design #####

# Creating Window ############################################################################
window = Tk()
window.title('E-Receipt')
window.geometry("600x540")

# Create Frame 1: Filter Buttons #############################################################
frame1 = Frame(window)
frame1.pack(side=LEFT, anchor=NW)

# Filter buttons
label_filtering = Label(frame1, text="Please Tap Your Card", font=("Arial", 8, "bold"))
btn_pax = Button(frame1, text="E-Receipts", font=("Arial", 8, "bold"), width=9, height=4, command=lambda: filtering('e-receipts'))
btn_occasion = Button(frame1, text="Refunds", font=("Arial", 8, "bold"), width=9, height=4, command=lambda: filtering('refunds'))
btn_location = Button(frame1, text="Rewards", font=("Arial", 8, "bold"), width=9, height=4, command=lambda: filtering('rewards'))
btn_time = Button(frame1, text="Report", font=("Arial", 8, "bold"), width=9, height=4, command=lambda: filtering('report'))

label_filtering.grid(row=0, column=0, padx=5, pady=5)
btn_pax.grid(row=1, column=0, padx=5, pady=5)
btn_occasion.grid(row=2, column=0, padx=5, pady=5)
btn_location.grid(row=3, column=0, padx=5, pady=5)
btn_time.grid(row=4, column=0, padx=5, pady=5)
# ############################################################################################

# Create Frame 2: Display Planning ###########################################################
frame2 = Frame(window)
frame2.pack(side=LEFT, anchor=N)
frame_display = Frame(frame2)
frame_display.pack()
# ############################################################################################

# Window 3: Event Description ################################################################
window3 = Frame(window)
window3.pack(side=LEFT, anchor=NE)
frame_display2 = Frame(window3)
frame_display2.pack()
# ############################################################################################

reload()

# Window Loop
window.mainloop()
