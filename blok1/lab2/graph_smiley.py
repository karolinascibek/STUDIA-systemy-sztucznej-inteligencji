import matplotlib.pyplot as plt
import numpy as np

class GraphSmiley():
    def __abs__(self):
        pass

    def display(self, a, b, r):
        theta = np.linspace(0, 2 * np.pi, 100)

        radius = r

        circleX = radius * np.cos(theta) + a
        circleY = radius * np.sin(theta) + b

        pointX = self.set_pointX(a, r)
        pointY = self.set_pointY(b, r)
        smileX = self.set_smailX(a, r)
        smileY = self.set_smailY(smileX, a, b, r)

        figure, axes = plt.subplots()

        axes.plot(circleX, circleY, "b-", label="lamane")

        axes.plot(pointX, pointY, "rs", label="punkty")
        axes.plot(smileX, smileY, "y-", label="sinus")

        margin = 1
        axes.set_ylim(b - r - margin, b + r + margin)
        axes.set_xlim(a - r - margin, a + r + margin)
        axes.set_aspect(1)
        axes.grid()
        plt.legend(loc="upper right")
        plt.title("Circle")
        plt.show()

    def set_pointX(self, a, r):
        return [a - r / 2, a + r / 2, a]

    def set_pointY(self, b, r):
        return [b + r / 2, b + r / 2, b]

    def set_smailX(self, a, r):
        return np.linspace(a - r / 2, a + r / 2, 50)

    def set_smailY(self, X, a, b, r):
        return 1/(r/2)*(X - a) ** 2 - r/2 + b
        # return np.sin(X-0.5*np.pi)