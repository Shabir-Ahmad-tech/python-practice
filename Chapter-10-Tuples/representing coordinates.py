# Representing coordinates using tuples

coordinated = [(0, 0), (1, 2), (3, 4), (5, 6)]  # list of tuples representing coordinates

for coord in coordinated:  # loop through each coordinate

    print("Coordinate:", coord)  # print the coordinate tuple

    print("X:", coord[0], "Y:", coord[1])  # print x and y values separately
    
    print()  # print a newline for better readability