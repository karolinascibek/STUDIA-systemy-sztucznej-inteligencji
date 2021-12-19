import numpy as np

class HopfieldNetwork():
    def __init__(self, bitmaps_pattern, bitmap_test):
        self.size = np.shape(bitmap_test)
        self.bitmaps_pattern = self.init_matrix(bitmaps_pattern)
        #print("bitmap pattern")
        #print(self.bitmaps_pattern)
        self.bitmap_test = self.init_matrix([bitmap_test])
        self.matrix_weights = self.initiate_matrix_weight()
        #print("bitmap test")
        #print(self.bitmap_test)

    def display(self):
        print("pattern: ")
        print(self.bitmaps_pattern)
        print("test: ")
        print(self.bitmap_test)
        self.teach_list_pictures()
        test = self.recognize_the_picture()

    def convert_bitmap_to_vector(self, bitmap):
        for i, el in enumerate(bitmap):
            if el == 0:
                bitmap[i] = -1
        return bitmap

    def convert_vector_to_bitmap(self, vector):
        for i, el in enumerate(vector):
            if el == -1:
                vector[i] = 0
        return vector

    def init_matrix(self, matrix):
        for i, m in enumerate(matrix):
            bitmap_as_vector = self.matrix_to_vector(m)
            matrix[i] = self.convert_bitmap_to_vector(bitmap_as_vector)
        return matrix

    def matrix_to_vector(self, matrix):
        return np.array(matrix).flatten()

    def initiate_matrix_weight(self):
        n, m = np.shape(self.bitmap_test)
        n = n*m
        return np.zeros((n, n))

    # -------- uczenie sieci wzorów ----------
    def teach_picture(self, bitmap):
        for i in range(len(bitmap)):
            for j in range(i, len(bitmap)):
                if i != j:
                    weight = (1/len(bitmap))*bitmap[i]*bitmap[j]
                    self.matrix_weights[i, j] += weight
                    self.matrix_weights[j, i] += weight


    def teach_list_pictures(self):
        for i in range(1):
            for bitmap in self.bitmaps_pattern:
                self.teach_picture(bitmap)
            #print("wagi")
            #print(self.matrix_weights)

    # ------------ rozpoznawanie obrazu --------
    def recognize_the_picture(self):
        test = self.bitmap_test[0]
        n = len(test)
        #print("testowy: ")
        #print(test)
        result = []
        for i in range(n):
            output = test*self.matrix_weights[i]
            output = sum(output)*1/n
            #print(output)
            if output >= 0:
                output = 1
            else:
                output = -1
            result.append(output)
        #print("rozpoznany: ")
        #print(result)
        r = np.array(result)
        result = self.convert_vector_to_bitmap(r)

        return np.reshape(result, self.size)





