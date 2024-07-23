import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime

root = tk.Tk()
root.geometry("700x700")
root.minsize(700, 500)
tkapp_notebook = ttk.Notebook(root)
tkapp_notebook.grid(row=0, column=0)
style = ttk.Style()

# Global vars
title_font = ("arial", 16)
style.configure("widget.TButton", font=("Times New Roman", 14))

# Widget and App Vars
app_name_var = tk.StringVar()
file_name_var = tk.StringVar()
widget_name_var = tk.StringVar()


# Tkapp Boilerplate Code
information_code = f"""# {app_name_var.get()} was created in Tkapp on {datetime.now()}.
Tkapp is a RAD tool created by Lloyd Andersen under the MIT license in 2024.
"""

start_code = f"""import tkinter as tk
from tkinter import ttk
"""

button_code = f"""{widget_name_var.get()} = tk.Button()
"""



# Widget frames controls


def close_widget_home_frame():
    widget_home_frame.grid_forget()


def widget_menu_go_back_to_home(current_frame):
    if current_frame == "page":
        widget_page_frame.grid_forget()
        widget_home_frame.grid(row=0, column=0, sticky="swen")
    elif current_frame == "label":
        widget_label_frame.grid_forget()
        widget_home_frame.grid(row=0, column=0, sticky="swen")
    elif current_frame == "button":
        widget_button_frame.grid_forget()
        widget_home_frame.grid(row=0, column=0, sticky="swen")
    elif current_frame == "entry":
        widget_entry_frame.grid_forget()
        widget_home_frame.grid(row=0, column=0, sticky="swen")
    elif current_frame == "box":
        widget_box_frame.grid_forget()
        widget_home_frame.grid(row=0, column=0, sticky="swen")
    elif current_frame == "control":
        widget_control_frame.grid_forget()
        widget_home_frame.grid(row=0, column=0, sticky="swen")
    elif current_frame == "graph":
        widget_graph_frame.grid_forget()
        widget_home_frame.grid(row=0, column=0, sticky="swen")
    elif current_frame == "dash":
        widget_dash_frame.grid_forget()
        widget_home_frame.grid(row=0, column=0, sticky="swen")
    elif current_frame == "info":
        widget_info_frame.grid_forget()
        widget_home_frame.grid(row=0, column=0, sticky="swen")
    elif current_frame == "time":
        widget_time_frame.grid_forget()
        widget_home_frame.grid(row=0, column=0, sticky="swen")


# Widget page frame
def open_widget_page_frame():
    close_widget_home_frame()
    widget_page_frame.grid(row=0, column=0, sticky="swen")
    back_button = ttk.Button(widget_page_frame, text="back", command=lambda: widget_menu_go_back_to_home("page"))
    back_button.grid(row=0, column=0, sticky="nw")

    # Widgets
    page_widget = ttk.Button(widget_page_frame, text="Page", style="widget.TButton")
    page_widget.grid(row=1, column=0, ipady=10)

    frame_widget = ttk.Button(widget_page_frame, text="Frame", style="widget.TButton")
    frame_widget.grid(row=1, column=1, ipady=10)

    vframe_widget = ttk.Button(widget_page_frame, text="vFrame", style="widget.TButton")
    vframe_widget.grid(row=2, column=0, ipady=10)

    hframe_widget = ttk.Button(widget_page_frame, text="hFrame", style="widget.TButton")
    hframe_widget.grid(row=2, column=1, ipady=10)

    canvas_widget = ttk.Button(widget_page_frame, text="Canvas", style="widget.TButton")
    canvas_widget.grid(row=3, column=0, ipady=10)

    treeview_widget = ttk.Button(widget_page_frame, text="Treeview", style="widget.TButton")
    treeview_widget.grid(row=3, column=1, ipady=10)

    menu_widget = ttk.Button(widget_page_frame, text="Menu", style="widget.TButton")
    menu_widget.grid(row=4, column=0, ipady=10)

    notebook_widget = ttk.Button(widget_page_frame, text="Notebook", style="widget.TButton")
    notebook_widget.grid(row=4, column=1, ipady=10)

    separator_widget = ttk.Button(widget_page_frame, text="Separator", style="widget.TButton")
    separator_widget.grid(row=5, column=0, ipady=10)

    text_widget = ttk.Button(widget_page_frame, text="Text", style="widget.TButton")
    text_widget.grid(row=5, column=1, ipady=10)

    row_configure_widget = ttk.Button(widget_page_frame, text="rConfigure", style="widget.TButton")
    row_configure_widget.grid(row=6, column=0, ipady=10)

    column_configure_widget = ttk.Button(widget_page_frame, text="cConfigure", style="widget.TButton")
    column_configure_widget.grid(row=6, column=1, ipady=10)


