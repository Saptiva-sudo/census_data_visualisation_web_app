import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


@st.cache()
def load_data():
	# Load the Adult Income dataset into DataFrame.

	df = pd.read_csv('https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/whitehat-ds-datasets/adult.csv', header=None)
	df.head()

	# Rename the column names in the DataFrame. 

	# Create the list
	column_name =['age', 'workclass', 'fnlwgt', 'education', 'education-years', 'marital-status', 'occupation', 'relationship', 'race', 'gender','capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'income']

	# Rename the columns using 'rename()'
	for i in range(df.shape[1]):
	  df.rename(columns={i:column_name[i]},inplace=True)

	# Print the first five rows of the DataFrame
	df.head()

	# Replace the invalid values ' ?' with 'np.nan'.

	df['native-country'] = df['native-country'].replace(' ?',np.nan)
	df['workclass'] = df['workclass'].replace(' ?',np.nan)
	df['occupation'] = df['occupation'].replace(' ?',np.nan)

	# Delete the rows with invalid values and the column not required 

	# Delete the rows with the 'dropna()' function
	df.dropna(inplace=True)

	# Delete the column with the 'drop()' function
	df.drop(columns='fnlwgt',axis=1,inplace=True)

	return df


census_df = load_data()
st.title("Census Data Visualisation Web App")
st.sidebar.title("Exploratory Data Analysis")
if (st.sidebar.checkbox("show raw data")):
    st.subheader("Census Data Set")
    st.write(census_df)
    st.write("No of rows:",census_df.shape[0])
    st.write("No of columns:",census_df.shape[1])
st.sidebar.subheader("Visualisation Selector")
plot_list = st.sidebar.multiselect("Select the charts or plots:",("Pie chart","Box Plot","Count Plot"))
st.set_option("deprecation.showPyplotGlobalUse",False)
if "Pie chart" in plot_list:
  st.subheader("Pie Chart")
  pie_data = census_df["income"].value_counts()
  plt.figure(figsize=(4,4))
  plt.title(f"Distribution of records for different income groups")
  plt.pie(pie_data,labels=pie_data.index,autopct="%1.2f%%",startangle=30,explode=np.linspace(0.05,0.1,2))
  st.pyplot()
  pie_data2 = census_df["gender"].value_counts()
  plt.figure(figsize=(4,4))
  plt.title(f"Distribution of records for different gender groups")
  plt.pie(pie_data2,labels=pie_data2.index,autopct="%1.2f%%",startangle=30,explode=np.linspace(0.05,0.1,2))
  st.pyplot()
if "Box Plot" in plot_list:
  st.subheader("Box Plot for the hours worked per week")
  plt.figure(figsize=(12,6))
  plt.title(f"Distribution for hours per week for different income groups")
  sns.boxplot(x="hours-per-week",y="income",data=census_df)
  plt.xlabel("Hours-per-week")
  plt.ylabel("Income-groups")
  st.pyplot()
  plt.figure(figsize=(12,6))
  plt.title(f"Distribution for hours per week for different gender groups")
  sns.boxplot(x="hours-per-week",y="gender",data=census_df)
  plt.xlabel("Hours-per-week")
  plt.ylabel("Gender")
  st.pyplot()
if "Count Plot" in plot_list:
  st.subheader("Count Plot for distribution of records for unique work-class groups")
  sns.countplot(x="workclass",data=census_df)
  st.pyplot()
