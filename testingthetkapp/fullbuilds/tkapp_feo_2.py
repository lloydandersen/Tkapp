import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter import filedialog
from tkinter import colorchooser

root = tk.Tk()
root.title("Tkapp")
root.minsize(700, 500)


# var
app_name_var = tk.StringVar()
file_name_var = tk.StringVar()
primary_color_var = tk.StringVar()
secondary_color_var = tk.StringVar()
body_font_type_var = tk.StringVar()
body_font_size_var = tk.StringVar()
primary_color_text_bool = True
secondary_color_text_bool = True

# group var
edit_var_1 = tk.StringVar()
edit_var_2 = tk.StringVar()
edit_var_3 = tk.StringVar()
edit_var_4 = tk.StringVar()
edit_var_5 = tk.StringVar()
edit_var_6 = tk.StringVar()
edit_var_7 = tk.StringVar()
edit_var_8 = tk.StringVar()
edit_var_9 = tk.StringVar()
edit_var_10 = tk.StringVar()
edit_var_11 = tk.StringVar()
edit_var_12 = tk.StringVar()
edit_var_13 = tk.StringVar()
edit_var_14 = tk.StringVar()
edit_var_15 = tk.StringVar()
edit_var_16 = tk.StringVar()
edit_var_17 = tk.StringVar()
edit_var_18 = tk.StringVar()
edit_var_19 = tk.StringVar()
edit_var_20 = tk.StringVar()
edit_var_21 = tk.StringVar()
edit_var_22 = tk.StringVar()


# Widget stuff
widget_name = tk.StringVar()
widget_iid = tk.StringVar()
widget_parent = tk.StringVar()
widget_type = tk.StringVar()


# Set variables
body_font_size_var.set("16")
body_font_type_var.set("Times New Roman")

# Program Lists/dictionaries
system_font_family_list = list()


# Functions
def get_system_font_families():
    families = tk.font.families()
    for fonts in families:
        system_font_family_list.append(fonts)
        system_font_family_list.sort()


def chose_primary_color():
    chosen_color = tk.colorchooser.askcolor(title="Primary Color")
    primary_color_var.set(f"{chosen_color[1]}")
    primary_color_button["relief"] = "flat"
    primary_color_button["background"] = chosen_color[1]


def chose_secondary_color():
    chosen_color = tk.colorchooser.askcolor(title="Secondary Color")
    secondary_color_var.set(chosen_color[1])
    secondary_color_button["relief"] = "flat"
    secondary_color_button["background"] = chosen_color[1]


def primary_text_color_changer(*args):
    global primary_color_text_bool
    if primary_color_text_bool is True:
        primary_color_button["foreground"] = "white"
        primary_color_text_bool = False

    else:
        primary_color_button["foreground"] = "black"
        primary_color_text_bool = True


def secondary_text_color_changer(*args):
    global secondary_color_text_bool
    if secondary_color_text_bool is True:
        secondary_color_button["foreground"] = "white"

        secondary_color_text_bool = False
    else:
        secondary_color_button["foreground"] = "black"
        secondary_color_text_bool = True


def update_color_box_font(*args):
    new_type = body_font_type_var.get()
    new_size = body_font_size_var.get()
    primary_color_button["font"] = (f"{new_type}", new_size)
    secondary_color_button["font"] = (f"{new_type}", new_size)


# Product view tree functions

# Product name count
database_count = 0
encrypted_database_count = 0
account_database_count = 0
spreadsheet_count = 0
variables_count = 0
connections_count = 0


def add_database_to_datatree():
    global database_count
    data_tree.insert("", tk.END, text=f"Database_{database_count}",
                     values=['column_1', 'col_1', 'column_2', 'col_2', None, None, None, None, None, None, None, None,
                             None, None, None, None, None, None, None, None, None, None, "Database"])
    database_count += 1


def add_encrypted_database_to_datatree():
    global encrypted_database_count
    data_tree.insert("", tk.END, text=f"Encrptyeddb_{encrypted_database_count}",
                     values=['column_1', 'col_1', 'column_2', 'col_2', None, None, None, None, None, None, None, None,
                             None, None, None, None, None, None, None, None, None, None, "EncryptedDB"])
    encrypted_database_count += 1


def add_account_database_to_datatree():
    global account_database_count
    data_tree.insert("", tk.END, text=f"Accountdb_{account_database_count}",
                     values=['column_1', 'col_1', 'column_2', 'col_2', None, None, None, None, None, None, None, None,
                             None, None, None, None, None, None, None, None, None, None, "AccountDB"])
    account_database_count += 1


