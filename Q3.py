#Q3
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    st.title("CSV File Uploader and Age Histogram Plotter")
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.subheader("Uploaded Data:")
        st.write(df)
        
        if 'name' in df.columns and 'age' in df.columns:
            st.subheader("Histogram of Ages:")
            plt.figure(figsize=(8, 6))
            sns.histplot(df['age'], bins=20, kde=True)
            plt.xlabel('Age')
            plt.ylabel('Frequency')
            st.pyplot()
        else:
            st.warning("The uploaded file does not contain the expected columns ('name' and 'age').")

if __name__ == "__main__":
    main()