import matplotlib.pyplot as plt
import numpy as np


class MatPlotScatterData:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


class MatPlotScatter:
    def __init__(self, data_obj) -> None:
        self.data = data_obj

    def collect_data(self):
        x = []
        y = []

        for item in self.data:
            x.append(item.x)
            y.append(item.y)
        return x, y

    def plot(self):
        x, y = self.collect_data()
        fig, ax = plt.subplots()

        ax.scatter(x, y, vmin=0, vmax=10)

        ax.set(ylim=(-1, 1))
        plt.show()
