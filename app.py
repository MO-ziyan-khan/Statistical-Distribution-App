import streamlit as st
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import base64
from distributions import dist_registry

# Page configuration
st.set_page_config(
    page_title="📊 Distribution Visualizer",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1f77b4;
    }
    .info-box {
        background-color: #e8f4fd;
        padding: 1rem;
        border-radius: 0.5rem;
        border: 1px solid #bee5eb;
    }
</style>
""", unsafe_allow_html=True)

# Main header
st.markdown('<h1 class="main-header">📊 Distribution Visualizer</h1>', unsafe_allow_html=True)

# Sidebar configuration
with st.sidebar:
    st.header("🎛️ Configuration")
    
    dist_list = list(dist_registry.keys())
    
    dist_name = st.selectbox("Choose a distribution:", dist_list, help="Select the statistical distribution to visualize")
    
    # Display options
    st.subheader("📈 Display Options")
    show_cdf = st.checkbox("Show CDF", value=False, help="Display the cumulative distribution function")
    show_stats = st.checkbox("Show Statistics", value=True, help="Display key statistics of the distribution")
    show_samples = st.checkbox("Generate Sample Data", value=False, help="Generate and display random samples")
    show_quantiles = st.checkbox("Show Quantiles", value=False, help="Display common quantiles on the plot for better interpretation")
    
    if show_samples:
        sample_size = st.slider("Sample Size", 10, 1000, 100, help="Number of random samples to generate")
    
    # Comparison mode
    st.subheader("🔄 Comparison Mode")
    enable_comparison = st.checkbox("Compare Distributions", value=False, help="Compare multiple distributions")
    
    if enable_comparison:
        comparison_dist = st.selectbox("Compare with:", dist_list, index=1, help="Select a second distribution for comparison")

# Main content area
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📊 Distribution Visualization")
    
    # Get distribution object
    dist_obj = dist_registry[dist_name]
    
    # Parameter input
    params = dist_obj.get_params(st)

# Generate main distribution data
x, y_pdf, y_cdf, dist_type = dist_obj.generate_data(params)

if x is not None:
    # Create the main plot
    fig = go.Figure()
    
    # Add PDF/PMF trace
    if dist_type == "PMF":
        fig.add_trace(go.Bar(x=x, y=y_pdf, name=f"{dist_name} {dist_type}", 
                            marker_color='#1f77b4', opacity=0.7))
    else:
        fig.add_trace(go.Scatter(x=x, y=y_pdf, mode="lines", name=f"{dist_name} {dist_type}", 
                                line=dict(color='#1f77b4', width=3)))
    
    # Add CDF if requested
    if show_cdf and y_cdf is not None:
        fig.add_trace(go.Scatter(x=x, y=y_cdf, mode="lines", name=f"{dist_name} CDF", 
                                line=dict(color='#ff7f0e', width=2, dash='dash')))
    
    # Add quantiles for better interpretation if requested
    if show_quantiles:
        q_dist = dist_obj.get_quantile_dist(params)
        if q_dist:
            quantiles = [0.025, 0.25, 0.5, 0.75, 0.975]
            q_values = q_dist.ppf(quantiles)
            for q, q_val in zip(quantiles, q_values):
                fig.add_trace(go.Scatter(x=[q_val, q_val], y=[0, max(y_pdf)], mode="lines", 
                                         line=dict(color="red", dash="dot", width=1),
                                         name=f"{int(q*100)}% Quantile", showlegend=False))
                fig.add_annotation(x=q_val, y=max(y_pdf)*0.9, text=f"{int(q*100)}%", showarrow=False, 
                                   font=dict(color="red"))
    
    # Add comparison if enabled
    if enable_comparison and comparison_dist != dist_name:
        comp_dist_obj = dist_registry[comparison_dist]
        comp_params = comp_dist_obj.get_default_comp_params()
        comp_x, comp_y_pdf, comp_y_cdf, comp_dist_type = comp_dist_obj.generate_data(comp_params, x)
        
        if comp_x is not None:
            if comp_dist_type == "PMF":
                fig.add_trace(go.Bar(x=comp_x, y=comp_y_pdf, name=f"{comparison_dist} {comp_dist_type}", 
                                    marker_color='#2ca02c', opacity=0.5))
            else:
                fig.add_trace(go.Scatter(x=comp_x, y=comp_y_pdf, mode="lines", name=f"{comparison_dist} {comp_dist_type}", 
                                        line=dict(color='#2ca02c', width=2, dash='dot')))
    
    # Update layout
    fig.update_layout(
        title=f"{dist_name} Distribution Visualization",
        xaxis_title="x",
        yaxis_title=f"{dist_type} / CDF",
        template="plotly_white",
        height=500,
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )
    
    # Display the plot
    st.plotly_chart(fig, use_container_width=True)
    
    # Generate sample data if requested
    if show_samples:
        st.subheader("📊 Sample Data")
        
        try:
            samples = dist_obj.generate_samples(params, sample_size)
            
            # Create sample histogram
            fig_samples = go.Figure()
            fig_samples.add_trace(go.Histogram(x=samples, nbinsx=30, name="Sample Histogram", 
                                             marker_color='#1f77b4', opacity=0.7))
            
            # Add theoretical PDF/PMF overlay
            if dist_type == "PMF":
                fig_samples.add_trace(go.Bar(x=x, y=y_pdf * sample_size / len(x), name="Theoretical PMF",
                                           marker_color='#ff7f0e', opacity=0.8))
            else:
                # Scale PDF to match histogram
                bin_width = (samples.max() - samples.min()) / 30 if len(samples) > 1 and samples.max() > samples.min() else 1
                fig_samples.add_trace(go.Scatter(x=x, y=y_pdf * sample_size * bin_width, 
                                               mode="lines", name="Theoretical PDF",
                                               line=dict(color='#ff7f0e', width=2)))
            
            fig_samples.update_layout(
                title=f"Sample Data vs Theoretical {dist_name} Distribution",
                xaxis_title="Value",
                yaxis_title="Frequency",
                template="plotly_white",
                height=400
            )
            
            st.plotly_chart(fig_samples, use_container_width=True)
            
            # Sample statistics
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Sample Mean", f"{np.mean(samples):.3f}")
            with col2:
                st.metric("Sample Std", f"{np.std(samples):.3f}")
            with col3:
                st.metric("Sample Min", f"{np.min(samples):.3f}")
            with col4:
                st.metric("Sample Max", f"{np.max(samples):.3f}")
                
        except Exception as e:
            st.error(f"Error generating samples: {str(e)}")

# Statistics display
if show_stats and x is not None:
    with col2:
        st.subheader("📈 Statistics")
        
        stats = dist_obj.calculate_stats(params)
        
        if stats:
            for stat_name, stat_value in stats.items():
                if isinstance(stat_value, (int, float)):
                    st.metric(stat_name, f"{stat_value:.3f}")
                else:
                    st.metric(stat_name, str(stat_value))

# Additional features
st.markdown("---")
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("💡 Distribution Info & Interpretation")
    
    st.info(dist_obj.get_info())

with col2:
    st.subheader("🔧 Export Options")
    
    if st.button("📊 Export Plot as PNG"):
        try:
            img_bytes = fig.to_image(format="png")
            st.download_button(
                label="Download PNG",
                data=img_bytes,
                file_name=f"{dist_name}_distribution.png",
                mime="image/png"
            )
        except Exception as e:
            st.error("Error exporting plot. Please install kaleido: `pip install kaleido`")
    
    if st.button("📄 Export Data as CSV"):
        try:
            df = pd.DataFrame({
                'x': x,
                'pdf_pmf': y_pdf,
                'cdf': y_cdf if y_cdf is not None else [None] * len(x)
            })
            csv = df.to_csv(index=False)
            st.download_button(
                label="Download CSV",
                data=csv,
                file_name=f"{dist_name}_distribution_data.csv",
                mime="text/csv"
            )
        except Exception as e:
            st.error(f"Error exporting data: {str(e)}")

with col3:
    st.subheader("🎯 Quick Actions")
    
    if st.button("🔄 Reset to Defaults"):
        st.rerun()
    
    if st.button("📚 Show Help"):
        st.info("""
        **How to use this app:**
        1. Select a distribution from the sidebar
        2. Adjust parameters using the sliders
        3. Toggle CDF, quantiles, or samples for better visualization and interpretation
        4. Use statistics and info sections to understand key properties
        5. Enable comparison mode to overlay distributions
        6. Export plots and data as needed
        
        **Interpretation Tips:**
        - Look at mean/variance for central tendency and spread
        - Skewness >0 means right-skewed (tail to right)
        - Kurtosis >3 means heavier tails than normal
        - Quantiles show data thresholds (e.g., 95% below 97.5% quantile)
        - Check 'Parameter Effects' in info for how sliders change the distribution
        """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p>📊 Distribution Visualizer | Built with Streamlit, Plotly, and SciPy</p>
    <p>For educational and statistical analysis purposes | Modularized into multiple files, added Parameter Effects</p>
</div>
""", unsafe_allow_html=True)