from tkinter import *
from tkinter import ttk
import time

# Counters
frames = 0
buttons = 0
latt = 0






def open_add_file(inp, file_name):
    with open(f"{file_name}.py", "a") as file:
        file.write(f"{inp}")


def finish_script():
    open_add_file("""# Start run loop.
root.mainloop()
    """, f"{app_name_var}")
    exit()


def start_script():
    global app_name_var
    x = app_name_var.get()
    app_name_var = x
    open_add_file(f"""from tkinter import *
from tkinter import ttk
root = Tk()
root.geometry('300x300')
root.title("{app_name_var}")
    """, f"{app_name_var}")


def add_page():
    global frames
    frames += 1
    open_add_file(f"""
frame{frames} = Frame(root)
frame{frames}.grid(row=0, column={frames})

""", f"{app_name_var}")


def add_button():
    global buttons, frames
    buttons += 1
    open_add_file(f"""
b_{buttons} = Button(frame{frames}, text="click me")
b_{buttons}.grid(row={buttons}, column=0)

    """, f"{app_name_var}")


def add_label():
    global latt, frames
    latt += 1
    open_add_file(f"""
l_{latt} = Label(frame{frames}, text="hey what up")
l_{latt}.grid(row={frames},column=1)

    """, f"{app_name_var}")


root = Tk()
root.geometry("200x750")
root.title("Tkapp")
start_frame = Frame(root)
start_frame.grid(row=0, column=0)
app_name_var = StringVar()


app_name_entry = Entry(start_frame, textvariable=app_name_var, width=20)
app_name_entry.grid(row=2, column=1, sticky=W, pady=12, padx=12)

add_start_button = Button(start_frame, text='start', command=start_script, width=10, height=10)
add_start_button.grid(row=0, column=0, sticky=W, pady=12, padx=12)

add_page_button = Button(start_frame, text='add page', command=add_page, width=10, height=10)
add_page_button.grid(row=1, column=0, sticky=W, pady=12, padx=12)

add_button_button = Button(start_frame, text='add button', command=add_button, width=10, height=10)
add_button_button.grid(row=2, column=0, sticky=W, pady=12, padx=12)

add_label_button = Button(start_frame, text='add label', command=add_label, width=10, height=10)
add_label_button.grid(row=3, column=0, sticky=W, pady=12, padx=12)

add_finish_button = Button(start_frame, text='finish', command=finish_script, width=10, height=10)
add_finish_button.grid(row=0, column=1, sticky=W, pady=12, padx=12)

root.mainloop()
time.sleep(3)