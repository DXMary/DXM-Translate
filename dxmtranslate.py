from tkinter import *
import googletrans
import textblob
import customtkinter
from tkinter import messagebox

WIN = customtkinter.CTk()
WIN.title("DXM - TRANSLATOR")
WIN.config(bg="#121212")
WIN.geometry("1060x300")
WIN.resizable(False, False)

def translate_it():

	translated_text.delete(1.0, END)

	try:

		for key, value in languages.items():
			if (value == original_combo.get()):
				from_language_key = key

		for key, value in languages.items():
			if (value == translated_combo.get()):
				to_language_key = key

		words = textblob.TextBlob(original_text.get(1.0, END))

		words = words.translate(from_lang=from_language_key , to=to_language_key)

		translated_text.insert(1.0, words)

	except Exception as e:

		messagebox.showerror("Translator", e)

def clear():

	original_text.delete(1.0, END)
	translated_text.delete(1.0, END)

languages = googletrans.LANGUAGES
language_list = list(languages.values())

# APP DESIGN 

spacer = Label(WIN)
spacer.config(bg="#121212")
spacer.grid(row=0, column=0, padx=17)

main_frame = customtkinter.CTkFrame(WIN, width=970, height=620, corner_radius=10, fg_color="#212124")
main_frame.grid(row=1, column=0, padx=17)

spacer1 = Label(main_frame)
spacer1.config(bg="#212124")
spacer1.grid(row=0, column=0, padx=17)

original_frame = customtkinter.CTkFrame(main_frame, width=650, height=50, corner_radius=10, fg_color="#2d2d31")
original_frame.grid(row=1, column=0, padx=17)

original_combo = customtkinter.CTkComboBox(original_frame, width=300, values=language_list, 
										  border_color="#45454c", fg_color="#45454c", 
										  button_color="#45454c", button_hover_color="#5915E4")
original_combo.grid(row=0, column=0, padx=17, pady=15)
original_combo.set("Select Source Language")

clear_button = customtkinter.CTkButton(original_frame, text="CLEAR TEXT", text_font=("Helvetica", 13), 
									  text_color="#c3c3c9", border_color="#8f8f9a", fg_color=None, 
									  hover_color="#212124", border_width=2, height=30, width=50, command=clear)
clear_button.grid(row=0, column=1, padx=15)

spacer2 = Label(main_frame)
spacer2.config(bg="#212124")
spacer2.grid(row=2, column=0, padx=17)

original_frame1 = customtkinter.CTkFrame(main_frame, width=600, height=230, corner_radius=10, fg_color="#2d2d31")
original_frame1.grid(row=3, column=0, padx=17)

original_text = Text(original_frame1, height=7, width=56, bd=0, font=("Helvetica", 14), 
					wrap=WORD, bg="#2d2d31", fg="#E3E6EA", highlightthickness=0)
original_text.pack(pady=10, padx=10)

spacer3 = Label(main_frame)
spacer3.config(bg="#212124")
spacer3.grid(row=4, column=0, padx=17)

translated_frame = customtkinter.CTkFrame(WIN, width=970, height=620, corner_radius=10, fg_color="#212124")
translated_frame.grid(row=1, column=1)

spacer4 = Label(translated_frame)
spacer4.config(bg="#212124")
spacer4.grid(row=0, column=0, padx=17)

translated_frame1 = customtkinter.CTkFrame(translated_frame, width=650, height=50, corner_radius=10, fg_color="#2d2d31")
translated_frame1.grid(row=1, column=0, padx=17)

translated_combo = customtkinter.CTkComboBox(translated_frame1, width=300, values=language_list, 
											border_color="#45454c", fg_color="#45454c", 
											button_color="#45454c", button_hover_color="#5915E4")
translated_combo.grid(row=0, column=0, padx=17, pady=15)
translated_combo.set("Select Target Language")

translate_button = customtkinter.CTkButton(translated_frame1, text="TRANSLATE", text_font=("Helvetica", 13), 
										  fg_color="#5915E4", hover_color="#4310AC", height=30, 
										  width=50, command=translate_it)
translate_button.grid(row=0, column=1, padx=17)

spacer5 = Label(translated_frame)
spacer5.config(bg="#212124")
spacer5.grid(row=2, column=0, padx=17)

translated_frame2 = customtkinter.CTkFrame(translated_frame, width=600, height=200, corner_radius=10, fg_color="#2d2d31")
translated_frame2.grid(row=3, column=0, padx=17)

translated_text = Text(translated_frame2, height=7, width=55, bd=0, font=("Helvetica", 14), wrap=WORD,
					  bg="#2d2d31", fg="#E3E6EA", highlightthickness=0)
translated_text.pack(pady=10, padx=10)

spacer6 = Label(translated_frame)
spacer6.config(bg="#212124")
spacer6.grid(row=4, column=0, padx=17)

WIN.mainloop()