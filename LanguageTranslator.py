from tkinter import *
from googletrans import Translator

# Initialize the Tkinter root window
root = Tk()
translator = Translator()
root.geometry("600x500")
root.title("Khatri's Language Translator")
root.configure(bg="lightgreen")

# Header Label
head = Label(root, text="TRANSLATOR", font=('Times', 24, 'bold'), bg="lightgreen", fg="black", pady=30)
head.grid(row=0, column=0, columnspan=2)

# Input Label
label = Label(root, text="Enter text to translate:", bg="lightgreen", fg="black", pady=10)
label.grid(row=1, column=0, sticky=W, padx=20)

# Input Text Field
mn = StringVar()
textEntry = Entry(root, textvariable=mn, font=('Arial', 12), width=40)
textEntry.grid(row=2, column=0, padx=20)

# Language Options
l1 = Label(root, text="Enter 1 for Hindi", bg="lightgreen", fg="black", anchor="w")
l1.grid(row=3, column=0, sticky=W, padx=20)
l2 = Label(root, text="Enter 2 for Punjabi", bg="lightgreen", fg="black", anchor="w")
l2.grid(row=4, column=0, sticky=W, padx=20)
l3 = Label(root, text="Enter 3 for Bengali", bg="lightgreen", fg="black", anchor="w")
l3.grid(row=5, column=0, sticky=W, padx=20)

# Choice Entry
ch = IntVar()
chEntry = Entry(root, textvariable=ch, font=('Arial', 12), width=5)
chEntry.grid(row=6, column=0, padx=20, pady=10, sticky=W)

# Output Label for displaying results
result_label = Label(root, text="", bg="lightgreen", fg="black", font=('Arial', 12, 'bold'), wraplength=500, justify=LEFT)
result_label.grid(row=8, column=0, padx=20, pady=10)

# Output Function
def output():
    try:
        # Get input text and language choice
        text_to_translate = mn.get()
        choice = ch.get()

        # Determine the destination language based on the choice
        if choice == 1:
            out = translator.translate(text_to_translate, dest='hi')
        elif choice == 2:
            out = translator.translate(text_to_translate, dest='pa')
        elif choice == 3:
            out = translator.translate(text_to_translate, dest='bn')
        else:
            out = "Invalid choice"
            result_label.config(text=out)
            return

        # Update the output label
        result_label.config(text=out.text)

    except Exception as e:
        result_label.config(text="Error during translation: " + str(e))

# Result Button
b = Button(root, text="Translate", command=output, bg="white", fg="black", font=('Arial', 12, 'bold'), padx=10, pady=5)
b.grid(row=7, column=0, pady=20)

root.mainloop()
