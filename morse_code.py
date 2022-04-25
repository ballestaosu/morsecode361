#Andre Ballesteros
#Morse Code Translator Project
#Sources: Michael Eramo Videos, Python tkinter docs
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from playsound import playsound
import Pmw

#Define window
root = tk.Tk()
root.title('Morse Code Translator')
root.iconphoto(False, tk.PhotoImage(False, file='./radio.png'))
root.geometry('625x600')
root.resizable(0,0)

#Define fonts colors
button_font = ('Georgia', 10)
border_font = ('Stratum', 12)
root_color = '#cd6e46'
frame_color = '#dcdcdc'
button_color = '#c0c0c0'
text_color = '#f8f8ff'
root.config(bg=root_color)

#Define functions
def morse():
    '''Translate from English to Morse Code'''
    morse_code_output = ""

    #Get input text 
    text = input_text.get("1.0", END)
    text = text.lower()

    #Remove any unwanted characters
    for alphanum in text:
        if alphanum not in english_to_morse.keys():
            text = text.replace(alphanum, '') 

    #Separate into words where needed
    word_list = text.split(" ")

    #Make a list, using word list, of each individual character
    for word in word_list:
        alphanums = list(word)
        #Grab each alphanum's relevant morse code representation
        for alphanum in alphanums:
            morse_character = english_to_morse[alphanum]
            morse_code_output += morse_character
            #add space after each word
            morse_code_output += " "
        #separate words with pipe '|'
        morse_code_output += '|'
    
        print(morse_code_output)
    
    output_text.insert("1.0", morse_code_output)

def english():
    '''Translate from Morse Code to English'''
    english_output = ""

    #Get input text
    text = input_text.get("1.0", END)
    
    #Remove any unwanted characters
    for alphanum in text:
        if alphanum not in morse_to_english.keys():
            text = text.replace(alphanum, '')

    #Separate based on pipe '|'
    word_list = text.split("|")

    #Make a list based on words 
    for word in word_list:
        alphanums = word.split(" ")
        #Grab english representation of each letter
        for alphanum in alphanums:
            english_character = morse_to_english[alphanum]
            english_output += english_character
        #separate words with space
        english_output += " " 

    output_text.insert("1.0", english_output)

def clear_all():
    '''Clear all input text fields'''
    answer = messagebox.askquestion("Clear All", "Are you sure?")
    if answer == 'yes':
        input_text.delete("1.0", END)
        output_text.delete("1.0", END)
    else:
        pass

def clear_one():
    '''Clear one text box'''
    answer = messagebox.askquestion("Clear", "Are you sure?")
    if answer == 'yes':
        if input_text:
            input_text.delete("1.0", END)
        else:
            output_text.delete("1.0", END)

def translate():
    ''''Use correct translation based on radio buttons'''
    #English
    if language.get() == 1:
        morse()
    elif language.get() == 2:
        english()

def play_morse():
    '''Play sounds for dash and dots'''
    #Caution pop up
    answer = messagebox.askquestion("Play tones?", "Play tones?")
    if answer == 'yes':
        # Grab location of the morse code
        if language.get() == 1:
            text = output_text.get("1.0", END)
        elif language.get() == 2:
            text = input_text.get("1.0", END)

        #Play following tones (., -, |, " ")
        for char in text:
            if char == ".":
                # '.'
                playsound('dot.mp3')
                #pause to play sound
                root.after(150)
            elif char == "-":
                playsound('dash.mp3')
                root.after(250)
            elif char == " ":
                root.after(250)
            elif char == "|":
                root.after(500)
    else: 
        pass

def show_alphanum_guide():
    '''In a separate window, show an alphanum morse code representation guide '''
    # morse_code image needs to be a global variable in order to be put in a window
    # guide window needs to be a global variable in order to be able to close the window
    global morse_img
    global guide

    #Create another window
    guide = tk.Toplevel()
    guide.title("Alphanum Guide")
    guide.iconphoto(False, tk.PhotoImage(False, file='./radio.png'))
    guide.geometry('400x400+' + str(root.winfo_x()+626) + "+" + str(root.winfo_y()))
    guide.config(bg=root_color)

    #Create morse_code image
    morse_img = ImageTk.PhotoImage(Image.open('morse_chart.jpg'))
    label = tk.Label(guide, image=morse_img, bg=frame_color)
    label.pack(padx=10, pady=10, ipadx=5, ipady=5)

    #Exit button for window
    close_button = tk.Button(guide, text='Close Window', font=button_font, bg=button_color, command=hide_window)
    close_button.pack(padx=10, ipadx=50)

    #Disable "Alphanum Button" once window is open
    alphanum_button.config(state=DISABLED)

