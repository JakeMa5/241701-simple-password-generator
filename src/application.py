
import customtkinter

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

        self.button = customtkinter.CTkButton(self, text="Generate", command=self.generate_password)
        self.output_label = customtkinter.CTkLabel(self)

        self.output_label.pack(padx=20, pady=25)
        self.button.pack(padx=20, pady=25)

    def generate_password(self):
        output = self.password.generate()
        self.output_label.configure(text=str(output))
