# Tkinter GUI Interface
from tkinter import *

from get_rfid import *
from firebase import *

val = {"User":"Tap Your Card", "Receipts":[]}

# Create frame_display which is destroyable for updating the informations to display
# Display all the information as individual buttons after filtering
def display():
    global frame2, frame_display, val

    frame_display.destroy()
    frame_display = Frame(frame2)
    frame_display.pack()

    # Using canvas to use scrollbar
    canvas = Canvas(frame_display, width=635, height=500)

    vsb = Scrollbar(frame_display, orient="vertical", command=canvas.yview)
    hsb = Scrollbar(frame_display, orient="horizontal", command=canvas.xview)

    frame_display.grid_rowconfigure(0, weight=1)
    frame_display.grid_columnconfigure(0, weight=1)
    canvas.configure(xscrollcommand=hsb.set, yscrollcommand=vsb.set)
    canvas.grid(row=0, column=0, sticky="nsew")
    vsb.grid(row=0, column=1, sticky="ns")
    hsb.grid(row=1, column=0, sticky="ew")

    label_display = Label(frame_display, text=val["User"], font=("Arial", 8, "bold"))
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
        dict_btn[key] = Button(canvas, text="Receipt No. {}".format(key+1), width=15, height=4, command=func)
        #dict_btn[key].bind('<FocusIn>', lambda event: (dict_btn[key].configure(bg="cyan")))

        # Place each button into its positions assigned
        canvas.create_window(i, j, anchor="nw", window=dict_btn[key])
        j+=75

    canvas.bind("<Configure>", lambda event: canvas.configure(scrollregion=canvas.bbox("all")))

def display2(key):
    global window3, val
    window3.destroy()
    window3 = Toplevel(window)
    window3.title("Receipt No. {}".format(key+1))
    frame3 = Frame(window3)
    frame3.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    # Display more information about the planning
    label_31 = Label(window3, text=val["Receipts"][key], font=("Arial", 8, "bold"))
    label_31.grid(row=1, column=0, padx=5, pady=5, sticky='w')

def reload():
    global val
    rfid,name = get_values()
    if rfid != "":
        #userdata = {"User":name, "Receipts":generate_receipt()}
        #set_receipt(rfid,userdata)
        
        val = dict(get_receipt(rfid))
        display()
    
    window.after(100, reload)
    
##### App Design #####

# Creating Window ############################################################################
window = Tk()
window.title('E-Receipt')
window.geometry("250x540")

# Create Frame 2: Display Planning ###########################################################
frame2 = Frame(window)
frame2.pack(side=LEFT, anchor=N)
frame_display = Frame(frame2)
frame_display.pack()
display()
# ############################################################################################

# Window 3: Event Description ################################################################
window3 = Toplevel(window)
window3.destroy()
# ############################################################################################

reload()

# Window Loop
window.mainloop()
