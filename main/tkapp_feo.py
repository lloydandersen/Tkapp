import tkinter as tk
from tkinter import ttk
from tkinter.colorchooser import askcolor
from tkinter.font import Font
from tkinter.dialog import Dialog



root = tk.Tk()
root.iconbitmap('Tkapplogomain.ico')
root.minsize(500, 500)
root.title("Tkapp")
style = ttk.Style()
style.configure("TNotebook.Tab", font=("Poor Richard", 20))
background_color = "#222222"
root["background"] = background_color
standard_widget_values = [0, 0, 0, 0, 0, 0, "", 1, 1, "#222222", "white", ("arial", 16, "bold"), None, None, None, None,
                          None, None, None]

# Variables
widget_selection_var = tk.StringVar()
widget_name_var = tk.StringVar()
widget_iid_var = tk.StringVar()
row_var = tk.StringVar()
column_var = tk.StringVar()
padx_var = tk.StringVar()
pady_var = tk.StringVar()
ipadx_var = tk.StringVar()
ipady_var = tk.StringVar()
sticky_var = tk.StringVar()
rowspan_var = tk.StringVar()
columnspan_var = tk.StringVar()
background_color_var = tk.StringVar()
foreground_color_var = tk.StringVar()
font_var = tk.StringVar()
var_1 = tk.StringVar()
var_2 = tk.StringVar()
var_3 = tk.StringVar()
var_4 = tk.StringVar()
var_5 = tk.StringVar()
var_6 = tk.StringVar()
current_subtype_var = tk.StringVar()
sample_var_1 = tk.StringVar()
sample_var_2 = tk.StringVar()
sample_var_3 = tk.StringVar()


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
standard_dialog_frame = tk.Frame()
data_dialog_frame = tk.Frame()
engineering_dialog_frame = tk.Frame()
special_dialog_frame = tk.Frame()
standard_grid_frame = tk.Frame()
special_var_frame = tk.Frame(edit_frame)
color_frame = tk.Frame(special_var_frame)
work_frame = tk.Frame()


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


def select_a_color(type):
    global background_color_var
    color = tk.colorchooser.askcolor()[1]
    if type == 'background':
        background_color_var.set(f"{color}")
    else:
        foreground_color_var.set(f"{color}")




def save_edit():
    font_tuple = (f"{sample_var_1.get()}", sample_var_2.get(), f"{sample_var_3.get()}")
    font_var.set(font_tuple)
    row = row_var.get()
    column = column_var.get()
    padx = padx_var.get()
    pady = pady_var.get()
    ipadx = ipadx_var.get()
    ipady = ipady_var.get()
    sticky = sticky_var.get()
    rowspan = rowspan_var.get()
    columnspan = columnspan_var.get()
    background = background_color_var.get()
    foreground = foreground_color_var.get()
    font = font_var.get()
    one = var_1.get()
    two = var_2.get()
    three = var_3.get()
    four = var_4.get()
    five = var_5.get()
    six = var_6.get()
    subtype = current_subtype_var.get()
    edited_list = [row, column, padx, pady, ipadx, ipady, sticky, rowspan, columnspan, background, foreground, font,
                   one, two, three, four, five, six, subtype]

    name = widget_name_var.get()
    iid = widget_iid_var.get()
    view_tree.item(iid, text=name, values=edited_list)
    for child in edit_frame.winfo_children():
        child.destroy()
        build_edit_frame()


