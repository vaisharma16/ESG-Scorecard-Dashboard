# ESG Scorecard Project

## Overview
This project analyzes Environmental, Social, and Governance (ESG) data for companies worldwide. It includes:

- **A Jupyter Notebook** for exploratory data analysis (EDA), data cleaning, and initial insights.
- **An interactive Streamlit dashboard** for dynamic exploration and visualization of ESG scores and ratings.

Together, these components demonstrate end-to-end data analytics skills, from raw data processing and analysis to building interactive tools for business users.

## Components

### 1. Jupyter Notebook (`ESG_Analysis.ipynb`)
- Data loading and preprocessing
- Handling missing values and encoding categorical variables
- Exploratory Data Analysis (EDA) with summary statistics and visualizations
- ESG rating assignment logic
- Initial insights and observations

### 2. Streamlit Dashboard (`esg_dashboard.py`)
- Interactive filters by Region, Industry, and Year
- Key Performance Indicators (KPIs) for ESG scores
- Visualizations including rating distributions, trends over time, and correlation heatmaps
- Company-specific ESG profile search
- Download filtered data as CSV
- Explanations and tooltips for user guidance

## Installation

1. Clone the repository:
   ```
   git clone 
   cd 
   ```

2. (Optional) Create and activate a virtual environment:
   ```
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
   Or install manually:
   ```
   pip install streamlit pandas matplotlib seaborn jupyter
   ```

4. Place your processed ESG data CSV in:
   ```
   C:/Users/Admin/ESG_scorecard_project/processed_data.csv
   ```
   (Update file paths in scripts if needed)

## Usage

- **Jupyter Notebook:**  
  Launch with:
  ```
  jupyter notebook ESG_Analysis.ipynb
  ```
  Use it to explore the data, understand preprocessing steps, and see initial analyses.

- **Streamlit Dashboard:**  
  Run with:
  ```
  streamlit run esg_dashboard.py
  ```
  Opens an interactive dashboard in your browser for deeper exploration.

## Project Structure

```
.
├── company_esg_financial_dataset # Original dataset from Kaggle
├── ESG_Analysis.ipynb          # Jupyter notebook with EDA and preprocessing
├── esg_dashboard.py            # Streamlit dashboard script
├── processed_data.csv          # Cleaned ESG dataset     
├── README.md                   # Project documentation
└── requirements.txt            # Python dependencies
```

## Future Work

- Deploy dashboard to cloud platforms (Streamlit Cloud, Heroku)
- Add predictive modeling for ESG risk and rating forecasts
- Integrate additional data sources (financial, textual ESG disclosures)
- Enhance the dashboard with more visualizations and user controls

## Contact

**Vaibhav Sharma**   
[LinkedIn](https://www.linkedin.com/in/vaibhavsharma16/)

---

*This project highlights skills in data cleaning, exploratory analysis, visualization, and interactive dashboard development, tailored for ESG and sustainability-focused data analyst roles.*
