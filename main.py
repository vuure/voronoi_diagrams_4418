import random
import math
import numpy

def generatePointsAndSortRanges():
    points = []
    for number in range(1, 21):

        r = random.uniform(2.5,15)

        if number <= 5:
            angle = random.randint(5, 85)
        elif number <= 10:
            angle = random.randint(95, 175)
        elif number <= 15:
            angle = random.randint(195, 265)
        elif number <= 20:
            angle = random.randint(275, 355)

        XofPoint = r * math.cos(angle)
        YofPoint = r * math.sin(angle)

        distance = math.sqrt(XofPoint ** 2 + YofPoint ** 2)

        points.append([number, XofPoint,YofPoint,distance])

    points.sort(key=lambda x: x[3])

    return points

points_list = generatePointsAndSortRanges()
print(points_list)

closest_points = []

points_unitVectors = []

while len(points_list)>0:
    closestPoint = points_list[0]
    closestPointIndex = closestPoint[0]

    closestPointX, closestPointY = closestPoint[1],closestPoint[2]

    bottomOfCalc = (closestPointX**2) + (closestPointY**2)
    print(bottomOfCalc)

    unitVectorX = -closestPointX / math.sqrt(bottomOfCalc)
    unitVectorY = -closestPointY / math.sqrt(bottomOfCalc)

    unitVector = numpy.array([unitVectorX, unitVectorY])

    points_unitVectors.append(unitVector)
    closest_points.append(closestPoint)

    del points_list[0]

    for indexNumber,a in enumerate(points_list, start=0):

        tryingPoint = points_list[indexNumber]
        tryingPointX, tryingPointY = tryingPoint[1], tryingPoint[2]

        bottomOfCalcTrying = (-tryingPointX) ** 2 + (-closestPointY) ** 2

        unitVector1Trying = -tryingPointX / math.sqrt(bottomOfCalcTrying)
        unitVector2Trying = -tryingPointY / math.sqrt(bottomOfCalcTrying)

        unitVectorTrying = numpy.array([unitVector1Trying,unitVector2Trying])

        if (numpy.matmul(unitVector, unitVectorTrying) < 0):
            del points_list[indexNumber]
        else:
            pass

print(len(closest_points))
