import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.iconbitmap('Tkapplogomain.ico')
# root.state('zoomed')
root.minsize(500, 500)
root.title("Tkapp")
style = ttk.Style()
style.configure("TNotebook.Tab", font=("Poor Richard", 20))
background_color = "#222222"
root["background"] = background_color

# Naming Counts
label_count = 0
button_count = 0
entry_count = 0
selection_count = 0
image_count = 0
graph_count = 0
gauge_count = 0
data_count = 0
map_count = 0
control_count = 0
icon_count = 0
table_count = 0

# App vars
widget_iid = tk.StringVar()
var_one = tk.StringVar()
var_two = tk.StringVar()
var_three = tk.StringVar()
var_four = tk.StringVar()
var_five = tk.StringVar()
var_six = tk.StringVar()
var_seven = tk.StringVar()
var_eight = tk.StringVar()
var_nine = tk.StringVar()
var_ten = tk.StringVar()
var_eleven = tk.StringVar()
var_twelve = tk.StringVar()
var_thirteen = tk.StringVar()
var_fourteen = tk.StringVar()
var_fifteen = tk.StringVar()
var_sixteen = tk.StringVar()
var_seventeen = tk.StringVar()
var_eighteen = tk.StringVar()
var_nineteen = tk.StringVar()
var_twenty = tk.StringVar()
var_twentyone = tk.StringVar()
var_twentytwo = tk.StringVar()

# Model Functions
def add_widget_to_tree(widget):
    global label_count, button_count, entry_count, selection_count, image_count, graph_count, gauge_count, data_count
    global map_count, control_count, icon_count, table_count
    if widget == "label":
        view_tree.insert("", tk.END, text=f"Label_{label_count}",
                         values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21])
        label_count += 1
    elif widget == "button":
        view_tree.insert("", tk.END, text=f"Button_{button_count}",
                         values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21])
        button_count += 1
    elif widget == "entry":
        view_tree.insert("", tk.END, text=f"Entry_{entry_count}",
                         values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21])
        entry_count += 1
    elif widget == "selection":
        view_tree.insert("", tk.END, text=f"Selection_{selection_count}",
                         values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21])
        selection_count += 1
    elif widget == "image":
        view_tree.insert("", tk.END, text=f"Image_{image_count}",
                         values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21])
        image_count += 1
    elif widget == "graph":
        view_tree.insert("", tk.END, text=f"Graph_{graph_count}",
                         values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21])
        graph_count += 1
    elif widget == "gauge":
        view_tree.insert("", tk.END, text=f"Gauge_{gauge_count}",
                         values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21])
        gauge_count += 1
    elif widget == "data":
        view_tree.insert("", tk.END, text=f"Data_{data_count}",
                         values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21])
        data_count += 1
    elif widget == "map":
        view_tree.insert("", tk.END, text=f"Map_{map_count}",
                         values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21])
        map_count += 1
    elif widget == "control":
        view_tree.insert("", tk.END, text=f"Control_{control_count}",
                         values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21])
        control_count += 1
    elif widget == "icon":
        view_tree.insert("", tk.END, text=f"Icon_{icon_count}",
                         values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21])
        icon_count += 1
    elif widget == "table":
        view_tree.insert("", tk.END, text=f"Table_{table_count}",
                         values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21])
        table_count += 1


def delete_selection():
    selected_item = view_tree.selection()
    view_tree.delete(selected_item)


def duplicate_selection():
    selected_item = view_tree.selection()
    selected_name = view_tree.item(selected_item)['text']
    selected_values = view_tree.item(selected_item)['values']
    view_tree.insert("", tk.END, text=f"{selected_name}", values=f"{selected_values}")


def edit_selection():
    selected_item = view_tree.selection()
    edit_item = view_tree.item(selected_item)
    item_values = edit_item['values']
    item_name = edit_item['text']

    # Set app vars
    widget_iid.set(selected_item)
    var_one.set(item_name)

    var_two.set(item_values[0])
    var_three.set(item_values[1])
    var_four.set(item_values[2])
    var_five.set(item_values[3])
    var_six.set(item_values[4])
    var_seven.set(item_values[5])
    var_eight.set(item_values[6])
    var_nine.set(item_values[7])
    var_ten.set(item_values[8])
    var_eleven.set(item_values[9])
    var_twelve.set(item_values[10])
    var_thirteen.set(item_values[11])
    var_fourteen.set(item_values[12])
    var_fifteen.set(item_values[13])
    var_sixteen.set(item_values[14])
    var_seventeen.set(item_values[15])
    var_eighteen.set(item_values[16])
    var_nineteen.set(item_values[17])
    var_twenty.set(item_values[18])
    var_twentyone.set(item_values[19])
    var_twentytwo.set(item_values[20])
    print(var_two.get())




def save_edited_selection():
    pass


def clear_edit_frame():
    for child in edit_frame.winfo_children():
        child.destroy()
    edit_title = tk.Label(edit_frame, text="Edit", font=("Roboto", 30), background=background_color, foreground="white")
    edit_title.grid(row=0, column=0, columnspan=3, sticky="swen", ipadx=60)

