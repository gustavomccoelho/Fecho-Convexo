import numpy as np
import math
import matplotlib.pyplot as plt
import random
import time

class gift_wrapping:

    def __init__(self, data, data_name=""):
        self.data = np.array(data)
        self.data_name = data_name

    # Returns the point with lowest y coordinate and highest x coordinate
    def find_lowest_right(self):
        lower_y = float("inf")
        for point in self.data:
            if point[1] < lower_y:
                lower_y = point[1]
                lower = point
        return list(lower)

    # Returns the target point with the lowest angle from the line c-b
    def lowest_angle(self, b, c):
        low_angle = float("inf")
        for a in self.data:
            if a[0] != b[0] or a[1] != b[1]:
                if a[0] != c[0] or a[1] != c[1]:
                    u = [c[0] - b[0], c[1] - b[1]]
                    v = [a[0] - b[0], a[1] - b[1]]
                    mag_u = math.sqrt((u[0]) ** 2 + (u[1]) ** 2)
                    mag_v = math.sqrt((v[0]) ** 2 + (v[1]) ** 2)
                    u = [u[0] / mag_u, u[1] / mag_u]
                    v = [v[0] / mag_v, v[1] / mag_v]
                    angle = math.acos(u[0] * v[0] + u[1] * v[1])
                    orient = b[0] * c[1] + b[1] * a[0] + c[0] * a[1] - a[0] * c[1] - a[1] * b[0] - c[0] * b[1]
                    if orient < 0:
                        angle = 2 * math.pi - angle
                    if angle < low_angle:
                        low_angle = angle
                        low_point = a
        return list(low_point)

    # Main function for the convex hull algorithm
    def convex_hull(self):
        a = self.find_lowest_right()
        b = self.lowest_angle(a, [1, a[1]])
        init = a
        hull = [a]
        while b[0] != init[0] or b[1] != init[1]:
            hull.append(b)
            a = b
            b = self.lowest_angle(a, hull[-2])
        return hull

    # Ploting the algorithm results
    def plot_hull(self):
        fig, ax = plt.subplots()
        ax.set_title(self.data_name)
        ax.scatter(self.data[:, 0], self.data[:, 1])
        hull = self.convex_hull()
        for i in range(len(hull)):
            if i != len(hull) - 1:
                plt.plot([hull[i][0], hull[i + 1][0]], [hull[i][1], hull[i + 1][1]], color="red")
            else:
                plt.plot([hull[i][0], hull[0][0]], [hull[i][1], hull[0][1]], color="red")
        plt.show()

    # Returns the points indexes related to each hull element
    def get_indexes(self):
        indexes = []
        for element in self.convex_hull():
            j = 0
            while element[0] != self.data[j][0] or element[1] != self.data[j][1]:
                j += 1
            indexes.append(j)
        return(indexes)

if __name__ == '__main__':

    data1 = gift_wrapping(np.loadtxt("nuvem1.txt"), "Nuvem_1")
    data2 = gift_wrapping(np.loadtxt("nuvem2.txt"), "Nuvem_2")

    data1.plot_hull()
    with open('fecho1.txt', 'w') as f:
        for item in data1.get_indexes():
            f.write("%s\n" % item)
    data2.plot_hull()
    with open('fecho2.txt', 'w') as f:
        for item in data2.get_indexes():
            f.write("%s\n" % item)

    N = 1000
    x = np.random.standard_normal(N)
    y = np.random.standard_normal(N)
    P = []
    for i in range(N):
        P.append([x[i], y[i]])
    P = gift_wrapping(P)
    P.plot_hull()

    # Ploting Runtime

    sizes = [50, 100, 500, 1000, 2000, 5000, 10000]
    run_time = []
    h = []

    for N in sizes:
        x = np.random.standard_normal(N)
        y = np.random.standard_normal(N)
        P = []
        for i in range(N):
            P.append([x[i], y[i]])
        P = gift_wrapping(P)
        start = time.time()
        P.convex_hull()
        end = time.time()
        run_time.append(end - start)
        h.append(len(P.convex_hull()))

    for i in range(len(h)):
        h[i] = h[i] * sizes[i]

    plt.plot(sizes, run_time, "r")
    plt.plot(sizes, [x / 150000 for x in h], "b")
    plt.xlabel('Input size')
    plt.ylabel('time (s)')
    plt.legend(["Gift_Wrapping", "n*h"])
    plt.grid(True)
    plt.show()