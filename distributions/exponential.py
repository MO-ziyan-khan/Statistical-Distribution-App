from .base import BaseDistribution
from scipy.stats import expon
import numpy as np
import streamlit as st

class ExponentialDistribution(BaseDistribution):
    def get_params(self, st):
        scale = st.slider("Scale (1/λ)", 0.1, 10.0, 1.0, step=0.1, help="Scale parameter (mean = 1/rate)")
        return {"scale": scale}

    def generate_data(self, params, x_range=None):
        if x_range is None:
            x = np.linspace(0, 5 * params["scale"], 500)
        else:
            x = x_range
        y_pdf = expon.pdf(x, scale=params["scale"])
        y_cdf = expon.cdf(x, scale=params["scale"])
        return x, y_pdf, y_cdf, "PDF"

    def calculate_stats(self, params):
        return {
            "Mean": params["scale"],
            "Variance": params["scale"]**2,
            "Standard Deviation": params["scale"],
            "Skewness": 2,
            "Kurtosis": 9
        }

    def get_info(self):
        return "Models time between events in a Poisson process. Always positive and right-skewed. Interpretation: Memoryless property; constant hazard rate.\n\n**Parameter Effects:**\n- Scale (1/λ): Increases the mean and spread; flattens the curve and extends the tail when larger."

    def generate_samples(self, params, size):
        return np.random.exponential(params["scale"], size)

    def get_quantile_dist(self, params):
        return expon(scale=params["scale"])

    def get_default_comp_params(self):
        return {"scale": 1.0}