def open_widget_label_frame():
    close_widget_home_frame()
    widget_label_frame.grid(row=0, column=0, sticky="swen")
    back_button = ttk.Button(widget_label_frame, text="back", command=lambda: widget_menu_go_back_to_home("label"))
    back_button.grid(row=0, column=0, sticky="nw")

    # Widgets
    label_widget = ttk.Button(widget_label_frame, text="Label", style="widget.TButton")
    label_widget.grid(row=1, column=0, ipady=10)

    ttklabel_widget = ttk.Button(widget_label_frame, text="kLabel", style="widget.TButton")
    ttklabel_widget.grid(row=1, column=1, ipady=10)


def open_widget_button_frame():
    close_widget_home_frame()
    widget_button_frame.grid(row=0, column=0, sticky="swen")
    back_button = ttk.Button(widget_button_frame, text="back", command=lambda: widget_menu_go_back_to_home("button"))
    back_button.grid(row=0, column=0, sticky="nw")

    # Widgets
    button_widget = ttk.Button(widget_button_frame, text="Button", style="widget.TButton")
    button_widget.grid(row=1, column=0, ipady=10)

    ttkbutton_widget = ttk.Button(widget_button_frame, text="kButton", style="widget.TButton")
    ttkbutton_widget.grid(row=1, column=1, ipady=10)

    toggle_button_widget = ttk.Button(widget_button_frame, text="tButton", style="widget.TButton")
    toggle_button_widget.grid(row=2, column=0, ipady=10)

    toggle_switch_widget = ttk.Button(widget_button_frame, text="tSwitch", style="widget.TButton")
    toggle_switch_widget.grid(row=2, column=1, ipady=10)

    toggle_swing_switch_widget = ttk.Button(widget_button_frame, text="sSwitch", style="widget.TButton")
    toggle_swing_switch_widget.grid(row=3, column=0, ipady=10)


def open_widget_entry_frame():
    close_widget_home_frame()
    widget_entry_frame.grid(row=0, column=0, sticky="swen")
    back_button = ttk.Button(widget_entry_frame, text="back", command=lambda: widget_menu_go_back_to_home("entry"))
    back_button.grid(row=0, column=0, sticky="nw")

    # Widgets
    entry_widget = ttk.Button(widget_entry_frame, text="Entry", style="widget.TButton")
    entry_widget.grid(row=1, column=0, ipady=10)

    validated_entry_widget = ttk.Button(widget_entry_frame, text="vEntry", style="widget.TButton")
    validated_entry_widget.grid(row=1, column=1, ipady=10)


def open_widget_box_frame():
    close_widget_home_frame()
    widget_box_frame.grid(row=0, column=0, sticky="swen")
    back_button = ttk.Button(widget_box_frame, text="back", command=lambda: widget_menu_go_back_to_home("box"))
    back_button.grid(row=0, column=0, sticky="nw")

    # Widgets
    combobox_widget = ttk.Button(widget_box_frame, text="Combobox", style="widget.TButton")
    combobox_widget.grid(row=1, column=0, ipady=10)

    spinbox_widget = ttk.Button(widget_box_frame, text="Spinbox", style="widget.TButton")
    spinbox_widget.grid(row=1, column=1, ipady=10)


def open_widget_control_frame():
    close_widget_home_frame()
    widget_control_frame.grid(row=0, column=0, sticky="swen")
    back_button = ttk.Button(widget_control_frame, text="back", command=lambda: widget_menu_go_back_to_home("control"))
    back_button.grid(row=0, column=0, sticky="nw")

    # Widgets
    dial_widget = ttk.Button(widget_control_frame, text="Dial", style="widget.TButton")
    dial_widget.grid(row=1, column=0, ipady=10)

    power_tower_widget = ttk.Button(widget_control_frame, text="PowerTower", style="widget.TButton")
    power_tower_widget.grid(row=1, column=1, ipady=10)

    slider_widget = ttk.Button(widget_control_frame, text="Slider", style="widget.TButton")
    slider_widget.grid(row=2, column=0, ipady=10)

    throttle_widget = ttk.Button(widget_control_frame, text="Throttle", style="widget.TButton")
    throttle_widget.grid(row=2, column=1, ipady=10)

    keypad_widget = ttk.Button(widget_control_frame, text="Keypad", style="widget.TButton")
    keypad_widget.grid(row=3, column=0, ipady=10)

    keyboard_widget = ttk.Button(widget_control_frame, text="Keyboard", style="widget.TButton")
    keyboard_widget.grid(row=3, column=1, ipady=10)

    navimenu_widget = ttk.Button(widget_control_frame, text="Navimenu", style="widget.TButton")
    navimenu_widget.grid(row=4, column=0, ipady=10)

    joystick_widget = ttk.Button(widget_control_frame, text="Joystick", style="widget.TButton")
    joystick_widget.grid(row=4, column=1, ipady=10)


