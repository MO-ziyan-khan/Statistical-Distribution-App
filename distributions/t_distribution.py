from .base import BaseDistribution
from scipy.stats import t
import numpy as np
import streamlit as st

class TDistribution(BaseDistribution):
    def get_params(self, st):
        df = st.slider("Degrees of Freedom (ν)", 1, 30, 10, help="Degrees of freedom parameter")
        return {"df": df}

    def generate_data(self, params, x_range=None):
        if x_range is None:
            x = np.linspace(-5, 5, 500)
        else:
            x = x_range
        y_pdf = t.pdf(x, df=params["df"])
        y_cdf = t.cdf(x, df=params["df"])
        return x, y_pdf, y_cdf, "PDF"

    def calculate_stats(self, params):
        stats = {}
        if params["df"] > 1:
            stats["Mean"] = 0
        else:
            stats["Mean"] = "∞"
        if params["df"] > 2:
            stats["Variance"] = params["df"] / (params["df"] - 2)
        else:
            stats["Variance"] = "∞"
        stats["Standard Deviation"] = "Complex"
        stats["Skewness"] = 0 if params["df"] > 3 else "∞"
        stats["Kurtosis"] = 6 / (params["df"] - 4) + 3 if params["df"] > 4 else "∞"
        return stats

    def get_info(self):
        return "Used for small sample inference when population variance is unknown. Interpretation: Similar to normal but heavier tails; approaches normal as df increases.\n\n**Parameter Effects:**\n- Degrees of Freedom (ν): Larger values make tails thinner and distribution closer to normal; smaller values increase tail heaviness and variance."

    def generate_samples(self, params, size):
        return np.random.standard_t(params["df"], size)

    def get_quantile_dist(self, params):
        return t(df=params["df"])

    def get_default_comp_params(self):
        return {"df": 5}