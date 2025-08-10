from .base import BaseDistribution
from scipy.stats import bernoulli
import numpy as np
import streamlit as st

class BernoulliDistribution(BaseDistribution):
    def get_params(self, st):
        p = st.slider("Probability of success (p)", 0.0, 1.0, 0.5, step=0.01, help="Probability of success")
        return {"p": p}

    def generate_data(self, params, x_range=None):
        x = np.array([0, 1])
        y_pdf = bernoulli.pmf(x, params["p"])
        y_cdf = bernoulli.cdf(x, params["p"])
        return x, y_pdf, y_cdf, "PMF"

    def calculate_stats(self, params):
        return {
            "Mean": params["p"],
            "Variance": params["p"] * (1 - params["p"]),
            "Standard Deviation": np.sqrt(params["p"] * (1 - params["p"])),
            "Skewness": (1 - 2*params["p"]) / np.sqrt(params["p"] * (1 - params["p"])),
            "Kurtosis": (1 - 6*params["p"]*(1-params["p"])) / (params["p"] * (1 - params["p"])) + 3
        }

    def get_info(self):
        return "A special case of binomial with n=1. Models a single trial with two outcomes. Interpretation: Binary outcome; foundation for binomial.\n\n**Parameter Effects:**\n- Probability of success (p): Increases probability of 1 (success) and decreases for 0; affects skewness (right-skewed if p<0.5, left if p>0.5)."

    def generate_samples(self, params, size):
        return np.random.binomial(1, params["p"], size)

    def get_default_comp_params(self):
        return {"p": 0.5}