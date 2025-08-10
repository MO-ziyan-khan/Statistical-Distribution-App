from .base import BaseDistribution
from scipy.stats import norm
import numpy as np
import streamlit as st

class NormalDistribution(BaseDistribution):
    def get_params(self, st):
        col_a, col_b = st.columns(2)
        with col_a:
            mean = st.slider("Mean (μ)", -10.0, 10.0, 0.0, step=0.1, help="Mean of the normal distribution")
        with col_b:
            std = st.slider("Standard Deviation (σ)", 0.1, 5.0, 1.0, step=0.1, help="Standard deviation of the normal distribution")
        return {"mean": mean, "std": std}

    def generate_data(self, params, x_range=None):
        if x_range is None:
            x = np.linspace(params["mean"] - 4*params["std"], params["mean"] + 4*params["std"], 500)
        else:
            x = x_range
        y_pdf = norm.pdf(x, loc=params["mean"], scale=params["std"])
        y_cdf = norm.cdf(x, loc=params["mean"], scale=params["std"])
        return x, y_pdf, y_cdf, "PDF"

    def calculate_stats(self, params):
        return {
            "Mean": params["mean"],
            "Variance": params["std"]**2,
            "Standard Deviation": params["std"],
            "Skewness": 0,
            "Kurtosis": 3
        }

    def get_info(self):
        return "The normal distribution is symmetric and bell-shaped. It's characterized by its mean and standard deviation. Interpretation: About 68% of data falls within 1 SD of the mean, 95% within 2 SDs.\n\n**Parameter Effects:**\n- Mean (μ): Shifts the entire distribution left or right without changing the shape.\n- Standard Deviation (σ): Increases the spread (flatter and wider curve) when larger; decreases the spread (taller and narrower curve) when smaller."

    def generate_samples(self, params, size):
        return np.random.normal(params["mean"], params["std"], size)

    def get_quantile_dist(self, params):
        return norm(loc=params["mean"], scale=params["std"])

    def get_default_comp_params(self):
        return {"mean": 0, "std": 1}