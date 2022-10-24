import os
from tkinter import *
from tkinter import messagebox

from gtts import gTTS
from playsound import playsound
from translate import MyTranslate
from pdf_to_txt import PDFToText

root = Tk()
root.geometry("1250x600")
img = PhotoImage(file="assets/Images/background.png")
label = Label(root, image=img)
label.place(x=0, y=0)
root.title("TEXT TO SPEECH")

Label(root, text="TEXT/PDF TO SPEECH", font="arial 20 bold", fg='black', bg='#fff').place(x=500, y=50)
Msg = StringVar()
lang = StringVar()

label1 = Label(root, text="Enter Text", font='arial 15 bold', fg='black', bg='#fff').place(x=220, y=160)
message_entry_field = Text(root, width=50, font="Robote 20", wrap=WORD)
message_entry_field.place(x=220, y=200, width=350, height=300)

label2 = Label(root, text="Enter Language (Hindi='hi', Marathi='mr')", font='arial 15 bold', fg='black',
               bg='#fff').place(x=600, y=160)
lang_entry_field = Entry(root, textvariable=lang, width=50, font="Robote 20")
lang_entry_field.place(x=600, y=200, width=350, height=40)


def text_to_speech(message, language):
    speech = gTTS(text=message, lang=language, slow=False)
    speech.save("assets/sounds/speech.mp3")
    playsound('assets/sounds/speech.mp3', True)
    os.remove('assets/sounds/speech.mp3')


def translate(text_input, language):
    translate_obj = MyTranslate(text_input=text_input, translate_to_language=language)
    message = translate_obj.connection()
    return message


def file_handler():
    language = lang_entry_field.get()
    if language == "":
        messagebox.showwarning("Warning", "Language field can't be empty")
    else:
        pdf_obj = PDFToText()
        pdf_data = pdf_obj.translate_pdf()
        file_message = translate(text_input=pdf_data, language=language)
        text_to_speech(message=file_message, language=language)


def input_text_handler():
    language = lang_entry_field.get()
    input_text_message = translate(text_input=message_entry_field.get("1.0", END), language=language)
    text_to_speech(message=input_text_message, language=language)


def exit_handler():
    root.destroy()


def reset():
    lang.set("")
    message_entry_field.delete("1.0", END)



speak_button = PhotoImage(file="assets/Images/speak-man.png")
Button(root, text="Speak", bg="white", compound=LEFT, image=speak_button, width=130, font="arial 14 bold",
       command=input_text_handler).place(x=600, y=320)

exit_button = PhotoImage(file="assets/Images/exit.png")
Button(root, font='arial 15 bold', text='EXIT', compound=LEFT, image=exit_button, width=130, command=exit_handler,
       bg='white').place(x=750, y=320)

reset_button = PhotoImage(file="assets/Images/reset.png")
Button(root, font='arial 15 bold', text='RESET', compound=LEFT, image=reset_button, width=130, command=reset,
       bg='white').place(x=900, y=320)

file_button = PhotoImage(file="assets/Images/file.png")
Button(root, text=" Play PDF File", font='arial 15 bold', command=file_handler, compound=LEFT, image=file_button,
       width=200, bg='white').place(x=600, y=400)

root.mainloop()
