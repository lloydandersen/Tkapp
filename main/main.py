import tkinter as tk
from tkinter import ttk
from tkinter.colorchooser import askcolor
from tkinter.font import Font


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
var_type = tk.StringVar()

# Edit Frame Style
edit_frame_font = ("Times New Roman", 14)
entry_box_font = ("Times New Roman", 14)
style.configure("save.TButton", font=("Poor Richards", 16))

edit_frame_background = '#222222'
edit_frame_foreground = 'white'


# Model Functions
def add_widget_to_tree(widget):
    global label_count, button_count, entry_count, selection_count, image_count, graph_count, gauge_count, data_count
    global map_count, control_count, icon_count, table_count
    if widget == "label":
        view_tree.insert("", tk.END, text=f"Label_{label_count}",
                         values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, "label"])
        label_count += 1
    elif widget == "button":
        view_tree.insert("", tk.END, text=f"Button_{button_count}",
                         values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, "button"])
        button_count += 1
    elif widget == "entry":
        view_tree.insert("", tk.END, text=f"Entry_{entry_count}",
                         values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, "entry"])
        entry_count += 1
    elif widget == "selection":
        view_tree.insert("", tk.END, text=f"Selection_{selection_count}",
                         values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
                                 "selection"])
        selection_count += 1
    elif widget == "image":
        view_tree.insert("", tk.END, text=f"Image_{image_count}",
                         values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, "image"])
        image_count += 1
    elif widget == "graph":
        view_tree.insert("", tk.END, text=f"Graph_{graph_count}",
                         values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, "graph"])
        graph_count += 1
    elif widget == "gauge":
        view_tree.insert("", tk.END, text=f"Gauge_{gauge_count}",
                         values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, "gauge"])
        gauge_count += 1
    elif widget == "data":
        view_tree.insert("", tk.END, text=f"Data_{data_count}",
                         values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, "data"])
        data_count += 1
    elif widget == "map":
        view_tree.insert("", tk.END, text=f"Map_{map_count}",
                         values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, "#222222", 14, 15, 16, 17, 18, 19, 20, 21, "map"])
        map_count += 1
    elif widget == "control":
        view_tree.insert("", tk.END, text=f"Control_{control_count}",
                         values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, "control"])
        control_count += 1
    elif widget == "icon":
        view_tree.insert("", tk.END, text=f"Icon_{icon_count}",
                         values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, "icon"])
        icon_count += 1
    elif widget == "table":
        view_tree.insert("", tk.END, text=f"Table_{table_count}",
                         values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, "table"])
        table_count += 1


