import tkinter as tk
from tkinter import ttk, filedialog
from googletrans import Translator, LANGUAGES
from PIL import Image, ImageTk
from gtts import gTTS
from playsound import playsound
import os
import speech_recognition as sr


class LanguageTranslatorApp:
    # Intialization
    def __init__(self, root):
        self.root = root
        self.root.title("Language Translator")
        self.root.configure(bg="#CAE4F4")
        self.root.geometry("1080x850")  # Set the size of the root window

        self.text_var = tk.StringVar()
        self.language_var = tk.StringVar()
        self.language_var.set("en")  # Default language is English

        self.create_widgets()

    # Creating Widgets
    def create_widgets(self):

         # Language Translator Label
        translator_label = tk.Label(self.root, text="  Language Translator  ", font=("Helvetica", 20, "bold"),bg ="white",fg="black",padx=5,pady=5)
        translator_label.place(relx=0.5, rely=0.05, anchor="center") 

        # Input Text
        text_label = tk.Label(self.root, text="Enter Text to Translate:", bg="#CAE4F4", fg="black", font=('Helvetica', 16, 'bold'))
        text_label.place(x=150, y=70)
        
        self.text_widget = tk.Text(self.root, height=15, width=50, bg="white", fg="black", font=("Helvetica", 14))
        self.text_widget.place(x=350, y=70)

        # Listen Button
        listen_button = tk.Button(self.root, text="Listen", command=self.listen_and_update_text)
        listen_button.place(x=650, y=350)

        # Language Dropdown
        language_label = tk.Label(self.root, text="Select Target Language:", bg="#CAE4F4", fg="black", font=('Helvetica', 16, 'bold'))
        language_label.place(x=150, y=350)

        language_combobox = ttk.Combobox(self.root, values=list(LANGUAGES.values()), textvariable=self.language_var)
        language_combobox.place(x=350, y=350)
        language_combobox.set("english")  # Set default language to English

        # Translate Button
        translate_button = tk.Button(self.root, text="Translate", command=self.translate_text)
        translate_button.place(x=450, y=400)

        # Clear Text Button
        clear_button = tk.Button(self.root, text="Clear Text", command=self.clear_text)
        clear_button.place(x=550, y=400)

        # Browse Button
        browse_button = tk.Button(self.root, text="Browse Image", command=self.browse_image)
        browse_button.place(x=150, y=400)

        
        # Load the image for the button
        self.button_image = tk.PhotoImage(file="text_to_speech_icon copy.png")

        # Button to Convert Text to Speech
        convert_button = tk.Button(self.root, 
        image =self.button_image, command=self.convert_to_speech,bd=0)
        convert_button.place(x=300, y=390)

        # # Bind the click event to the function
        # convert_button.bind("<Button-1>", lambda event: self.convert_to_speech())

        # Know Basic Button
        know_basic_button = tk.Button(self.root, text="Know Basic", command=self.know_basic_info)
        know_basic_button.place(x=650, y=400)

        # Output Text
        output_label = tk.Label(self.root, text="Translated Text:", bg="#CAE4F4", fg="black", font=('Helvetica', 16, 'bold'))
        output_label.place(x=150, y=450)

        self.output_text = tk.Text(self.root, height=15, width=50, bg="white", fg="black", font=("Helvetica", 14))
        self.output_text.place(x=350, y=450)

    def browse_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
        # Set the file path to the image widget or handle the image processing as required

    """"
        # This function should handle the image conversion and text insertion
        # You need to implement the logic to extract text from the image
        # For example, you can use pytesseract or any other OCR library
        # For simplicity, I'll just insert a placeholder text into the text widget
        Functionn for img to text conversion
    def convert_image_to_text(self):
        if hasattr(self, 'image_path'):
            try:
                img = Image.open(self.image_path)
                text = pytesseract.image_to_string(img)
                self.text_display.delete(1.0, tk.END)  # Clear previous text
                self.text_display.insert(tk.END, text)
            except Exception as e:
                self.text_display.delete(1.0, tk.END)
                self.text_display.insert(tk.END, f"Error: {str(e)}")
        else:
            self.text_display.delete(1.0, tk.END)
            self.text_display.insert(tk.END, "Please select an image first.")        
        """
    def convert_to_speech(self): 
        try: 
            # Get text from input
            text = self.output_text.get("1.0", tk.END) 

            # Generate speech
            tts = gTTS(text=text, lang='en')
            tts.save("output.mp3")

            # Play speech
            playsound("output.mp3")

            # Delete temporary file
            os.remove("output.mp3") 

        except AssertionError:
            self.show_alert("No text Entered")
            
        
    def listen_and_update_text(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
        
        try:
            print("Recognizing...")
            text = recognizer.recognize_google(audio)
            self.text_widget.insert(tk.END, text)
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Error fetching results; {0}".format(e))

    # Function to show Alerts                   
    def show_alert(self,message):
        # Create a new Toplevel window
        alert_window = tk.Toplevel(self.root)
        alert_window.title("Alert")

        # Display the message in a Label widget
        alert_label = tk.Label(alert_window, text=message)
        alert_label.pack(padx=20, pady=10)

        # Add a button to close the alert window
        close_button = tk.Button(alert_window, text="OK", command=alert_window.destroy)
        close_button.pack(pady=10)

    # Function to know Basic_info
    def know_basic_info(self):
        # Retrieve the selected target language
        target_language = self.language_var.get()
        target_language = target_language.lower()

        # Open a new window to display the basic information
        self.display_basic_info(target_language)

    # Function to display Basic info
    def display_basic_info(self, language_name):

        # Create a new window for displaying basic information
        info_window = tk.Toplevel(self.root)
        info_window.title(f"Basic Information about {language_name}")
        info_window.geometry("900x900")
        info_window.configure(bg="#CAE4F4")
  
        #Basics  
        basic = """ 1. Greetings:
   -  Hi
   - How are you?
   - What's your name?

2. Introductions:
   - My name is...
   - I'm from...

3. Polite Expressions:
   - Thank you / Thanks
   - Excuse me / Sorry

4. Basic Questions:
   - Where is...?
   - How much does this cost?

5. Directions and Location:
   - Left / Right
   - Straight ahead

6. Numbers:
   - 1,2,3,4,5,6,7,8,9
   - How much? / How many?

7. Emergency Phrases:
   - Help!
   - I need a doctor / police

8. Farewells:
   - Goodbye / Bye
   - See you later / See you soon
    """
        translated_basic = self.translate(basic,language_name)
        # Display the basic information

        #Basics Label
        info_label = tk.Text(info_window,padx=20,
         height = 35,width = 35,pady=20,font=("Helvetica", 16),fg ="black",bg ="white")
        info_label.insert("end", basic)
        info_label.place(x=100,y=30)

        # Translated Basic Label
        basic_tranlated_label = tk.Text(info_window,width=35,height=35,  padx=20, pady=20,font=("Helvetica", 16),fg ="black",bg ="white")
        basic_tranlated_label.insert("end", translated_basic)
        basic_tranlated_label.place(x=500,y=30)  

    #function to translate and display translated text 
    def translate_text(self):
        text_to_translate = self.text_widget.get("1.0", tk.END)
        target_language = self.language_var.get()

        try:
            translator = Translator()
            translation = translator.translate(text_to_translate, dest=target_language)
            translated_text = translation.text
        except ValueError:
            self.show_alert("Invalid Language")
        except ConnectionError:
            self.show_alert("Unable to Reach server! Please try Again Later.")  
        except IndexError:
             self.show_alert("Input Text Empty")     
        

        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, translated_text)

    # Function to return translated text
    def translate(self,text_to_translate,target_language):
        translator = Translator()
        translation = translator.translate(text_to_translate, dest=target_language)
        translated_text = translation.text
        return translated_text
    
     # Clear Txt Function   
    def clear_text(self):
        self.text_widget.delete(1.0, tk.END)
        self.output_text.delete(1.0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = LanguageTranslatorApp(root)
    root.mainloop()


