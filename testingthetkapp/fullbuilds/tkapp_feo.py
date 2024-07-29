import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import colorchooser
from tkinter import font
from datetime import datetime
import toml
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import random


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
primary_color_var = tk.StringVar()
secondary_color_var = tk.StringVar()
accent_color_var = tk.StringVar()
help_color_var = tk.StringVar()
primary_text_bool = tk.BooleanVar()
secondary_text_bool = tk.BooleanVar()
accent_text_bool = tk.BooleanVar()
help_text_bool = tk.BooleanVar()
body_text_type = tk.StringVar()
body_text_size = tk.StringVar()
test_text_var = tk.StringVar()
color_palette_selected = tk.StringVar()


# System var
font_list = list()
color_one_var = tk.StringVar()
color_two_var = tk.StringVar()
color_three_var = tk.StringVar()
color_four_var = tk.StringVar()
color_five_var = tk.StringVar()
color_six_var = tk.StringVar()
color_seven_var = tk.StringVar()
color_eight_var = tk.StringVar()
color_nine_var = tk.StringVar()
color_ten_var = tk.StringVar()

color_one_bool_var = tk.BooleanVar()
color_two_bool_var = tk.BooleanVar()
color_three_bool_var = tk.BooleanVar()
color_four_bool_var = tk.BooleanVar()
color_five_bool_var = tk.BooleanVar()
color_six_bool_var = tk.BooleanVar()
color_seven_bool_var = tk.BooleanVar()
color_eight_bool_var = tk.BooleanVar()
color_nine_bool_var = tk.BooleanVar()
color_ten_bool_var = tk.BooleanVar()

color_one_bool_var.set(True)


# App lists
color_palette_list = ["tab10", "deep", "muted", "pastel", "bright", "dark", "colorblind", "tab20", "tab20b", "tab20c",
                      "hls", "husl", "rocket", "mako", "flare", "crest", "viridis", "plasma", "inferno", "magma",
                      "cividis", "bwr", "seismic", "vlag", "icefire", "coolwarm", "greys", "reds", "greens", "blues", "oranges", "purples", "rdgy", "spectral"]
tab10_list = ["#5778a4", "#e49444", "#d1615d", "#85b6b2", "#6a9f58", "#e7ca60", "#a87c9f", "#f1a2a9", "#967662", "#b8b0ac"]
deep_list = ["#4c72b0", "#dd8452", "#55a868", "#c44e52", "#8172b3", "#937860", "#da8bc3", "#8c8c8c", "#ccb974", "#64b5cd"]
muted_list = ["#4878d0", "#ee854a", "#6acc64", "#d65f5f", "#956cb4", "#8c613c", "#dc7ec0", "#797979", "#d5bb67", "#82c6e2"]
pastel_list = ["#a1c9f4", "#ffb482", "#8de5a1", "#ff9f9b", "#d0bbff", "#debb9b", "#fab0e4", "#cfcfcf", "#fffea3", "#b9f2f0"]
bright_list = ["#023eff", "#ff7c00", "#1ac938", "#e8000b", "#8b2be2", "#9f4800", "#f14cc1", "#a3a3a3", "#ffc400", "#00d7ff"]
dark_list = ["#001c7f", "#b1400d", "#12711c", "#8c0800", "#591e71", "#592f0d", "#a23582", "#3c3c3c", "#b8850a", "#006374"]
colorblind_list = ["#0173b2", "#de8f05", "#029e73", "#d55e00", "#cc78bc", "#ca9161", "#fbafe4", "#949494", "#ece133", "#56b4e9"]
tab20_list = ["#1f77b4", "#aec7e8", "#ff7f0e", "#ffbb78", "#2ca02c", "#98df8a", "#d62728", "#ff9896", "#9467bd", "#c5b0d5"]
tab20b_list = ["#393b79", "#5254a3", "#6b6ecf", "#9c9ede", "#637939", "#8ca252", "#b5cf6b", "#cedb9c", "#8c6d31", "#bd9e39"]
tab20c_list = ["#3182bd", "#6baed6", "#9ecae1", "#c6dbef", "#e6550d", "#fd8d3c", "#fdae6b", "#fdd0a2", "#31a354", "#74c476"]
hls_list = ["#db5e56", "#dbae56", "#b8db56", "#69db56", "#56db93", "$56d3db", "#5683db", "#7956db", "#c856db", "#db569e"]
husl_list = ["#f67088", "#db8831", "#ad9c31", "#77aa31", "#33b07a", "#35aca4", "#38a8c5", "#6e9af4", "#cc79f4", "#f565cc"]
rocket_list = ["#221330", "#441b46", "#691f55", "#911c5b", "#b81656", "#d92747", "#ed503e", "#f37d56", "#f5a47b", "#f6c8aa"]
mako_list = ["#221526", "#35264b", "#3f3974", "#3c5296", "#356d9f", "#3487a5", "#35a0aa", "#43bbad", "#6dd2ac", "#ade2bf"]
flare_list = ["#ea9972", "#e88265", "#e36c56", "#da555c", "#cb4563", "#b73d6a", "#a1376f", "#8b3170", "#752c6e", "#5f2868"]
crest_list = ["#8bc091", "#71b490", "#5ca790", "#4a998f", "#3b8b8d", "#2c7e8c", "#1f708a", "#1c6187", "#225182", "#28417a"]
viridis_list = ["#482172", "#423d84", "#38578c", "#2d6f8e", "#24858d", "#1e9a89", "#2ab07e", "#51c468", "#86d449", "#c2df22"]
plasma_list = ["#3d039b", "#6200a6", "#8506a6", "#a51f97", "#bf3982", "#d5536d", "#e76e5a", "#f58d45", "#fcad31", "#fbd124"]
inferno_list = ["#130a34", "#390962", "#5f126e", "#85206a", "#a92e5e", "#cb4049", "#e65c2e", "#f78310", "#fbae12", "#f4db4b"]
magma_list = ["#110c31", "#321067", "#58157e", "#7e2481", "#a3307e", "#c83d72", "#e85461", "#f97d5d", "#fea873", "#fdd295"]
cividis_list = ["#003170", "#2f426c", "#48516b", "#5e626e", "#727374", "#868378", "#9d9575", "#b5a86e", "#cdbc62", "#e6d04f"]
bwr_list = ["#2e2eff", "#5c5cff", "#8a8aff", "#babaff", "#e8e8ff", "#ffe8e8", "#ffbaba", "#ff8a8a", "#ff5c5c", "#ff2e2e"]
vlag_list = ["#5781bc", "#7e9ac2", "#a3b3cd", "#c9d0dd", "#efedf0", "#f6e9e8", "#e6c5c2", "#d6a09d", "#c87d7b", "#b95b5a"]
seismic_list = ["#00008c", "#0000cd", "#1515ff", "#7575ff", "#d1d1ff", "#ffd1d1", "#ff7575", "#ff1515", "#db0000", "#ad0000"]
icefire_list = ["#7abbce", "#3f8fce", "#465bbb", "#3a3865", "#22212a", "#2d1e21", "#612937", "#a82f43", "#dc5433", "#f29457"]
coolwarm_list = ["#5673e0", "#7497f5", "#94b5fe", "#b4cdfa", "#d0dae9", "#e7d6cc", "#f5c1a8", "#f5a182", "#ea7b60", "#d34d40"]
greys_list = ["#f4f4f4", "#e5e5e5", "#d4d4d4", "#bfbfbf", "#a4a4a4", "#898989", "#707070", "#575757", "#383838", "#1a1a1a"]
reds_list = ["#fee5da", "#fdcfbc", "#fcb499", "#fc9575", "#fb7858", "#f6593f", "#ec382a", "#d01d1f", "#b51218", "#930a12"]
greens_list = ["#eaf6e5", "#d7efd1", "#c0e6b9", "#a4da9e", "#84cb83", "#61ba6c", "#3ea85b", "#279048", "#0f7a37", "#006127"]
blues_list = ["#e4eff9", "#d3e3f3", "#bfd8ec", "#a1cbe2", "#7db8d9", "#5ca3d0", "#3f8fc4", "#2676b7", "#135fa7", "#08478e"]
oranges_list = ["#feead6", "#fddcba", "#fdca98", "#fdb06f", "#fd984c", "#f8802d", "#ef6611", "#dc4d03", "#bc3d02", "#9b3103"]
purples_list = ["#f2f0f7", "#e5e4f0", "#d5d5e8", "#bebfdd", "#a8a6cf", "#938fc2", "#7e79b8", "#6d58a6", "#5d3997", "#4e1c89"]
rdgy_list = ["#aa1529", "#ce5146", "#eb9072", "#f9c7ae", "#feeee5", "#f1f1f1", "#d2d2d2", "#ababab", "#7b7b7b", "#484848"]
spectral_list = ["#cf384d", "#ed6345", "#fa9a58", "#fdce7c", "#fef1a7", "#f3faad", "#d1ec9c", "#96d5a4", "#5bb6a9", "#3682ba"]






