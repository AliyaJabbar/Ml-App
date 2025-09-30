# streamlit_app.py

import streamlit as st
import pandas as pd
import numpy as np

# 1. Page setup
st.set_page_config(page_title="My Streamlit App", page_icon="🚀", layout="wide")
st.title("🚀 My First Streamlit App")
st.write("This is a rough starter template for you to build on.")

# 2. Sidebar controls
st.sidebar.header("⚙️ Settings")
user_name = st.sidebar.text_input("Enter your name:", "Aliya")
option = st.sidebar.selectbox("Choose an option:", ["Show Data", "Generate Random Numbers", "About"])

# 3. Main app logic
if option == "Show Data":
    st.subheader(f"Hello, {user_name}! 👋 Here’s a sample dataset:")
    df = pd.DataFrame({
        "A": np.random.randint(1, 100, 10),
        "B": np.random.randint(100, 200, 10)
    })
    st.dataframe(df)

elif option == "Generate Random Numbers":
    st.subheader("🔢 Random Numbers")
    nums = np.random.randn(10)
    st.line_chart(nums)

elif option == "About":
    st.subheader("ℹ️ About this App")
    st.write("""
    - This is a **rough Streamlit skeleton**.
    - Replace the logic with your own project idea.
    - You can add data analysis, ML predictions, or visual dashboards.
    """)

# 4. Footer
st.write("---")
st.caption("Built with ❤️ using Streamlit")
