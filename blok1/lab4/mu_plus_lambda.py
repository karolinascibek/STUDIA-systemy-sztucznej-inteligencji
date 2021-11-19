import numpy as np
import matplotlib.pyplot as plt


class MuPlusLambda():

    def adaption_function(self, x1, x2):
        p1 = 0.05
        p2 = 0.15
        return np.sin(x1*p1) + np.sin(x2*p1)*0.4*np.sin(x1*p2)*np.sin(x2*p2)

    def mu_plus_lambda(self, m, l,  l_iteracji=20, zakres_zmiennosci=(0, 100)):
        x_min, x_max = zakres_zmiennosci

        parents = np.random.rand(m, 2)*(x_min+(x_max-x_min))
        osobnik = np.zeros(len(parents))

        for i in range(l_iteracji):
            # Oceń każdy osobnik z puli rodzicielskiej za pomocą funkcji przystosowania


            osobnik_potomny = np.zeros(l)
            for (i, p) in enumerate(parents):
                osobnik[i] = self.adaption_function(p[0], p[1])


        print(parents)
        print(osobnik)