def palette_list_creator(*args):
    # Change colors
    palette_name = color_palette_selected.get()
    if palette_name == "tab10":
        update_palette_buttons(tab10_list)

    elif palette_name == "deep":
        update_palette_buttons(deep_list)

    elif palette_name == "muted":
        update_palette_buttons(muted_list)

    elif palette_name == "pastel":
        update_palette_buttons(pastel_list)

    elif palette_name == "bright":
        update_palette_buttons(bright_list)

    elif palette_name == "dark":
        update_palette_buttons(dark_list)

    elif palette_name == "colorblind":
        update_palette_buttons(colorblind_list)

    elif palette_name == "tab20":
        update_palette_buttons(tab20_list)

    elif palette_name == "tab20b":
        update_palette_buttons(tab20b_list)

    elif palette_name == "tab20c":
        update_palette_buttons(tab20c_list)

    elif palette_name == "hls":
        update_palette_buttons(hls_list)

    elif palette_name == "husl":
        update_palette_buttons(husl_list)

    elif palette_name == "rocket":
        update_palette_buttons(rocket_list)

    elif palette_name == "mako":
        update_palette_buttons(mako_list)

    elif palette_name == "flare":
        update_palette_buttons(flare_list)

    elif palette_name == "crest":
        update_palette_buttons(crest_list)

    elif palette_name == "viridis":
        update_palette_buttons(viridis_list)

    elif palette_name == "plasma":
        update_palette_buttons(plasma_list)

    elif palette_name == "inferno":
        update_palette_buttons(inferno_list)

    elif palette_name == "magma":
        update_palette_buttons(magma_list)

    elif palette_name == "cividis":
        update_palette_buttons(cividis_list)

    elif palette_name == "bwr":
        update_palette_buttons(bwr_list)

    elif palette_name == "seismic":
        update_palette_buttons(seismic_list)

    elif palette_name == "vlag":
        update_palette_buttons(vlag_list)

    elif palette_name == "icefire":
        update_palette_buttons(icefire_list)

    elif palette_name == "coolwarm":
        update_palette_buttons(coolwarm_list)

    elif palette_name == "greys":
        update_palette_buttons(greys_list)

    elif palette_name == "reds":
        update_palette_buttons(reds_list)

    elif palette_name == "greens":
        update_palette_buttons(greens_list)

    elif palette_name == "blues":
        update_palette_buttons(blues_list)

    elif palette_name == "oranges":
        update_palette_buttons(oranges_list)

    elif palette_name == "purples":
        update_palette_buttons(purples_list)

    elif palette_name == "rdgy":
        update_palette_buttons(rdgy_list)

    elif palette_name == "spectral":
        update_palette_buttons(spectral_list)



def update_palette_frame_var(list_name):
    color_one_var.set(list_name[0])
    color_two_var.set(list_name[1])
    color_three_var.set(list_name[2])
    color_four_var.set(list_name[3])
    color_five_var.set(list_name[4])
    color_six_var.set(list_name[5])
    color_seven_var.set(list_name[6])
    color_eight_var.set(list_name[7])
    color_nine_var.set(list_name[8])
    color_ten_var.set(list_name[9])


def update_palette_buttons(list_name):
    update_palette_frame_var(list_name)
    color_one_button["background"] = color_one_var.get()
    color_one_button["text"] = color_one_var.get()

    color_two_button["background"] = color_two_var.get()
    color_two_button["text"] = color_two_var.get()

    color_three_button["background"] = color_three_var.get()
    color_three_button["text"] = color_three_var.get()

    color_four_button["background"] = color_four_var.get()
    color_four_button["text"] = color_four_var.get()

    color_five_button["background"] = color_five_var.get()
    color_five_button["text"] = color_five_var.get()

    color_six_button["background"] = color_six_var.get()
    color_six_button["text"] = color_six_var.get()

    color_seven_button["background"] = color_seven_var.get()
    color_seven_button["text"] = color_seven_var.get()

    color_eight_button["background"] = color_eight_var.get()
    color_eight_button["text"] = color_eight_var.get()

    color_nine_button["background"] = color_nine_var.get()
    color_nine_button["text"] = color_nine_var.get()

    color_ten_button["background"] = color_ten_var.get()
    color_ten_button["text"] = color_ten_var.get()



def update_color_palette_button_text_color(button_number, *args):
    if button_number == 1:
        if color_one_bool_var.get() is True:
            color_one_button["foreground"] = "white"
            color_one_bool_var.set(False)
        else:
            color_one_button["foreground"] = "black"
            color_one_bool_var.set(True)



# Autoset
primary_text_bool.set(True)
secondary_text_bool.set(True)
accent_text_bool.set(True)
help_text_bool.set(True)
test_text_var.set("Test Text")
body_text_type.set("Times New Roman")
body_text_size.set(18)
color_palette_selected.set("tab10")


# Tkapp Boilerplate Code
information_code = f"""# {app_name_var.get()} was created in Tkapp on {datetime.now()}.
Tkapp is a RAD tool created by Lloyd Andersen under the MIT license in 2024.
"""

start_code = f"""import tkinter as tk
from tkinter import ttk
"""

button_code = f"""{widget_name_var.get()} = tk.Button()
"""

def get_system_fonts():
    fonts = tk.font.families()
    for font in fonts:
        font_list.append(font)


get_system_fonts()


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


# Graph frame Designs
def graph_menu_go_back_to_graph(current_frame):
    if current_frame == "pairwise":
        graph_pairwise_frame.grid_forget()
        widget_graph_frame.grid(row=0, column=0, sticky="swen")
    elif current_frame == "statistical":
        graph_statistical_distributions_frame.grid_forget()
        widget_graph_frame.grid(row=0, column=0, sticky="swen")
    elif current_frame == "gridded":
        graph_gridded_data_frame.grid_forget()
        widget_graph_frame.grid(row=0, column=0, sticky="swen")
    elif current_frame == "irr gridded":
        graph_irregularly_gridded_data_frame.grid_forget()
        widget_graph_frame.grid(row=0, column=0, sticky="swen")
    elif current_frame == "3d":
        graph_3d_frame.grid_forget()
        widget_graph_frame.grid(row=0, column=0, sticky="swen")
    elif current_frame == "spatial":
        graph_spatial_data_frame.grid_forget()
        widget_graph_frame.grid(row=0, column=0, sticky="swen")


