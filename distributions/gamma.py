from .base import BaseDistribution
from scipy.stats import gamma
import numpy as np
import streamlit as st

class GammaDistribution(BaseDistribution):
    def get_params(self, st):
        col_a, col_b = st.columns(2)
        with col_a:
            shape = st.slider("Shape (k)", 0.1, 10.0, 2.0, step=0.1, help="Shape parameter")
        with col_b:
            scale = st.slider("Scale (θ)", 0.1, 5.0, 2.0, step=0.1, help="Scale parameter")
        return {"shape": shape, "scale": scale}

    def generate_data(self, params, x_range=None):
        if x_range is None:
            x = np.linspace(0, 20, 500)
        else:
            x = x_range
        y_pdf = gamma.pdf(x, params["shape"], scale=params["scale"])
        y_cdf = gamma.cdf(x, params["shape"], scale=params["scale"])
        return x, y_pdf, y_cdf, "PDF"

    def calculate_stats(self, params):
        return {
            "Mean": params["shape"] * params["scale"],
            "Variance": params["shape"] * params["scale"]**2,
            "Standard Deviation": np.sqrt(params["shape"]) * params["scale"],
            "Skewness": 2 / np.sqrt(params["shape"]),
            "Kurtosis": 6 / params["shape"] + 3
        }

    def get_info(self):
        return "Used for modeling waiting times and continuous positive data. Interpretation: Generalizes exponential; shape and scale control form.\n\n**Parameter Effects:**\n- Shape (k): Larger values reduce skewness and make it more symmetric (approaches normal).\n- Scale (θ): Stretches the distribution horizontally; increases mean and variance."

    def generate_samples(self, params, size):
        return np.random.gamma(params["shape"], params["scale"], size)

    def get_quantile_dist(self, params):
        return gamma(a=params["shape"], scale=params["scale"])

    def get_default_comp_params(self):
        return {"shape": 2, "scale": 1}