import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from datetime import datetime
import toml

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
primary_text_bool = tk.BooleanVar()
secondary_text_bool = tk.BooleanVar()
accent_text_bool = tk.BooleanVar()
body_text_type = tk.StringVar()
body_text_size = tk.StringVar()
subtitle_text_type = tk.StringVar()
subtitle_text_size = tk.StringVar()


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
    back_button = ttk.Button(graph_statistical_distributions_frame, text="back", command=lambda: graph_menu_go_back_to_graph("statistical"))
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
    back_button = ttk.Button(graph_gridded_data_frame, text="back", command=lambda: graph_menu_go_back_to_graph("gridded"))
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
    back_button = ttk.Button(graph_irregularly_gridded_data_frame, text="back", command=lambda: graph_menu_go_back_to_graph("irr gridded"))
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
    back_button = ttk.Button(graph_spatial_data_frame, text="back", command=lambda: graph_menu_go_back_to_graph("spatial"))
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
    app_file = open(f'{file_name}', "rb")
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


app_name_label = ttk.Label(create_page, text="App Name")
app_name_label.grid(row=4, column=0)
app_name_entry = ttk.Entry(create_page, textvariable=app_name_var)
app_name_entry.grid(row=4, column=1)

file_name_label = ttk.Label(create_page, text="File Name")
file_name_label.grid(row=5, column=0)
file_name_entry = ttk.Entry(create_page, textvariable=file_name_var)
file_name_entry.grid(row=5, column=1)

root.mainloop()