def dash_menu_go_back_to_dash(current_frame):
    if current_frame == "car":
        dash_car_frame.grid_forget()
        widget_dash_frame.grid(row=0, column=0, sticky="swen")
    elif current_frame == "plane":
        dash_plane_frame.grid_forget()
        widget_dash_frame.grid(row=0, column=0, sticky="swen")
    elif current_frame == "measure":
        dash_measurement_frame.grid_forget()
        widget_dash_frame.grid(row=0, column=0, sticky="swen")
    elif current_frame == "board":
        dashboard_frame.grid_forget()
        widget_dash_frame.grid(row=0, column=0, sticky="swen")


def open_car_dash_frame():
    widget_dash_frame.grid_forget()
    dash_car_frame.grid(row=0, column=0, sticky="swen")
    back_button = ttk.Button(dash_car_frame, text="back", command=lambda: dash_menu_go_back_to_dash("car"))
    back_button.grid(row=0, column=0, sticky="nw")

    # Widgets
    icon_widget = ttk.Button(dash_car_frame, text="Icon", style="widget.TButton")
    icon_widget.grid(row=1, column=0, ipady=10)

    speedometer_widget = ttk.Button(dash_car_frame, text="Speedometer", style="widget.TButton")
    speedometer_widget.grid(row=1, column=1, ipady=10)

    tachometer_widget = ttk.Button(dash_car_frame, text="Tachometer", style="widget.TButton")
    tachometer_widget.grid(row=2, column=0, ipady=10)

    fuel_gauge_widget = ttk.Button(dash_car_frame, text="Fuel Gauge", style="widget.TButton")
    fuel_gauge_widget.grid(row=2, column=1, ipady=10)

    oil_pressure_widget = ttk.Button(dash_car_frame, text="Oil Pressure", style="widget.TButton")
    oil_pressure_widget.grid(row=3, column=0, ipady=10)

    coolant_temperature_widget = ttk.Button(dash_car_frame, text="Cool Temp", style="widget.TButton")
    coolant_temperature_widget.grid(row=3, column=1, ipady=10)

    battery_voltage_widget = ttk.Button(dash_car_frame, text="Battery Volt", style="widget.TButton")
    battery_voltage_widget.grid(row=4, column=0, ipady=10)

    tire_pressure_widget = ttk.Button(dash_car_frame, text="Tire Pressure", style="widget.TButton")
    tire_pressure_widget.grid(row=4, column=1, ipady=10)


def open_plane_dash_frame():
    widget_dash_frame.grid_forget()
    dash_plane_frame.grid(row=0, column=0, sticky="swen")
    back_button = ttk.Button(dash_plane_frame, text="back", command=lambda: dash_menu_go_back_to_dash("plane"))
    back_button.grid(row=0, column=0, sticky="nw")

    # Widgets
    altimeter_widget = ttk.Button(dash_plane_frame, text="Altimeter", style="widget.TButton")
    altimeter_widget.grid(row=1, column=0, ipady=10)

    airspeed_indicator_widget = ttk.Button(dash_plane_frame, text="Airspeed", style="widget.TButton")
    airspeed_indicator_widget.grid(row=1, column=1, ipady=10)

    vertical_speed_indicator_widget = ttk.Button(dash_plane_frame, text="VSI", style="widget.TButton")
    vertical_speed_indicator_widget.grid(row=2, column=0, ipady=10)

    attitude_indicator_widget = ttk.Button(dash_plane_frame, text="Attitude", style="widget.TButton")
    attitude_indicator_widget.grid(row=2, column=1, ipady=10)

    heading_indicator_widget = ttk.Button(dash_plane_frame, text="HI", style="widget.TButton")
    heading_indicator_widget.grid(row=3, column=0, ipady=10)

    turn_coordinator_widget = ttk.Button(dash_plane_frame, text="TC", style="widget.TButton")
    turn_coordinator_widget.grid(row=3, column=1, ipady=10)

    compass_widget = ttk.Button(dash_plane_frame, text="Compass", style="widget.TButton")
    compass_widget.grid(row=4, column=0, ipady=10)

    instrument_landing_widget = ttk.Button(dash_plane_frame, text="ILS", style="widget.TButton")
    instrument_landing_widget.grid(row=4, column=1, ipady=10)

    angle_of_attack_indicator_widget = ttk.Button(dash_plane_frame, text="AOA", style="widget.TButton")
    angle_of_attack_indicator_widget.grid(row=5, column=0, ipady=10)

    bank_indicator_widget = ttk.Button(dash_plane_frame, text="Bank", style="widget.TButton")
    bank_indicator_widget.grid(row=5, column=1, ipady=10)


def open_measurement_dash_frame():
    widget_dash_frame.grid_forget()
    dash_measurement_frame.grid(row=0, column=0, sticky="swen")
    back_button = ttk.Button(dash_measurement_frame, text="back", command=lambda: dash_menu_go_back_to_dash("measure"))
    back_button.grid(row=0, column=0, sticky="nw")

    # Widgets
    pressure_widget = ttk.Button(dash_measurement_frame, text="Pressure", style="widget.TButton")
    pressure_widget.grid(row=1, column=0, ipady=10)

    light_block_widget = ttk.Button(dash_measurement_frame, text="Light Block", style="widget.TButton")
    light_block_widget.grid(row=1, column=1, ipady=10)

    temperature_widget = ttk.Button(dash_measurement_frame, text="Temperature", style="widget.TButton")
    temperature_widget.grid(row=2, column=0, ipady=10)

    ammeter_widget = ttk.Button(dash_measurement_frame, text="Ammeter", style="widget.TButton")
    ammeter_widget.grid(row=2, column=1, ipady=10)

    voltameter_widget = ttk.Button(dash_measurement_frame, text="Voltameter", style="widget.TButton")
    voltameter_widget.grid(row=3, column=0, ipady=10)

    humidity_widget = ttk.Button(dash_measurement_frame, text="Humidity", style="widget.TButton")
    humidity_widget.grid(row=3, column=1, ipady=10)

    warning_icon_widget = ttk.Button(dash_measurement_frame, text="Warnicon", style="widget.TButton")
    warning_icon_widget.grid(row=4, column=0, ipady=10)

    gyro_compass_widget = ttk.Button(dash_measurement_frame, text="Gyro Comp", style="widget.TButton")
    gyro_compass_widget.grid(row=4, column=1, ipady=10)

    roll_widget = ttk.Button(dash_measurement_frame, text="Roll", style="widget.TButton")
    roll_widget.grid(row=5, column=0, ipady=10)

    pitch_widget = ttk.Button(dash_measurement_frame, text="Pitch", style="widget.TButton")
    pitch_widget.grid(row=5, column=1, ipady=10)

    yaw_widget = ttk.Button(dash_measurement_frame, text="Yaw", style="widget.TButton")
    yaw_widget.grid(row=6, column=0, ipady=10)

    thrust_widget = ttk.Button(dash_measurement_frame, text="Thrust", style="widget.TButton")
    thrust_widget.grid(row=6, column=1, ipady=10)


def open_dashboard_frame():
    widget_dash_frame.grid_forget()
    dashboard_frame.grid(row=0, column=0, sticky="swen")
    back_button = ttk.Button(dashboard_frame, text="back", command=lambda: dash_menu_go_back_to_dash("board"))
    back_button.grid(row=0, column=0, sticky="nw")

    # Widgets
    sales_widget = ttk.Button(dashboard_frame, text="Sales", style="widget.TButton")
    sales_widget.grid(row=1, column=0, ipady=10)

    marketing_widget = ttk.Button(dashboard_frame, text="Marketing", style="widget.TButton")
    marketing_widget.grid(row=1, column=1, ipady=10)

    ecommerce_widget = ttk.Button(dashboard_frame, text="Ecommerce", style="widget.TButton")
    ecommerce_widget.grid(row=2, column=0, ipady=10)

    saas_daily_widget = ttk.Button(dashboard_frame, text="Saas Day", style="widget.TButton")
    saas_daily_widget.grid(row=2, column=1, ipady=10)


