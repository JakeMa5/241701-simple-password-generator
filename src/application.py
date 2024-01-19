
import customtkinter
import pyperclip
import tkinter.messagebox

from module.third_party.nltk import WordGenerator
from module.password import Password

class Application(customtkinter.CTk):
    def __init__(self) -> None:
        super().__init__()

        self.geometry("400x200")
        self.resizable(False, False)

        self.wm_title = "Simple Password Generator"

        self.word_generator = WordGenerator()
        self.word_generator.download_content()

        self.password = Password(self.word_generator)
        self.output = ""

        self.gen_button = customtkinter.CTkButton(self, text="Generate", command=self.generate_password, fg_color=("#CC705F", "#CC705F"))
        self.copy_button = customtkinter.CTkButton(self, text="Copy to clipboard", command=self.copy_password, fg_color=("#CCCCCC", "#3A3A3A"), text_color=("#000000", "#FFFFFF"))
        self.output_label = customtkinter.CTkLabel(self)

        self.output_label.pack(padx=20, pady=25)
        self.output_label.configure(text="Click the button to start.")

        self.copy_button._state = "disabled"

        self.gen_button.pack(padx=20, pady=10)
        self.copy_button.pack(padx=20, pady=0)

    def generate_password(self) -> None:
        self.output = self.password.generate()
        self.output_label.configure(text=str(self.output))

        if self.output != "":
            self.copy_button._state = "normal"
        else:
            self.copy_button._state = "disabled"

    def copy_password(self) -> None:
        pyperclip.copy(str(self.output))
        tkinter.messagebox.showinfo("Success", "Password was copied successfully.")