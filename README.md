# 📊 Distribution Visualizer Pro

A comprehensive statistical distribution visualization tool built with Streamlit, Plotly, and SciPy. This application allows users to explore and compare various probability distributions with interactive visualizations, statistical analysis, and data export capabilities.

## ✨ Features

### 🎯 Core Functionality
- **11 Statistical Distributions**: Normal, Standard Normal, Chi-square, Binomial, Bernoulli, Uniform, F-distribution, t-distribution, Poisson, Beta, and Gamma
- **Interactive Parameter Controls**: Real-time adjustment of distribution parameters with intuitive sliders
- **Dual Visualization**: Display both Probability Density/Mass Functions (PDF/PMF) and Cumulative Distribution Functions (CDF)
- **Responsive Design**: Modern, clean interface with sidebar layout and responsive columns

### 📈 Advanced Features
- **Statistical Analysis**: Real-time calculation and display of key statistics (mean, variance, standard deviation, skewness, kurtosis)
- **Sample Data Generation**: Generate random samples from distributions with customizable sample sizes
- **Distribution Comparison**: Compare multiple distributions side-by-side
- **Data Export**: Export plots as PNG images and distribution data as CSV files
- **Educational Information**: Built-in help and distribution descriptions

### 🎨 User Experience
- **Modern UI**: Professional styling with custom CSS and intuitive navigation
- **Helpful Tooltips**: Context-sensitive help for all controls and parameters
- **Error Handling**: Robust error handling with user-friendly messages
- **Responsive Layout**: Optimized for different screen sizes

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup Instructions

1. **Clone or download the project files**
   ```bash
   # If using git
   git clone <repository-url>
   cd "Distribution APP"
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Open your browser**
   - The app will automatically open at `http://localhost:8501`
   - If it doesn't open automatically, navigate to the URL shown in your terminal

## 📖 Usage Guide

### Basic Usage
1. **Select a Distribution**: Choose from the dropdown menu in the sidebar
2. **Adjust Parameters**: Use the sliders to modify distribution parameters
3. **View Visualization**: The main plot updates in real-time
4. **Toggle Options**: Enable/disable CDF display, statistics, and sample generation

### Advanced Features

#### 📊 Statistical Analysis
- Enable "Show Statistics" to view key distribution properties
- Statistics include mean, variance, standard deviation, skewness, and kurtosis
- Values update automatically when parameters change

#### 🔄 Distribution Comparison
1. Enable "Compare Distributions" in the sidebar
2. Select a second distribution for comparison
3. Both distributions will be plotted on the same graph
4. Use different line styles and colors to distinguish between them

#### 📈 Sample Data Generation
1. Enable "Generate Sample Data"
2. Adjust sample size (10-1000 samples)
3. View histogram of generated samples
4. Compare with theoretical distribution
5. See sample statistics (mean, std, min, max)

#### 💾 Export Functionality
- **Export Plot**: Download the current visualization as a PNG image
- **Export Data**: Download distribution data as a CSV file
- Files are automatically named with the distribution type

## 📚 Supported Distributions

### Continuous Distributions
- **Normal Distribution**: μ (mean), σ (standard deviation)
- **Standard Normal**: Fixed μ=0, σ=1
- **Chi-square**: ν (degrees of freedom)
- **Uniform**: a (lower bound), b (upper bound)
- **F-distribution**: dfn (numerator df), dfd (denominator df)
- **t-distribution**: ν (degrees of freedom)
- **Beta**: α (alpha), β (beta) shape parameters
- **Gamma**: k (shape), θ (scale) parameters

### Discrete Distributions
- **Binomial**: n (trials), p (success probability)
- **Bernoulli**: p (success probability)
- **Poisson**: λ (rate parameter)

## 🛠️ Technical Details

### Dependencies
- **Streamlit**: Web application framework
- **Plotly**: Interactive plotting library
- **SciPy**: Scientific computing and statistical functions
- **NumPy**: Numerical computing
- **Pandas**: Data manipulation and export
- **Kaleido**: Static image export for Plotly

### Architecture
- **Frontend**: Streamlit web interface
- **Backend**: Python with SciPy statistical functions
- **Visualization**: Plotly interactive charts
- **Data Processing**: NumPy and Pandas

## 🎯 Use Cases

### Educational
- Statistics and probability courses
- Data science education
- Research methodology training

### Professional
- Statistical analysis and modeling
- Data exploration and visualization
- Quality control and process monitoring
- Risk assessment and modeling

### Research
- Distribution fitting and comparison
- Statistical hypothesis testing preparation
- Monte Carlo simulation planning

## 🔧 Customization

### Adding New Distributions
1. Add the distribution name to the `dist_list`
2. Implement parameter controls in the main section
3. Add distribution logic to `generate_distribution_data()`
4. Add statistics calculation to `calculate_statistics()`
5. Update the information text dictionary

### Styling Customization
- Modify the CSS in the `st.markdown()` section
- Adjust colors, fonts, and layout parameters
- Customize the page configuration

## 🐛 Troubleshooting

### Common Issues

**Import Errors**
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Check Python version compatibility (3.8+)

**Plot Export Issues**
- Install Kaleido: `pip install kaleido`
- Ensure sufficient disk space for file downloads

**Performance Issues**
- Reduce sample size for large datasets
- Close other applications to free up memory

**Display Issues**
- Clear browser cache and refresh
- Try different browsers (Chrome, Firefox, Safari)

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues, feature requests, or pull requests.

## 📞 Support

For questions or support, please open an issue in the project repository or contact the development team.

---

**Built with ❤️ using Streamlit, Plotly, and SciPy**