def build_placement_widgets():
    placement_frame = tk.Frame(edit_frame, background=background_color)
    placement_frame.grid(row=6, column=0, columnspan=2, sticky="swen")
    chosen_placement = var_two.get()
    fill_value_list = ["none", "x", "y", "both"]
    if chosen_placement == "pack":
        pack_expand_label = tk.Label(placement_frame, text="Expand", background=edit_frame_background,
                                     foreground=edit_frame_foreground)
        pack_expand_label.grid(row=0, column=0, columnspan=1, sticky="swen", padx=5)
        pack_expand_true = ttk.Radiobutton(placement_frame, variable=var_three, text="True", value="true")
        pack_expand_true.grid(row=0, column=1, sticky="w", ipadx=20)
        pack_expand_false = ttk.Radiobutton(placement_frame, variable=var_three, text="False", value="false")
        pack_expand_false.grid(row=0, column=1, sticky="e", ipadx=20)

        pack_fill_label = tk.Label(placement_frame, text="Fill", background=edit_frame_background,
                                   foreground=edit_frame_foreground)
        pack_fill_label.grid(row=1, column=0, sticky="swen", padx=5)
        pack_fill_selection = ttk.Combobox(placement_frame, textvariable=var_four, values=fill_value_list,
                                           background=edit_frame_background, foreground=edit_frame_foreground,
                                           state="readonly", justify="center")
        pack_fill_selection.grid(row=1, column=1, sticky="swen")

        side_navigation_title = tk.Label(placement_frame, text="Side", background="#222222", foreground="white")
        side_navigation_title.grid(row=2, column=0, columnspan=2)

        anchor_navigation_title = tk.Label(placement_frame, text="Anchor", background="#222222", foreground="white")
        anchor_navigation_title.grid(row=4, column=0, columnspan=2)

        # Pack Side Navigation
        pack_side_navigation_frame = tk.Frame(placement_frame, background="#222222")
        pack_side_navigation_frame.grid(row=3, column=0, columnspan=2, sticky="n")
        navigation_button_height = 2
        navigation_button_width = 10

        top_button = tk.Button(pack_side_navigation_frame, text="Top", command=lambda: var_five.set('top'),
                               width=navigation_button_width, height=navigation_button_height,
                               background=edit_frame_background, foreground=edit_frame_foreground)
        top_button.grid(row=0, column=1)

        bottom_button = tk.Button(pack_side_navigation_frame, text="Buttom", command=lambda: var_five.set('bottom'),
                                  width=navigation_button_width, height=navigation_button_height,
                                  background=edit_frame_background, foreground=edit_frame_foreground)
        bottom_button.grid(row=2, column=1)

        left_button = tk.Button(pack_side_navigation_frame, text="Left", command=lambda: var_five.set('left'),
                                width=navigation_button_width, height=navigation_button_height,
                                background=edit_frame_background, foreground=edit_frame_foreground)
        left_button.grid(row=1, column=0)

        right_button = tk.Button(pack_side_navigation_frame, text="Right", command=lambda: var_five.set('right'),
                                 width=navigation_button_width, height=navigation_button_height,
                                 background=edit_frame_background, foreground=edit_frame_foreground)
        right_button.grid(row=1, column=2)

        side_choice_button = tk.Button(pack_side_navigation_frame, width=navigation_button_width, height=navigation_button_height,
                                background=edit_frame_background, foreground=edit_frame_foreground, textvariable=var_five)
        side_choice_button.grid(row=1, column=1)

        # Pack Anchor Selection
        pack_anchor_navigation_frame = tk.Frame(placement_frame, background="#222222")
        pack_anchor_navigation_frame.grid(row=5, column=0, columnspan=2, sticky="n")

        north_button = tk.Button(pack_anchor_navigation_frame, text="North", command=lambda: var_six.set('n'),
                                 width=navigation_button_width, height=navigation_button_height,
                                 background=edit_frame_background, foreground=edit_frame_foreground)
        north_button.grid(row=0, column=1)

        south_button = tk.Button(pack_anchor_navigation_frame, text="South", command=lambda: var_six.set('s'),
                                 width=navigation_button_width, height=navigation_button_height,
                                 background=edit_frame_background, foreground=edit_frame_foreground)
        south_button.grid(row=2, column=1)

        west_button = tk.Button(pack_anchor_navigation_frame, text="West", command=lambda: var_six.set('w'),
                                width=navigation_button_width, height=navigation_button_height,
                                background=edit_frame_background, foreground=edit_frame_foreground)
        west_button.grid(row=1, column=0)

        east_button = tk.Button(pack_anchor_navigation_frame, text="East", command=lambda: var_six.set('e'),
                                width=navigation_button_width, height=navigation_button_height,
                                background=edit_frame_background, foreground=edit_frame_foreground)
        east_button.grid(row=1, column=2)

        center_button = tk.Button(pack_anchor_navigation_frame, text="Center", command=lambda: var_six.set('center'),
                                  width=navigation_button_width, height=navigation_button_height,
                                  background=edit_frame_background, foreground=edit_frame_foreground,
                                  textvariable=var_six)
        center_button.grid(row=1, column=1)

        pack_padx_label = tk.Label(placement_frame, text="Padx", background=edit_frame_background,
                                   foreground=edit_frame_foreground)
        pack_padx_label.grid(row=6, column=0, sticky="swen")
        pack_padx_spinbox = tk.Spinbox(placement_frame, textvariable=var_seven, from_=0, to=100,
                                       background=edit_frame_background, foreground=edit_frame_foreground)
        pack_padx_spinbox.grid(row=6, column=1, sticky="swen")

        pack_pady_label = tk.Label(placement_frame, text="Pady", background=edit_frame_background,
                                   foreground=edit_frame_foreground)
        pack_pady_label.grid(row=7, column=0, sticky="swen")
        pack_pady_spinbox = tk.Spinbox(placement_frame, textvariable=var_eight, from_=0, to=100,
                                       background=edit_frame_background, foreground=edit_frame_foreground)
        pack_pady_spinbox.grid(row=7, column=1, sticky="swen")

        pack_ipadx_label = tk.Label(placement_frame, text="IPadx", background=edit_frame_background,
                                    foreground=edit_frame_foreground)
        pack_ipadx_label.grid(row=8, column=0, sticky="swen")
        pack_ipadx_spinbox = tk.Spinbox(placement_frame, textvariable=var_nine, from_=0, to=100,
                                        background=edit_frame_background, foreground=edit_frame_foreground)
        pack_ipadx_spinbox.grid(row=8, column=1, sticky="swen")

        pack_ipady_label = tk.Label(placement_frame, text="IPady", background=edit_frame_background,
                                    foreground=edit_frame_foreground)
        pack_ipady_label.grid(row=9, column=0, sticky="swen")
        pack_ipady_spinbox = tk.Spinbox(placement_frame, textvariable=var_ten, from_=0, to=100,
                                        background=edit_frame_background, foreground=edit_frame_foreground)
        pack_ipady_spinbox.grid(row=9, column=1, sticky="swen")


    elif chosen_placement == "grid":
        grid_row_label = tk.Label(placement_frame, text="Row", background=edit_frame_background,
                                  foreground=edit_frame_foreground)
        grid_row_label.grid(row=0, column=0, sticky="swen")
        grid_row_spinbox = tk.Spinbox(placement_frame, textvariable=var_three, from_=0, to=100,
                                      background=edit_frame_background, foreground=edit_frame_foreground)
        grid_row_spinbox.grid(row=0, column=1, sticky="swen")

        grid_column_label = tk.Label(placement_frame, text="Column", background=edit_frame_background,
                                     foreground=edit_frame_foreground)
        grid_column_label.grid(row=1, column=0, sticky="swen")
        grid_column_spinbox = tk.Spinbox(placement_frame, textvariable=var_four, from_=0, to=100,
                                         background=edit_frame_background, foreground=edit_frame_foreground)
        grid_column_spinbox.grid(row=1, column=1, sticky="swen")

        grid_padx_label = tk.Label(placement_frame, text="Padx", background=edit_frame_background,
                                   foreground=edit_frame_foreground)
        grid_padx_label.grid(row=2, column=0, sticky="swen")
        grid_padx_spinbox = tk.Spinbox(placement_frame, textvariable=var_five, from_=0, to=100,
                                       background=edit_frame_background, foreground=edit_frame_foreground)
        grid_padx_spinbox.grid(row=2, column=1, sticky="swen")

        grid_pady_label = tk.Label(placement_frame, text="Pady", background=edit_frame_background,
                                   foreground=edit_frame_foreground)
        grid_pady_label.grid(row=3, column=0, sticky="swen")
        grid_pady_spinbox = tk.Spinbox(placement_frame, textvariable=var_six, from_=0, to=100,
                                       background=edit_frame_background, foreground=edit_frame_foreground)
        grid_pady_spinbox.grid(row=3, column=1, sticky="swen")

        grid_ipadx_label = tk.Label(placement_frame, text="Ipadx", background=edit_frame_background,
                                    foreground=edit_frame_foreground)
        grid_ipadx_label.grid(row=4, column=0, sticky="swen")
        grid_ipadx_spinbox = tk.Spinbox(placement_frame, textvariable=var_seven, from_=0, to=100,
                                        background=edit_frame_background, foreground=edit_frame_foreground)
        grid_ipadx_spinbox.grid(row=4, column=1, sticky="swen")

        grid_ipady_label = tk.Label(placement_frame, text="Ipady", background=edit_frame_background,
                                    foreground=edit_frame_foreground)
        grid_ipady_label.grid(row=5, column=0, sticky="swen")
        grid_ipady_spinbox = tk.Spinbox(placement_frame, textvariable=var_eight, from_=0, to=100,
                                        background=edit_frame_background, foreground=edit_frame_foreground)
        grid_ipady_spinbox.grid(row=5, column=1, sticky="swen")

        grid_rowspan_label = tk.Label(placement_frame, text="Rowspan", background=edit_frame_background,
                                      foreground=edit_frame_foreground)
        grid_rowspan_label.grid(row=6, column=0, sticky="swen")
        grid_rowspan_spinbox = tk.Spinbox(placement_frame, textvariable=var_ten, from_=0, to=100,
                                          background=edit_frame_background, foreground=edit_frame_foreground)
        grid_rowspan_spinbox.grid(row=6, column=1, sticky="swen")

        grid_columnspan_label = tk.Label(placement_frame, text="Columnspan", background=edit_frame_background,
                                         foreground=edit_frame_foreground)
        grid_columnspan_label.grid(row=7, column=0, sticky="swen")
        grid_columnspan_spinbox = tk.Spinbox(placement_frame, textvariable=var_eleven, from_=0, to=100,
                                             background=edit_frame_background, foreground=edit_frame_foreground)
        grid_columnspan_spinbox.grid(row=7, column=1, sticky="swen")


        navigation_title = tk.Label(placement_frame, text="Sticky", background=edit_frame_background,
                                    foreground=edit_frame_foreground)
        navigation_title.grid(row=8, column=0, columnspan=2, sticky="swen")

        # Grid Sticky Navigation
        navigation_frame = tk.Frame(placement_frame)
        navigation_frame.grid(row=9, column=0, columnspan=2, sticky="n")
        navigation_button_height = 2
        navigation_button_width = 10

        north_button = tk.Button(navigation_frame, text="North", command=lambda: var_nine.set("n"),
                                 height=navigation_button_height, width=navigation_button_width,
                                 background=edit_frame_background, foreground=edit_frame_foreground)
        north_button.grid(row=0, column=1)

        south_button = tk.Button(navigation_frame, text="South", command=lambda: var_nine.set("s"),
                                 height=navigation_button_height, width=navigation_button_width,
                                 background=edit_frame_background, foreground=edit_frame_foreground)
        south_button.grid(row=2, column=1)

        west_button = tk.Button(navigation_frame, text="West", command=lambda: var_nine.set("w"),
                                height=navigation_button_height, width=navigation_button_width,
                                background=edit_frame_background, foreground=edit_frame_foreground)
        west_button.grid(row=1, column=0)

        east_button = tk.Button(navigation_frame, text="East", command=lambda: var_nine.set("e"),
                                height=navigation_button_height, width=navigation_button_width,
                                background=edit_frame_background, foreground=edit_frame_foreground)
        east_button.grid(row=1, column=2)

        northwest_button = tk.Button(navigation_frame, text="NW", command=lambda: var_nine.set("nw"),
                                     height=navigation_button_height, width=navigation_button_width,
                                     background=edit_frame_background, foreground=edit_frame_foreground)
        northwest_button.grid(row=0, column=0)

        northeast_button = tk.Button(navigation_frame, text="NE", command=lambda: var_nine.set("ne"),
                                     height=navigation_button_height, width=navigation_button_width,
                                     background=edit_frame_background, foreground=edit_frame_foreground)
        northeast_button.grid(row=0, column=2)

        southwest_button = tk.Button(navigation_frame, text="SW", command=lambda: var_nine.set("sw"),
                                     height=navigation_button_height, width=navigation_button_width,
                                     background=edit_frame_background, foreground=edit_frame_foreground)
        southwest_button.grid(row=2, column=0)

        southeast_button = tk.Button(navigation_frame, text="SE", command=lambda: var_nine.set("se"),
                                     height=navigation_button_height, width=navigation_button_width,
                                     background=edit_frame_background, foreground=edit_frame_foreground)
        southeast_button.grid(row=2, column=2)

        center_button = tk.Button(navigation_frame, text="", command=lambda: var_nine.set(""),
                                  height=navigation_button_height, width=navigation_button_width,
                                  background=edit_frame_background, foreground=edit_frame_foreground,
                                  textvariable=var_nine)
        center_button.grid(row=1, column=1)
        center_button.bind("<Button-3>", lambda e: var_nine.set("swen"))

    else:
        navigation_button_height = 2
        navigation_button_width = 10
        place_x_label = tk.Label(placement_frame, text="X", background=edit_frame_background,
                                 foreground=edit_frame_foreground)
        place_x_label.grid(row=0, column=0, sticky="swen")

        place_x_spinbox = tk.Spinbox(placement_frame, textvariable=var_three, from_=0, to=100,
                                     background=edit_frame_background, foreground=edit_frame_foreground)
        place_x_spinbox.grid(row=0, column=1, sticky="swen")

        place_y_label = tk.Label(placement_frame, text="Y", background=edit_frame_background,
                                 foreground=edit_frame_foreground)
        place_y_label.grid(row=1, column=0, sticky="swen")
        place_y_spinbox = tk.Spinbox(placement_frame, textvariable=var_four, from_=0, to=100,
                                     background=edit_frame_background, foreground=edit_frame_foreground)
        place_y_spinbox.grid(row=1, column=1, sticky="swen")

        place_relx_label = tk.Label(placement_frame, text="RelX", background=edit_frame_background,
                                    foreground=edit_frame_foreground)
        place_relx_label.grid(row=2, column=0, sticky="swen")
        place_relx_spinbox = tk.Spinbox(placement_frame, textvariable=var_five, from_=0, to=100,
                                        background=edit_frame_background, foreground=edit_frame_foreground)
        place_relx_spinbox.grid(row=2, column=1, sticky="swen")

        place_rely_label = tk.Label(placement_frame, text="RelY", background=edit_frame_background,
                                    foreground=edit_frame_foreground)
        place_rely_label.grid(row=3, column=0, sticky="swen")
        place_rely_spinbox = tk.Spinbox(placement_frame, textvariable=var_six, from_=0, to=100,
                                        background=edit_frame_background, foreground=edit_frame_foreground)
        place_rely_spinbox.grid(row=3, column=1, sticky="swen")

        place_relwidth_label = tk.Label(placement_frame, text="Relwidth", background=edit_frame_background,
                                        foreground=edit_frame_foreground)
        place_relwidth_label.grid(row=4, column=0, sticky="swen")
        place_relwidth_spinbox = tk.Spinbox(placement_frame, textvariable=var_seven, from_=0, to=100,
                                            background=edit_frame_background, foreground=edit_frame_foreground)
        place_relwidth_spinbox.grid(row=4, column=1, sticky="swen")

        place_relheight_label = tk.Label(placement_frame, text="Relheight", background=edit_frame_background,
                                         foreground=edit_frame_foreground)
        place_relheight_label.grid(row=5, column=0, sticky="swen")
        place_relheight_spinbox = tk.Spinbox(placement_frame, textvariable=var_eight, from_=0, to=100,
                                             background=edit_frame_background, foreground=edit_frame_foreground)
        place_relheight_spinbox.grid(row=5, column=1, sticky="swen")

        # Place Navigation
        anchor_navigation_title = tk.Label(placement_frame, text="Anchor", background="#222222",
                                           foreground="white")
        anchor_navigation_title.grid(row=6, column=0, columnspan=2)
        place_anchor_navigation_frame = tk.Frame(placement_frame, background="#222222")
        place_anchor_navigation_frame.grid(row=7, column=0, columnspan=2, sticky="n")

        north_button = tk.Button(place_anchor_navigation_frame, text="North", command=lambda: var_nine.set('n'),
                                 height=navigation_button_height, width=navigation_button_width,
                                 background=edit_frame_background, foreground=edit_frame_foreground)
        north_button.grid(row=0, column=1)

        south_button = tk.Button(place_anchor_navigation_frame, text="South", command=lambda: var_nine.set('s'),
                                 height=navigation_button_height, width=navigation_button_width,
                                 background=edit_frame_background, foreground=edit_frame_foreground)
        south_button.grid(row=2, column=1)

        west_button = tk.Button(place_anchor_navigation_frame, text="West", command=lambda: var_nine.set('w'),
                                height=navigation_button_height, width=navigation_button_width,
                                background=edit_frame_background, foreground=edit_frame_foreground)
        west_button.grid(row=1, column=0)

        east_button = tk.Button(place_anchor_navigation_frame, text="East", command=lambda: var_nine.set('e'),
                                height=navigation_button_height, width=navigation_button_width,
                                background=edit_frame_background, foreground=edit_frame_foreground)
        east_button.grid(row=1, column=2)

        center_button = tk.Button(place_anchor_navigation_frame, text="Center", command=lambda: var_nine.set('center'),
                                  height=navigation_button_height, width=navigation_button_width,
                                  background=edit_frame_background, foreground=edit_frame_foreground, textvariable=var_nine)
        center_button.grid(row=1, column=1)