def add_spreadsheet_to_datatree():
    global spreadsheet_count
    data_tree.insert("", tk.END, text=f"Spreadsheet_{spreadsheet_count}", values=['column_1', 'col_1', 'column_2',
                                                                                  'col_2', None, None, None, None, None,
                                                                                  None, None, None, None, None, None,
                                                                                  None, None, None, None, None, None,
                                                                                  None, "Spreadsheet"])
    spreadsheet_count += 1


def add_variables_to_datatree():
    global variables_count
    data_tree.insert("", tk.END, text=f"Variable_{variables_count}", values=['column_1', 'col_1', 'column_2',
                                                                             'col_2', None, None, None, None, None,
                                                                             None, None, None, None, None, None, None,
                                                                             None, None, None, None, None, None,
                                                                             "Variable"])
    variables_count += 1


def add_connections_to_datatree():
    global connections_count
    data_tree.insert("", tk.END, text=f"Connection_{connections_count}", values=['column_1', 'col_1', 'column_2',
                                                                                 'col_2', None, None, None, None, None,
                                                                                 None, None, None, None, None, None,
                                                                                 None, None, None, None, None, None,
                                                                                 None, "Connection"])
    connections_count += 1


# Data tree functions
def delete_item_on_data_tree(*args):
    try:
        erase_help_message = ttk.Label(data_tree_help_frame)
        erase_help_message.grid(row=0, column=0)
        item_selected = data_tree.selection()[0]
        data_tree.delete(item_selected)
    except:
        no_data_item_selection_help_message()


def duplicate_item_on_data_tree(*args):
    try:
        erase_help_message = ttk.Label(data_tree_help_frame)
        erase_help_message.grid(row=0, column=0)
        item_selected = data_tree.selection()[0]
        x = data_tree.item(item_selected)
        data_tree.insert("", tk.END, text=f"{x['text']}", values=x['values'])
    except:
        no_data_item_selection_help_message()


# Data edit page
def make_data_edit_frame(*args):
    try:
        erase_help_message = ttk.Label(data_tree_help_frame)
        erase_help_message.grid(row=0, column=0)
        special_data_edit_frame.grid_forget()
        # Get widget info
        item_selected = data_tree.selection()[0]
        x = data_tree.item(item_selected)
        widget_name.set(x['text'])
        widget_iid.set(item_selected)
        widget_parent.set(data_tree.parent(item_selected))
        edit_var_1.set(x['values'][0])
        edit_var_2.set(x['values'][1])
        edit_var_3.set(x['values'][2])
        edit_var_4.set(x['values'][3])
        edit_var_5.set(x['values'][4])
        edit_var_6.set(x['values'][5])
        edit_var_7.set(x['values'][6])
        edit_var_8.set(x['values'][7])
        edit_var_9.set(x['values'][8])
        edit_var_10.set(x['values'][9])
        edit_var_11.set(x['values'][10])
        edit_var_12.set(x['values'][11])
        edit_var_13.set(x['values'][12])
        edit_var_14.set(x['values'][13])
        edit_var_15.set(x['values'][14])
        edit_var_16.set(x['values'][15])
        edit_var_17.set(x['values'][16])
        edit_var_18.set(x['values'][17])
        edit_var_19.set(x['values'][18])
        edit_var_20.set(x['values'][19])
        edit_var_21.set(x['values'][20])
        edit_var_22.set(x['values'][21])
        widget_type.set(x['values'][22])
        if widget_type.get() == 'Database':
            database_editable_frame()
        elif widget_type.get() == 'EncryptedDB':
            encrypted_database_editable_frame()
        elif widget_type.get() == 'AccountDB':
            account_database_editable_frame()
        elif widget_type.get() == 'Spreadsheet':
            spreadsheet_editable_frame()
        elif widget_type.get() == 'Variable':
            variable_editable_frame()
        elif widget_type.get() == 'Connection':
            connection_editable_frame()

    except:
        no_data_item_selection_help_message()



def no_data_item_selection_help_message(toggle):
    help_label = ttk.Label(data_tree_help_frame, text="Select Item")
    help_label.grid(row=0, column=0)




def connection_edit_save(iid):
    data_tree.item(iid, text=f"{widget_name.get()}")
    special_data_edit_frame.grid_forget()