def open_pairwise_data_frame():
    widget_graph_frame.grid_forget()
    graph_pairwise_frame.grid(row=0, column=0, sticky="swen")
    back_button = ttk.Button(graph_pairwise_frame, text="back", command=lambda: graph_menu_go_back_to_graph("pairwise"))
    back_button.grid(row=0, column=0, sticky="nw")

    # Widgets
    plot_widget = ttk.Button(graph_pairwise_frame, text="Plot", style="widget.TButton")
    plot_widget.grid(row=1, column=0, ipady=10)

    scatter_widget = ttk.Button(graph_pairwise_frame, text="Scatter", style="widget.TButton")
    scatter_widget.grid(row=1, column=1, ipady=10)

    bar_widget = ttk.Button(graph_pairwise_frame, text="Bar", style="widget.TButton")
    bar_widget.grid(row=2, column=0, ipady=10)

    stem_widget = ttk.Button(graph_pairwise_frame, text="Stem", style="widget.TButton")
    stem_widget.grid(row=2, column=1, ipady=10)

    fill_between_widget = ttk.Button(graph_pairwise_frame, text="Fill_Bet", style="widget.TButton")
    fill_between_widget.grid(row=3, column=0, ipady=10)

    stack_plot_widget = ttk.Button(graph_pairwise_frame, text="Stackplot", style="widget.TButton")
    stack_plot_widget.grid(row=3, column=1, ipady=10)

    stairs_widget = ttk.Button(graph_pairwise_frame, text="Stairs", style="widget.TButton")
    stairs_widget.grid(row=4, column=0, ipady=10)


def open_statistical_data_frame():
    widget_graph_frame.grid_forget()
    graph_statistical_distributions_frame.grid(row=0, column=0, sticky="swen")
    back_button = ttk.Button(graph_statistical_distributions_frame, text="back",
                             command=lambda: graph_menu_go_back_to_graph("statistical"))
    back_button.grid(row=0, column=0, sticky="nw")

    # Widgets
    hist_widget = ttk.Button(graph_statistical_distributions_frame, text="Hist", style="widget.TButton")
    hist_widget.grid(row=1, column=0, ipady=10)

    box_plot_widget = ttk.Button(graph_statistical_distributions_frame, text="Boxplot", style="widget.TButton")
    box_plot_widget.grid(row=1, column=1, ipady=10)

    error_bar_widget = ttk.Button(graph_statistical_distributions_frame, text="Errorbar", style="widget.TButton")
    error_bar_widget.grid(row=2, column=0, ipady=10)

    violin_plot_widget = ttk.Button(graph_statistical_distributions_frame, text="Violinplot", style="widget.TButton")
    violin_plot_widget.grid(row=2, column=1, ipady=10)

    event_plot_widget = ttk.Button(graph_statistical_distributions_frame, text="Eventplot", style="widget.TButton")
    event_plot_widget.grid(row=3, column=0, ipady=10)

    hist_2d_widget = ttk.Button(graph_statistical_distributions_frame, text="Hist2d", style="widget.TButton")
    hist_2d_widget.grid(row=3, column=1, ipady=10)

    hexbin_widget = ttk.Button(graph_statistical_distributions_frame, text="hexbin", style="widget.TButton")
    hexbin_widget.grid(row=4, column=0, ipady=10)

    pie_widget = ttk.Button(graph_statistical_distributions_frame, text="Pie", style="widget.TButton")
    pie_widget.grid(row=4, column=1, ipady=10)

    ecdf_widget = ttk.Button(graph_statistical_distributions_frame, text="ecdf", style="widget.TButton")
    ecdf_widget.grid(row=5, column=0, ipady=10)


def open_gridded_data_frame():
    widget_graph_frame.grid_forget()
    graph_gridded_data_frame.grid(row=0, column=0, sticky="swen")
    back_button = ttk.Button(graph_gridded_data_frame, text="back",
                             command=lambda: graph_menu_go_back_to_graph("gridded"))
    back_button.grid(row=0, column=0, sticky="nw")

    # Widgets
    imshow_widget = ttk.Button(graph_gridded_data_frame, text="imshow", style="widget.TButton")
    imshow_widget.grid(row=1, column=0, ipady=10)

    pcolormesh_widget = ttk.Button(graph_gridded_data_frame, text="pcolormesh", style="widget.TButton")
    pcolormesh_widget.grid(row=1, column=1, ipady=10)

    contour_widget = ttk.Button(graph_gridded_data_frame, text="countour", style="widget.TButton")
    contour_widget.grid(row=2, column=0, ipady=10)

    countourf_widget = ttk.Button(graph_gridded_data_frame, text="countourf", style="widget.TButton")
    countourf_widget.grid(row=2, column=1, ipady=10)

    barbs_widget = ttk.Button(graph_gridded_data_frame, text="barbs", style="widget.TButton")
    barbs_widget.grid(row=3, column=0, ipady=10)

    quiver_widget = ttk.Button(graph_gridded_data_frame, text="quiver", style="widget.TButton")
    quiver_widget.grid(row=3, column=1, ipady=10)

    stream_plot_widget = ttk.Button(graph_gridded_data_frame, text="streamplot", style="widget.TButton")
    stream_plot_widget.grid(row=4, column=0, ipady=10)


def open_irr_gridded_data_frame():
    widget_graph_frame.grid_forget()
    graph_irregularly_gridded_data_frame.grid(row=0, column=0, sticky="swen")
    back_button = ttk.Button(graph_irregularly_gridded_data_frame, text="back",
                             command=lambda: graph_menu_go_back_to_graph("irr gridded"))
    back_button.grid(row=0, column=0, sticky="nw")

    # Widgets
    tricontour_widget = ttk.Button(graph_irregularly_gridded_data_frame, text="tricontour", style="widget.TButton")
    tricontour_widget.grid(row=1, column=0, ipady=10)

    tricontourf_widget = ttk.Button(graph_irregularly_gridded_data_frame, text="tricontourf", style="widget.TButton")
    tricontourf_widget.grid(row=1, column=1, ipady=10)

    tripcolor_widget = ttk.Button(graph_irregularly_gridded_data_frame, text="tripcolor", style="widget.TButton")
    tripcolor_widget.grid(row=2, column=0, ipady=10)

    triplot_widget = ttk.Button(graph_irregularly_gridded_data_frame, text="triplot", style="widget.TButton")
    triplot_widget.grid(row=2, column=1, ipady=10)


def open_3d_data_frame():
    widget_graph_frame.grid_forget()
    graph_3d_frame.grid(row=0, column=0, sticky="swen")
    back_button = ttk.Button(graph_3d_frame, text="back", command=lambda: graph_menu_go_back_to_graph("3d"))
    back_button.grid(row=0, column=0, sticky="nw")

    # Widgets
    bar_3d_widget = ttk.Button(graph_3d_frame, text="Bar 3d", style="widget.TButton")
    bar_3d_widget.grid(row=1, column=0, ipady=10)

    plot_3d_widget = ttk.Button(graph_3d_frame, text="Plot 3d", style="widget.TButton")
    plot_3d_widget.grid(row=1, column=1, ipady=10)

    quiver_3d_widget = ttk.Button(graph_3d_frame, text="Quiver 3d", style="widget.TButton")
    quiver_3d_widget.grid(row=2, column=0, ipady=10)

    scatter_3d_widget = ttk.Button(graph_3d_frame, text="Scatter 3d", style="widget.TButton")
    scatter_3d_widget.grid(row=2, column=1, ipady=10)

    stem_3d_widget = ttk.Button(graph_3d_frame, text="Stem 3d", style="widget.TButton")
    stem_3d_widget.grid(row=3, column=0, ipady=10)

    plot_surface_widget = ttk.Button(graph_3d_frame, text="Plot Surf", style="widget.TButton")
    plot_surface_widget.grid(row=3, column=1, ipady=10)

    plot_tri_surface_widget = ttk.Button(graph_3d_frame, text="Plot Trisurf", style="widget.TButton")
    plot_tri_surface_widget.grid(row=4, column=0, ipady=10)

    voxel_widget = ttk.Button(graph_3d_frame, text="Voxel", style="widget.TButton")
    voxel_widget.grid(row=4, column=1, ipady=10)

    plot_wire_frame_widget = ttk.Button(graph_3d_frame, text="Plot wire", style="widget.TButton")
    plot_wire_frame_widget.grid(row=5, column=0, ipady=10)


