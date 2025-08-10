from .base import BaseDistribution
from .normal import NormalDistribution
from .standard_normal import StandardNormalDistribution
from .chi_square import ChiSquareDistribution
from .binomial import BinomialDistribution
from .bernoulli import BernoulliDistribution
from .uniform import UniformDistribution
from .f_distribution import FDistribution
from .t_distribution import TDistribution
from .poisson import PoissonDistribution
from .beta import BetaDistribution
from .gamma import GammaDistribution
from .exponential import ExponentialDistribution
from .log_normal import LogNormalDistribution

dist_registry = {
    "Normal": NormalDistribution(),
    "Standard Normal": StandardNormalDistribution(),
    "Chi-square": ChiSquareDistribution(),
    "Binomial": BinomialDistribution(),
    "Bernoulli": BernoulliDistribution(),
    "Uniform": UniformDistribution(),
    "F-distribution": FDistribution(),
    "t-distribution": TDistribution(),
    "Poisson": PoissonDistribution(),
    "Beta": BetaDistribution(),
    "Gamma": GammaDistribution(),
    "Exponential": ExponentialDistribution(),
    "Log-Normal": LogNormalDistribution()
}