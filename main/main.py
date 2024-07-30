import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.iconbitmap('Tkapplogomain.ico')
# root.state('zoomed')
root.minsize(500, 500)
root.title("Tkapp")
style = ttk.Style()
style.configure("TNotebook.Tab", font=("Poor Richard", 20))
root["background"] = "#ADD8E6"


build_page = tk.Frame(root, background="#ADD8E6")
build_page.pack(fill="both", side="top")

build_page.grid_columnconfigure(0, weight=0)
build_page.grid_columnconfigure(1, weight=6)
build_page.grid_rowconfigure(1, weight=1)
build_page.grid_rowconfigure(0, weight=1)


create_page = tk.Frame(root, background="#ADD8E6")

# Build Page
widget_frame = tk.Frame(build_page, background="#ADD8E6")
widget_frame.grid(row=0, column=0, sticky="n")

tree_frame = tk.Frame(build_page, background="#ADD8E6")
tree_frame.grid(row=0, column=1, sticky="n")

edit_frame = tk.Frame(build_page, background="#ADD8E6")
edit_frame.grid(row=0, column=2, sticky="n")

control_frame = tk.Frame(build_page, background="#ADD8E6")
control_frame.grid(row=1, column=1, sticky="n")


# Tree Frame
view_tree = ttk.Treeview(tree_frame)
view_tree.grid(row=0, column=0, sticky="swen", ipadx=15)
view_tree.heading("#0", text="View Tree")

# Control frame
delete_button = ttk.Button(control_frame, text="Delete")
delete_button.grid(row=0, column=0)

duplicate_button = ttk.Button(control_frame, text="Duplicate")
duplicate_button.grid(row=0, column=1)

edit_button = ttk.Button(control_frame, text="Edit")
edit_button.grid(row=0, column=2)


# Widget Frame
widget_width = 5
widget_height = 10
label_widget = ttk.Button(widget_frame, text="Label")
label_widget.grid(row=0, column=0, ipadx=widget_width, ipady=widget_height, padx=1, pady=1)

button_widget = ttk.Button(widget_frame, text="Button")
button_widget.grid(row=0, column=1, ipadx=widget_width, ipady=widget_height, padx=1, pady=1)

entry_widget = ttk.Button(widget_frame, text="Entry")
entry_widget.grid(row=0, column=2, ipadx=widget_width, ipady=widget_height, padx=1, pady=1)

selection_widget = ttk.Button(widget_frame, text="Selection")
selection_widget.grid(row=1, column=0, ipadx=widget_width, ipady=widget_height, padx=1, pady=1)

image_widget = ttk.Button(widget_frame, text="Image")
image_widget.grid(row=1, column=1, ipadx=widget_width, ipady=widget_height, padx=1, pady=1)

graph_widget = ttk.Button(widget_frame, text="Graph")
graph_widget.grid(row=1, column=2, ipadx=widget_width, ipady=widget_height, padx=1, pady=1)

gauge_widget = ttk.Button(widget_frame, text="Gauge")
gauge_widget.grid(row=2, column=0, ipadx=widget_width, ipady=widget_height, padx=1, pady=1)

data_widget = ttk.Button(widget_frame, text="Data")
data_widget.grid(row=2, column=1, ipadx=widget_width, ipady=widget_height, padx=1, pady=1)

map_widget = ttk.Button(widget_frame, text="Map")
map_widget.grid(row=2, column=2, ipadx=widget_width, ipady=widget_height, padx=1, pady=1)

control_widget = ttk.Button(widget_frame, text="Control")
control_widget.grid(row=3, column=0, ipadx=widget_width, ipady=widget_height, padx=1, pady=1)

icon_widget = ttk.Button(widget_frame, text="Icon")
icon_widget.grid(row=3, column=1, ipadx=widget_width, ipady=widget_height, padx=1, pady=1)

table_widget = ttk.Button(widget_frame, text="Table")
table_widget.grid(row=3, column=2, ipadx=widget_width, ipady=widget_height, padx=1, pady=1)


root.mainloop()