def connection_editable_frame():
    special_data_edit_frame.grid(row=1, column=0, sticky="swen")
    name_label = ttk.Label(special_data_edit_frame, text="Name")
    name_label.grid(row=0, column=0)
    name_entry = ttk.Entry(special_data_edit_frame, textvariable=widget_name, justify="center")
    name_entry.grid(row=0, column=1)
    save_button = ttk.Button(special_data_edit_frame, text="Save", command=lambda: connection_edit_save(widget_iid.get()))
    save_button.grid(row=1, column=0, columnspan=2, sticky="swen")


def spreadsheet_edit_save(iid):
    data_tree.item(iid, text=f"{widget_name.get()}")
    special_data_edit_frame.grid_forget()


def spreadsheet_editable_frame():
    special_data_edit_frame.grid(row=1, column=0, sticky="swen")
    name_label = ttk.Label(special_data_edit_frame, text="Name")
    name_label.grid(row=0, column=0)
    name_entry = ttk.Entry(special_data_edit_frame, textvariable=widget_name, justify="center")
    name_entry.grid(row=0, column=1)
    save_button = ttk.Button(special_data_edit_frame, text="Save", command=lambda: spreadsheet_edit_save(widget_iid.get()))
    save_button.grid(row=1, column=0, columnspan=2, sticky="swen")


def account_database_edit_save(iid):
    data_tree.item(iid, text=f"{widget_name.get()}")
    special_data_edit_frame.grid_forget()


def account_database_editable_frame():
    special_data_edit_frame.grid(row=1, column=0, sticky="swen")
    name_label = ttk.Label(special_data_edit_frame, text="Name")
    name_label.grid(row=0, column=0)
    name_entry = ttk.Entry(special_data_edit_frame, textvariable=widget_name, justify="center")
    name_entry.grid(row=0, column=1)
    save_button = ttk.Button(special_data_edit_frame, text="Save", command=lambda: account_database_edit_save(widget_iid.get()))
    save_button.grid(row=1, column=0, columnspan=2, sticky="swen")


def variable_edit_save(iid):
    data_tree.item(iid, text=f"{widget_name.get()}")
    special_data_edit_frame.grid_forget()


def variable_editable_frame():
    special_data_edit_frame.grid(row=1, column=0, sticky="swen")
    name_label = ttk.Label(special_data_edit_frame, text="Name")
    name_label.grid(row=0, column=0)
    name_entry = ttk.Entry(special_data_edit_frame, textvariable=widget_name, justify="center")
    name_entry.grid(row=0, column=1)
    save_button = ttk.Button(special_data_edit_frame, text="Save", command=lambda: variable_edit_save(widget_iid.get()))
    save_button.grid(row=1, column=0, columnspan=2, sticky="swen")


def encrypted_database_edit_save(iid):
    data_tree.item(iid, text=f"{widget_name.get()}")
    special_data_edit_frame.grid_forget()


def encrypted_database_editable_frame():
    special_data_edit_frame.grid(row=1, column=0, sticky="swen")
    name_label = ttk.Label(special_data_edit_frame, text="Name")
    name_label.grid(row=0, column=0)
    name_entry = ttk.Entry(special_data_edit_frame, textvariable=widget_name, justify="center")
    name_entry.grid(row=0, column=1)
    save_button = ttk.Button(special_data_edit_frame, text="Save", command=lambda: encrypted_database_edit_save(widget_iid.get()))
    save_button.grid(row=1, column=0, columnspan=2, sticky="swen")


def database_edit_save(iid):
    data_tree.item(iid, text=f"{widget_name.get()}")
    special_data_edit_frame.grid_forget()


def database_editable_frame():
    special_data_edit_frame.grid(row=1, column=0, sticky="swen")
    name_label = ttk.Label(special_data_edit_frame, text="Name")
    name_label.grid(row=0, column=0)
    name_entry = ttk.Entry(special_data_edit_frame, textvariable=widget_name, justify="center")
    name_entry.grid(row=0, column=1)
    save_button = ttk.Button(special_data_edit_frame, text="Save", command=lambda: database_edit_save(widget_iid.get()))
    save_button.grid(row=1, column=0, columnspan=2, sticky="swen")


# Running functions
get_system_font_families()

# App notebook
tkapp_notebook = ttk.Notebook(root)
tkapp_notebook.grid(row=0, column=0)

build_page = ttk.Frame(tkapp_notebook)
tkapp_notebook.add(build_page, text="Build")

data_page = ttk.Frame(tkapp_notebook)
tkapp_notebook.add(data_page, text="Data")

