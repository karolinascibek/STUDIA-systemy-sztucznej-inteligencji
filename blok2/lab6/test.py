# GreedyPoint
from blok2.lab6.greedy_point import GreedyPoint
test1 = [
    [0, 0, 0, 0],
    [0, 0, 1, 1],
    [0, 1, 1, 1],
    [0, 0, 0, 1],
    [0, 0, 0, 1],
]
test2 = [
    [1, 1, 1, 1],
    [0, 0, 0, 1],
    [1, 1, 1, 1],
    [0, 0, 1, 1],
    [1, 1, 1, 1],
]
test3 = [
    [1, 1, 1, 1],
    [0, 0, 0, 1],
    [0, 0, 1, 0],
    [1, 1, 0, 0],
    [1, 1, 1, 1],
]

bitmap1 = [
    [0, 0, 0, 1],
    [0, 0, 1, 1],
    [0, 1, 0, 1],
    [0, 0, 0, 1],
    [0, 0, 0, 1],
]
bitmap2 = [
    [0, 1, 1, 1],
    [1, 0, 0, 1],
    [0, 0, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 1, 1],
]
bitmap3 = [
    [1, 1, 1, 0],
    [0, 0, 0, 1],
    [1, 1, 1, 1],
    [0, 0, 0, 1],
    [1, 1, 1, 0],
]

bitmaps = [bitmap1, bitmap2, bitmap3]
#bitmaps_test = [test1, test2, test3]

gp = GreedyPoint(test2, bitmaps)
print("test: ", test2)
print("wzor1: ", bitmap1)
gp.alg()