def hide_window():
    '''Hide Alphanum Guide'''
    alphanum_button.config(state=NORMAL)
    guide.destroy()


#Create our morse code dictionaries
english_to_morse = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..',
                    'e': '.', 'f': '..-.', 'g': '--.', 'h': '....',
                    'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
                    'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
                    'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
                    'u': '..--', 'v': '...-', 'w': '.--', 'x': '-..-',
                    'y': '-.--', 'z': '--..', '1': '.----',
                    '2': '..---', '3': '...--', '4': '....-', '5': '.....',
                    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
                    '0': '-----', ' ':' ', '|':'|', "":"" }

morse_to_english = dict([(value, key) for key, value in english_to_morse.items()])

#Define layout
#Define frames
generate_frame = tk.LabelFrame(root, bg=frame_color, text='1a. Generate Random text', font=border_font, borderwidth=3)
input_frame = tk.LabelFrame(root, bg=frame_color, text='1b. Enter text', font=border_font, borderwidth=3)
output_frame = tk.LabelFrame(root, bg=frame_color, text='2. Translated text', font=border_font, borderwidth=3)
#generate_frame.pack(padx=16,pady=(16, 8))
generate_frame.pack(padx=15, pady=10)
input_frame.pack(padx=15, pady=16)
output_frame.pack(padx=15, pady=10)

#RANDOM GENERATE
#Layout for Random Generate frame
generate_text= tk.Text(generate_frame, height=8, width=30, bg=text_color)
generate_text.grid(row=0, column=1, rowspan=4, padx=5, pady=5)

generate_button = tk.Button(generate_frame, text='Random Text', font=button_font, bg=button_color)
clear_button = tk.Button(generate_frame, text='Clear', font=button_font, bg=button_color)

generate_button.grid(row=3, column=0, padx=5, pady=40, ipadx=25)
clear_button.grid(row=3, column=0, padx=5, pady=5, sticky='SWE')


#INPUT 
#Layout for the input frame
input_text = tk.Text(input_frame, height=8, width=30, bg=text_color)
input_text.grid(row=0,column=1, rowspan=4, padx=5, pady=5)

language = IntVar()
language.set(1)
morse_button = tk.Radiobutton(input_frame, text='English -> Morse Code', variable=language, value=1, font=button_font, bg=frame_color)
english_button = tk.Radiobutton(input_frame, text='Morse Code -> English', variable=language, value=2, font=button_font, bg=frame_color)
clear_button = tk.Button(input_frame, text='Clear', font=button_font, bg=button_color, command = clear_one)
alphanum_button = tk.Button(input_frame, text='Alphanum Guide', font=button_font, bg=button_color, command = show_alphanum_guide)

morse_button.grid(row=0, column=0, pady=(15,0))
english_button.grid(row=1, column=0)
alphanum_button.grid(row=2,column=0, padx=10, sticky='WE')
clear_button.grid(row=3,column=0, padx=10, sticky='WE')


#OUTPUT
#Layout for the output frame
output_text = tk.Text(output_frame, height=8, width=30, bg=text_color)
output_text.grid(row=0, column=1, rowspan=4, padx=5, pady=5)

translate_button = tk.Button(output_frame, text='Translate', font=button_font, bg=button_color, command=translate)
clear_all_button = tk.Button(output_frame, text='Clear All', font=button_font, bg=button_color, command = clear_all)
play_morse_button = tk.Button(output_frame, text='Play Morse', font=button_font, bg=button_color, command = play_morse)
exit_button = tk.Button(output_frame, text='Exit', font=button_font, bg=button_color, command=root.destroy)

translate_button.grid(row=0, column=0, padx=10, ipadx=37)
play_morse_button.grid(row=1, column=0, padx=10, sticky='WE')
clear_all_button.grid(row=2, column=0, padx=10, sticky='WE')
exit_button.grid(row=3, column=0, padx=10, sticky='WE')


#Create instance of Balloon for tooltip 
tip = Pmw.Balloon(root)

#Bind button with balloon instance
tip.bind(generate_button, "Sentences are generated randomly")
tip.bind(alphanum_button, "Letter representation in morse code")
tip.bind(play_morse_button, "Audible dash and dots tones")

#Run window's main loop
root.mainloop()