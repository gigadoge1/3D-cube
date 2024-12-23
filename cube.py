import math

#creating the grid
cartesian = []
zcartesian = []
square = []
for _ in range(101):
    cartesian.append([" "] * 101)
    zcartesian.append([" "] * 101)

#code to display the output
def display():
    for x in cartesian:
        print(' '.join(x))

#making a cube
for z in range(0, 31):
    for y in range(35, 66):
        for x in range(35, 66):
            try:
                if int(cartesian[y][x]) < -z:
                    cartesian[y][x] = str(-z)
            except:
                cartesian[y][x] = str(-z)
            char = ""
            if z == 0 or z == 30:
                if x == 35 or x == 65:
                    char = "$"
                elif y == 35 or y == 65:
                    char = "$"
                else:
                    char = "."
            elif y == 35 or y == 65:
                if x == 35 or x == 65:
                    char = "$"
                else:
                    char = "."
            else:
                char = "."
            square.append([50-x, 50-y, -z, char])

def clear():
    for x in range(101):
        for y in range(101):
            cartesian[x][y] = " "
clear()
def clearz():
    for x in range(101):
        for y in range(101):
            zcartesian[x][y] = " "
clearz()

for r in range(200):
    for x in range(len(square)):
        xcoord = square[x][0]
        ycoord = square[x][1]
        zcoord = square[x][2]
        char = square[x][3]
        sinx = math.sin(math.radians(2.8125))
        cosx = math.cos(math.radians(2.8125))
        newx = xcoord*cosx - zcoord*sinx
        newy = ycoord
        newz = xcoord*sinx + zcoord*cosx
        if (100-newz) != 0:
            apparenty = (newy*(100))/(100-newz)
        else:
            apparenty = newy
        square[x][0] = newx
        square[x][1] = newy
        square[x][2] = newz
        try:
            if float(zcartesian[50-round(apparenty)][50-round(newx)]) < newz:
                zcartesian[50-round(apparenty)][50-round(newx)] = str(newz)
                cartesian[50-round(apparenty)][50-round(newx)] = char
        except:
            zcartesian[50-round(apparenty)][50-round(newx)] = str(newz)
            cartesian[50-round(apparenty)][50-round(newx)] = char
    display()
    clear()
    clearz()