def delete_selection():
    selected_item = view_tree.selection()[0]
    view_tree.delete(selected_item)


def duplicate_selection():
    selected_item = view_tree.selection()[0]
    selected_name = view_tree.item(selected_item)['text']
    selected_values = view_tree.item(selected_item)['values']
    view_tree.insert("", tk.END, text=selected_name, values=selected_values)


def edit_selection():
    selected_item = view_tree.selection()[0]
    edit_item = view_tree.item(selected_item)
    item_values = edit_item['values']
    item_name = edit_item['text']

    # Set app vars
    widget_iid.set(selected_item)
    var_one.set(item_name)
    var_type.set(item_values[21])

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
    if var_type.get() == "label":
        label_edit_frame()
    elif var_type.get() == "button":
        button_edit_frame()
    elif var_type.get() == "entry":
        entry_edit_frame()
    elif var_type.get() == "selection":
        selection_edit_frame()
    elif var_type.get() == "image":
        image_edit_frame()
    elif var_type.get() == "graph":
        graph_edit_frame()
    elif var_type.get() == "gauge":
        gauge_edit_frame()
    elif var_type.get() == "data":
        data_edit_frame()
    elif var_type.get() == "map":
        map_edit_frame()
    elif var_type.get() == "control":
        control_edit_frame()
    elif var_type.get() == "icon":
        icon_edit_frame()
    elif var_type.get() == "table":
        table_edit_frame()