def open_spatial_data_frame():
    widget_graph_frame.grid_forget()
    graph_spatial_data_frame.grid(row=0, column=0, sticky="swen")
    back_button = ttk.Button(graph_spatial_data_frame, text="back",
                             command=lambda: graph_menu_go_back_to_graph("spatial"))
    back_button.grid(row=0, column=0, sticky="nw")

    # Widgets
    map_widget = ttk.Button(graph_spatial_data_frame, text="Map", style="widget.TButton")
    map_widget.grid(row=1, column=0, ipady=10)

    sat_track_widget = ttk.Button(graph_spatial_data_frame, text="SatTrack", style="widget.TButton")
    sat_track_widget.grid(row=1, column=1, ipady=10)

    choropleth_map_widget = ttk.Button(graph_spatial_data_frame, text="Choropleth", style="widget.TButton")
    choropleth_map_widget.grid(row=2, column=0, ipady=10)

    base_map_plot_widget = ttk.Button(graph_spatial_data_frame, text="BaseMap", style="widget.TButton")
    base_map_plot_widget.grid(row=2, column=1, ipady=10)

    nuke_map_widget = ttk.Button(graph_spatial_data_frame, text="NukeMap", style="widget.TButton")
    nuke_map_widget.grid(row=3, column=0, ipady=10)

    network_plot_widget = ttk.Button(graph_spatial_data_frame, text="Network", style="widget.TButton")
    network_plot_widget.grid(row=3, column=1, ipady=10)


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

    round_button_widget = ttk.Button(widget_button_frame, text="rButton", style="widget.TButton")
    round_button_widget.grid(row=3, column=1, ipady=10)

    oval_button_widget = ttk.Button(widget_button_frame, text="oButton", style="widget.TButton")
    oval_button_widget.grid(row=4, column=0, ipady=10)

    check_button_widget = ttk.Button(widget_button_frame, text="CheckButton", style="widget.TButton")
    check_button_widget.grid(row=4, column=1, ipady=10)


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

    listbox_widget = ttk.Button(widget_box_frame, text="Listbox", style="widget.TButton")
    listbox_widget.grid(row=2, column=0, ipady=10)

    checkbox_widget = ttk.Button(widget_box_frame, text="Listbox", style="widget.TButton")
    checkbox_widget.grid(row=2, column=0, ipady=10)


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

    gamepad_widget = ttk.Button(widget_control_frame, text="Gamepad", style="widget.TButton")
    gamepad_widget.grid(row=5, column=0, ipady=10)

    simplenav_widget = ttk.Button(widget_control_frame, text="Simplenav", style="widget.TButton")
    simplenav_widget.grid(row=5, column=1, ipady=10)

    navipad_arrow_widget = ttk.Button(widget_control_frame, text="Arrowpad", style="widget.TButton")
    navipad_arrow_widget.grid(row=6, column=0, ipady=10)

    navipad_direction_widget = ttk.Button(widget_control_frame, text="Directpad", style="widget.TButton")
    navipad_direction_widget.grid(row=6, column=1, ipady=10)

    powerwheel_widget = ttk.Button(widget_control_frame, text="PowerWheel", style="widget.TButton")
    powerwheel_widget.grid(row=7, column=0, ipady=10)


def open_widget_graph_frame():
    close_widget_home_frame()
    widget_graph_frame.grid(row=0, column=0, sticky="swen")
    back_button = ttk.Button(widget_graph_frame, text="back", command=lambda: widget_menu_go_back_to_home("graph"))
    back_button.grid(row=0, column=0, sticky="nw")

    # Categories
    pairwise_data_button = ttk.Button(widget_graph_frame, text="Pairwise", style="widget.TButton",
                                      command=open_pairwise_data_frame)
    pairwise_data_button.grid(row=1, column=0, sticky="swen")

    statistical_data_button = ttk.Button(widget_graph_frame, text="Statistical", style="widget.TButton",
                                         command=open_statistical_data_frame)
    statistical_data_button.grid(row=2, column=0, sticky="swen")

    gridded_data_button = ttk.Button(widget_graph_frame, text="Gridded", style="widget.TButton",
                                     command=open_gridded_data_frame)
    gridded_data_button.grid(row=3, column=0, sticky="swen")

    irrgrid_data_button = ttk.Button(widget_graph_frame, text="IrrGridded", style="widget.TButton",
                                     command=open_irr_gridded_data_frame)
    irrgrid_data_button.grid(row=4, column=0, sticky="swen")

    three_d_data_button = ttk.Button(widget_graph_frame, text="3D", style="widget.TButton",
                                     command=open_3d_data_frame)
    three_d_data_button.grid(row=5, column=0, sticky="swen")

    spatial_data_button = ttk.Button(widget_graph_frame, text="Spatial", style="widget.TButton",
                                     command=open_spatial_data_frame)
    spatial_data_button.grid(row=6, column=0, sticky="swen")


def open_widget_dash_frame():
    close_widget_home_frame()
    widget_dash_frame.grid(row=0, column=0, sticky="swen")
    back_button = ttk.Button(widget_dash_frame, text="back", command=lambda: widget_menu_go_back_to_home("dash"))
    back_button.grid(row=0, column=0, sticky="nw")

    # Categories
    car_dash_button = ttk.Button(widget_dash_frame, text="Car", style="widget.TButton",
                                 command=open_car_dash_frame)
    car_dash_button.grid(row=1, column=0, sticky="swen")

    plane_dash_button = ttk.Button(widget_dash_frame, text="Plane", style="widget.TButton",
                                   command=open_plane_dash_frame)
    plane_dash_button.grid(row=2, column=0, sticky="swen")

    measurement_dash_button = ttk.Button(widget_dash_frame, text="Measure", style="widget.TButton",
                                         command=open_measurement_dash_frame)
    measurement_dash_button.grid(row=3, column=0, sticky="swen")

    dashboard_button = ttk.Button(widget_dash_frame, text="Dashboard", style="widget.TButton",
                                  command=open_dashboard_frame)
    dashboard_button.grid(row=4, column=0, sticky="swen")