def build_grid_frame():
    global widget_name_var, widget_iid_var, row_var, column_var, padx_var, pady_var, ipadx_var, ipady_var, sticky_var
    global rowspan_var, columnspan_var, background_color_var, foreground_color_var, font_var, var_1, var_2, var_3
    global var_4, var_5, var_6, current_subtype_var

    standard_grid_frame = tk.Frame(edit_frame, background="#222222")
    standard_grid_frame.grid(row=1, column=0, padx=(10, 0))
    grid_title = tk.Label(standard_grid_frame, text="Placement", background=background_color, foreground="white", font=("Times New Roman", 18))
    grid_title.grid(row=0, column=0, columnspan=2)

    row_placement_label = tk.Label(standard_grid_frame, text="Row", background=background_color, foreground="white")
    row_placement_label.grid(row=1, column=0, padx=5, pady=5)

    row_placement_spinbox = tk.Spinbox(standard_grid_frame, textvariable=row_var, from_=0, to=50, state="readonly",
                                       background="white", foreground="#222222")
    row_placement_spinbox.grid(row=1, column=1)

    column_placement_label = tk.Label(standard_grid_frame, text="Column", background=background_color, foreground="white")
    column_placement_label.grid(row=2, column=0, padx=5, pady=5)

    column_placement_spinbox = tk.Spinbox(standard_grid_frame, textvariable=column_var, from_=0, to=50, state="readonly",
                                       background="white", foreground="#222222")
    column_placement_spinbox.grid(row=2, column=1)

    padx_placement_label = tk.Label(standard_grid_frame, text="Padx", background=background_color, foreground="white")
    padx_placement_label.grid(row=3, column=0, padx=5, pady=5)

    padx_placement_spinbox = tk.Spinbox(standard_grid_frame, textvariable=padx_var, from_=0, to=50, state="readonly",
                                       background="white", foreground="#222222")
    padx_placement_spinbox.grid(row=3, column=1)

    pady_placement_label = tk.Label(standard_grid_frame, text="Pady", background=background_color, foreground="white")
    pady_placement_label.grid(row=4, column=0, padx=5, pady=5)

    pady_placement_spinbox = tk.Spinbox(standard_grid_frame, textvariable=pady_var, from_=0, to=50, state="readonly",
                                       background="white", foreground="#222222")
    pady_placement_spinbox.grid(row=4, column=1)

    ipadx_placement_label = tk.Label(standard_grid_frame, text="Ipadx", background=background_color, foreground="white")
    ipadx_placement_label.grid(row=5, column=0, padx=5, pady=5)

    ipadx_placement_spinbox = tk.Spinbox(standard_grid_frame, textvariable=ipadx_var, from_=0, to=50, state="readonly",
                                       background="white", foreground="#222222")
    ipadx_placement_spinbox.grid(row=5, column=1)

    ipady_placement_label = tk.Label(standard_grid_frame, text="Ipady", background=background_color, foreground="white")
    ipady_placement_label.grid(row=6, column=0, padx=5, pady=5)

    ipady_placement_spinbox = tk.Spinbox(standard_grid_frame, textvariable=ipady_var, from_=0, to=50, state="readonly",
                                       background="white", foreground="#222222")
    ipady_placement_spinbox.grid(row=6, column=1)

    rowspan_placement_label = tk.Label(standard_grid_frame, text="Rowspan", background=background_color, foreground="white")
    rowspan_placement_label.grid(row=7, column=0, padx=5, pady=5)

    rowspan_placement_spinbox = tk.Spinbox(standard_grid_frame, textvariable=rowspan_var, from_=1, to=50, state="readonly",
                                       background="white", foreground="#222222")
    rowspan_placement_spinbox.grid(row=7, column=1)

    columnspan_placement_label = tk.Label(standard_grid_frame, text="Columnspan", background=background_color, foreground="white")
    columnspan_placement_label.grid(row=8, column=0, padx=5, pady=5)

    columnspan_placement_spinbox = tk.Spinbox(standard_grid_frame, textvariable=columnspan_var, from_=1, to=50, state="readonly",
                                       background="white", foreground="#222222")
    columnspan_placement_spinbox.grid(row=8, column=1)

    sticky_placement_frame = tk.Frame(standard_grid_frame, background=background_color)
    sticky_placement_frame.grid(row=9, column=0, columnspan=2)

    navi_button_background = "white"
    navi_button_foreground = "#222222"
    navi_button_width = 10
    navi_button_height = 3

    north_button = tk.Button(sticky_placement_frame, text="North", background=navi_button_background,
                             foreground=navi_button_foreground, command=lambda: sticky_var.set("n"), width=navi_button_width, height=navi_button_height)
    north_button.grid(row=0, column=1)

    northwest_button = tk.Button(sticky_placement_frame, text="NW", background=navi_button_background,
                             foreground=navi_button_foreground, command=lambda: sticky_var.set("nw"), width=navi_button_width, height=navi_button_height)
    northwest_button.grid(row=0, column=0)

    northeast_button = tk.Button(sticky_placement_frame, text="NE", background=navi_button_background,
                             foreground=navi_button_foreground, command=lambda: sticky_var.set("ne"), width=navi_button_width, height=navi_button_height)
    northeast_button.grid(row=0, column=2)

    east_button = tk.Button(sticky_placement_frame, text="East", background=navi_button_background,
                             foreground=navi_button_foreground, command=lambda: sticky_var.set("e"), width=navi_button_width, height=navi_button_height)
    east_button.grid(row=1, column=2)

    west_button = tk.Button(sticky_placement_frame, text="West", background=navi_button_background,
                             foreground=navi_button_foreground, command=lambda: sticky_var.set("w"), width=navi_button_width, height=navi_button_height)
    west_button.grid(row=1, column=0)

    south_button = tk.Button(sticky_placement_frame, text="South", background=navi_button_background,
                             foreground=navi_button_foreground, command=lambda: sticky_var.set("s"), width=navi_button_width, height=navi_button_height)
    south_button.grid(row=2, column=1)

    southeast_button = tk.Button(sticky_placement_frame, text="SE", background=navi_button_background,
                             foreground=navi_button_foreground, command=lambda: sticky_var.set("se"), width=navi_button_width, height=navi_button_height)
    southeast_button.grid(row=2, column=2)

    southwest_button = tk.Button(sticky_placement_frame, text="SW", background=navi_button_background,
                             foreground=navi_button_foreground, command=lambda: sticky_var.set("sw"), width=navi_button_width, height=navi_button_height)
    southwest_button.grid(row=2, column=0)
    center_button = tk.Button(sticky_placement_frame, text="Sticky", background=navi_button_background,
                             foreground=navi_button_foreground, command=lambda: sticky_var.set(""),
                             textvariable=sticky_var, width=navi_button_width, height=navi_button_height)
    center_button.grid(row=1, column=1)
    center_button.bind("<Button-3>", lambda e: sticky_var.set("swen"))

    # other building blocks
    color_frame = tk.Frame(standard_grid_frame)
    color_button_height = 3
    color_button_width = 10
    background_color_button = tk.Button(color_frame, text="Background", command=lambda: select_a_color("background"),
                                        width=color_button_width, height=color_button_height, font=font_var.get())

    background_color_button.grid(row=0, column=0)

    foreground_color_button = tk.Button(color_frame, text="Foreground", command=lambda: select_a_color("foreground"),
                                        width=color_button_width, height=color_button_height, font=font_var.get())
    foreground_color_button.grid(row=0, column=1)

    background_color_button['background'] = background_color_var.get()
    foreground_color_button['background'] = foreground_color_var.get()

    color_frame.grid(row=0, column=2)

    work_frame = tk.Frame(standard_grid_frame, background=background_color)
    work_frame.grid(row=1, column=2, rowspan=6)

    save_button = tk.Button(standard_grid_frame, text="Save", command=save_edit, width=10, height=3)
    save_button.grid(row=8, column=2)
    widget_type = current_subtype_var.get()

    test_font = font_var.get()

    system_font_list = []
    for family in tk.font.families():
        system_font_list.append(family)

    if widget_type == 'Label':
        text_label = tk.Label(work_frame, text="Text", background=background_color, foreground="white")
        text_label.grid(row=0, column=0, padx=5, pady=5)

        text_entry = tk.Entry(work_frame, textvariable=var_1, font=test_font)
        text_entry.grid(row=0, column=1)



        font_family_label = tk.Label(work_frame, text="Family", background=background_color, foreground="white")
        font_family_label.grid(row=2, column=0, padx=5, pady=5)

        font_family_entry = ttk.Combobox(work_frame, textvariable=sample_var_1, values=system_font_list)
        font_family_entry.grid(row=2, column=1)

        font_size_label = tk.Label(work_frame, text="Size", background=background_color, foreground="white")
        font_size_label.grid(row=3, column=0, padx=5, pady=5)

        font_size_entry = tk.Entry(work_frame, textvariable=sample_var_2)
        font_size_entry.grid(row=3, column=1)

        font_weight_label = tk.Label(work_frame, text="Weight", background=background_color, foreground="white")
        font_weight_label.grid(row=4, column=0, padx=5, pady=5)

        font_weight_entry = tk.Entry(work_frame, textvariable=sample_var_3)
        font_weight_entry.grid(row=4, column=1)