def save_edited_selection():
    iid = widget_iid.get()
    value_list = [var_two.get(), var_three.get(), var_four.get(), var_five.get(), var_six.get(), var_seven.get(),
                  var_eight.get(), var_nine.get(), var_ten.get(), var_eleven.get(), var_twelve.get(),
                  var_thirteen.get(), var_fourteen.get(), var_fifteen.get(), var_sixteen.get(), var_seventeen.get(),
                  var_eighteen.get(), var_nineteen.get(), var_twenty.get(), var_twentyone.get(), var_twentytwo.get(),
                  var_type.get()]
    view_tree.item(iid, text=var_one.get(), values=value_list)
    print(view_tree.item(iid)['values'])


def clear_edit_frame():
    for child in edit_frame.winfo_children():
        child.destroy()


def build_edit_frame():
    clear_edit_frame()
    title = tk.Label(edit_frame, text="Edit", font=("Roboto", 30), background=background_color, foreground="white")
    title.grid(row=0, column=0, columnspan=3, sticky="swen", ipadx=60)
    widget_name_label = tk.Label(edit_frame, text="Name", background=background_color, foreground="white")
    widget_name_label.grid(row=1, column=0, padx=(15, 5), pady=5)
    widget_name_entry = tk.Entry(edit_frame, textvariable=var_one)
    widget_name_entry.grid(row=1, column=1, padx=(5, 15), pady=5)

    # Placement
    pack_placement_type = tk.Radiobutton(edit_frame, variable=var_two, value='pack', text="Pack",
                                         background=edit_frame_background, foreground=edit_frame_foreground,
                                         selectcolor="#222222")
    pack_placement_type.grid(row=2, column=0, sticky="n")
    grid_placement_type = tk.Radiobutton(edit_frame, variable=var_two, value='grid', text="Grid",
                                         background=edit_frame_background, foreground=edit_frame_foreground,
                                         selectcolor="#222222")
    grid_placement_type.grid(row=3, column=0, sticky="n")
    grid_placement_type = tk.Radiobutton(edit_frame, variable=var_two, value='place', text="Place",
                                         background=edit_frame_background, foreground=edit_frame_foreground,
                                         selectcolor="#222222")
    grid_placement_type.grid(row=4, column=0, sticky="n")

    placement_choice_button = ttk.Button(edit_frame, text="Select", command=build_placement_widgets, textvariable=var_two)
    placement_choice_button.grid(row=2, column=1, rowspan=3, pady=15, padx=15)
    build_placement_widgets()

    save_button = ttk.Button(edit_frame, text="Save", command=save_edited_selection)
    save_button.grid(row=10, column=0, columnspan=2, pady=10, ipadx=10, ipady=5)