def open_widget_info_frame():
    close_widget_home_frame()
    widget_info_frame.grid(row=0, column=0, sticky="swen")
    back_button = ttk.Button(widget_info_frame, text="back", command=lambda: widget_menu_go_back_to_home("info"))
    back_button.grid(row=0, column=0, sticky="nw")

    # Widgets
    spreadsheet_widget = ttk.Button(widget_info_frame, text="Spreadsheet", style="widget.TButton")
    spreadsheet_widget.grid(row=1, column=0, ipady=10)

    stockchart_widget = ttk.Button(widget_info_frame, text="StockChart", style="widget.TButton")
    stockchart_widget.grid(row=1, column=1, ipady=10)

    video_player_widget = ttk.Button(widget_info_frame, text="Videoplayer", style="widget.TButton")
    video_player_widget.grid(row=2, column=0, ipady=10)

    weather_widget = ttk.Button(widget_info_frame, text="Weather", style="widget.TButton")
    weather_widget.grid(row=2, column=1, ipady=10)

    music_player_widget = ttk.Button(widget_info_frame, text="Music", style="widget.TButton")
    music_player_widget.grid(row=3, column=0, ipady=10)

    radio_widget = ttk.Button(widget_info_frame, text="Radio", style="widget.TButton")
    radio_widget.grid(row=3, column=1, ipady=10)

    webcam_widget = ttk.Button(widget_info_frame, text="Webcam", style="widget.TButton")
    webcam_widget.grid(row=4, column=0, ipady=10)

    system_info_widget = ttk.Button(widget_info_frame, text="System", style="widget.TButton")
    system_info_widget.grid(row=4, column=1, ipady=10)

    internet_info_widget = ttk.Button(widget_info_frame, text="Internet", style="widget.TButton")
    internet_info_widget.grid(row=5, column=0, ipady=10)

    car_damage_widget = ttk.Button(widget_info_frame, text="Car Dam", style="widget.TButton")
    car_damage_widget.grid(row=5, column=1, ipady=10)

    plane_damage_widget = ttk.Button(widget_info_frame, text="Plane Dam", style="widget.TButton")
    plane_damage_widget.grid(row=6, column=0, ipady=10)

    human_damage_widget = ttk.Button(widget_info_frame, text="Human Dam", style="widget.TButton")
    human_damage_widget.grid(row=6, column=1, ipady=10)

    image_widget = ttk.Button(widget_info_frame, text="Image", style="widget.TButton")
    image_widget.grid(row=7, column=0, ipady=10)

    tank_damage_widget = ttk.Button(widget_info_frame, text="Tank Dam", style="widget.TButton")
    tank_damage_widget.grid(row=7, column=1, ipady=10)


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


def select_color_theme():
    pass

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


# Dash Widget Frames
dash_car_frame = ttk.Frame(build_page)
dash_plane_frame = ttk.Frame(build_page)
dash_measurement_frame = ttk.Frame(build_page)
dashboard_frame = ttk.Frame(build_page)

# Graph Widgets Frame
graph_pairwise_frame = ttk.Frame(build_page)
graph_statistical_distributions_frame = ttk.Frame(build_page)
graph_gridded_data_frame = ttk.Frame(build_page)
graph_irregularly_gridded_data_frame = ttk.Frame(build_page)
graph_3d_frame = ttk.Frame(build_page)
graph_spatial_data_frame = ttk.Frame(build_page)


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
    app_file = open(f"{file_name_var.get()}.toml", "w")
    config = dict()
    config["app_name"] = f"{app_name_var.get()}"
    config["file_name"] = f"{file_name_var.get()}"
    config["primary_color"] = f"{primary_color_var.get()}"
    config["secondary_color"] = f"{secondary_color_var.get()}"
    config["accent_color"] = f"{accent_color_var.get()}"

    toml.dump(config, app_file)
    app_file.close()


def save_app_dialog():
    answer = tk.messagebox.askyesno("Save App", "Do you want to save this App?")
    if answer is True:
        save_app_file()
        tk.messagebox.showinfo("Save Confirmation", "App Save Successful!")
    else:
        pass


def open_app_file(file_name):
    app_file = open(f'{file_name}', "r")
    config = toml.load(app_file)
    app_name = config['app_name']
    appended_file_name = config['file_name']

    # configure app
    app_name_var.set(app_name)
    file_name_var.set(appended_file_name)

    app_file.close()


def open_app_dialog():
    file_name = tk.filedialog.askopenfilename(filetypes=[("Toml files", "*.toml")])
    open_app_file(file_name)


def create_tkapp():
    pass


def create_tkapp_dialog():
    answer = tk.messagebox.askyesno("Create Tkapp", "Do you want to create a Tkapp?")
    if answer is True:
        pass
    else:
        pass


# Create Page
save_app_button = ttk.Button(create_page, text="Save", command=save_app_dialog)
save_app_button.grid(row=0, column=0)

open_app_button = ttk.Button(create_page, text="Open", command=open_app_dialog)
open_app_button.grid(row=1, column=0)

create_tkapp_button = ttk.Button(create_page, text="Create", command=create_tkapp_dialog)
create_tkapp_button.grid(row=2, column=0)


app_name_label = ttk.Label(create_page, text="App Name")
app_name_label.grid(row=4, column=0)
app_name_entry = ttk.Entry(create_page, textvariable=app_name_var)
app_name_entry.grid(row=4, column=1)

file_name_label = ttk.Label(create_page, text="File Name")
file_name_label.grid(row=5, column=0)
file_name_entry = ttk.Entry(create_page, textvariable=file_name_var)
file_name_entry.grid(row=5, column=1)

palette_frame = ttk.Frame(style_page)
palette_frame.grid(row=7, column=0, columnspan=2, sticky="swen")

def style_page_text_color_change(button, *args):
    if button == "primary":
        if primary_text_bool.get() is True:
            primary_color_button["foreground"] = "black"
            primary_text_bool.set(False)
        else:
            primary_color_button["foreground"] = "white"
            primary_text_bool.set(True)

    elif button == "secondary":
        if secondary_text_bool.get() is True:
            secondary_color_button["foreground"] = "black"
            secondary_text_bool.set(False)
        else:
            secondary_color_button["foreground"] = "white"
            secondary_text_bool.set(True)

    elif button == "accent":
        if accent_text_bool.get() is True:
            accent_color_button["foreground"] = "black"
            accent_text_bool.set(False)
        else:
            accent_color_button["foreground"] = "white"
            accent_text_bool.set(True)

    elif button == "help":
        if help_text_bool.get() is True:
            help_color_button["foreground"] = "black"
            help_text_bool.set(False)
        else:
            help_color_button["foreground"] = "white"
            help_text_bool.set(True)



print(accent_text_bool.get())

def select_color_with_button(button, *args):
    if button == "primary":
        color = tk.colorchooser.askcolor()
        primary_color_var.set(color[1])
        primary_color_button["background"] = primary_color_var.get()
        print(primary_color_var.get())
    elif button == "secondary":
        color = tk.colorchooser.askcolor()
        secondary_color_var.set(color[1])
        secondary_color_button["background"] = secondary_color_var.get()
    elif button == "accent":
        color = tk.colorchooser.askcolor()
        accent_color_var.set(color[1])
        accent_color_button["background"] = accent_color_var.get()
    elif button == "help":
        color = tk.colorchooser.askcolor()
        help_color_var.set(color[1])
        help_color_button["background"] = help_color_var.get()



def update_test_text(*args):
    new_text = test_text_var.get()
    primary_color_button['text'] = new_text
    secondary_color_button['text'] = new_text
    accent_color_button['text'] = new_text
    help_color_button['text'] = new_text


def update_font_selections(*args):
    type = body_text_type.get()
    size = body_text_size.get()

    primary_color_button["font"] = (f"{type}", size)
    secondary_color_button["font"] = (f"{type}", size)
    accent_color_button["font"] = (f"{type}", size)
    help_color_button["font"] = (f"{type}", size)