def edit_selection():
    global widget_name_var, widget_iid_var, row_var, column_var, padx_var, pady_var, ipadx_var, ipady_var, sticky_var
    global rowspan_var, columnspan_var, background_color_var, foreground_color_var, font_var, var_1, var_2, var_3
    global var_4, var_5, var_6, current_subtype_var
    selection = view_tree.selection()[0]
    item = view_tree.item(selection)
    widget_name = item['text']
    widget_values = item['values']
    print(widget_name, widget_values)


    # Set variables
    widget_name_var.set(widget_name)
    widget_iid_var.set(selection)
    row_var.set(widget_values[0])
    column_var.set(widget_values[1])
    padx_var.set(widget_values[2])
    pady_var.set(widget_values[3])
    ipadx_var.set(widget_values[4])
    ipady_var.set(widget_values[5])
    sticky_var.set(widget_values[6])
    rowspan_var.set(widget_values[7])
    columnspan_var.set(widget_values[8])
    background_color_var.set(widget_values[9])
    foreground_color_var.set(widget_values[10])
    font_var.set(widget_values[11])
    var_1.set(widget_values[12])
    var_2.set(widget_values[13])
    var_3.set(widget_values[14])
    var_4.set(widget_values[15])
    var_5.set(widget_values[16])
    var_6.set(widget_values[17])
    current_subtype_var.set(widget_values[18])
    font_list = []
    for item in font_var.get():
        font_list.append(item)

    sample_var_1.set(font_list)
    print(sample_var_1.get())
    sample_var_2.set("no")
    sample_var_3.set("no")
    print(font_var.get())
    build_grid_frame()



