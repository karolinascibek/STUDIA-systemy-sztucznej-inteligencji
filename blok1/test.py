from matplotlib import pyplot as plt
import random
from blok1.lab1.decision_system import DecisionSystem

def chooseNumbers(count, grid):
    numbers = []
    while len(numbers) != count:
        r = random.randint(0, len(grid))
        if r not in numbers:
            numbers.append(r)
    return sorted(numbers)


def getCenters(count, grid):
    numbers = chooseNumbers(count, grid)
    centers = []
    for i in range(len(numbers)):
        for row in grid:
            if grid.index(row) == numbers[i]:
                centers.append(row)
    return centers


def createXlist(n):
    X = []
    for i in range(n):
        X.append([])
    return X


def meanXY(grid, grid2, n, fcm_m):  # to jest źle x2
    x = 0
    y = 0
    suma = 0
    for row in grid:
        if grid.index(row) == n:
            for i in range(len(row)):
                for s in range(len(grid2)):
                    suma += row[i] ** fcm_m
                    x += (row[i] ** fcm_m) * grid2[s][0]
                    y += (row[i] ** fcm_m) * grid2[s][1]
            break
    x = x / suma
    y = y / suma
    return x, y


def sumRow(grid):
    result = []
    grid = [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0]))]
    for row in grid:
        suma = 0
        for i in range(len(row)):
            suma += row[i]
        result.append(round(suma, 1))
    return result


def mixColors(grid, sample):
    R = 1
    G = 1
    B = 1
    table = [R, G, B]
    grid = [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0]))]
    for row in grid:
        if grid.index(row) == sample:
            for x in range(len(row)):
                table[x] = table[x] * row[x]
    color = (table[0], table[1], table[2])
    return color


def sumRowandOperate(grid, n, fcm_m):
    suma = 0
    for row in grid:
        if grid.index(row) == n:
            for x in range(len(row)):
                if row[x] == 0:
                    suma += 0
                else:
                    suma += row[x] ** (1 / 1 - fcm_m)
    return suma


def centersXY(centers):
    X = []
    Y = []
    for x in range(len(centers)):
        X.append(centers[x][0])
        Y.append(centers[x][1])
    return X, Y


def euclideanDistance(Xsource, Ysource, Xdestination, Ydestination):
    d = ((Xdestination - Xsource) ** 2 + (Ydestination - Ysource) ** 2) ** 0.5
    if d < 1e-10:
        d = 1e-10
    return d


def FCM(grid, m, iterations, fcm_m=2):
    plt.figure(1)
    plt.show(block=False)
    plt.axis([-2, 2, -2, 2])
    U = createXlist(m)
    V = getCenters(m, grid)
    print(V)
    Colors = ['r', 'g', 'b']
    D = createXlist(m)
    D.clear()
    X, Y = centersXY(grid)
    plt.plot(X, Y, '.')
    for j in range(m):
        D.append([])
    for s in range(len(grid)):
        for centeri in range(m):
            D[centeri].append(euclideanDistance(grid[s][0], grid[s][1], V[centeri][0], V[centeri][1]))
    for s in range(len(grid)):
        for centeri in range(m):
            if D[centeri][s] == 0:
                U[centeri].append(0.0)
            else:
                U[centeri].append(((D[centeri][s]) ** (1 / 1 - fcm_m)) / (sumRowandOperate(D, centeri, fcm_m)))
    probki.wys(U)
    for centeri in range(m):
        V[centeri] = meanXY(U, V, centeri, fcm_m)
        X = V[centeri][0]
        Y = V[centeri][1]
        plt.plot(X, Y, 'o', c=Colors[centeri])
    for row in grid:
        color = mixColors(U, grid.index(row))
        plt.plot(row[0], row[1], '.', c=color)
    plt.pause(5)
    for i in range(iterations):
        plt.clf()
        D.clear()
        U.clear()
        for j in range(m):
            D.append([])
            U.append([])
        for s in range(len(grid)):
            for centeri in range(m):
                D[centeri].append(euclideanDistance(grid[s][0], grid[s][1], V[centeri][0], V[centeri][1]))
        for s in range(len(grid)):
            for centeri in range(m):
                if D[centeri][s] == 0:
                    U[centeri].append(0.0)
                else:
                    U[centeri].append(((D[centeri][s]) ** (1 / 1 - fcm_m)) / (sumRowandOperate(D, centeri, fcm_m)))
        for centeri in range(m):
            V[centeri] = meanXY(U, V, centeri, fcm_m)
            X = V[centeri][0]
            Y = V[centeri][1]
            plt.plot(X, Y, 'o', c=Colors[centeri])
        for row in grid:
            color = mixColors(U, grid.index(row))
            plt.plot(row[0], row[1], '.', c=color)
        plt.title(i)
        plt.pause(1)
    plt.show()

system.load_samples("lab3/spirala.txt", "   ")
system.load_headers("lab3/spirala-type.txt", ',')

s = probki.SystemProbek("../Dane/3/spirala.txt", "../Dane/3/spirala-type.txt")
grid, grid2 = s.SplitData()

FCM(grid, 3, 100, 2)