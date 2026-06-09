import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 1. Image Banner & Title
st.image(r'C:\Users\Dell\Downloads\WhatsApp Image 2026-06-09 at 21.35.58.jpeg')
st.title("Global Poverty & Economic Inequality Dashboard")

# 2. Load Data
df = pd.read_csv(r"C:\Users\Dell\Downloads\global_poverty_economic_inequality.csv")

st.subheader("Raw Data")
st.write(df)

# ==============================================================================
# OBJECTIVE 1: Poverty Rates by Region
# ==============================================================================
st.markdown("---")
st.header("Objective 1")
st.write("**To identify which regions have the highest and lowest average poverty rates.**")

# Fix: Changed 'data' to 'df'
st.write(df.columns.tolist())
# Or print to terminal: print(df.columns)
region_poverty = df.groupby('region')['poverty_rate_pct'].mean().sort_values(ascending=False)

st.subheader("Average Poverty Rate by Region")
st.dataframe(region_poverty.round(2).reset_index())

# Key Findings
highest_region = region_poverty.idxmax()
highest_value = region_poverty.max()
lowest_region = region_poverty.idxmin()
lowest_value = region_poverty.min()

st.subheader("Key Findings")
st.success(f"**Highest Poverty Region:** {highest_region} ({highest_value:.2f}%)")
st.info(f"**Lowest Poverty Region:** {lowest_region} ({lowest_value:.2f}%)")

# Fix: Render Matplotlib figure inside Streamlit properly
fig, ax = plt.subplots(figsize=(10, 6))
region_poverty.sort_values().plot(kind='barh', color='maroon', ax=ax)
ax.set_title('Average Poverty Rate by Region')
ax.set_xlabel('Average Poverty Rate (%)')
ax.set_ylabel('Region')
plt.tight_layout()

# Use st.pyplot(fig) instead of plt.show()
st.pyplot(fig)


# ==============================================================================
# OBJECTIVE 2: GDP vs Poverty Rate
# ==============================================================================
st.markdown("---")
st.header("Objective 2")
st.write("**To investigate the relationship between GDP per capita and poverty rate.**")

# Fix: Changed 'data' to 'df'
correlation = df['gdp_per_capita_usd'].corr(df['poverty_rate_pct'])

st.subheader("Correlation Analysis")
st.metric(label="Correlation Coefficient", value=f"{correlation:.3f}")

# Adding a brief interpretation for Objective 2
st.write("""
**Interpretation:** * A value close to **-1** indicates a strong negative relationship (as GDP per capita increases, poverty rates tend to drop significantly).
* A value close to **0** means there is no clear linear relationship.
""")

# Create a scatter plot for GDP vs Poverty Rate
fig2, ax2 = plt.subplots(figsize=(10, 6))
ax2.scatter(df['gdp_per_capita_usd'], df['poverty_rate_pct'], color='teal', alpha=0.6, edgecolors='w')
ax2.set_title('GDP per Capita vs. Poverty Rate')
ax2.set_xlabel('GDP per Capita (USD)')
ax2.set_ylabel('Poverty Rate (%)')
ax2.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()

# Render scatter plot
st.pyplot(fig2)


# ==============================================================================
# OBJECTIVE 3: Income Inequality (Gini Index) Analysis
# ==============================================================================
st.markdown("---")
st.header("Objective 3")
st.write("**To analyze income inequality (Gini Index) across different regions.**")

# 1. Calculate average Gini Index by region
# (Assuming your column is named 'gini_index' or 'Gini Index')
region_gini = df.groupby('region')['gini_coefficient'].mean().sort_values(ascending=False)

st.subheader("Average Gini Index by Region")
st.dataframe(region_gini.round(2).reset_index())

# 2. Identify highest and lowest inequality regions
highest_gini_region = region_gini.idxmax()
highest_gini_value = region_gini.max()
lowest_gini_region = region_gini.idxmin()
lowest_gini_value = region_gini.min()

st.subheader("Key Inequality Findings")
st.error(f"**Highest Income Inequality:** {highest_gini_region} (Gini Index: {highest_gini_value:.2f})")
st.success(f"**Most Equal Income Distribution:** {lowest_gini_region} (Gini Index: {lowest_gini_value:.2f})")

# 3. Create a bar chart for Gini Index
fig3, ax3 = plt.subplots(figsize=(10, 6))
region_gini.plot(kind='bar', color='darkorange', ax=ax3)
ax3.set_title('Average Gini Index by Region (Higher = More Unequal)')
ax3.set_xlabel('Region')
ax3.set_ylabel('Average Gini Index')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Render Gini plot
st.pyplot(fig3)