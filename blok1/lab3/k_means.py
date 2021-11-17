import random
import math
import numpy as np
import matplotlib.pyplot as plt


class KMeans():
    def __init__(self, samples):
        self.samples = samples
        self.iteracja = 0

    def metrics_euklidesowa(self, x1, x2, y1, y2):
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    def alg(self, centers):
        centers_group = centers
        groups = []
        for cg in centers_group:
            groups.append([])

        # pętla po wszytkich M probkach, s to indexs aktualnej probki
        for s in self.samples:
            first_center = centers_group[0]
            idx_group = 0

            # wylicz dleglosc miedzy probka s a każdym środkiem grupy V
            distant = self.metrics_euklidesowa(s[0], first_center[0], s[1], first_center[1])
            for idx_c, center in enumerate(centers_group[1: len(centers_group)]):
                temp = self.metrics_euklidesowa(s[0], center[0], s[1], center[1])

                #  Wyznacz us równy indeksowi najbliższego środka grupy dla s-tej próbki
                if distant > temp:
                    distant = temp
                    idx_group = idx_c + 1

            # posortowanie próbek względem grup
            groups[idx_group].append(s)

        # ustalamy nowe środki
        centers_group = []
        for group in groups:
            if group:
                group = np.array(group)
                x = group[:, 0]
                y = group[:, 1]
                new_center_x = np.average(x)
                new_center_y = np.average(y)
                centers_group.append(np.array([new_center_x, new_center_y]))
            else:
                print("pusta grupa")

        # print("nowe środki: ", np.array(centers_group))
        return centers_group, groups

    def k_means(self, m=4, iterations=1):

        centers_group = []
        # wybierz losowo m różnych próbek
        for n in range(m):
            sample_index = random.randint(0, len(self.samples) - 1)
            sample = self.samples[sample_index]
            centers_group.append(sample)

        # wykonaj algorytm dla n-liczby iteracji
        groups = []

        for i in range(iterations):

            centers, groups = self.alg(centers_group)
            # if i == 0:
            #     self.graph(groups, centers_group)
            self.graph(groups, centers_group)
            centers_group = centers
            self.iteracja += 1

        return groups, centers_group

    def graph(self, groups, centers):
        # wykres
        for i, group in enumerate(groups):
            if group:
                group = np.array(group)
                x = group[:, 0]
                y = group[:, 1]

                center = centers[i]
                xc = center[0]
                yc = center[1]

                # x = np.append(x, xc)
                # y = np.append(y, yc)

                plt.plot(x, y, ".", label=str(i+1))
                plt.plot(xc, yc, "m+")

        # for center in centers:
        #     x = center[0]
        #     y = center[1]
        #     plt.plot(x, y, "m+")
        plt.legend()
        plt.title("K-średnich iteracja: {0}".format(self.iteracja))
        plt.xlabel("x")
        plt.ylabel("y")
        plt.pause(1)
        plt.clf()