def add_selection_to_tree():
    selected_widget = widget_selection_var.get()
    if selected_widget != "":
        standard_widget_values[18] = selected_widget
        view_tree.insert("", tk.END, text=f"{selected_widget}", values=standard_widget_values)
    else:
        pass


# Widget Dialog Frames
def build_standard_dialog_frame():
    widget_selection_var.set("")
    standard_widgets_list = ['Button', 'Label', 'Toggle Button', 'Toggle Switch']
    dialog_box = tk.Toplevel(root, background=background_color)
    standard_dialog_frame = tk.Frame(dialog_box, background=background_color)
    standard_dialog_frame.pack(side="top", fill="both")

    selection_box = ttk.Combobox(standard_dialog_frame, textvariable=widget_selection_var, values=standard_widgets_list,
                                 state="readonly")
    selection_box.grid(row=0, column=0)

    selection_button = ttk.Button(standard_dialog_frame, text="Add", command=add_selection_to_tree)
    selection_button.grid(row=1, column=0, sticky="swen")
    widget_selection_var.set(standard_widgets_list[0])


def build_data_dialog_frame():
    widget_selection_var.set("")
    data_widgets_list = ['Plot', 'Bar']
    dialog_box = tk.Toplevel(root, background=background_color)
    data_dialog_frame = tk.Frame(dialog_box, background=background_color)
    data_dialog_frame.pack(side="top", fill="both")

    selection_box = ttk.Combobox(data_dialog_frame, textvariable=widget_selection_var, values=data_widgets_list,
                                 state="readonly")
    selection_box.grid(row=0, column=0)

    selection_button = ttk.Button(data_dialog_frame, text="Add", command=add_selection_to_tree)
    selection_button.grid(row=1, column=0, sticky="swen")
    widget_selection_var.set(data_widgets_list[0])