def open_widget_graph_frame():
    close_widget_home_frame()
    widget_graph_frame.grid(row=0, column=0, sticky="swen")
    back_button = ttk.Button(widget_graph_frame, text="back", command=lambda: widget_menu_go_back_to_home("graph"))
    back_button.grid(row=0, column=0, sticky="nw")




def open_widget_dash_frame():
    close_widget_home_frame()
    widget_dash_frame.grid(row=0, column=0, sticky="swen")
    back_button = ttk.Button(widget_dash_frame, text="back", command=lambda: widget_menu_go_back_to_home("dash"))
    back_button.grid(row=0, column=0, sticky="nw")



def open_widget_info_frame():
    close_widget_home_frame()
    widget_info_frame.grid(row=0, column=0, sticky="swen")
    back_button = ttk.Button(widget_info_frame, text="back", command=lambda: widget_menu_go_back_to_home("info"))
    back_button.grid(row=0, column=0, sticky="nw")


def open_widget_time_frame():
    close_widget_home_frame()
    widget_time_frame.grid(row=0, column=0, sticky="swen")
    back_button = ttk.Button(widget_time_frame, text="back", command=lambda: widget_menu_go_back_to_home("time"))
    back_button.grid(row=0, column=0, sticky="nw")

    # Widgets
    analog_widget = ttk.Button(widget_time_frame, text="Analog", style="widget.TButton")
    analog_widget.grid(row=1, column=0, ipady=10)

    digital_widget = ttk.Button(widget_time_frame, text="Digital", style="widget.TButton")
    digital_widget.grid(row=1, column=1, ipady=10)

    timer_widget = ttk.Button(widget_time_frame, text="Timer", style="widget.TButton")
    timer_widget.grid(row=2, column=0, ipady=10)

    calender_widget = ttk.Button(widget_time_frame, text="Calender", style="widget.TButton")
    calender_widget.grid(row=2, column=1, ipady=10)

    date_slider_widget = ttk.Button(widget_time_frame, text="Slider", style="widget.TButton")
    date_slider_widget.grid(row=3, column=0, ipady=10)

    date_spinner_widget = ttk.Button(widget_time_frame, text="Spinner", style="widget.TButton")
    date_spinner_widget.grid(row=3, column=1, ipady=10)


# Global Styles
build_page = ttk.Frame(tkapp_notebook)
tkapp_notebook.add(build_page, text="Build")

style_page = ttk.Frame(tkapp_notebook)
tkapp_notebook.add(style_page, text="Style")

create_page = ttk.Frame(tkapp_notebook)
tkapp_notebook.add(create_page, text="Create")

# Build Page
# Widget Frames
widget_home_frame = ttk.Frame(build_page)
widget_home_frame.grid(row=0, column=0, padx=(5, 0), pady=5)

widget_home_frame_title = ttk.Label(widget_home_frame, text="Widgets", font=title_font)
widget_home_frame_title.grid(row=0, column=0)

widget_home_title_seperator = ttk.Separator(widget_home_frame, orient="vertical")
widget_home_title_seperator.grid(row=1, column=0, sticky="swen")
# Widget Frame Open Buttons
widget_page_button = ttk.Button(widget_home_frame, text="Page", style="widget.TButton",
                                command=open_widget_page_frame)
widget_page_button.grid(row=2, column=0)

widget_label_button = ttk.Button(widget_home_frame, text="Label", style="widget.TButton",
                                 command=open_widget_label_frame)
widget_label_button.grid(row=3, column=0)

widget_button_button = ttk.Button(widget_home_frame, text="Button", style="widget.TButton",
                                  command=open_widget_button_frame)
widget_button_button.grid(row=4, column=0)

widget_entry_button = ttk.Button(widget_home_frame, text="Entry", style="widget.TButton",
                                 command=open_widget_entry_frame)
