import json
import line_class
import IOPi
#i2c_helper = ABEHelpers()
#i2c_bus = i2c_helper.get_smbus()
#from Adafruit_PWM_Servo_Driver import PWM

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
        # pwm[colour+"_pwm"]
