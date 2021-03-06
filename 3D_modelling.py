from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

class Model:
    def __init__(self, fig):
        self.fig = fig

    def calculating(self):
        theta = np.linspace(0, 2*np.pi, 100)
        r = np.linspace(0, 2, 100)
        t,R =np.meshgrid(theta, r)

        X = 2.5*R*np.cos(t) + 5
        Y = 2.5*R*np.sin(t) + 5
        Z = ((R)**2) *1.15

        return [X,Y,Z]

    def plotting(self, fig):
        axesList = self.calculating()
        ax = self.fig.add_subplot(111, projection='3d')
        ax.set_xlabel('Muye Cup')
        ax.set_ylabel('Length/10.5cm')
        ax.set_zlabel('Height/4.7cm')
        ax.set_xlim(-1,11)
        ax.set_ylim(-1,11)
        ax.set_zlim(0,11)

        ax.plot_surface(axesList[0], axesList[1], axesList[2], alpha=0.95, cmap=cm.copper)
        plt.show()

if __name__ == '__main__':
    fig = plt.figure(figsize=(5,5))
    my3D = Model(fig)
    my3D.plotting(fig)
