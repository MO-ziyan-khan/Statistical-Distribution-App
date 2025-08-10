from .base import BaseDistribution
from scipy.stats import lognorm
import numpy as np
import streamlit as st

class LogNormalDistribution(BaseDistribution):
    def get_params(self, st):
        col_a, col_b = st.columns(2)
        with col_a:
            mean = st.slider("Mean (μ)", -5.0, 5.0, 0.0, step=0.1, help="Mean of the underlying normal distribution")
        with col_b:
            std = st.slider("Standard Deviation (σ)", 0.1, 5.0, 1.0, step=0.1, help="Standard deviation of the underlying normal distribution")
        return {"mean": mean, "std": std}

    def generate_data(self, params, x_range=None):
        if x_range is None:
            x = np.linspace(0, np.exp(params["mean"] + 4 * params["std"]), 500)
        else:
            x = x_range
        y_pdf = lognorm.pdf(x, s=params["std"], scale=np.exp(params["mean"]))
        y_cdf = lognorm.cdf(x, s=params["std"], scale=np.exp(params["mean"]))
        return x, y_pdf, y_cdf, "PDF"

    def calculate_stats(self, params):
        mu = params["mean"]
        sigma = params["std"]
        mean = np.exp(mu + sigma**2 / 2)
        variance = (np.exp(sigma**2) - 1) * np.exp(2*mu + sigma**2)
        return {
            "Mean": mean,
            "Variance": variance,
            "Standard Deviation": np.sqrt(variance),
            "Skewness": (np.exp(sigma**2) + 2) * np.sqrt(np.exp(sigma**2) - 1),
            "Kurtosis": np.exp(4*sigma**2) + 2*np.exp(3*sigma**2) + 3*np.exp(2*sigma**2) - 3
        }

    def get_info(self):
        return "Models data whose logarithm is normally distributed. Useful for positive skewed data like incomes. Interpretation: Multiplicative effects; right-skewed.\n\n**Parameter Effects:**\n- Mean (μ): Shifts the location (increases the peak position exponentially).\n- Standard Deviation (σ): Increases skewness and tail length when larger; makes distribution more spread out."

    def generate_samples(self, params, size):
        return np.random.lognormal(params["mean"], params["std"], size)

    def get_quantile_dist(self, params):
        return lognorm(s=params["std"], scale=np.exp(params["mean"]))

    def get_default_comp_params(self):
        return {"mean": 0, "std": 1}