def build_font_edit_frame(row, column):
    font_edit_frame = tk.Frame(edit_frame, background="#222222")
    font_edit_frame.grid(row=row, column=column, rowspan=2, sticky="n")

    font_title = tk.Label(font_edit_frame, text="Font", background="#222222", foreground="white",
                          font=("Poor Richard", 18))
    font_title.grid(row=0, column=0, columnspan=2)
    font_title.bind("<Button-1>", lambda e: font_title.configure(font=(f"{var_fifteen.get()}", var_sixteen.get(), f"{var_seventeen.get()}")))

    font_families = []
    for family in tk.font.families():
        font_families.append(family)

    font_weights = ["normal", "bold", "italic", "bold italic"]

    # Widgets
    font_type_label = tk.Label(font_edit_frame, text="Family", background="#222222", foreground="white")
    font_type_label.grid(row=1, column=0)

    font_type_selection = ttk.Combobox(font_edit_frame, textvariable=var_fifteen, values=font_families)
    font_type_selection.grid(row=1, column=1)

    font_type_label = tk.Label(font_edit_frame, text="Family", background="#222222", foreground="white")
    font_type_label.grid(row=2, column=0)

    font_type_selection = tk.Spinbox(font_edit_frame, textvariable=var_sixteen, from_=6,
                                     background="#222222", foreground="white", to=100)
    font_type_selection.grid(row=2, column=1)

    font_weight_label = tk.Label(font_edit_frame, text="Weight", background="#222222", foreground="white")
    font_weight_label.grid(row=3, column=0)

    font_weight_selection = ttk.Combobox(font_edit_frame, textvariable=var_seventeen, values=font_weights)
    font_weight_selection.grid(row=3, column=1)


