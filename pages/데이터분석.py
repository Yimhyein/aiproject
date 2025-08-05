import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Streamlit app title soupçon
st.title("Student Grades Visualization")

# Data
data = {
    "name": ["lee", "park", "kim"],
    "grade": [2, 2, 2],
    "number": [1, 2, 3],
    "kor": [90, 88, 99],
    "eng": [91, 89, 99],
    "math": [81, 77, 99],
    "info": [100, 100, 100]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display raw data
st.subheader("Raw Data")
st.dataframe(df)

# Bar chart for individual student grades
st.subheader("Individual Student Grades")
fig1 = px.bar(
    df,
    x="name",
    y=["kor", "eng", "math", "info"],
    barmode="group",
    title="Grades by Student",
    labels={"value": "Score", "variable": "Subject"},
)
st.plotly_chart(fig1)

# Calculate average scores per subject
avg_scores = df[["kor", "eng", "math", "info"]].mean().reset_index()
avg_scores.columns = ["Subject", "Average Score"]

# Bar chart for average scores per subject
st.subheader("Average Scores by Subject")
fig2 = px.bar(
    avg_scores,
    x="Subject",
    y="Average Score",
    title="Average Scores per Subject",
    color="Subject",
)
st.plotly_chart(fig2)

# Summary statistics
st.subheader("Summary Statistics")
st.write(df[["kor", "eng", "math", "info"]].describe())