create_page = ttk.Frame(tkapp_notebook)
tkapp_notebook.add(create_page, text="Create")

# Create Page
create_page_title = ttk.Label(create_page, text="Create Page", font=("Times New Roman", 24))
create_page_title.grid(row=0, column=0, columnspan=5)

app_name_label = ttk.Label(create_page, text="App Name")
app_name_label.grid(row=2, column=0, padx=(0, 5))

app_name_entry = ttk.Entry(create_page, textvariable=app_name_var)
app_name_entry.grid(row=2, column=1)

create_page_seperator_vert_top = ttk.Separator(create_page, orient='vertical')
create_page_seperator_vert_top.grid(row=2, column=2, rowspan=1, padx=5, sticky="swen")

create_page_seperator_vert_bottom = ttk.Separator(create_page, orient='vertical')
create_page_seperator_vert_bottom.grid(row=4, column=2, rowspan=1, padx=5, sticky="swen")

create_page_seperator_top = ttk.Separator(create_page, orient='horizontal')
create_page_seperator_top.grid(row=1, column=0, columnspan=5, padx=5, sticky="swen", pady=4)

create_page_seperator_bottom = ttk.Separator(create_page, orient='horizontal')
create_page_seperator_bottom.grid(row=3, column=0, columnspan=5, padx=5, sticky="swen", pady=4)


file_name_label = ttk.Label(create_page, text="File Name")
file_name_label.grid(row=2, column=3, padx=2)


file_name_entry = ttk.Entry(create_page, textvariable=file_name_var)
file_name_entry.grid(row=2, column=4)

create_app_button = ttk.Button(create_page, text="Create")
create_app_button.grid(row=4, column=0, columnspan=2, sticky="nwes", ipady=10)

open_config_button = ttk.Button(create_page, text="Open")
open_config_button.grid(row=4, column=3, sticky="nwes", ipady=10)

save_config_button = ttk.Button(create_page, text="Save")
save_config_button.grid(row=4, column=4, sticky="nwes", ipady=10)

# Design Buttons
design_frame_seperator = ttk.Separator(create_page, orient="horizontal")
design_frame_seperator.grid(row=5, column=0, columnspan=5, sticky="nwes", pady=5)
design_frame = ttk.Frame(create_page)
design_frame.grid(row=6, column=0, columnspan=5, sticky="nwes")

design_frame_title = ttk.Label(design_frame, text="Design Frame", font=("Times New Roman", 16))
design_frame_title.grid(row=0, column=0, columnspan=2, pady=(0, 5))

design_frame_title_seperator = ttk.Separator(design_frame, orient="horizontal")
design_frame_title_seperator.grid(row=1, column=0, columnspan=2, sticky="nwes", pady=5)

color_selection_label = ttk.Label(design_frame, text="Color Selection")
color_selection_label.grid(row=2, column=0, columnspan=2)

color_selection_label_seperator = ttk.Separator(design_frame, orient="horizontal")
color_selection_label_seperator.grid(row=3, column=0, columnspan=2, sticky="nwes", pady=5)

primary_color_button = tk.Button(design_frame, text="Primary", command=chose_primary_color, relief="ridge", width=10,
                                 height=3, font=("roboto", 16))
primary_color_button.grid(row=4, column=0, padx=(5, 0))
primary_color_button.bind('<Button-3>', primary_text_color_changer)

secondary_color_button = tk.Button(design_frame, text="Secondary", command=chose_secondary_color, relief="ridge",
                                   width=10, height=3, font=("roboto", 16))
secondary_color_button.grid(row=4, column=1, padx=(2, 5))
secondary_color_button.bind('<Button-3>', secondary_text_color_changer)

body_font_top_seperator = ttk.Separator(design_frame, orient="horizontal")
body_font_top_seperator.grid(row=5, column=0, columnspan=2, sticky="nwes", pady=5)

body_font_label = ttk.Label(design_frame, text="Body Font")
body_font_label.grid(row=6, column=0, columnspan=2)

body_font_bottom_seperator = ttk.Separator(design_frame, orient="horizontal")
body_font_bottom_seperator.grid(row=7, column=0, columnspan=2, sticky="nwes", pady=5)

body_font_type_selector = ttk.Combobox(design_frame, textvariable=body_font_type_var, values=system_font_family_list)
body_font_type_selector.grid(row=8, column=0)

body_font_type_selector.bind('<Button-3>', update_color_box_font)

