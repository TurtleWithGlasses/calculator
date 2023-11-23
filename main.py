import customtkinter as ctk
import darkdetect
from settings import *
from ctypes import windll, byref, sizeof, c_int

class Calculator(ctk.CTk):
    def __init__(self,is_dark):
        # setup
        super().__init__(fg_color=(WHITE,BLACK))
        self.title("Calculator")
        ctk.set_appearance_mode(f'{"dark" if is_dark else "light"}')
        self.geometry(f"{APP_SIZE[0]}x{APP_SIZE[1]}")
        self.resizable(False,False)
        self.title_bar_color(is_dark)

        self.mainloop()

    def title_bar_color(self,is_dark):
        try:
            HWND = windll.user32.GetParent(self.winfo_id())
            DWMWA_ATTRIBUTE = 35
            COLOR = TITLE_BAR_HEX_COLORS["dark"] if is_dark else TITLE_BAR_HEX_COLORS["light"]
            windll.dwmapi.DwmSetWindowAttribute(HWND, DWMWA_ATTRIBUTE, byref(c_int(COLOR)),sizeof(c_int))
        except:
            pass

if __name__ == "__main__":
    Calculator(darkdetect.isLight())