widget_entry_button.grid(row=5, column=0)

widget_box_button = ttk.Button(widget_home_frame, text="Box", style="widget.TButton",
                               command=open_widget_box_frame)
widget_box_button.grid(row=6, column=0)

widget_control_button = ttk.Button(widget_home_frame, text="Controls", style="widget.TButton",
                                   command=open_widget_control_frame)
widget_control_button.grid(row=7, column=0)

widget_graph_button = ttk.Button(widget_home_frame, text="Graph", style="widget.TButton",
                                 command=open_widget_graph_frame)
widget_graph_button.grid(row=8, column=0)

widget_dash_button = ttk.Button(widget_home_frame, text="Dash", style="widget.TButton",
                                command=open_widget_dash_frame)
widget_dash_button.grid(row=9, column=0)

widget_info_button = ttk.Button(widget_home_frame, text="Info", style="widget.TButton",
                                command=open_widget_info_frame)
widget_info_button.grid(row=10, column=0)

widget_time_button = ttk.Button(widget_home_frame, text="Time", style="widget.TButton",
                                command=open_widget_time_frame)
widget_time_button.grid(row=11, column=0)

# Widget Storage Frames
widget_page_frame = ttk.Frame(build_page)
widget_label_frame = ttk.Frame(build_page)
widget_button_frame = ttk.Frame(build_page)
widget_entry_frame = ttk.Frame(build_page)
widget_box_frame = ttk.Frame(build_page)
widget_control_frame = ttk.Frame(build_page)
widget_graph_frame = ttk.Frame(build_page)
widget_dash_frame = ttk.Frame(build_page)
widget_info_frame = ttk.Frame(build_page)
widget_time_frame = ttk.Frame(build_page)


# Tree Frames
tree_frame = ttk.Frame(build_page)
tree_frame.grid(row=0, column=2, sticky="swen")

widget_tree = ttk.Treeview(tree_frame, height=15)
widget_tree.grid(row=0, column=0, sticky="swen")
widget_tree.heading("#0", text="Widget View")

# Tree Frame Controls
tree_frame_buttons_frame = ttk.Frame(tree_frame)
tree_frame_buttons_frame.grid(row=1, column=0, sticky="swen")
tree_frame_delete_button = ttk.Button(tree_frame_buttons_frame, text="Delete")
tree_frame_delete_button.grid(row=0, column=0)

tree_frame_duplicate_button = ttk.Button(tree_frame_buttons_frame, text="Duplicate")
tree_frame_duplicate_button.grid(row=0, column=1)

tree_frame_edit_button = ttk.Button(tree_frame_buttons_frame, text="Edit")
tree_frame_edit_button.grid(row=0, column=2)

# Edit Frames


def edit_frame_control():
    pass


# Build Page Separators
build_page_left_separator = ttk.Separator(build_page, orient="vertical")
build_page_left_separator.grid(row=0, column=1, sticky="swen", ipadx=5, padx=(8, 0))

build_page_right_separator = ttk.Separator(build_page, orient="vertical")
build_page_right_separator.grid(row=0, column=3, sticky="swen", ipadx=5, padx=(8, 0))

build_page_bottom_separator = ttk.Separator(build_page, orient="horizontal")
build_page_right_separator.grid(row=1, column=0, columnspan=4, sticky="swen", ipady=1, pady=(5, 0))

def save_app_file():
    pass


def save_app_dialog():
    answer = tk.messagebox.askyesno("Save App", "Do you want to save this App?")
    if answer is True:
        save_app_file()
        tk.messagebox.showinfo("Save Confirmation", "App Save Successful!")
    else:
        pass


def open_app_file():
    pass


def open_app_dialog():
    answer = tk.messagebox.askyesno("Open App", "Do you want to open this App?")
    if answer is True:
        open_app_file()
    else:
        pass


def create_tkapp():
    pass


def create_tkapp_dialog():
    answer = tk.messagebox.askyesno("Create Tkapp", "Do you want to create a Tkapp?")
    if answer is True:
        create_page
    else:
        pass


# Create Page
save_app_button = ttk.Button(create_page, text="Save", command=save_app_dialog)
save_app_button.grid(row=0, column=0)

open_app_button = ttk.Button(create_page, text="Open", command=open_app_dialog)
open_app_button.grid(row=1, column=0)

create_tkapp_button = ttk.Button(create_page, text="Create", command=create_tkapp_dialog)
create_tkapp_button.grid(row=2, column=0)

root.mainloop()
