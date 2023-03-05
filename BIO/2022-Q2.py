
class hex():
    def __init__(self):
        self.sides = []
        for i in range(6):  #hexagon sides
            side = "_"
            self.sides.append(side)

class hive():
    def __init__(self):
        self.hexagons = []
        self.rows_list = []
        for row in range(5):
            hex_ = hex()
            self.hexagons.append(hex_)
            self.rows_list.append(self.hexagons)
    
    def __str__(self):
        output = ""
        for r in self.rows_list:
            for n in self.hexagons:
                value = n.sides
                for i in value:
                    output = output + " " + i
                output = output + "     "
            output = output + "\n"
        return output

class drone():
    def __init__(self, pos, direct, move, rotate):
        self.position_row = pos[0]
        self.position_hexagon = pos[1]
        self.direction = direct
        self.move_distance = int(move)
        self.rotation = rotate

    def __str__(self):
        outstring = str(self.position_row) + ", " + str(self.position_hexagon) + " dir " + str(self.direction)
        return outstring

    def move(self):
        
        self.position_row += self.move_distance // 5
        self.position_hexagon += self.move_distance % 5
        
        while self.position_hexagon > 4:

            self.position_hexagon -= 5
            self.position_row += 1
        
        while self.position_row > 4:
            self.position_row -= 5

        self.direction += self.rotation
        if self.direction > 5:
            self.direction = 0
        if self.direction < 0:
            self.direction = 5

#_________________________________________________________________________________________________________________________________

RED = input("RED MOVES between 1 and 25:")
BLUE = input("BLUE MOVES between 1 and 25:")

hive_ = hive()
print(hive_)

red_drone = drone([0, 0], 0, RED, 1)
red_drone.move()
print(red_drone)

blue_drone = drone([4, 4], 5, BLUE, -1)
blue_drone.move()
print(blue_drone)
