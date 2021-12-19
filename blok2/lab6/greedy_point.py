import math


class GreedyPoint():
    def __init__(self, test, bitmap):
        self.bitmap_test = test
        self.bitmaps = bitmap
        self.size = (len(bitmap), len(bitmap[0]))

    def display(self):
        print(self.bitmap)

    def metrics_euklidesowa(self, x1, x2, y1, y2):
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    def cut_column(self, array, idx):
        result = []
        for row in array:
            result.append(row[idx])
        return result

    def calculate_min_distant(self, x1, x2, y1, y2, min_distant):
        distant = self.metrics_euklidesowa(x1, x2, y1, y2)
        # print("r - A(%i, %i) dla B(%i, %i) = %i "%(i, j, i, y, distant ))
        return min(min_distant, distant)

    def check_vector(self, vector, x, y,  distant, pos="r"):
        min_distant = distant
        for v, elB in enumerate(vector):
            if elB == 1:
                # distant = self.metrics_euklidesowa(i, i, j, y)
                # #print("r - A(%i, %i) dla B(%i, %i) = %i "%(i, j, i, y, distant ))
                # min_distant = min(min_distant, distant)
                if pos == "r":
                    min_distant = self.calculate_min_distant(x, x, y, v, min_distant)
                if pos == "c":
                    min_distant = self.calculate_min_distant(x, v, y, y, min_distant)
                if min_distant == 0:
                    break
        return min_distant

    def measure_of_improbability(self, bitmap_A, bitmap_B):
        measure = 0
        for i, rowA in enumerate(bitmap_A):
            for j, elA in enumerate(rowA):
                min_distant = len(bitmap_A) * len(rowA)
                if elA == 1:
                    min_distant = self.check_vector(bitmap_B[i], i, j, min_distant, pos="r")
                    column = self.cut_column(bitmap_B, j)
                    min_distant = self.check_vector(column, i, j, min_distant, pos="c")
                    measure += min_distant
        return measure

    def measure_of_improbability2(self, bitmap_A, bitmap_B):
        measure = 0
        for i, rowA in enumerate(bitmap_A):
            for j, elA in enumerate(rowA):
                min_distant = len(bitmap_A) * len(rowA)
                if elA == 1:
                    min_distant = self.check_vector(bitmap_B[i], i, j, min_distant, pos="r")
                    column = self.cut_column(bitmap_B, j)
                    min_distant = self.check_vector(column, i, j, min_distant, pos="c")
                    measure += min_distant
        return measure

    def alg(self):
        min_measure = - max(self.size[0], self.size[1])**3
        idx = 0
        for i, bitmap in enumerate(self.bitmaps):
            measure1 = self.measure_of_improbability(bitmap, self.bitmap_test)
            measure2 = self.measure_of_improbability(self.bitmap_test, bitmap)
            #print("measure 1:  ", measure1)
            #print("measure 2:  ", measure2)
            measure = - measure1 - measure2
            if min_measure < measure:
                min_measure = measure
                idx = i
        #print("miara =  %i, idx bitmapy najnbardziej podobnej = %i"%(min_measure, idx))
        return min_measure, idx



