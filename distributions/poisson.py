from .base import BaseDistribution
from scipy.stats import poisson
import numpy as np
import streamlit as st

class PoissonDistribution(BaseDistribution):
    def get_params(self, st):
        mu = st.slider("Lambda (λ)", 0.1, 20.0, 4.0, step=0.1, help="Rate parameter (mean number of events)")
        return {"mu": mu}

    def generate_data(self, params, x_range=None):
        x = np.arange(0, min(30, int(3*params["mu"]) + 5))
        y_pdf = poisson.pmf(x, mu=params["mu"])
        y_cdf = poisson.cdf(x, mu=params["mu"])
        return x, y_pdf, y_cdf, "PMF"

    def calculate_stats(self, params):
        return {
            "Mean": params["mu"],
            "Variance": params["mu"],
            "Standard Deviation": np.sqrt(params["mu"]),
            "Skewness": 1 / np.sqrt(params["mu"]),
            "Kurtosis": 1 / params["mu"] + 3
        }

    def get_info(self):
        return "Models the number of events occurring in a fixed time interval. Interpretation: Discrete; for rare events; mean = variance.\n\n**Parameter Effects:**\n- Lambda (λ): Increases the mean and variance; reduces skewness as λ grows, making it more symmetric and approximating normal."

    def generate_samples(self, params, size):
        return np.random.poisson(params["mu"], size)

    def get_default_comp_params(self):
        return {"mu": 3}