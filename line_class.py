import json


class Line:
    # line class holds list of sectors and methods for adding, getting and moving trains
    def __init__(self, name):
        with open("./"+name+"Sectors.json", "r") as sectors_file:
            self.sectors = json.load(sectors_file)
        self.name = name

    def overflow(self, index, length):
        if index > length:
            return index - length
        else:
            return index

    def __set_speed(self, speed, sector):
        if speed == "stop":
            self.sectors[sector]["set_speed"] = 0
            print(sector+": speed at stop")
        elif speed == "one_third":
            self.sectors[sector]["set_speed"] = 33
            print(sector+": speed at 1/3")
        elif speed == "two_third":
            self.sectors[sector]["set_speed"] = 66
            print(sector+": speed at 2/3")
        elif speed == "full":
            self.sectors[sector]["set_speed"] = 100
            print(sector+": speed at full")

    def __speed_selector(self, sector, difference):
        # selects speed of sector if there is a train in front
        if difference == -1 or difference == 15:
            self.__set_speed("stop", sector)
        elif difference == -2 or difference == 14:
            self.__set_speed("one_third", sector)
        elif difference == -3 or difference == 13:
            self.__set_speed("two_third", sector)
        return True

    def check_speed(self):
        for sector in self.sectors:
            length = len(self.sectors)
            speed_set = False
            for i in range(1, 4):
                next_sector = str(self.overflow(int(sector) + i, length))
                if self.sectors[next_sector]["train"]:
                    difference = int(sector) - int(next_sector)
                    speed_set = self.__speed_selector(sector, difference)
                    break
            if not speed_set:
                self.__set_speed("full", sector)

    def move_train(self, sector):
        length = len(self.sectors)
        next_index = int(sector) + 1
        next_sector = str(self.overflow(next_index, length))

        self.__push_train(sector, next_sector)
        self.check_speed()
        self.save_sectors()

    def __push_train(self, current_sector, target_sector):
        self.sectors[target_sector]["train"] = self.sectors[current_sector]["train"]
        self.sectors[target_sector]["train_values"] = self.sectors[current_sector]["train_values"]
        self.sectors[current_sector]["train"] = ''
        self.sectors[current_sector]["train_values"] = {}

    def save_sectors(self):
        json_obj = json.dumps(self.sectors, indent=4)
        with open("./"+self.name+"Sectors.json", "w") as sectors_file:
            sectors_file.write(json_obj)


class PWM:
    def __init__(self, pwm_dict):
        print("placeholder")


if __name__ == "__main__":
    red = Line("red")
    red.check_speed()
    print(json.dumps(red.sectors, indent=4))
