from data import *
# from .data import *
import math

class LeastSquaresMethod(object):
    @classmethod
    def determinant_x(cls):
        quadratic_sum = sum(
            sample["x"][i] for i in range(n)
        )**2

        sum_of_squares = sum(
            sample["x"][i]**2 for i in range(n)
        )

        return n*sum_of_squares - quadratic_sum

    @classmethod
    def determinant_y(cls):
        quadratic_sum = sum(
            sample["y"][i] for i in range(n)
        )**2

        sum_of_squares = sum(
            sample["y"][i]**2 for i in range(n)
        )

        return n*sum_of_squares - quadratic_sum

    @classmethod
    def d_alpha_x(cls):
        a = sum(
            sample["x"][i]**2 for i in range(n)
        )

        b = sum(
            sample["y"][i] for i in range(n)
        )

        c = sum(
            sample["x"][i] for i in range(n)
        )

        d = sum(
            sample["x"][i]*sample["y"][i] for i in range(n)
        )

        return a*b - c*d

    @classmethod
    def d_alpha_y(cls):
        a = sum(
            sample["y"][i]**2 for i in range(n)
        )

        b = sum(
            sample["x"][i] for i in range(n)
        )

        c = sum(
            sample["y"][i] for i in range(n)
        )

        d = sum(
            sample["x"][i]*sample["y"][i] for i in range(n)
        )

        return a*b - c*d

    @classmethod
    def d_beta_x(cls):
        a = sum(
            sample["x"][i]*sample["y"][i] for i in range(n)
        )

        b = sum(
            sample["x"][i] for i in range(n)
        )

        c = sum(
            sample["y"][i] for i in range(n)
        )

        return n*a - b*c

    @classmethod
    def d_beta_y(cls):
        a = sum(
            sample["y"][i]*sample["x"][i] for i in range(n)
        )

        b = sum(
            sample["y"][i] for i in range(n)
        )

        c = sum(
            sample["x"][i] for i in range(n)
        )

        return n*a - b*c

    @classmethod
    def alpha_x(cls):
        return cls.d_alpha_x()/cls.determinant_x()

    @classmethod
    def beta_x(cls):
        return cls.d_beta_x()/cls.determinant_x()

    @classmethod
    def alpha_y(cls):
        return cls.d_alpha_y()/cls.determinant_y()

    @classmethod
    def beta_y(cls):
        return cls.d_beta_y()/cls.determinant_y()

class StaticCorrelationCoefficientMethod(object):
    @classmethod
    def avg(cls, array):
        return sum(array)/len(array)

    @classmethod
    def avg_sqr_deviation(cls, arr):
        n = len(arr)
        average = cls.avg(arr)

        return math.sqrt((1/n) * sum((x - average)**2 for x in arr))

    @classmethod
    def K(cls):
        n = len(sample["x"])
        avg_x = cls.avg(sample["x"])
        avg_y = cls.avg(sample["y"])

        sum_ = sum(
            (sample["x"][i] - avg_x)*(sample["y"][i] - avg_y) for i in range(n)
        )

        return (1/n) * sum_

    @classmethod
    def r_xy(cls):
        return cls.K()/(
            cls.avg_sqr_deviation(sample["x"])*cls.avg_sqr_deviation(sample["y"])
        )

    @classmethod
    def avg_x(cls):
        return cls.avg(sample["x"])

    @classmethod
    def avg_y(cls):
        return cls.avg(sample["y"])

    @classmethod
    def S_0x(cls):
        return cls.avg_sqr_deviation(sample["x"])

    @classmethod
    def S_0y(cls):
        return cls.avg_sqr_deviation(sample["y"])

    @classmethod
    def r_x_to_y(cls):
        return cls.r_xy() * (cls.S_0x()/cls.S_0y())

    @classmethod
    def r_y_to_x(cls):
        return cls.r_xy() * (cls.S_0y()/cls.S_0x())
