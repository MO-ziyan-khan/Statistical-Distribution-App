from .base import BaseDistribution
from scipy.stats import f
import numpy as np
import streamlit as st

class FDistribution(BaseDistribution):
    def get_params(self, st):
        col_a, col_b = st.columns(2)
        with col_a:
            dfn = st.slider("dfn (numerator)", 1, 50, 5, help="Degrees of freedom for numerator")
        with col_b:
            dfd = st.slider("dfd (denominator)", 1, 50, 2, help="Degrees of freedom for denominator")
        return {"dfn": dfn, "dfd": dfd}

    def generate_data(self, params, x_range=None):
        if x_range is None:
            x = np.linspace(0, 5, 500)
        else:
            x = x_range
        y_pdf = f.pdf(x, params["dfn"], params["dfd"])
        y_cdf = f.cdf(x, params["dfn"], params["dfd"])
        return x, y_pdf, y_cdf, "PDF"

    def calculate_stats(self, params):
        stats = {}
        if params["dfd"] > 2:
            stats["Mean"] = params["dfd"] / (params["dfd"] - 2)
        else:
            stats["Mean"] = "∞"
        if params["dfd"] > 4:
            stats["Variance"] = (2 * params["dfd"]**2 * (params["dfn"] + params["dfd"] - 2)) / (params["dfn"] * (params["dfd"] - 2)**2 * (params["dfd"] - 4))
        else:
            stats["Variance"] = "∞"
        stats["Standard Deviation"] = "Complex"
        stats["Skewness"] = "Complex"
        stats["Kurtosis"] = "Complex"
        return stats

    def get_info(self):
        return "Used in analysis of variance (ANOVA) and regression analysis. Interpretation: Ratio of two chi-squares; right-skewed.\n\n**Parameter Effects:**\n- dfn (numerator): Affects skewness; larger values make the distribution less skewed.\n- dfd (denominator): Affects mean and variance; larger values make it approach 1 and reduce variance."

    def generate_samples(self, params, size):
        return np.random.f(params["dfn"], params["dfd"], size)

    def get_quantile_dist(self, params):
        return f(dfn=params["dfn"], dfd=params["dfd"])

    def get_default_comp_params(self):
        return {"dfn": 3, "dfd": 5}