def set_background_color():
    color = tk.colorchooser.askcolor()[1]
    var_thirteen.set(color)



def set_foreground_color():
    color = tk.colorchooser.askcolor()[1]
    var_fourteen.set(color)
    foreground_color_selection['foreground'] = f"{var_fourteen.get()}"





def build_tk_colors_frame(row, column):
    tk_colors_frame = tk.Frame(edit_frame, background="#222222")
    tk_colors_frame.grid(row=row, column=column, rowspan=3, sticky="n")
    color_frame_title = tk.Label(tk_colors_frame, text="Colors", background="#222222", foreground="white", font=("Poor Richard", 18))
    color_frame_title.grid(row=0, column=0, columnspan=2, sticky="swen")

    background_color_label = tk.Label(tk_colors_frame, text="Background")
    background_color_label.grid(row=1, column=0)

    background_color_selection = tk.Button(tk_colors_frame, command=set_background_color, textvariable=var_thirteen)
    background_color_selection.grid(row=1, column=1)
    background_color_selection.bind("<Button-3>", lambda e: background_color_selection.configure(background=var_thirteen.get()))


    foreground_color_label = tk.Label(tk_colors_frame, text="Foreground")
    foreground_color_label.grid(row=2, column=0)

    foreground_color_selection = tk.Button(tk_colors_frame, command=set_foreground_color, textvariable=var_fourteen)
    foreground_color_selection.grid(row=2, column=1)

    foreground_color_selection.bind("<Button-3>",
                                    lambda e: foreground_color_selection.configure(background=var_fourteen.get()))