def mix_the_colors():
    palette_name = color_palette_selected.get()
    num_to_select = 4
    if palette_name == "tab10":
        list_of_random_colors = random.sample(tab10_list, num_to_select)
        primary_color_button["background"] = list_of_random_colors[0]
        secondary_color_button["background"] = list_of_random_colors[1]
        accent_color_button["background"] = list_of_random_colors[2]
        help_color_button["background"] = list_of_random_colors[3]
    elif palette_name == "deep":
        list_of_random_colors = random.sample(deep_list, num_to_select)
        primary_color_button["background"] = list_of_random_colors[0]
        secondary_color_button["background"] = list_of_random_colors[1]
        accent_color_button["background"] = list_of_random_colors[2]
        help_color_button["background"] = list_of_random_colors[3]
    elif palette_name == "muted":
        list_of_random_colors = random.sample(muted_list, num_to_select)
        primary_color_button["background"] = list_of_random_colors[0]
        secondary_color_button["background"] = list_of_random_colors[1]
        accent_color_button["background"] = list_of_random_colors[2]
        help_color_button["background"] = list_of_random_colors[3]
    elif palette_name == "pastel":
        list_of_random_colors = random.sample(pastel_list, num_to_select)
        primary_color_button["background"] = list_of_random_colors[0]
        secondary_color_button["background"] = list_of_random_colors[1]
        accent_color_button["background"] = list_of_random_colors[2]
        help_color_button["background"] = list_of_random_colors[3]
    elif palette_name == "bright":
        list_of_random_colors = random.sample(bright_list, num_to_select)
        primary_color_button["background"] = list_of_random_colors[0]
        secondary_color_button["background"] = list_of_random_colors[1]
        accent_color_button["background"] = list_of_random_colors[2]
        help_color_button["background"] = list_of_random_colors[3]
    elif palette_name == "dark":
        list_of_random_colors = random.sample(dark_list, num_to_select)
        primary_color_button["background"] = list_of_random_colors[0]
        secondary_color_button["background"] = list_of_random_colors[1]
        accent_color_button["background"] = list_of_random_colors[2]
        help_color_button["background"] = list_of_random_colors[3]
    elif palette_name == "colorblind":
        list_of_random_colors = random.sample(colorblind_list, num_to_select)
        primary_color_button["background"] = list_of_random_colors[0]
        secondary_color_button["background"] = list_of_random_colors[1]
        accent_color_button["background"] = list_of_random_colors[2]
        help_color_button["background"] = list_of_random_colors[3]
    elif palette_name == "tab20":
        list_of_random_colors = random.sample(tab20_list, num_to_select)
        primary_color_button["background"] = list_of_random_colors[0]
        secondary_color_button["background"] = list_of_random_colors[1]
        accent_color_button["background"] = list_of_random_colors[2]
        help_color_button["background"] = list_of_random_colors[3]
    elif palette_name == "tab20b":
        list_of_random_colors = random.sample(tab20b_list, num_to_select)
        primary_color_button["background"] = list_of_random_colors[0]
        secondary_color_button["background"] = list_of_random_colors[1]
        accent_color_button["background"] = list_of_random_colors[2]
        help_color_button["background"] = list_of_random_colors[3]
    elif palette_name == "tab20c":
        list_of_random_colors = random.sample(tab20c_list, num_to_select)
        primary_color_button["background"] = list_of_random_colors[0]
        secondary_color_button["background"] = list_of_random_colors[1]
        accent_color_button["background"] = list_of_random_colors[2]
        help_color_button["background"] = list_of_random_colors[3]
    elif palette_name == "hls":
        list_of_random_colors = random.sample(hls_list, num_to_select)
        primary_color_button["background"] = list_of_random_colors[0]
        secondary_color_button["background"] = list_of_random_colors[1]
        accent_color_button["background"] = list_of_random_colors[2]
        help_color_button["background"] = list_of_random_colors[3]
    elif palette_name == "husl":
        list_of_random_colors = random.sample(husl_list, num_to_select)
        primary_color_button["background"] = list_of_random_colors[0]
        secondary_color_button["background"] = list_of_random_colors[1]
        accent_color_button["background"] = list_of_random_colors[2]
        help_color_button["background"] = list_of_random_colors[3]
    elif palette_name == "rocket":
        list_of_random_colors = random.sample(rocket_list, num_to_select)
        primary_color_button["background"] = list_of_random_colors[0]
        secondary_color_button["background"] = list_of_random_colors[1]
        accent_color_button["background"] = list_of_random_colors[2]
        help_color_button["background"] = list_of_random_colors[3]
    elif palette_name == "mako":
        list_of_random_colors = random.sample(mako_list, num_to_select)
        primary_color_button["background"] = list_of_random_colors[0]
        secondary_color_button["background"] = list_of_random_colors[1]
        accent_color_button["background"] = list_of_random_colors[2]
        help_color_button["background"] = list_of_random_colors[3]
    elif palette_name == "flare":
        list_of_random_colors = random.sample(flare_list, num_to_select)
        primary_color_button["background"] = list_of_random_colors[0]
        secondary_color_button["background"] = list_of_random_colors[1]
        accent_color_button["background"] = list_of_random_colors[2]
        help_color_button["background"] = list_of_random_colors[3]
    elif palette_name == "crest":
        list_of_random_colors = random.sample(crest_list, num_to_select)
        primary_color_button["background"] = list_of_random_colors[0]
        secondary_color_button["background"] = list_of_random_colors[1]
        accent_color_button["background"] = list_of_random_colors[2]
        help_color_button["background"] = list_of_random_colors[3]
    elif palette_name == "viridis":
        list_of_random_colors = random.sample(viridis_list, num_to_select)
        primary_color_button["background"] = list_of_random_colors[0]
        secondary_color_button["background"] = list_of_random_colors[1]
        accent_color_button["background"] = list_of_random_colors[2]
        help_color_button["background"] = list_of_random_colors[3]
    elif palette_name == "plasma":
        list_of_random_colors = random.sample(plasma_list, num_to_select)
        primary_color_button["background"] = list_of_random_colors[0]
        secondary_color_button["background"] = list_of_random_colors[1]
        accent_color_button["background"] = list_of_random_colors[2]
        help_color_button["background"] = list_of_random_colors[3]
    elif palette_name == "inferno":
        list_of_random_colors = random.sample(inferno_list, num_to_select)
        primary_color_button["background"] = list_of_random_colors[0]
        secondary_color_button["background"] = list_of_random_colors[1]
        accent_color_button["background"] = list_of_random_colors[2]
        help_color_button["background"] = list_of_random_colors[3]
    elif palette_name == "magma":
        list_of_random_colors = random.sample(magma_list, num_to_select)
        primary_color_button["background"] = list_of_random_colors[0]
        secondary_color_button["background"] = list_of_random_colors[1]
        accent_color_button["background"] = list_of_random_colors[2]
        help_color_button["background"] = list_of_random_colors[3]
    elif palette_name == "cividis":
        list_of_random_colors = random.sample(cividis_list, num_to_select)
        primary_color_button["background"] = list_of_random_colors[0]
        secondary_color_button["background"] = list_of_random_colors[1]
        accent_color_button["background"] = list_of_random_colors[2]
        help_color_button["background"] = list_of_random_colors[3]
    elif palette_name == "bwr":
        list_of_random_colors = random.sample(bwr_list, num_to_select)
        primary_color_button["background"] = list_of_random_colors[0]
        secondary_color_button["background"] = list_of_random_colors[1]
        accent_color_button["background"] = list_of_random_colors[2]
        help_color_button["background"] = list_of_random_colors[3]
    elif palette_name == "seismic":
        list_of_random_colors = random.sample(seismic_list, num_to_select)
        primary_color_button["background"] = list_of_random_colors[0]
        secondary_color_button["background"] = list_of_random_colors[1]
        accent_color_button["background"] = list_of_random_colors[2]
        help_color_button["background"] = list_of_random_colors[3]
    elif palette_name == "vlag":
        list_of_random_colors = random.sample(vlag_list, num_to_select)
        primary_color_button["background"] = list_of_random_colors[0]
        secondary_color_button["background"] = list_of_random_colors[1]
        accent_color_button["background"] = list_of_random_colors[2]
        help_color_button["background"] = list_of_random_colors[3]
    elif palette_name == "icefire":
        list_of_random_colors = random.sample(icefire_list, num_to_select)
        primary_color_button["background"] = list_of_random_colors[0]
        secondary_color_button["background"] = list_of_random_colors[1]
        accent_color_button["background"] = list_of_random_colors[2]
        help_color_button["background"] = list_of_random_colors[3]
    elif palette_name == "coolwarm":
        list_of_random_colors = random.sample(coolwarm_list, num_to_select)
        primary_color_button["background"] = list_of_random_colors[0]
        secondary_color_button["background"] = list_of_random_colors[1]
        accent_color_button["background"] = list_of_random_colors[2]
        help_color_button["background"] = list_of_random_colors[3]
    elif palette_name == "greys":
        list_of_random_colors = random.sample(greys_list, num_to_select)
        primary_color_button["background"] = list_of_random_colors[0]
        secondary_color_button["background"] = list_of_random_colors[1]
        accent_color_button["background"] = list_of_random_colors[2]
        help_color_button["background"] = list_of_random_colors[3]
    elif palette_name == "reds":
        list_of_random_colors = random.sample(reds_list, num_to_select)
        primary_color_button["background"] = list_of_random_colors[0]
        secondary_color_button["background"] = list_of_random_colors[1]
        accent_color_button["background"] = list_of_random_colors[2]
        help_color_button["background"] = list_of_random_colors[3]
    elif palette_name == "greens":
        list_of_random_colors = random.sample(greens_list, num_to_select)
        primary_color_button["background"] = list_of_random_colors[0]
        secondary_color_button["background"] = list_of_random_colors[1]
        accent_color_button["background"] = list_of_random_colors[2]
        help_color_button["background"] = list_of_random_colors[3]
    elif palette_name == "blues":
        list_of_random_colors = random.sample(blues_list, num_to_select)
        primary_color_button["background"] = list_of_random_colors[0]
        secondary_color_button["background"] = list_of_random_colors[1]
        accent_color_button["background"] = list_of_random_colors[2]
        help_color_button["background"] = list_of_random_colors[3]
    elif palette_name == "oranges":
        list_of_random_colors = random.sample(oranges_list, num_to_select)
        primary_color_button["background"] = list_of_random_colors[0]
        secondary_color_button["background"] = list_of_random_colors[1]
        accent_color_button["background"] = list_of_random_colors[2]
        help_color_button["background"] = list_of_random_colors[3]
    elif palette_name == "purples":
        list_of_random_colors = random.sample(purples_list, num_to_select)
        primary_color_button["background"] = list_of_random_colors[0]
        secondary_color_button["background"] = list_of_random_colors[1]
        accent_color_button["background"] = list_of_random_colors[2]
        help_color_button["background"] = list_of_random_colors[3]
    elif palette_name == "rdgy":
        list_of_random_colors = random.sample(rdgy_list, num_to_select)
        primary_color_button["background"] = list_of_random_colors[0]
        secondary_color_button["background"] = list_of_random_colors[1]
        accent_color_button["background"] = list_of_random_colors[2]
        help_color_button["background"] = list_of_random_colors[3]
    elif palette_name == "spectral":
        list_of_random_colors = random.sample(spectral_list, num_to_select)
        primary_color_button["background"] = list_of_random_colors[0]
        secondary_color_button["background"] = list_of_random_colors[1]
        accent_color_button["background"] = list_of_random_colors[2]
        help_color_button["background"] = list_of_random_colors[3]



