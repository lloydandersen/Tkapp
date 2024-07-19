import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Tkapp")
root.minsize(500, 500)


# var
app_name_var = tk.StringVar()
file_name_var = tk.StringVar()

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
create_page_title = ttk.Label(create_page, text="Create Page")
create_page_title.grid(row=0, column=0, columnspan=5)

app_name_label = ttk.Label(create_page, text="App Name")
app_name_label.grid(row=2, column=0, padx=(5, 5))

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



# Data Page
# Data Items
data_items_frame = ttk.Frame()


data_tree_frame = ttk.Frame()


data_edit_frame = ttk.Frame()

root.mainloop()
