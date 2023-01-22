
class hex():
    def __init__(self):
        self.sides = []
        for i in range(6):  #hexagon sides
            side = "_"
            self.sides.append(side)

class hive():
    def __init__(self):
        self.hexagons = []
        for i in range(27):  #number of hexagons
            hex_ = hex()
            self.hexagons.append(hex_)
    
    def __str__(self):
        output = ""
        for n in self.hexagons:
            value = n.sides
            for i in value:
                output = output + " " + i
            output = output + "\n"
        return output

class drone():
    def __init__(self, pos, direct):
        self.position = pos
        self.direction = direct

    def delete(self):
        print("Hello, my position is",self.position)
    
    def __str__(self):
        outstring = str(self.position) + ", " + str(self.direction)
        return outstring

hive_ = hive()
print(hive_)

red_drone = drone(0, 0)
print(red_drone)
blue_drone = drone(27, 5)
print(blue_drone)
blue_drone.delete()