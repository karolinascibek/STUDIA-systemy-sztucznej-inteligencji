
import math
import numpy as np
import matplotlib.pyplot as plt

class CMeans():
    def __init__(self, samples):
        self.samples = samples

    def metrics_euklidesowa(self, x1, x2, y1, y2):
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    def calcutate_the_value_U(self, D, m, M, fcm_m):
        U = np.zeros((m, M))
        U = U.T
        D = D.T
        for s in range(M):
            for j in range(m):
                U[s, j] = (D[s, j] ** (1 / (1 - fcm_m))) / (np.sum(D[s] ** (1 / (1 - fcm_m))))
        return U.T

    def calculate_center_group(self, U, m, n, M, fcm_m):
        V = np.zeros((m, n))
        for j in range(m):
            for i in range(n):
                UX = np.ones(M)
                for s in range(M):
                    UX[s] = (U[j, s] ** fcm_m) * self.samples[s, i]
                V[j, i] = np.sum(UX) / np.sum(U[j] ** fcm_m)
        return V

    def calculate_distans(self, m, M, V):
        D = np.random.rand(m, M)
        for j in range(m):
            for s in range(M):
                sample = self.samples[s]
                v = V[j]
                d = self.metrics_euklidesowa(sample[0], v[0], sample[1], v[1]) ** 2

                # 2.2
                if d < 1 ** (-10):
                    d = 1 ** (-10)
                D[j, s] = d
        return D

    def setColors(self, V):

        wsp = np.random.random()
        colors = np.random.rand(len(V), 4)
        rgba_groups = []

        rgba = colors

        for c in colors:
            group = []
            for s in self.samples:
                group.append(c)
            rgba_groups.append(np.array(group))

        return np.array(rgba_groups), np.array(rgba)




    def c_means(self, m, iterations=3, fcm_m=2):
        M = len(self.samples)
        n = len(self.samples[0])

        D = np.random.rand(m, M) # odleglosci każdej próbki dla każdej grupy

        #1.4 Wyliczenie każdej wartości w tablicy Uj, s(j=1..m; s = 1..M).
        U = self.calcutate_the_value_U(D, m, M, fcm_m)

        # 1.5 Obliczenie środków grup Vj,i (j=1..m; i=1..n; m to liczba grup, n to liczba atrybutów)
        V = self.calculate_center_group(U, m, n, M, fcm_m)

        # 2. Główna pętla programu wykonywana przez zadaną liczbę iteracji.

        # set colors to  graph
        rgba_groups, rgba = self.setColors(V)

        x = self.samples[:, 0]
        y = self.samples[:, 1]

        for t in range(iterations):
            # wykres
            # ustawienie kolorów dla grup
            UT = U.T
            for i in range(m):
                # print(np.size(rgb))
                rgba_groups[i, :, 3] = UT[:, i]

            for iv, sv in enumerate(V):
                plt.scatter(x, y, color=rgba_groups[iv], s=50, linewidths=1)

            xV = V[:, 0]
            yV = V[:, 1]

            plt.scatter(xV, yV, color=rgba, marker="+", alpha=1)

            plt.title("FCM , i:" + str(t))
            plt.xlabel("x")
            plt.ylabel("y")
            plt.pause(1)
            plt.clf()

            # 2.1. Obliczenie odległości między każdą próbką a grupą: Dj,s
            D = self.calculate_distans(m, M, V)

            # 2.3 Wyliczenie każdej wartości w tablicy Uj, s(j=1..m; s = 1..M).
            U = self.calcutate_the_value_U(D, m, M, fcm_m)

            #? 2.4. Należy sprawdzić, czy przypadkiem U nie zawiera wartości nieoznaczonych (w takim przypadku należy przerwać program i wyświetlić komunikat ostrzegawczy)

            # 2.5 Obliczenie środków grup Vj,i (j=1..m; i=1..n; m to liczba grup, n to liczba atrybutów)
            V = self.calculate_center_group(U, m, n, M, fcm_m)



