# Configuration file for Distribution Visualizer Pro

# App Configuration
APP_CONFIG = {
    "title": "📊 Distribution Visualizer Pro",
    "page_icon": "📊",
    "layout": "wide",
    "initial_sidebar_state": "expanded"
}

# Available Distributions
DISTRIBUTIONS = {
    "Normal": {
        "type": "continuous",
        "parameters": ["mean", "std"],
        "description": "The normal distribution is symmetric and bell-shaped. It's characterized by its mean and standard deviation."
    },
    "Standard Normal": {
        "type": "continuous", 
        "parameters": [],
        "description": "A normal distribution with mean=0 and standard deviation=1. Used as a reference distribution."
    },
    "Chi-square": {
        "type": "continuous",
        "parameters": ["df"],
        "description": "Used for testing variance and goodness-of-fit. Always positive and right-skewed."
    },
    "Binomial": {
        "type": "discrete",
        "parameters": ["n", "p"],
        "description": "Models the number of successes in n independent trials with probability p of success."
    },
    "Bernoulli": {
        "type": "discrete",
        "parameters": ["p"],
        "description": "A special case of binomial with n=1. Models a single trial with two outcomes."
    },
    "Uniform": {
        "type": "continuous",
        "parameters": ["low", "high"],
        "description": "All values in the range [a,b] are equally likely. Has constant probability density."
    },
    "F-distribution": {
        "type": "continuous",
        "parameters": ["dfn", "dfd"],
        "description": "Used in analysis of variance (ANOVA) and regression analysis."
    },
    "t-distribution": {
        "type": "continuous",
        "parameters": ["df"],
        "description": "Used for small sample inference when population variance is unknown."
    },
    "Poisson": {
        "type": "discrete",
        "parameters": ["mu"],
        "description": "Models the number of events occurring in a fixed time interval."
    },
    "Beta": {
        "type": "continuous",
        "parameters": ["a", "b"],
        "description": "Bounded between 0 and 1. Useful for modeling probabilities and proportions."
    },
    "Gamma": {
        "type": "continuous",
        "parameters": ["shape", "scale"],
        "description": "Used for modeling waiting times and continuous positive data."
    }
}

# Parameter Ranges and Defaults
PARAMETER_CONFIGS = {
    "mean": {"min": -10.0, "max": 10.0, "default": 0.0, "step": 0.1},
    "std": {"min": 0.1, "max": 5.0, "default": 1.0, "step": 0.1},
    "df": {"min": 1, "max": 30, "default": 5, "step": 1},
    "n": {"min": 1, "max": 100, "default": 20, "step": 1},
    "p": {"min": 0.0, "max": 1.0, "default": 0.5, "step": 0.01},
    "low": {"min": -10.0, "max": 10.0, "default": 0.0, "step": 0.1},
    "high": {"min": -10.0, "max": 10.0, "default": 5.0, "step": 0.1},
    "dfn": {"min": 1, "max": 50, "default": 5, "step": 1},
    "dfd": {"min": 1, "max": 50, "default": 2, "step": 1},
    "mu": {"min": 0.1, "max": 20.0, "default": 4.0, "step": 0.1},
    "a": {"min": 0.1, "max": 10.0, "default": 2.0, "step": 0.1},
    "b": {"min": 0.1, "max": 10.0, "default": 5.0, "step": 0.1},
    "shape": {"min": 0.1, "max": 10.0, "default": 2.0, "step": 0.1},
    "scale": {"min": 0.1, "max": 5.0, "default": 2.0, "step": 0.1}
}

# Sample Generation Settings
SAMPLE_CONFIG = {
    "min_size": 10,
    "max_size": 1000,
    "default_size": 100,
    "histogram_bins": 30
}

# Plot Configuration
PLOT_CONFIG = {
    "template": "plotly_white",
    "height": 500,
    "colors": {
        "primary": "#1f77b4",
        "secondary": "#ff7f0e",
        "comparison": "#2ca02c"
    },
    "line_width": 3,
    "opacity": 0.7
}

# Export Settings
EXPORT_CONFIG = {
    "image_format": "png",
    "image_quality": 100,
    "csv_encoding": "utf-8"
}

# UI Configuration
UI_CONFIG = {
    "main_header_size": "2.5rem",
    "main_header_color": "#1f77b4",
    "metric_card_bg": "#f0f2f6",
    "info_box_bg": "#e8f4fd",
    "info_box_border": "#bee5eb"
}
