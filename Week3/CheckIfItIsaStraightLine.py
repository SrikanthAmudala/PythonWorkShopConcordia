"""
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.
"""

def checkStraightLine(coordinates):
    point1 = coordinates[0]
    point2 = coordinates[1]
    
    if point2[0] - point1[0] == 0:
        for (x, y) in coordinates[2:]:
            if x!=point1[0]:
                return False
        else:
            return True

    m = (point2[-1] - point1[-1])/(point2[0] - point1[0])

    for (x, y) in coordinates[2:]:
        if m * (x - point1[0]) - (y - point1[-1])==0:
            pass
        else:
            return False
    return True

coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
# coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
print(checkStraightLine(coordinates))