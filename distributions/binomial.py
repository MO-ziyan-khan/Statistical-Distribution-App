from .base import BaseDistribution
from scipy.stats import binom
import numpy as np
import streamlit as st

class BinomialDistribution(BaseDistribution):
    def get_params(self, st):
        col_a, col_b = st.columns(2)
        with col_a:
            n = st.slider("Number of trials (n)", 1, 100, 20, help="Number of independent trials")
        with col_b:
            p = st.slider("Probability of success (p)", 0.0, 1.0, 0.5, step=0.01, help="Probability of success in each trial")
        return {"n": n, "p": p}

    def generate_data(self, params, x_range=None):
        x = np.arange(0, params["n"] + 1)
        y_pdf = binom.pmf(x, params["n"], params["p"])
        y_cdf = binom.cdf(x, params["n"], params["p"])
        return x, y_pdf, y_cdf, "PMF"

    def calculate_stats(self, params):
        return {
            "Mean": params["n"] * params["p"],
            "Variance": params["n"] * params["p"] * (1 - params["p"]),
            "Standard Deviation": np.sqrt(params["n"] * params["p"] * (1 - params["p"])),
            "Skewness": (1 - 2*params["p"]) / np.sqrt(params["n"] * params["p"] * (1 - params["p"])),
            "Kurtosis": (1 - 6*params["p"]*(1-params["p"])) / (params["n"] * params["p"] * (1 - params["p"])) + 3
        }

    def get_info(self):
        return "Models the number of successes in n independent trials with probability p of success. Interpretation: Discrete; approximates normal for large n.\n\n**Parameter Effects:**\n- Number of trials (n): Increases the range and variance; makes the distribution more symmetric for p=0.5 as n grows.\n- Probability of success (p): Shifts the mean (n*p); makes it right-skewed if p<0.5, left-skewed if p>0.5."

    def generate_samples(self, params, size):
        return np.random.binomial(params["n"], params["p"], size)

    def get_default_comp_params(self):
        return {"n": 10, "p": 0.5}