import json
import line_class
import tkinter as tk
from tkinter import ttk
# import IOPi
# i2c_helper = ABEHelpers()
# i2c_bus = i2c_helper.get_smbus()
# from Adafruit_PWM_Servo_Driver import PWM


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Trewern Trains")
        self.geometry("1000x700+100+100")

        # Start Trains Button
        self.start_trains_btn = ttk.Button(
            self,
            text="Start Trains",
            command=self.start_trains
        )
        self.start_trains_btn.pack()

        # Add New Train Button
        self.new_train_btn = ttk.Button(
            self,
            text="Add New Train",
            command=self.new_train
        )
        self.new_train_btn.pack()

        # Modify Sectors Button
        self.change_sectors_btn = ttk.Button(
            self,
            text="Modify Sectors",
            command=self.change_sectors
        )
        self.change_sectors_btn.pack()

    def start_trains(self):
        print("placeholder")

    def new_train(self):
        new_train_window = New_Train_Window()

    def change_sectors(self):
        print("placeholder")


class New_Train_Window(tk.Toplevel):
    def __init__(self):
        super().__init__()

        self.title = "Add/Enter train in database"
        self.geometry("500x500+300+300")

        self.label = ttk.Label(
            self,
            text="Enter a Train Number:"
        )
        self.label.pack()

        self.train_num = tk.StringVar()
        self.textbox = ttk.Entry(
            self,
            textvariable=self.train_num
        )
        self.textbox.pack()
        self.textbox.focus()

        self.enter = ttk.Button(
            self,
            text="Enter",
            command=lambda: self.check_database()
        )
        self.enter.pack()

        self.wait_visibility()
        self.grab_set()

    def check_database(self):
        with open("./trains.json") as train_db_file:
            self.train_db = json.load(train_db_file)
        try:
            self.train_db[self.train_num.get()]
            self.edit_train()
        except KeyError:
            self.add_train()

    def edit_train(self):
        print("edit train")

    def add_train(self):
        print("add train")


if __name__ == "__main__":
    lines = {}
    line_colours = ["red", "blue"]
    points = ["point1", "point2", "point3"]
    """
    # set address values for pwm board
    pwm = {
        "red": PWM(0x40),
        "blue": PWM(0x41),
        "point1": PWM(0x42),
        "point2": PWM(0x43),
        "point3": PWM(0x44)
    }
    pwm["red"].setPWMFreq(15000)
    pwm["blue"].setPWMFreq(15000)
    for point in points:
        pwm[point].setPWMFreq(50)

    # set address values for IO board
    io_bus = {
        "red1": IOPi(0x20)
        "red2": IOPi(0x21)
        "blue1": IOPi(0x22)
        "blue2": IOPi(0x23)
        "exit": IOPi(0x24)
    }
    
    for i in range(1,17):
        j = i-1
        for point in ["point1", "point2", "point3"]:
            pwm[point].setPWM(j,0,205)
        pwm["red"].setPWM(j,0,0)
        pwm["blue"].setPWM(j,0,0)
        for colour in line_colours:
            for num in ["1", "2"]:
                # setup pins 1-16 as input
                io_bus[colour+num].set_pin_direction(i,1)
                # setup input on bus as pullup
                io_bus[colour+num].set_pin_pullup(i,1)
                # invert input on bus so o/c gives logic 1
                io_bus[colour+num].invert_pin(i,1)
        io_bus["exit"].set_pin_direction(i,1)
        io_bus["exit"].set_pin_pullup(i,1)
        io_bus["exit"].invert_pin(i,1)
    """
    for colour in line_colours:
        lines[colour] = line_class.Line(colour)
        print(json.dumps(lines[colour].sectors, indent=4))

    app = App()
    app.mainloop()
