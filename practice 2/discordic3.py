"""
Ну понеслась, теерь накидываем модель
"""


import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.neighbors import KNeighborsRegressor
from matplotlib.colors import Normalize
import matplotlib as mpl
from sklearn.pipeline import Pipeline
from sklearn.datasets import make_blobs, make_moons
from sklearn.pipeline import Pipeline


def make_liner_regression(num_points, noise=0.1):
    x, _ = make_moons(num_points, noise=noise)
    weights = np.random.randn(3)
    y = x.dot(weights[:2]) + weights[-1]
    y = y + noise * np.random.randn(len(y))
    return x, y


def plot_data_regr2d_w_model(x, y, model, gap=0.1):
    x_lim = np.min(x), np.max(x)
    x_lim = x_lim[0] - (x_lim[1] - x_lim[0]) * gap, x_lim[1] + (x_lim[1] - x_lim[0]) * gap

    plt.figure(figsize=(7, 7))
    plt.xlim(*x_lim) # Задаем границы координаты осей координат
    plt.ylim(*x_lim)

    norm = Normalize(np.min(y), np.max(y))
    cm = mpl.colormaps["plasma"]

    xx, yy = np.meshgrid(np.linspace(x_lim[0], x_lim[1], 200),
                         np.linspace(x_lim[0], x_lim[1], 200))

    x_mesh = np.stack([xx.reshape(-1), yy.reshape(-1)], axis=1)
    y_mesh = model.predict(x_mesh)

    plt.pcolormesh(xx, yy, y_mesh.reshape(xx.shape), cmap=cm, shading='gouraud', norm=norm)
    plt.scatter(x[:, 0], x[:, 1], s=80, c=y, cmap=cm, linewidth=1, edgecolor="black", norm=norm)

    plt.grid()
    plt.tight_layout()


x, y = make_liner_regression(150, noise=0.09)
model = Pipeline([
    ("scaler", StandardScaler()),
    ("regr", LinearRegression())
])
model.fit(x, y)
plot_data_regr2d_w_model(x, y, model)
plt.show()

