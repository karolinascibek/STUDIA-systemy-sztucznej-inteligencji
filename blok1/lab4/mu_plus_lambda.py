import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


class MuPlusLambda():

    def adaption_function(self, x1, x2):
        p1 = 0.05
        p2 = 0.15
        return np.sin(x1*p1) + np.sin(x2*p1) + 0.4*np.sin(x1*p2)*np.sin(x2*p2)

    def ratings_chaps(self, population):
        grade_population = np.ones(len(population))
        for (j, p) in enumerate(population):
            grade_population[j] = self.adaption_function(p[0], p[1])
        return grade_population

    def tournament(self, parents, m, size_tournament):
        oss_turniej = np.zeros((size_tournament, 2))
        oss_turniej_f = np.zeros((size_tournament, 1))
        for tura in range(size_tournament):
            idx_parent = np.random.randint(m)
            player = parents[idx_parent]
            player_f = self.adaption_function(player[0], player[1])
            oss_turniej[tura] = player
            oss_turniej_f[tura] = player_f
        return oss_turniej_f, oss_turniej

    def generate_next_generation(self, parents, l, m, size_tournament, mutation_level):
        next_generation = np.zeros((l, 2))

        for t in range(l):
            oss_turniej_f, oss_turniej = self.tournament(parents, m, size_tournament)

            # najlepszy osobnik z puli potomków
            os_n = oss_turniej[np.argmax(oss_turniej_f)]

            # mutacja
            a = np.random.randint(-mutation_level, mutation_level)
            b = np.random.randint(-mutation_level, mutation_level)
            mutation = np.array([a, b])

            next_generation[t] = os_n + mutation
        return next_generation


    def generate_new_parents(self, p_plus_g, grade_p_plus_g, m ):
        parents = np.zeros((m, 2))
        for idx_np in range(m):
            idx = np.argmax(grade_p_plus_g)
            #print("idx: ", idx)
            parents[idx_np] = p_plus_g[idx]
            # print("wybrany rodzic: ", parents[idx_np] )
            grade_p_plus_g = np.delete(grade_p_plus_g, idx)
            p_plus_g = np.delete(p_plus_g, idx, 0)
            # print("ll: ", p_plus_g.shape)
        return parents


    def mu_plus_lambda(self, m=4, l=10, mutation_level=100/10, iterations=20, zakres_zmiennosci=(0, 100), size_tournament=2):
        x_min, x_max = zakres_zmiennosci
        X = np.arange(x_min, x_max+1)
        Y = np.arange(x_min, x_max+1)

        X, Y = np.meshgrid(X, Y)
        Z = self.adaption_function(X, Y)

        atr = 2
        os_n = None

        # losuj pule osobników rodzicielskich
        parents = np.random.rand(m, 2) * x_max

        # wykres funkcji 3d
        # fig, ax = plt.subplots()
        # ax = plt.axes(projection='3d')
        # surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)
        # plt.pause(3)
        fig, ax = plt.subplots()
        # pętla głowna
        for i in range(iterations):


            # ocena funkcją przystosowania rodziców
            grade_parents = self.ratings_chaps(parents)
            #print("FPP: ", grade_parents)

            # pula osobników potomnych
            next_generation = self.generate_next_generation(parents, l, m, size_tournament, mutation_level)
            #print("NG: ",next_generation)

            # ocena funkcją przystosowania puli lambda potomkow
            grade_next_generation = self.ratings_chaps(next_generation)

            # połaczenie puli potomków z pólą rodziców
            p_plus_g = np.concatenate([parents, next_generation])
            grade_p_plus_g = np.concatenate([grade_parents, grade_next_generation])

            # wykres
            cnt = ax.contour(Z, vmin=abs(Z).min(), vmax=abs(Z).max(), extend=[x_min, x_min, x_min, x_max])
            points = ax.plot(parents[:, 0], parents[:, 1], "xb", linewidth=3, label="populacja rodzicielska")
            points = ax.plot(next_generation[:, 0], next_generation[:, 1], ".r", label="populacja potomna ")
            plt.legend(loc="upper right")
            plt.axis([x_min, x_max, x_min, x_max])


            # ustalamy 'm' najlepszych osobników i tworzymy z nich pule rodzicielsko
            parents = self.generate_new_parents(p_plus_g, grade_p_plus_g, m )

            # najlepszy osobnik z nowej puli rodzicielskiej
            os_n = parents[0]

            # cd. wykresu
            plt.title("Algorytm μ+λ")
            plt.xlabel("x1")
            plt.ylabel("x2")
            plt.pause(1)
            ax.clear()

        return os_n






