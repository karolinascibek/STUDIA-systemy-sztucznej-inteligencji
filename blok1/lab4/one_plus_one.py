import numpy as np
import matplotlib.pyplot as plt


class OnePlusOne():

    def adaption_function(self, x):
        return np.sin(x/10)*np.sin(x/200)

    def one_plus_one(self, rozrzut=10, wsp_przyrostu=1.1, l_iteracji=20, zakres_zmiennosci=(0, 100)):
        x_min, x_max = zakres_zmiennosci
        X = np.arange(x_min, x_max, 0.1)
        x_idx = np.random.randint(x_min, len(X))
        x = X[x_idx]

        y = self.adaption_function(x)
        Y = self.adaption_function(X)

        for i in range(l_iteracji):

            # wykres
            txt = "i: "+str(i)+", r: "+str(rozrzut)
            plt.plot(X, Y)
            plt.annotate(txt, (x, y))
            plt.pause(0.3)
            plt.clf()


            r = np.random.randint(-rozrzut, rozrzut + 1)
            x_pot = x + r
            if x_pot > X[-1]:
                x_pot = X[-1]

            if x_pot < X[0]:
                x_pot = X[0]

            y_pot = self.adaption_function(x_pot)
            if y_pot >= y:
                y = y_pot
                x = x_pot
                rozrzut *= wsp_przyrostu
            else:
                rozrzut /= wsp_przyrostu