def build_subtype_frames():
    subtype = var_twelve.get()
    if subtype == "tk label":
        build_tk_colors_frame(2, 6)
        build_font_edit_frame(5, 6)
        text_label = tk.Label(edit_frame, text="Text", foreground="white", background="#222222")
        text_label.grid(row=7, column=6, sticky="n")
    elif subtype == "ttk label":
        pass



def build_type_frame(types):
    type_frame = tk.Frame(edit_frame, background="#222222")
    type_frame.grid(row=0, column=6)
    label_selection_label = tk.Label(type_frame, text="Type", background="#222222", foreground="white")
    label_selection_label.grid(row=0, column=0, padx=5, pady=5)
    label_selection = ttk.Combobox(type_frame, values=types, state="readonly", textvariable=var_twelve)
    label_selection.grid(row=0, column=1)
    build_frame_button = tk.Button(type_frame, text="Build", command=build_subtype_frames)
    build_frame_button.grid(row=1, column=0, columnspan=2, sticky="swen")
    build_subtype_frames()


# Widget Edit Frames
def label_edit_frame():
    build_edit_frame()
    label_types = ["tk label", "ttk label"]
    build_type_frame(label_types)


def button_edit_frame():
    build_edit_frame()
    button_types = ["tk button", "ttk button"]
    build_type_frame(button_types)