# Widget Edit Frames
def label_edit_frame():
    pass


build_page = tk.Frame(root, background=background_color)
build_page.pack(fill="both", side="top")

build_page.grid_columnconfigure(0, weight=0)
build_page.grid_columnconfigure(1, weight=1)
build_page.grid_rowconfigure(1, weight=1)
build_page.grid_rowconfigure(0, weight=1)
build_page.grid_columnconfigure(2, weight=1)


create_page = tk.Frame(root, background=background_color)

# Build Page
widget_frame = tk.Frame(build_page, background=background_color)
widget_frame.grid(row=0, column=0, sticky="n")

tree_frame = tk.Frame(build_page, background=background_color)
tree_frame.grid(row=0, column=1, sticky="n")

edit_frame = tk.Frame(build_page, background=background_color)
edit_frame.grid(row=0, column=2, sticky="n")

control_frame = tk.Frame(build_page, background=background_color)
control_frame.grid(row=1, column=1, sticky="n")


# Tree Frame
view_tree = ttk.Treeview(tree_frame)
view_tree.grid(row=1, column=0, sticky="swen", ipadx=15, ipady=10)
view_tree.heading("#0", text="Widgets")

view_title = tk.Label(tree_frame, text="View", font=("Roboto", 30), background=background_color, foreground="white")
view_title.grid(row=0, column=0, columnspan=3, sticky="swen")

# Control frame
delete_button = ttk.Button(control_frame, text="Delete", command=delete_selection)
delete_button.grid(row=0, column=0, padx=1, pady=1)

duplicate_button = ttk.Button(control_frame, text="Duplicate", command=duplicate_selection)
duplicate_button.grid(row=0, column=1, padx=1, pady=1)

edit_button = ttk.Button(control_frame, text="Edit", command=edit_selection)
edit_button.grid(row=0, column=2, padx=1, pady=1)


# Widget Frame
widget_width = 5
widget_height = 10
widget_title = tk.Label(widget_frame, text="Widgets", font=("Roboto", 30), background=background_color, foreground="white")
widget_title.grid(row=0, column=0, columnspan=3, sticky="swen")

label_widget = ttk.Button(widget_frame, text="Label", command=lambda: add_widget_to_tree("label"))
label_widget.grid(row=1, column=0, ipadx=widget_width, ipady=widget_height, padx=1, pady=1)

button_widget = ttk.Button(widget_frame, text="Button", command=lambda: add_widget_to_tree("button"))
button_widget.grid(row=1, column=1, ipadx=widget_width, ipady=widget_height, padx=1, pady=1)

entry_widget = ttk.Button(widget_frame, text="Entry", command=lambda: add_widget_to_tree("entry"))
entry_widget.grid(row=1, column=2, ipadx=widget_width, ipady=widget_height, padx=1, pady=1)

selection_widget = ttk.Button(widget_frame, text="Selection", command=lambda: add_widget_to_tree("selection"))
selection_widget.grid(row=2, column=0, ipadx=widget_width, ipady=widget_height, padx=1, pady=1)

image_widget = ttk.Button(widget_frame, text="Image", command=lambda: add_widget_to_tree("image"))
image_widget.grid(row=2, column=1, ipadx=widget_width, ipady=widget_height, padx=1, pady=1)

graph_widget = ttk.Button(widget_frame, text="Graph", command=lambda: add_widget_to_tree("graph"))
graph_widget.grid(row=2, column=2, ipadx=widget_width, ipady=widget_height, padx=1, pady=1)

gauge_widget = ttk.Button(widget_frame, text="Gauge", command=lambda: add_widget_to_tree("gauge"))
gauge_widget.grid(row=3, column=0, ipadx=widget_width, ipady=widget_height, padx=1, pady=1)

data_widget = ttk.Button(widget_frame, text="Data", command=lambda: add_widget_to_tree("data"))
data_widget.grid(row=3, column=1, ipadx=widget_width, ipady=widget_height, padx=1, pady=1)

map_widget = ttk.Button(widget_frame, text="Map", command=lambda: add_widget_to_tree("map"))
map_widget.grid(row=3, column=2, ipadx=widget_width, ipady=widget_height, padx=1, pady=1)

control_widget = ttk.Button(widget_frame, text="Control", command=lambda: add_widget_to_tree("control"))
control_widget.grid(row=4, column=0, ipadx=widget_width, ipady=widget_height, padx=1, pady=1)

icon_widget = ttk.Button(widget_frame, text="Icon", command=lambda: add_widget_to_tree("icon"))
icon_widget.grid(row=4, column=1, ipadx=widget_width, ipady=widget_height, padx=1, pady=1)

table_widget = ttk.Button(widget_frame, text="Table", command=lambda: add_widget_to_tree("table"))
table_widget.grid(row=4, column=2, ipadx=widget_width, ipady=widget_height, padx=1, pady=1)

# Edit Frame
edit_title = tk.Label(edit_frame, text="Edit", font=("Roboto", 30), background=background_color, foreground="white")
edit_title.grid(row=0, column=0, columnspan=3, sticky="swen", ipadx=60)


root.mainloop()
