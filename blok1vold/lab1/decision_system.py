import numpy as np
from tabulate import tabulate
import matplotlib.pyplot as plt
from blok1.lab2.graph_smiley import GraphSmiley



class DecisionSystem():
    def __init__(self):
        self.__samples = []
        self.__headers = []
        self.__types = []
        self.__class_type = []

    def __load_data(self, path, separator, type="str"):
        try:
            file = open(path, "r")
            lines = file.readlines()
            data = []
            for line in lines:
                line = line.strip()
                if line != "":
                    line = line.split(separator)
                    if type == 'num':
                        line = np.array(line, dtype='f')
                    data.append(line)
            return np.array(data)
        except:
            raise ValueError(" -- Nieparwidłowa ścieżka do pliku")

    def load_samples(self, path, separator):
        self.__samples = self.__load_data(path, separator, type='num')


    def load_headers(self, path, separator):
        self.__headers = self.__load_data(path, separator)
        self.__class_type = self.get_class_atrs_from_headers()

    # zadnie 2 lab 2
    def view_the_graph_smial(self, a, b, r):
        graph = GraphSmiley()
        graph.display(a, b, r)

    # lab2 zadanie 4
    def draw_chart(self, class_type):
        samples = self.filter_samples_by_class(str(class_type))

        fig, ax = plt.subplots(2, 2)
        fig.suptitle("Próbki dla klasy " + str(self.get_name_filter_class(class_type)))

        data = self.sort_by_column(samples, 2)

        ax[0, 0].plot(data[:, 2], data[:, 3], "ro")
        ax[0, 0].plot(data[:, 3], data[:, 3], "yo")
        ax[0, 0].plot(data[:, 4], data[:, 3], "bo")
        ax[0, 0].set_xlabel('atrybut 3')
        ax[0, 0].set_ylabel('atrybut 4')

        data = self.sort_by_column(samples, 1)

        ax[0, 1].plot(data[:, 1], data[:, 3], "bs")
        ax[0, 1].set_xlabel('atrybut 2')
        ax[0, 1].set_ylabel('atrybut 4')

        data = self.sort_by_column(samples, 0)

        ax[1, 0].plot(data[:, 0], data[:, 3], "g*")
        ax[1, 0].set_xlabel('atrybut 1')
        ax[1, 0].set_ylabel('atrybut 4')

        data = self.sort_by_column(samples, 1)

        ax[1, 1].plot(data[:, 1], data[:, 2], "m+")
        ax[1, 1].set_xlabel('atrybut 2')
        ax[1, 1].set_ylabel('atrybut 3')

        plt.show()

    def show(self, ):

        fig, ax = plt.subplots(2, 2)
        fig.suptitle("Wykresy dla danych Iris ")

        col = ["r.", "b*", "g+"]

        # indeksy atrybutów potrzebnych do wykresow
        X = [2, 1, 0, 1]
        Y = [3, 3, 3, 2]
        chart = 0
        for i in range(2):
            for j in range(2):
                for index_class, value in enumerate(self.__class_type):
                    samples = self.filter_samples_by_class(int(value[0]))
                    # samples = self.sort_by_column(samples, X[chart])
                    ax[i, j].plot(samples[:, X[chart]], samples[:, Y[chart]], col[index_class], label=value[1])


                ax[i, j].set_xlabel('atrybut '+str(X[chart]+1))
                ax[i, j].set_ylabel('atrybut '+str(Y[chart]+1))
                ax[i, j].legend(loc="upper right")
                chart = chart + 1
        plt.show()

    def sort_by_column(self, array, index):
        return array[array[:, index].argsort()]

    def get_name_filter_class(self, filter):
        for type in self.__class_type:
            if type[0] == str(filter):
                return type[1]
        return None

    def get_class_atrs_from_headers(self):
        last_index = len(self.__headers) - 1
        atrs = self.__headers[last_index][0]
        array_atrs = atrs[6:len(atrs) - 1].split(",")
        class_to_filter = []
        for el in array_atrs:
            class_to_filter.append(el.split("="))

        # self.__class_type = class_to_filter
        return class_to_filter

    def filter_samples_by_class(self, filter):
        class_one = np.isin(self.__samples[:, 4], filter)
        return self.__samples[class_one, :]

    def display(self):
        print(tabulate(self.__samples.tolist(), self.__headers[:, 0].tolist()))

    def display_headers(self):
        print(tabulate(self.__headers.tolist()))

    def display_samples(self):
        print(tabulate(self.__samples.tolist()))

    def name_atr(self, nr):
        return self.__headers[nr][0]

    def if_atr_symb(self, nr):
        if self.__headers[nr][1] == "s":
            return True
        return False

    def get_samples(self):
        return self.__samples

    def get_headers(self):
        return self.__headers



