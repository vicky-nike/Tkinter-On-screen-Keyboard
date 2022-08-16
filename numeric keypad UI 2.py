from tkinter import *
from tkinter import ttk
import tkinter.font as tkfont

root = Tk()
root.state('zoomed')
#root.attributes("-fullscreen", True)
key = None
keyboard_list = []

def clear_keyboard_list(event, var):
    keyboard_list.clear()
    keyboard_list.extend([var])

def check_keyboard(event):
    if key is None:
        display_keyboard()
    try:
        key.destroy()
        display_keyboard()
    except TclError:
        display_keyboard()

def display_keyboard():
    global key
    key = Toplevel(root)
    key.title('On Screen Keyboard')
     # get screen height and width
    positionRight = int(root.winfo_screenwidth()/2 - 270/2)
    positionDown = int(root.winfo_screenheight()/2 - 350/2)
    
    key.geometry("{}x{}+{}+{}".format(270, 350, (positionRight-400), (positionDown+150)))
    style = ttk.Style()
    key.configure(bg='gray27')
    style.configure('TButton', background='gray21')
    style.configure('TButton', foreground='white')
    style.map('TButton', foreground=[('active', 'black')])

    global theme
    theme = "light"
    global is_shift
    is_shift = False

    def press(num):
        global currentEntry
        currentEntry = keyboard_list[0]
        current = currentEntry.get()
        currentEntry.delete(0, END)
        currentEntry.insert(0, str(current) + str(num))

    def Backspace():
        current = currentEntry.get()
        currentEntry.delete(len(current)-1)

    def Clear():
        currentEntry.delete(0, END)

    def Theme():
        global theme
        if theme == "dark":
            key.configure(bg='gray27')
            style.configure('TButton', background='gray21')
            style.configure('TButton', foreground='white')
            style.map('TButton', foreground=[('active', 'black')])
            theme = "light"
        elif theme == "light":
            key.configure(bg='gray99')
            style.configure('TButton', background='azure')
            style.configure('TButton', foreground='black', cursor='man')
            style.map('TButton', foreground=[('active', 'white')], background=[('active', 'grey')])
            theme = "dark"
    
    def keyboard_display():
            # Adding keys line wise
            # First Line Button
            num7 = ttk.Button(key, text='7', command=lambda: press('7'))
            num7.place(anchor='w', relheight=0.2, relwidth=0.29, relx=0.03, rely=0.12)

            num8 = ttk.Button(key, text='8', command=lambda: press('8'))
            num8.place(anchor='w', relheight=0.2, relwidth=0.29, relx=0.35, rely=0.12)
            
            num9 = ttk.Button(key, text='9', command=lambda: press('9'))
            num9.place(anchor='w', relheight=0.2, relwidth=0.29, relx=0.675, rely=0.12)

            num4 = ttk.Button(key, text='4', command=lambda: press('4'))
            num4.place(anchor='w', relheight=0.2, relwidth=0.29, relx=0.03, rely=0.33)

            num5 = ttk.Button(key, text='5', command=lambda: press('5'))
            num5.place(anchor='w', relheight=0.2, relwidth=0.29, relx=0.35, rely=0.33)

            num6 = ttk.Button(key, text='6', command=lambda: press('6'))
            num6.place(anchor='w', relheight=0.2, relwidth=0.29, relx=0.675, rely=0.33)

            num1 = ttk.Button(key, text='1', command=lambda: press('1'))
            num1.place(anchor='w', relheight=0.2, relwidth=0.29, relx=0.03, rely=0.54)

            num2 = ttk.Button(key, text='2', command=lambda: press('2'))
            num2.place(anchor='w', relheight=0.2, relwidth=0.29, relx=0.35, rely=0.54)

            num3 = ttk.Button(key, text='3', command=lambda: press('3'))
            num3.place(anchor='w', relheight=0.2, relwidth=0.29, relx=0.675, rely=0.54)

            num0 = ttk.Button(key, text='0', command=lambda: press('0'))
            num0.place(anchor='w', relheight=0.2, relwidth=0.29, relx=0.03, rely=0.75)

            dot = ttk.Button(key, text='.', command=lambda: press('.'))
            dot.place(anchor='w', relheight=0.2, relwidth=0.29, relx=0.35, rely=0.75)

            backspace = ttk.Button(key, text='Backspace', command=Backspace)
            backspace.place(anchor='w', relheight=0.2, relwidth=0.29, relx=0.675, rely=0.75)

            theme = ttk.Button(key, text='Theme', command=Theme)
            theme.place(anchor='w', relheight=0.12, relwidth=0.452, relx=0.03, rely=0.925)
            
            enter = ttk.Button(key, text='Close', command=lambda: key.destroy())
            enter.place(anchor='w', relheight=0.12, relwidth=0.452, relx=0.515, rely=0.925)

    keyboard_display()

def rootFocus():
    root.focus()


label1 = Label(root, text='enter')
entry1 = Entry(root, borderwidth=1)
entry1.bind('<Button-1>', lambda event:clear_keyboard_list(event, entry1), add="+")
entry1.bind('<Button-1>', check_keyboard, add="+")

label1.place(anchor=W, relheight=0.05, relwidth=0.40, relx=0.35, rely=0.15)
entry1.place(anchor=W, relheight=0.05, relwidth=0.40, relx=0.35, rely=0.35)

root.mainloop()