
import pyperclip
import ttkbootstrap as ttb
from slugify import slugify
from ttkbootstrap.constants import *


def get_slug(line_string: str) -> str:
    line_string = line_string.replace('й', 'j')
    line_string = line_string.replace('ё', 'e')
    line_string = line_string.replace('я', 'ya')
    result = slugify(line_string)  # allow_unicode = True
    # print(result)
    return result


class App(ttb.Window):
    def __init__(self):
        super().__init__()

        self.style.theme_use("superhero")
        self.geometry("483x246+700+300")

        # self.wm_iconbitmap(f"src/transparent.ico")

        self.tk.call('tk', 'scaling', 1.2)
        self.title("Transliterate text")
        self.resizable(False, False)

        self.input = ttb.Text(height=4, width=75)
        self.input.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky=NW)

        self.result = ttb.Text(height=4, width=75)
        self.result.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky=NW)

        self.btn_generate = ttb.Button(
            self, bootstyle="success",
            text="Translit", width=33, command=self.click_btn_generate)
        self.btn_generate.grid(row=3, column=0, padx=10, pady=10, sticky=NW)

        self.btn_copy = ttb.Button(
            self, bootstyle="info",
            text="Copy", width=33, command=self.click_btn_copy)
        self.btn_copy.grid(row=3, column=1, padx=10, pady=10, sticky=NW)

        self.result.bind('<FocusIn>', lambda e: self.click_btn_generate())
        self.input.bind('<FocusIn>', lambda e: self.paste_buffer_input())

    def click_btn_generate(self, *args):

        self.result.configure(state=NORMAL)
        self.result.delete("1.0", END)

        result = get_slug(self.input.get('1.0', END))
        self.result.insert('1.0', result)
        self.result.configure(state=DISABLED)

    def click_btn_copy(self):
        self.click_btn_generate()
        result = self.result.get('1.0', END)
        if result:
            pyperclip.copy(result)

    def paste_buffer_input(self, *args):
        text = pyperclip.paste()
        # print(text)
        self.input.insert("1.0", text)


if __name__ == "__main__":
    app = App()
    app.mainloop()
