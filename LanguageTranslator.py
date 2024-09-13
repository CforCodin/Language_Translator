from tkinter import *
from googletrans import Translator, LANGUAGES

# Initialize the Tkinter root window
root = Tk()
translator = Translator()
root.geometry("600x500")
root.title("Khatri's Language Translator")
root.configure(bg="lightgreen")

# Header Label
head = Label(root, text="TRANSLATOR", font=('Times', 24, 'bold'), bg="lightgreen", fg="black", pady=20)
head.grid(row=0, column=0, columnspan=2)

# Input Label
label = Label(root, text="Enter text to translate:", bg="lightgreen", fg="black", pady=10)
label.grid(row=1, column=0, sticky=W, padx=20)

# Input Text Field
mn = StringVar()
textEntry = Entry(root, textvariable=mn, font=('Arial', 12), width=40)
textEntry.grid(row=2, column=0, padx=20)

# Language Selection Dropdown Menu
language_options = list(LANGUAGES.values())  # List of language names
language_codes = list(LANGUAGES.keys())  # List of language codes
selected_language = StringVar(root)
selected_language.set("Select Language")  # Default value

language_menu = OptionMenu(root, selected_language, *language_options)
language_menu.config(font=('Arial', 12), bg="white")
language_menu.grid(row=3, column=0, padx=20, pady=10)

# Output Label for displaying results
result_label = Label(root, text="", bg="lightgreen", fg="black", font=('Arial', 12, 'bold'), wraplength=500, justify=LEFT)
result_label.grid(row=5, column=0, padx=20, pady=10)

# Output Function
def output():
    try:
        # Get input text and selected language
        text_to_translate = mn.get()
        language = selected_language.get()

        # Check if a language is selected
        if language == "Select Language":
            result_label.config(text="Please select a language.")
            return

        # Get the corresponding language code
        language_code = language_codes[language_options.index(language)]

        # Perform translation
        out = translator.translate(text_to_translate, dest=language_code)

        # Update the output label
        result_label.config(text=out.text)

    except Exception as e:
        result_label.config(text="Error during translation: " + str(e))

# Result Button
b = Button(root, text="Translate", command=output, bg="white", fg="black", font=('Arial', 12, 'bold'), padx=10, pady=5)
b.grid(row=4, column=0, pady=20)

root.mainloop()
