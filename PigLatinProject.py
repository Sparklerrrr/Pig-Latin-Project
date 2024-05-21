# (c) Copyright Skillage I.T.
# (c) This file is Skillage I.T. software and is made available under license.
# (c) This software is developed by: [REDACTED], for Kelly Smith.
# (c) Date: 11th May 2024 Time: 13.20
# (c) File Name: Example.cs Version: 1.5
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
import pyperclip
from tkinter import filedialog #this imports the file dialog moduale from the tkinter package.

def pig_latin(text):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    consonant_clusters = {'bl', 'br', 'ch', 'cl', 'cr', 'dr', 'fl', 'fr', 'gl', 'gr', 'pl', 'pr', 'qu', 'sc', 'sh', 'sk', 'sl', 'sm', 'sn', 'sp', 'st', 'sw', 'th', 'tr', 'tw', 'wh', 'wr'}
    words = text.split()
    translated_words = []
    for word in words:
        # Checks for specific consonant clusters
        if word[:2].lower() in consonant_clusters:
            # Word starts with a consonant cluster, move it to the end and add 'ay'
            translated_word = word[2:] + word[:2] + 'ay'
        elif word[0].lower() in vowels:
            # Word starts with a vowel, just add 'way'
            translated_word = word + 'way'
        else:
            # Word starts with a single consonant, move it to the end and add 'ay'
            translated_word = word[1:] + word[0] + 'ay'
        translated_words.append(translated_word)
    return ' '.join(translated_words)


def translate():
    input_text = entry.get()
    translated_text = pig_latin(input_text)
    output_label.config(text=translated_text)

def copy_to_clipboard():
    translated_text = output_label.cget("text")
    pyperclip.copy(translated_text)
    msgbox.showinfo("Copied!", "Translated text has been copied to clipboard.")

def convert_file_to_pig_latin(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        translated_content = pig_latin(content)
        with open(file_path, 'w') as file:
            file.write(translated_content)
        msgbox.showinfo("Success", "File successfully converted to Pig Latin and rewritten.")
    except Exception as e:
        msgbox.showerror("Error", str(e))

def open_file_and_convert():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        convert_file_to_pig_latin(file_path)

# Create GUI
root = tk.Tk()
root.title("Pig Latin Translator")

# Sets the window size (width x height)
root.geometry("500x300")

label = tk.Label(root, text="Enter text:")
label.pack()

entry = tk.Entry(root, width=70)  # Set width of entry box
entry.pack()

translate_button = tk.Button(root, text="Translate", command=translate)
translate_button.pack()

output_label = tk.Label(root, text="")
output_label.pack()

copy_button = tk.Button(root, text="Copy", command=copy_to_clipboard)
copy_button.pack()

#This converts a text file to pig latin
open_convert_button = tk.Button(root, text="Open File and Convert", command=open_file_and_convert)
open_convert_button.pack()
# Copyright and version label
copyright_label = tk.Label(root, text="© SkillageIT 2024", fg="gray")
copyright_label.pack(side="bottom", padx=5, pady=10)

version_label = tk.Label(root, text="Version 1.5", fg="gray")
version_label.pack(side="bottom", padx=5, pady=10)

root.mainloop()

