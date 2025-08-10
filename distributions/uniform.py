from .base import BaseDistribution
from scipy.stats import uniform
import numpy as np
import streamlit as st

class UniformDistribution(BaseDistribution):
    def get_params(self, st):
        col_a, col_b = st.columns(2)
        with col_a:
            low = st.slider("Lower bound (a)", -10.0, 10.0, 0.0, step=0.1, help="Lower bound of the uniform distribution")
        with col_b:
            high = st.slider("Upper bound (b)", -10.0, 10.0, 5.0, step=0.1, help="Upper bound of the uniform distribution")
        if low >= high:
            st.error("❌ Lower bound must be less than upper bound!")
            st.stop()
        return {"low": low, "high": high}

    def generate_data(self, params, x_range=None):
        if x_range is None:
            x = np.linspace(params["low"] - 1, params["high"] + 1, 500)
        else:
            x = x_range
        y_pdf = uniform.pdf(x, loc=params["low"], scale=params["high"] - params["low"])
        y_cdf = uniform.cdf(x, loc=params["low"], scale=params["high"] - params["low"])
        return x, y_pdf, y_cdf, "PDF"

    def calculate_stats(self, params):
        return {
            "Mean": (params["low"] + params["high"]) / 2,
            "Variance": (params["high"] - params["low"])**2 / 12,
            "Standard Deviation": (params["high"] - params["low"]) / np.sqrt(12),
            "Skewness": 0,
            "Kurtosis": 9/5
        }

    def get_info(self):
        return "All values in the range [a,b] are equally likely. Has constant probability density. Interpretation: No preference for any value in range.\n\n**Parameter Effects:**\n- Lower bound (a): Shifts the start of the flat density; increases mean if raised.\n- Upper bound (b): Shifts the end of the flat density; increases mean and variance if raised."

    def generate_samples(self, params, size):
        return np.random.uniform(params["low"], params["high"], size)

    def get_quantile_dist(self, params):
        return uniform(loc=params["low"], scale=params["high"] - params["low"])

    def get_default_comp_params(self):
        return {"low": -2, "high": 2}