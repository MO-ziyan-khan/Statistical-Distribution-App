from abc import ABC, abstractmethod
import streamlit as st

class BaseDistribution(ABC):
    @abstractmethod
    def get_params(self, st):
        pass

    @abstractmethod
    def generate_data(self, params, x_range=None):
        pass

    @abstractmethod
    def calculate_stats(self, params):
        pass

    @abstractmethod
    def get_info(self):
        pass

    @abstractmethod
    def generate_samples(self, params, size):
        pass

    def get_quantile_dist(self, params):
        return None

    def get_default_comp_params(self):
        return {}