def entry_edit_frame():
    build_edit_frame()
    entry_types = ["tk entry", "ttk entry", "Multitext", "Validated entry", "Password entry"]
    build_type_frame(entry_types)


def selection_edit_frame():
    build_edit_frame()
    selection_types = ["Combobox", "Keypad", "Navipad", "Directpad", "Spinbox", "Dateslider", "Calender"]
    build_type_frame(selection_types)


def image_edit_frame():
    build_edit_frame()
    image_types = ["Image", "Videoplayer"]
    build_type_frame(image_types)


def graph_edit_frame():
    build_edit_frame()
    graph_types = ["Plot", "Plot3d"]
    build_type_frame(graph_types)


def gauge_edit_frame():
    build_edit_frame()
    gauge_types = ["Speedometer", "Voltameter"]
    build_type_frame(gauge_types)


def data_edit_frame():
    build_edit_frame()
    data_types = ["Weekly Sales Dash", "Weekly Customer Dash"]
    build_type_frame(data_types)


def map_edit_frame():
    build_edit_frame()
    map_types = ["Choropleth", "Map"]
    build_type_frame(map_types)


def control_edit_frame():
    build_edit_frame()
    control_types = ["Dial", "Slider"]
    build_type_frame(control_types)


def icon_edit_frame():
    build_edit_frame()
    icon_types = ["Icon", "Dashicon"]
    build_type_frame(icon_types)


def table_edit_frame():
    build_edit_frame()
    table_types = ["Spreadsheet", "Table"]
    build_type_frame(table_types)

    if var_twelve == "Spreadsheet":
        row_count_label = tk.Label()

        row_count_spinbox = tk.Spinbox()

    elif var_twelve == "Table":
        row_count_label = tk.Label(edit_frame, text="Rows")
        row_count_label.grid(row=2, column=6)

        row_count_spinbox = tk.Spinbox(edit_frame)
        row_count_spinbox.grid(row=2, column=7)



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
tree_frame.grid(row=0, column=1, sticky="swen")

edit_frame = tk.Frame(build_page, background=background_color)
edit_frame.grid(row=0, column=2, sticky="n", rowspan=2)

control_frame = tk.Frame(build_page, background=background_color)
control_frame.grid(row=1, column=1, sticky="n")


# Tree Frame
view_tree = ttk.Treeview(tree_frame)
view_tree.grid(row=1, column=0, sticky="swen", ipadx=15, ipady=100)
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
widget_title = tk.Label(widget_frame, text="Widgets", font=("Roboto", 30), background=background_color,
                        foreground="white")
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

placement_frame = tk.Frame()
pack_side_navigation_frame = tk.Frame()
pack_anchor_navigation_frame = tk.Frame()
place_anchor_navigation_frame = tk.Frame()
font_edit_frame = tk.Frame()
type_frame = tk.Frame()
tk_colors_frame = tk.Frame()
background_color_selection = tk.Button(tk_colors_frame)
foreground_color_selection = tk.Button(tk_colors_frame)


root.mainloop()
