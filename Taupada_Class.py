import tkinter as tk
from tkinter import ttk
from random import choice
from tkinter import scrolledtext

class Taupada(tk.Tk):
    def __init__(self, title, size):
        
        # main setup
        super().__init__()
        self.title(title)
        self.geometry(f'{size[0]}x{size[1]}')
        self.minsize(size[0],size[1])
        self.maxsize(size[0],size[1])
        
        # widgets
        self.menu = Menu(self)
        self.main = Main(self)
        
        # run the app
        self.mainloop()
 
class Menu(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(x=0, y=0, relwidth=0.3, relheight=1)
        self.create_widgets()
        
    def create_widgets(self):
        
        # create the widgets
        menu_button1 = ttk.Button(self, text = 'Button1')
        menu_button2 = ttk.Button(self, text = 'Button2')
        menu_button3 = ttk.Button(self, text = 'Button3')
        
        menu_slider1 = ttk.Scale(self, orient = 'vertical')
        menu_slider2 = ttk.Scale(self, orient = 'vertical')
        
        toggle_frame = ttk.Frame(self)
        menu_toggle1 = ttk.Checkbutton(toggle_frame, text = 'check 1')
        menu_toggle2 = ttk.Checkbutton(toggle_frame, text = 'check 2')
        
        # create the grid
        self.columnconfigure((0,1,2), weight=1, uniform='a')
        self.rowconfigure((0,1,2,3,4), weight=1, uniform='a')

        # place the widgets
        # menu_button1.grid(row=0, column=0, sticky='nswe', columnspan=2)
        # menu_button2.grid(row=0, column=2, sticky='nswe')
        # menu_button3.grid(row=1, column=0, sticky='nsew', columnspan=3)
        
        # menu_slider1.grid(row=2, column=0, sticky='nsew', rowspan=2, pady=20)
        # menu_slider2.grid(row=2, column=2, sticky='nsew', rowspan=2, pady=20)
        
        # # toggle layout
        # toggle_frame.grid(row=4, column=0, columnspan=3, sticky='nsew')
        # menu_toggle1.pack(side='left', expand=True)
        # menu_toggle2.pack(side='left', expand=True)
        

class Main(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(relx=0.3, y=0, relwidth=0.7, relheight=1)
        
        check_var1 = tk.IntVar()
        check_var2 = tk.IntVar()
        check_var3 = tk.IntVar()
        check_var4 = tk.IntVar()
        check_var5 = tk.IntVar()
        check_var6 = tk.IntVar()
        
        Entry(self, 'Inst 1', check_var1)
        Entry(self, 'Inst 2', check_var2)
        Entry(self, 'Inst 3', check_var3)
        Entry(self, 'Inst 4', check_var4)
        Entry(self, 'Inst 5', check_var5)
        Entry(self, 'Inst 6', check_var6)
        


        
class Entry(ttk.Frame):
    def __init__(self, parent, toggle_text, check_var):
        super().__init__(parent)
        
        toggle = ttk.Checkbutton(self, text = toggle_text, command=lambda:print(check_var.get()), variable=check_var)
        label = ttk.Label(self, text=toggle_text+'\nVolume') 
        slider = ttk.Scale(self, orient = 'vertical')

        toggle.pack(expand=True)
        label.pack(expand=True)
        slider.pack(expand=True, fill='both')

        self.pack(side='left', expand=True, fill='both', padx=20, pady=20)

# Run the App
Taupada('Taupada', (1200,600))