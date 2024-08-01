import tkinter as tk
from tkinter import ttk
from tkinter.colorchooser import askcolor
from tkinter.font import Font


root = tk.Tk()
root.iconbitmap('Tkapplogomain.ico')
root.minsize(500, 500)
root.title("Tkapp")
style = ttk.Style()
style.configure("TNotebook.Tab", font=("Poor Richard", 20))
background_color = "#222222"
root["background"] = background_color

# Icons. Thank You, Google!
standard_icon = tk.PhotoImage(file=r"standard_app_icon.png").subsample(5, 5)
data_icon = tk.PhotoImage(file=r"data_widget_icon.png").subsample(5, 5)
engineering_icon = tk.PhotoImage(file=r"engineering_widget_icon.png").subsample(5, 5)
special_icon = tk.PhotoImage(file=r"special_widgets_icon.png").subsample(5, 5)

# Color and Fonts
frame_title_text_background_color = "#222222"
frame_title_text_foreground_color = "white"
frame_title_text_font = ("Poor Richard", 30)
button_background = "white"
button_foreground = "#222222"

# Frames
widget_frame = tk.Frame(root, background=background_color, width=100)
widget_frame.pack(side="left", fill="both", padx=30)
tree_frame = tk.Frame(root, background=background_color)
tree_frame.pack(side="left", fill="both", padx=30)
edit_frame = tk.Frame(root, background=background_color, width=800)
edit_frame.pack(side="left", fill="both", padx=30)

# Control and model functions
def delete_selection():
    selection = view_tree.selection()[0]
    view_tree.delete(selection)

def duplicate_selection():
    selection = view_tree.selection()[0]
    item = view_tree.item(selection)
    text = item['text']
    values = item['values']
    view_tree.insert("", tk.END, text=text, values=values)

def edit_selection():
    pass


# View Tree
view_tree = ttk.Treeview(tree_frame)

def build_tree_frame():
    view_tree_title = tk.Label(tree_frame, text="View Tree", background=frame_title_text_background_color,
                               foreground=frame_title_text_foreground_color, font=frame_title_text_font)
    view_tree_title.grid(row=0, column=0, columnspan=3, pady=(0, 10))
    view_tree.grid(row=1, column=0, columnspan=3, sticky="swen")
    view_tree.heading("#0", text="Select Widget")

    delete_button = tk.Button(tree_frame, text="Delete", command=delete_selection, width=10, height=2,
                              background=button_background, foreground=button_foreground)
    delete_button.grid(row=2, column=0)

    duplicate_button = tk.Button(tree_frame, text="Duplicate", command=duplicate_selection, width=10, height=2,
                                 background=button_background, foreground=button_foreground)
    duplicate_button.grid(row=2, column=1)

    edit_button = tk.Button(tree_frame, text="Edit", command=edit_selection, width=10, height=2, background=button_background,
                            foreground=button_foreground)
    edit_button.grid(row=2, column=2)


def build_widget_frame():
    widgets_title = tk.Label(widget_frame, text="Widgets", background=frame_title_text_background_color,
                               foreground=frame_title_text_foreground_color, font=frame_title_text_font)
    widgets_title.grid(row=0, column=0, columnspan=1, pady=(0, 10))

    # widgets dimensions
    widget_width = 20
    widget_height = 30
    widget_font = ("Times New Roman", 15)

    standard_widgets = tk.Button(widget_frame, text="Standard", background=button_background, foreground=button_foreground, width=widget_width, height=widget_height, image=standard_icon, compound="left", font=widget_font)
    standard_widgets.grid(row=1, column=0, sticky="swen")

    data_widgets = tk.Button(widget_frame, text="Data", background=button_background,
                                 foreground=button_foreground, width=widget_width, height=widget_height, image=data_icon, compound="left", font=widget_font)
    data_widgets.grid(row=2, column=0, sticky="swen")

    engineering_widgets = tk.Button(widget_frame, text="Engineering", background=button_background,
                                 foreground=button_foreground, width=widget_width, height=widget_height, image=engineering_icon, compound="left", font=widget_font)
    engineering_widgets.grid(row=3, column=0, sticky="swen")

    special_widgets = tk.Button(widget_frame, text="Special", background=button_background,
                                 foreground=button_foreground, width=widget_width, height=widget_height, image=special_icon, compound="left", font=widget_font)
    special_widgets.grid(row=4, column=0, sticky="swen")

def build_edit_frame():
    edit_title = tk.Label(edit_frame, text="Edit", background=frame_title_text_background_color,
                               foreground=frame_title_text_foreground_color, font=frame_title_text_font,
                          justify="center")
    edit_title.grid(row=0, column=0)

def run_app():
    build_tree_frame()
    build_edit_frame()
    build_widget_frame()


run_app()
root.mainloop()