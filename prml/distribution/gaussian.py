import math
import numpy as np
from typing import Optional
from prml.distribution.distribution import Distribution


class Gaussian(Distribution):
    """
    The Gaussian distribution

    p(x|mu, var) = exp{-0.5 * (x - mu)^2 / var} / sqrt(2pi * var)
    """

    def __init__(self, mu: Optional[float], var: Optional[float]):
        self.mu = mu
        self.var = var

    def fit_ml(self, x: np.ndarray, unbiased: bool):
        self.mu = np.mean(x)
        if unbiased:
            self.var = np.sum(np.power(x - self.mu, 2)) / (x.size - 1)
        else:
            self.var = np.var(x)

    def pdf(self, x: float):
        d = x - self.mu
        return np.exp(-d ** 2 / (2 * self.var)) / np.sqrt(2 * np.pi * self.var)

    def sample(self, sample_size: int):
        return np.random.normal(loc=self.mu, scale=math.sqrt(self.var), size=(sample_size,))