def build_engineering_dialog_frame():
    widget_selection_var.set("")
    engineering_widgets_list = ['Knob', 'Warning Light', 'Icon Light', 'Speedometer']
    dialog_box = tk.Toplevel(root, background=background_color)
    engineering_dialog_frame = tk.Frame(dialog_box, background=background_color)
    engineering_dialog_frame.pack(side="top", fill="both")

    selection_box = ttk.Combobox(engineering_dialog_frame, textvariable=widget_selection_var,
                                 values=engineering_widgets_list, state="readonly")
    selection_box.grid(row=0, column=0)

    selection_button = ttk.Button(engineering_dialog_frame, text="Add", command=add_selection_to_tree)
    selection_button.grid(row=1, column=0, sticky="swen")

    widget_selection_var.set(engineering_widgets_list[0])


def build_special_dialog_frame():
    special_widgets_list = ['Map', 'Calender']
    dialog_box = tk.Toplevel(root, background=background_color)
    special_dialog_frame = tk.Frame(dialog_box, background=background_color)
    special_dialog_frame.pack(side="top", fill="both")
    widget_selection_var.set(special_widgets_list[0])

    selection_box = ttk.Combobox(special_dialog_frame, textvariable=widget_selection_var, values=special_widgets_list,
                                 state="readonly")
    selection_box.grid(row=0, column=0)

    selection_button = ttk.Button(special_dialog_frame, text="Add", command=add_selection_to_tree)
    selection_button.grid(row=1, column=0, sticky="swen")


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

    edit_button = tk.Button(tree_frame, text="Edit", command=edit_selection, width=10, height=2,
                            background=button_background, foreground=button_foreground)
    edit_button.grid(row=2, column=2)


def build_widget_frame():
    widgets_title = tk.Label(widget_frame, text="Widgets", background=frame_title_text_background_color,
                             foreground=frame_title_text_foreground_color, font=frame_title_text_font)
    widgets_title.grid(row=0, column=0, columnspan=1, pady=(0, 10))

    # widgets dimensions
    widget_width = 100
    widget_height = 60
    widget_font = ("Times New Roman", 15)

    standard_widgets = tk.Button(widget_frame, text="Standard", background=button_background,
                                 foreground=button_foreground, width=widget_width, height=widget_height,
                                 image=standard_icon, compound="left", font=widget_font,
                                 command=build_standard_dialog_frame)
    standard_widgets.grid(row=1, column=0, sticky="swen", ipadx=50)

    data_widgets = tk.Button(widget_frame, text="Data", background=button_background,
                             foreground=button_foreground, width=widget_width, height=widget_height,
                             image=data_icon, compound="left", font=widget_font, command=build_data_dialog_frame)
    data_widgets.grid(row=2, column=0, sticky="swen")

    engineering_widgets = tk.Button(widget_frame, text="Engineering", background=button_background,
                                    foreground=button_foreground, width=widget_width, height=widget_height,
                                    image=engineering_icon, compound="left", font=widget_font,
                                    command=build_engineering_dialog_frame)
    engineering_widgets.grid(row=3, column=0, sticky="swen")

    special_widgets = tk.Button(widget_frame, text="Special", background=button_background,
                                foreground=button_foreground, width=widget_width, height=widget_height,
                                image=special_icon, compound="left", font=widget_font,
                                command=build_special_dialog_frame)
    special_widgets.grid(row=4, column=0, sticky="swen")


def build_edit_frame():
    edit_title = tk.Label(edit_frame, text="Edit", background=frame_title_text_background_color,
                          foreground=frame_title_text_foreground_color, font=frame_title_text_font, justify="center")
    edit_title.grid(row=0, column=0, columnspan=2)


def run_app():
    build_tree_frame()
    build_edit_frame()
    build_widget_frame()


run_app()
root.mainloop()
