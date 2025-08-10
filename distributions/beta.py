from .base import BaseDistribution
from scipy.stats import beta
import numpy as np
import streamlit as st

class BetaDistribution(BaseDistribution):
    def get_params(self, st):
        col_a, col_b = st.columns(2)
        with col_a:
            a = st.slider("Alpha (α)", 0.1, 10.0, 2.0, step=0.1, help="First shape parameter")
        with col_b:
            b = st.slider("Beta (β)", 0.1, 10.0, 5.0, step=0.1, help="Second shape parameter")
        return {"a": a, "b": b}

    def generate_data(self, params, x_range=None):
        if x_range is None:
            x = np.linspace(0, 1, 500)
        else:
            x = x_range
        y_pdf = beta.pdf(x, params["a"], params["b"])
        y_cdf = beta.cdf(x, params["a"], params["b"])
        return x, y_pdf, y_cdf, "PDF"

    def calculate_stats(self, params):
        return {
            "Mean": params["a"] / (params["a"] + params["b"]),
            "Variance": (params["a"] * params["b"]) / ((params["a"] + params["b"])**2 * (params["a"] + params["b"] + 1)),
            "Standard Deviation": np.sqrt((params["a"] * params["b"]) / ((params["a"] + params["b"])**2 * (params["a"] + params["b"] + 1))),
            "Skewness": (2 * (params["b"] - params["a"]) * np.sqrt(params["a"] + params["b"] + 1)) / ((params["a"] + params["b"] + 2) * np.sqrt(params["a"] * params["b"])),
            "Kurtosis": "Complex"
        }

    def get_info(self):
        return "Bounded between 0 and 1. Useful for modeling probabilities and proportions. Interpretation: Flexible shapes based on α and β.\n\n**Parameter Effects:**\n- Alpha (α): Increases weight toward 1; if α > β, skews left; affects shape (U, bell, etc.).\n- Beta (β): Increases weight toward 0; if β > α, skews right; symmetric if α = β."

    def generate_samples(self, params, size):
        return np.random.beta(params["a"], params["b"], size)

    def get_quantile_dist(self, params):
        return beta(a=params["a"], b=params["b"])

    def get_default_comp_params(self):
        return {"a": 2, "b": 2}