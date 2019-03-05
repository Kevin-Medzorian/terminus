from Tkinter import *
from mission_map import map

TOP_FRAME_HEIGHT = 325
BOT_FRAME_HEIGHT = 100
# frame paddings
PADX = 5
PADY = 5
# button paddings
bPADX = 10
bPADY = 2.5
# button width and heigth (in text units) 
BUTTON_WIDTH = 17
BUTTON_HEIGHT = 2

class Base_Station_GUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Yonder Arctic OPS")

        self.top_frame = Frame(self.master, bd = 1) 
        self.top_frame.pack( fill = BOTH, side = TOP, padx = PADX, pady = PADY, expand = YES)

        self.bot_frame = Frame(self.master, bd = 1)
        self.bot_frame.pack( fill = BOTH, side = BOTTOM, padx = PADX, pady = PADY, expand = YES)
 
        self.init_function_frame()
        self.init_map_frame()
        self.init_status_frame()
        self.init_log_frame()
        self.init_legend_frame()
        self.init_config_frame()
        self.create_function_buttons()

        self.create_map(self.map_frame)

    # Create the frame for functions
    def init_function_frame(self):
        self.functions_frame = Frame(self.top_frame, height = TOP_FRAME_HEIGHT, width = 150, bd = 1, relief = SUNKEN)
        self.functions_frame.pack( padx = PADX, pady = PADY, side = LEFT, expand = NO)
        self.functions_frame.pack_propagate(0)
        #self.function_label = Label(self.functions_frame, text = "in functions frame").pack() 

    # Create the frame for the x, y map
    def init_map_frame(self):
        self.map_frame = Frame(self.top_frame, height = TOP_FRAME_HEIGHT, width = 335, bd = 1, relief = SUNKEN)
        self.map_frame.pack( fill = BOTH, padx = PADX, pady = PADY, side = LEFT, expand = YES)
        self.map_frame.pack_propagate(0)
        #self.map_label = Label(self.map_frame, text = "in map label").pack()

    
    def init_status_frame(self):
        self.status_frame = Frame(self.top_frame, height = TOP_FRAME_HEIGHT, width = 350, bd = 1, relief = SUNKEN )
        self.status_frame.pack(fill = BOTH, padx = PADX, pady = PADY, side = LEFT, expand = NO)
        self.status_frame.pack_propagate(0)
        self.status_label = Label(self.status_frame, text = "Vehicle Stats", font = ("Comic Sans", 20))
        self.status_label.pack() 
        self.status_label.place(relx = 0.22, rely = 0.02)
        
        self.position_label_string = StringVar()
        self.position_label = Label(self.status_frame, textvariable = self.position_label_string, font = ("Comic Sans", 14), justify = LEFT)
        self.position_label.pack()
        self.position_label_string.set("Position \n \tX: \t Y: ")
        self.position_label.place(relx = 0.05, rely = 0.30, anchor = 'sw') 

        self.heading_label_string = StringVar()
        self.heading_label = Label(self.status_frame, textvariable = self.heading_label_string, font = ("Comic Sans", 14), justify = LEFT)
        self.heading_label.pack()
        self.heading_label_string.set("Heading: ")
        self.heading_label.place(relx = 0.05, rely = 0.40, anchor = 'sw')

        self.battery_status_string = StringVar()
        self.battery_voltage = Label(self.status_frame, textvariable = self.battery_status_string, font = ("Comic Sans", 14))
        self.battery_voltage.pack()
        self.battery_status_string.set("Battery Voltage: ")
        self.battery_voltage.place(relx = 0.05, rely = 0.50, anchor = 'sw')

        self.vehicle_status_string = StringVar()
        self.vehicle_status = Label(self.status_frame, textvariable = self.vehicle_status_string, font = ("Comic Sans", 14))
        self.vehicle_status.pack()
        self.vehicle_status_string.set("Vehicle Status: Manual Control")
        self.vehicle_status.place(relx = 0.05, rely = 0.60, anchor = 'sw')

        self.comms_status_string = StringVar()
        self.comms_status = Label(self.status_frame, textvariable = self.comms_status_string, font = ("Comic Sans", 14))
        self.comms_status.pack()
        self.comms_status_string.set("Comms Status: Not connected")
        self.comms_status.place(relx = 0.05, rely = 0.70, anchor = 'sw')

    def init_log_frame(self):
        self.log_frame = Frame(self.bot_frame, height = BOT_FRAME_HEIGHT, width = 100, bd = 1, relief = SUNKEN )
        self.log_frame.pack( fill = BOTH, padx = PADX, pady = PADY, side = LEFT, expand = YES)
        self.log_frame.pack_propagate(0)
        #self.log_label = Label(self.log_frame, text = "in log frame").pack()

    def init_legend_frame(self): 
        self.legend_frame = Frame(self.bot_frame, height = BOT_FRAME_HEIGHT, width = 100, bd = 1, relief = SUNKEN)
        self.legend_frame.pack( fill = BOTH, padx = PADX, pady = PADY, side = LEFT, expand = YES)
        self.legend_frame.pack_propagate(0)
        #self.legend_label = Label(self.legend_frame, text = "in legend frame").pack()

    def init_config_frame(self):
        self.config_frame = Frame(self.bot_frame, height = BOT_FRAME_HEIGHT, width = 100, bd = 1, relief = SUNKEN)
        self.config_frame.pack( fill = BOTH, padx = PADX, pady = PADY, side = LEFT, expand = YES)
        self.config_frame.pack_propagate(0)
        #self.config_label = Label(self.config_frame, text = "in config frame").pack() 

    def create_function_buttons(self):
        self.origin_button           = Button(self.functions_frame, text = "Set Origin", takefocus = False, width = BUTTON_WIDTH, height = BUTTON_HEIGHT,
																						padx = bPADX, pady = bPADY, command = lambda: None)
        self.add_waypoint_button     = Button(self.functions_frame, text = "Add Waypoint", takefocus = False, width = BUTTON_WIDTH, height = BUTTON_HEIGHT, 
																						padx = bPADX, pady = bPADY, command = lambda: None)
        self.nav_to_waypoint_button  = Button(self.functions_frame, text = "Navigate to Waypoint", takefocus = False, width = BUTTON_WIDTH, height = BUTTON_HEIGHT,
																						padx = bPADX, pady = bPADY, command = lambda: None)
        self.ballast_button          = Button(self.functions_frame, text = "Start Ballast", takefocus = False, width = BUTTON_WIDTH, height = BUTTON_HEIGHT,
																						padx = bPADX, pady = bPADY, command = lambda: None)
        self.switch_to_manual_button = Button(self.functions_frame, text = "Switch to Manual", takefocus = False, width = BUTTON_WIDTH, height = BUTTON_HEIGHT,
																						padx = bPADX, pady = bPADY, command = lambda: None)
        self.abort_button            = Button(self.functions_frame, text = "Stop Manual", takefocus = False, width = BUTTON_WIDTH, height = BUTTON_HEIGHT,
																						padx = bPADX, pady = bPADY, command = lambda: None)
        self.stop_manual_button      = Button(self.functions_frame, text = "ABORT MISSION", takefocus = False, width = BUTTON_WIDTH, height = BUTTON_HEIGHT,
																						padx = bPADX, pady = bPADY, command = lambda: None)

        self.origin_button.pack(pady = 3)
        self.add_waypoint_button.pack(pady = 3)
        self.nav_to_waypoint_button.pack(pady = 3)
        self.ballast_button.pack(pady = 3)
        self.switch_to_manual_button.pack(pady = 3)
        self.abort_button.pack(pady = 3)
        self.stop_manual_button.pack(pady = 3)
        
    def create_map(self, frame):
        self.map = map(frame)        

root = Tk()
root.geometry("1200x600") 
Base_Station_GUI = Base_Station_GUI(root)
root.mainloop()