# "tab10", "deep", "muted", "pastel", "bright", "dark", "colorblind", "tab20", "tab20b", "tab20c",
#                       "hls", "husl", "rocket", "mako", "flare", "crest", "viridis", "plasma", "inferno", "magma",
#                       "cividis", "bwr", "seismic"
# "vlag", "icefire", "coolwarm", "greys", "reds", "greens", "blues", "oranges", "purples", "rdgy", "spectral"

# Style Page
primary_color_button = tk.Button(style_page, height=3, width=20, command=lambda: select_color_with_button("primary"), textvariable=test_text_var)
primary_color_button.grid(row=0, column=1)
primary_color_button.bind("<Button-3>", lambda e: style_page_text_color_change("primary"))
primary_color_label = ttk.Label(style_page, text="Primary")
primary_color_label.grid(row=0, column=0)

secondary_color_button = tk.Button(style_page, height=3, width=20, command=lambda: select_color_with_button("secondary"), textvariable=test_text_var)
secondary_color_button.grid(row=1, column=1)
secondary_color_button.bind("<Button-3>", lambda e: style_page_text_color_change("secondary"))
secondary_color_label = ttk.Label(style_page, text="Secondary")
secondary_color_label.grid(row=1, column=0)

accent_color_button = tk.Button(style_page, height=3, width=20, command=lambda: select_color_with_button("accent"), textvariable=test_text_var)
accent_color_button.grid(row=2, column=1)
accent_color_button.bind("<Button-3>", lambda e: style_page_text_color_change("accent"))
accent_color_label = ttk.Label(style_page, text="Accent")
accent_color_label.grid(row=2, column=0)

help_color_button = tk.Button(style_page, height=3, width=20, command=lambda: select_color_with_button("help"), textvariable=test_text_var)
help_color_button.grid(row=3, column=1)
help_color_button.bind("<Button-3>", lambda e: style_page_text_color_change("help"))
help_color_label = ttk.Label(style_page, text="Help")
help_color_label.grid(row=3, column=0)

body_text_type_combobox = ttk.Combobox(style_page, textvariable=body_text_type, values=font_list)
body_text_type_combobox.grid(row=4, column=0)
body_text_type_combobox.bind("<Button-3>", update_font_selections)

body_text_size_spinbox = ttk.Spinbox(style_page, from_=10, to=30, textvariable=body_text_size, state="readonly")
body_text_size_spinbox.grid(row=4, column=1)
body_text_size_spinbox.bind("<Button-3>", update_font_selections)

test_text_entry = ttk.Entry(style_page, textvariable=test_text_var)
test_text_entry.grid(row=5, column=0)
test_text_entry.bind("<Return>", update_test_text)


random_color_type_combobox = ttk.Combobox(style_page, values=color_palette_list, textvariable=color_palette_selected)
random_color_type_combobox.grid(row=6, column=0)
random_color_type_combobox.bind("<Button-3>", palette_list_creator)

random_color_mix_button = ttk.Button(style_page, text="Mix", command=mix_the_colors)
random_color_mix_button.grid(row=6, column=1)




color_button_height = 2
color_button_width = 8

color_one_button = tk.Button(palette_frame, height=color_button_height, width=color_button_width)
color_one_button.grid(row=0, column=0, sticky="swen")
color_one_button.bind("<Button-3>", lambda e: update_color_palette_button_text_color(1))

color_two_button = tk.Button(palette_frame, height=color_button_height, width=color_button_width)
color_two_button.grid(row=0, column=1, sticky="swen")

color_three_button = tk.Button(palette_frame, height=color_button_height, width=color_button_width)
color_three_button.grid(row=0, column=2, sticky="swen")

color_four_button = tk.Button(palette_frame, height=color_button_height, width=color_button_width)
color_four_button.grid(row=0, column=3, sticky="swen")

color_five_button = tk.Button(palette_frame, height=color_button_height, width=color_button_width)
color_five_button.grid(row=0, column=4, sticky="swen")

color_six_button = tk.Button(palette_frame, height=color_button_height, width=color_button_width)
color_six_button.grid(row=0, column=5, sticky="swen")

color_seven_button = tk.Button(palette_frame, height=color_button_height, width=color_button_width)
color_seven_button.grid(row=0, column=6, sticky="swen")

color_eight_button = tk.Button(palette_frame, height=color_button_height, width=color_button_width)
color_eight_button.grid(row=0, column=7, sticky="swen")

color_nine_button = tk.Button(palette_frame, height=color_button_height, width=color_button_width)
color_nine_button.grid(row=0, column=8, sticky="swen")

color_ten_button = tk.Button(palette_frame, height=color_button_height, width=color_button_width)
color_ten_button.grid(row=0, column=9, sticky="swen")

root.mainloop()