body_font_size_selector = ttk.Spinbox(design_frame, textvariable=body_font_size_var, from_=10, to=30, state='readonly')
body_font_size_selector.grid(row=8, column=1)

body_font_size_selector.bind('<Button-3>', update_color_box_font)

bottom_design_seperator = ttk.Separator(design_frame, orient="horizontal")
bottom_design_seperator.grid(row=9, column=0, columnspan=2, sticky="nwes", pady=5)

right_design_seperator = ttk.Separator(design_frame, orient="vertical")
right_design_seperator.grid(row=1, column=3, rowspan=9, sticky="nwes", pady=5)

# Data Page
# Data Items
data_items_frame = ttk.Frame(data_page)
data_items_frame.grid(row=0, column=0, sticky="nwes")

data_page_seperator_left = ttk.Separator(data_page, orient="vertical")
data_page_seperator_left.grid(row=0, column=1, sticky="nwes", padx=5)


data_tree_frame = ttk.Frame(data_page)
data_tree_frame.grid(row=0, column=2, sticky="nwes")

data_page_seperator_right = ttk.Separator(data_page, orient="vertical")
data_page_seperator_right.grid(row=0, column=3, sticky="nwes", padx=5)


data_edit_frame = ttk.Frame(data_page)
data_edit_frame.grid(row=0, column=4, sticky="nwes")

special_data_edit_frame = ttk.Frame(data_edit_frame)
special_data_edit_frame.grid(row=1, column=0, sticky="swen")

data_tree_help_frame = ttk.Frame(data_tree_frame, relief="ridge", borderwidth=5)
data_tree_help_frame.grid(row=2, column=1, sticky="nwes")


# Data Product Menu
data_product_menu_title = ttk.Label(data_items_frame, text="Data Products", font=("Times New Roman", 18))
data_product_menu_title.grid(row=0, column=0, columnspan=2, padx=10, pady=(5, 0))

# Data Products
product_height = 5
product_width = 4
database_product_button = ttk.Button(data_items_frame, text="DB", command=add_database_to_datatree)
database_product_button.grid(row=1, column=0, ipady=product_height, ipadx=product_width)

encrypteddb_product_button = ttk.Button(data_items_frame, text="EncrpytedDB",
                                        command=add_encrypted_database_to_datatree)
encrypteddb_product_button.grid(row=1, column=1, ipady=product_height, ipadx=product_width)

account_product_button = ttk.Button(data_items_frame, text="Account", command=add_account_database_to_datatree)
account_product_button.grid(row=2, column=0, ipady=product_height, ipadx=product_width)

spreadsheet_product_button = ttk.Button(data_items_frame, text="Spreadsheet", command=add_spreadsheet_to_datatree)
spreadsheet_product_button.grid(row=2, column=1, ipady=product_height, ipadx=product_width)

var_product_button = ttk.Button(data_items_frame, text="Variable", command=add_variables_to_datatree)
var_product_button.grid(row=3, column=0, ipady=product_height, ipadx=product_width)

connect_product_button = ttk.Button(data_items_frame, text="Connect", command=add_connections_to_datatree)
connect_product_button.grid(row=3, column=1, ipady=product_height, ipadx=product_width)


# data tree frame
data_tree = ttk.Treeview(data_tree_frame)
data_tree.grid(row=0, column=0, columnspan=3, sticky="nwes")
data_tree.heading('#0', text="Data View")
data_tree.bind("<Double-Button-1>", make_data_edit_frame)

# Data Tree Buttons
data_tree_delete_button = ttk.Button(data_tree_frame, text="Delete")
data_tree_delete_button.grid(row=1, column=0, sticky="nwes")
data_tree_delete_button.bind("<Double-Button-1>", delete_item_on_data_tree)

data_tree_duplicate_button = ttk.Button(data_tree_frame, text="Duplicate")
data_tree_duplicate_button.grid(row=1, column=1, sticky="nwes")
data_tree_duplicate_button.bind("<Button-1>", duplicate_item_on_data_tree)

data_tree_edit_button = ttk.Button(data_tree_frame, text="Edit", command=make_data_edit_frame)
data_tree_edit_button.grid(row=1, column=2, sticky="nwes")


# Data edit frame
data_edit_title = ttk.Label(data_edit_frame, text="Edit", font=("Times New Roman", 18))
data_edit_title.grid(row=0, column=0, sticky="ew", padx=60, pady=(5, 0))


root.mainloop()
