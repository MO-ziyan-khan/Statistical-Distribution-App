from .base import BaseDistribution
from scipy.stats import chi2
import numpy as np
import streamlit as st

class ChiSquareDistribution(BaseDistribution):
    def get_params(self, st):
        df = st.slider("Degrees of Freedom (ν)", 1, 30, 5, help="Degrees of freedom parameter")
        return {"df": df}

    def generate_data(self, params, x_range=None):
        if x_range is None:
            x = np.linspace(0, max(30, 3*params["df"]), 500)
        else:
            x = x_range
        y_pdf = chi2.pdf(x, df=params["df"])
        y_cdf = chi2.cdf(x, df=params["df"])
        return x, y_pdf, y_cdf, "PDF"

    def calculate_stats(self, params):
        return {
            "Mean": params["df"],
            "Variance": 2 * params["df"],
            "Standard Deviation": np.sqrt(2 * params["df"]),
            "Skewness": np.sqrt(8 / params["df"]),
            "Kurtosis": 12 / params["df"] + 3
        }

    def get_info(self):
        return "Used for testing variance and goodness-of-fit. Always positive and right-skewed. Interpretation: Sum of squares of standard normals; skewness decreases with df.\n\n**Parameter Effects:**\n- Degrees of Freedom (ν): Increases the mean and variance; reduces skewness and makes the distribution more symmetric as ν grows."

    def generate_samples(self, params, size):
        return np.random.chisquare(params["df"], size)

    def get_quantile_dist(self, params):
        return chi2(df=params["df"])

    def get_default_comp_params(self):
        return {"df": 3}