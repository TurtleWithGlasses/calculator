import customtkinter as ctk
from buttons import Button, ImageButton
import darkdetect
from settings import *
from ctypes import windll, byref, sizeof, c_int
from PIL import Image, ImageTk

class Calculator(ctk.CTk):
    def __init__(self,is_dark):
        # setup
        super().__init__(fg_color=(WHITE,BLACK))
        self.title("Calculator")
        ctk.set_appearance_mode(f'{"dark" if is_dark else "light"}')
        self.geometry(f"{APP_SIZE[0]}x{APP_SIZE[1]}")
        self.resizable(False,False)
        self.title_bar_color(is_dark)

        # grid layout
        self.rowconfigure(list(range(MAIN_ROWS)), weight=1, uniform="a")
        self.columnconfigure(list(range(MAIN_COLUMNS)), weight=1, uniform="a")

        # data
        self.result_string = ctk.StringVar(value="0")
        self.formula_string = ctk.StringVar(value="")

        # widgets
        self.create_widgets()

        self.mainloop()

    def create_widgets(self):
        # fonts
        main_font = ctk.CTkFont(family=FONT,size=NORMAL_FONT_SIZE)
        result_font = ctk.CTkFont(family=FONT,size=OUTPUT_FONT_SIZE)

        # output labels
        OutputLabel(self,0,"se",main_font,self.formula_string)
        OutputLabel(self,1,"e",result_font,self.result_string)

        # clear button
        Button(parent=self,
               text= OPERATORS["clear"]["text"],
               func=self.clear,
               col=OPERATORS["clear"]["col"],
               row=OPERATORS["clear"]["row"],
               font=main_font)

        # percentage button
        Button(parent=self,
               text= OPERATORS["percent"]["text"],
               func=self.percent,
               col=OPERATORS["percent"]["col"],
               row=OPERATORS["percent"]["row"],
               font=main_font)

        # invert buutton
        invert_image = ctk.CTkImage(
            light_image=Image.open("invert_dark.png"),
            dark_image=Image.open("invert_light.png")
        )
        ImageButton(parent=self,
               image=invert_image,
               func=self.invert,
               col=OPERATORS["invert"]["col"],
               row=OPERATORS["invert"]["row"],
               )


    def clear(self):
        print("clear")

    def percent(self):
        print("percent")
    
    def invert(self):
        print("invert")

    def title_bar_color(self,is_dark):
        try:
            HWND = windll.user32.GetParent(self.winfo_id())
            DWMWA_ATTRIBUTE = 35
            COLOR = TITLE_BAR_HEX_COLORS["dark"] if is_dark else TITLE_BAR_HEX_COLORS["light"]
            windll.dwmapi.DwmSetWindowAttribute(HWND, DWMWA_ATTRIBUTE, byref(c_int(COLOR)),sizeof(c_int))
        except:
            pass

class OutputLabel(ctk.CTkLabel):
    def __init__(self,parent,row,anchor,font,string_var):
        super().__init__(parent,font=font,textvariable=string_var)
        self.grid(column=0,columnspan=4,row=row,sticky=anchor,padx=10)


if __name__ == "__main__":
    Calculator(True)