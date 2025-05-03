import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set seaborn style and palette
sns.set_style('whitegrid')
palette = 'viridis'

@st.cache_data
def load_data():
    df = pd.read_csv('C:/Users/Admin/ESG_scorecard_project/processed_data.csv')

    # Map encoded Region back to names if needed (adjust mapping as per your data)
    region_map = {0: 'Africa', 1: 'Asia', 2: 'Europe', 3: 'Latin America', 4: 'Middle East', 5: 'North America', 6: 'Oceania'}
    if df['Region'].dtype != 'object':
        df['Region'] = df['Region'].map(region_map)

    # Ensure ESG_Rating is categorical with order
    rating_order = ['AAA', 'AA', 'A', 'BBB', 'BB', 'CCC']
    df['ESG_Rating'] = pd.Categorical(df['ESG_Rating'], categories=rating_order, ordered=True)

    return df

def main():
    st.title("🌿 ESG Scorecard Dashboard")

    df = load_data()

    # Sidebar filters
    st.sidebar.header("Filter Options")
    regions = df['Region'].dropna().unique()
    industries = df['Industry'].dropna().unique()
    years = df['Year'].dropna().unique()

    selected_regions = st.sidebar.multiselect("Select Region(s):", options=regions, default=list(regions))
    selected_industries = st.sidebar.multiselect("Select Industry(s):", options=industries, default=list(industries))
    selected_years = st.sidebar.multiselect("Select Year(s):", options=years, default=list(years))

    filtered_df = df[
        (df['Region'].isin(selected_regions)) &
        (df['Industry'].isin(selected_industries)) &
        (df['Year'].isin(selected_years))
    ]

    st.markdown(f"### Filtered Data: {filtered_df.shape[0]} companies")

    # KPIs
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Avg Environmental Score", f"{filtered_df['ESG_Environmental'].mean():.2f}")
    col2.metric("Avg Social Score", f"{filtered_df['ESG_Social'].mean():.2f}")
    col3.metric("Avg Governance Score", f"{filtered_df['ESG_Governance'].mean():.2f}")
    col4.metric("Avg ESG Score", f"{filtered_df[['ESG_Environmental', 'ESG_Social', 'ESG_Governance']].mean(axis=1).mean():.2f}")

    # ESG Rating distribution
    st.subheader("ESG Rating Distribution")
    rating_counts = filtered_df['ESG_Rating'].value_counts().reindex(['AAA', 'AA', 'A', 'BBB', 'BB', 'CCC']).fillna(0)

    fig, ax = plt.subplots()
    sns.barplot(x=rating_counts.index, y=rating_counts.values, palette=palette, ax=ax)
    ax.set_xlabel("ESG Rating")
    ax.set_ylabel("Number of Companies")
    st.pyplot(fig)

    # Average ESG scores by Region
    st.subheader("Average ESG Scores by Region")
    avg_scores_region = filtered_df.groupby('Region')[['ESG_Environmental', 'ESG_Social', 'ESG_Governance']].mean().reset_index()
    avg_scores_region_melted = avg_scores_region.melt(id_vars='Region', var_name='ESG Pillar', value_name='Average Score')

    fig2, ax2 = plt.subplots(figsize=(10,6))
    sns.barplot(data=avg_scores_region_melted, x='Region', y='Average Score', hue='ESG Pillar', palette=palette, ax=ax2)
    plt.xticks(rotation=45)
    st.pyplot(fig2)

    # ESG Scores Over Years
    st.subheader("ESG Scores Over Years")
    esg_yearly = filtered_df.groupby('Year')[['ESG_Environmental', 'ESG_Social', 'ESG_Governance']].mean().reset_index()

    fig3, ax3 = plt.subplots(figsize=(10,5))
    sns.lineplot(data=esg_yearly, x='Year', y='ESG_Environmental', label='Environmental', ax=ax3, palette=palette)
    sns.lineplot(data=esg_yearly, x='Year', y='ESG_Social', label='Social', ax=ax3, palette=palette)
    sns.lineplot(data=esg_yearly, x='Year', y='ESG_Governance', label='Governance', ax=ax3, palette=palette)
    ax3.set_title('Average ESG Pillar Scores Over Years')
    ax3.set_ylabel('Average Score')
    st.pyplot(fig3)

    # ESG Rating counts over years
    st.subheader("ESG Rating Counts Over Years")
    rating_yearly = filtered_df.groupby(['Year', 'ESG_Rating']).size().reset_index(name='Count')

    fig4, ax4 = plt.subplots(figsize=(10,5))
    sns.lineplot(data=rating_yearly, x='Year', y='Count', hue='ESG_Rating', marker='o', palette=palette, ax=ax4)
    ax4.set_title('ESG Rating Counts Over Years')
    st.pyplot(fig4)

    # Average ESG Scores by Industry
    st.subheader("Average ESG Scores by Industry")
    industry_avg = filtered_df.groupby('Industry')[['ESG_Environmental', 'ESG_Social', 'ESG_Governance']].mean().reset_index()
    industry_avg_melted = industry_avg.melt(id_vars='Industry', var_name='ESG Pillar', value_name='Average Score')

    fig5, ax5 = plt.subplots(figsize=(12,6))
    sns.barplot(data=industry_avg_melted, x='Industry', y='Average Score', hue='ESG Pillar', palette=palette, ax=ax5)
    plt.xticks(rotation=90)
    st.pyplot(fig5)

    # Correlation Heatmap
    st.subheader("Correlation Heatmap of ESG Pillars")
    corr = filtered_df[['ESG_Environmental', 'ESG_Social', 'ESG_Governance']].corr()
    fig_heatmap, ax_heatmap = plt.subplots()
    sns.heatmap(corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1, ax=ax_heatmap)
    ax_heatmap.set_title("Correlation Matrix")
    st.pyplot(fig_heatmap)

    # Scatter plot Environmental vs Social
    st.subheader("Scatter Plot: Environmental vs Social Scores")
    fig_scatter, ax_scatter = plt.subplots(figsize=(8,6))
    sns.scatterplot(data=filtered_df, x='ESG_Environmental', y='ESG_Social', hue='ESG_Rating', palette=palette, alpha=0.7, ax=ax_scatter)
    ax_scatter.set_xlabel("Environmental Score")
    ax_scatter.set_ylabel("Social Score")
    ax_scatter.set_title("Environmental vs Social Scores by ESG Rating")
    st.pyplot(fig_scatter)

    # Company ESG Profile Lookup
    st.subheader("Company ESG Profile Lookup")
    company_search = st.text_input("Enter company name (partial or full):")

    if company_search:
        company_results = df[df['CompanyName'].str.contains(company_search, case=False, na=False)]
        if not company_results.empty:
            st.dataframe(company_results[['CompanyName', 'Industry', 'Year', 'Region', 'ESG_Environmental', 'ESG_Social', 'ESG_Governance', 'ESG_Rating']])
        else:
            st.write("No companies found matching your search.")

    # Download filtered data
    st.subheader("Download Filtered Data")
    csv = filtered_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download CSV",
        data=csv,
        file_name='filtered_esg_data.csv',
        mime='text/csv',
    )

    # Explanations and info
    st.markdown("""
    ---
    ### Dashboard Insights  
    - **Correlation Heatmap** shows how ESG pillars relate to each other.  
    - **Scatter Plot** reveals clusters and outliers by ESG rating.  
    - Use filters to dive deeper into specific regions, industries, or years.
    """)
    st.info("Hover over charts to see detailed values. Use the company search to lookup specific ESG profiles.")

    with st.expander("More about ESG Ratings"):
        st.write("""
        ESG Ratings are assigned based on the average of Environmental, Social, and Governance scores:
        - AAA: Excellent (>=75)
        - AA: Very Good (60-74)
        - A: Good (50-59)
        - BBB: Moderate (40-49)
        - BB: Below Average (30-39)
        - CCC: Poor (<30)
        """)

if __name__ == "__main__":
    main()
