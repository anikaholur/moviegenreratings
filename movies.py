import pymongo
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings("ignore")

# establishing the connection between MongoDB and Python
client = pymongo.MongoClient("mongodb://localhost:27017")

# identifying the database we want to read from
db = client["fakedata"]

# identifying the collection we want to read from
mycollection = db["movies"]

# saving data in Pandas dataframe
df = pd.DataFrame(list(mycollection.find()))

# getting rid of the id field
df1 = df.drop(['_id'], axis=1)

# data is ready to go in a Pandas dataframe: we just need to visualize it on Streamlit!

# setting screen size
st.set_page_config(layout="wide", page_title="Netflix Movies and TV Shows")

# main title
st.title("Ratings Across Movie Genres")
st.subheader("A simple web app that shows statistics on Netflix Movies and TV Shows over the years")

st.write(df1.describe())
st.dataframe(df1)

# creating a chart
# fig, ax = plt.subplots()
# ax.scatter(x=df1['GENRE'], y=df1['VOTES'])
# ax.set_xlabel('GENRE')
# ax.set_ylabel('RATING')
# ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
# st.pyplot(fig)
# creating a bar chart using seaborn
sns.set_theme(style='darkgrid', rc={'figure.dpi': 147},
              font_scale=0.7)
fig, ax = plt.subplots(figsize=(7, 2))
ax.set_title("Ratings Across Various Genres")
chart = sns.barplot(x='GENRE', y='RATING', data=df1, ci=None)
ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
plt.xticks(fontsize=7)
# ax.figure
for p in chart.patches:
    chart.annotate("%.1f" % p.get_height(), (p.get_x() + p.get_width() / 2., p.get_height()),
                   ha='center', va='center', fontsize=5, color='black', xytext=(0, 10),
                   textcoords='offset points')

st.pyplot(fig)

# uploaded_file = st.file_uploader('Upload your file here')

# if uploaded_file:
# st.header('Data Statistics')
# df = pd.read_csv(uploaded_file)
# st.write(df.describe())

# st.header('Data Header')
# st.write(df.head())

# fig, ax = plt.subplots()
# ax.scatter(x=df['GENRE'], y=df['VOTES'])
# ax.set_xlabel('GENRE')
# ax.set_ylabel('VOTES')
# ax.set_xticklabels(ax.get_xticklabels(), rotation=90)

# st.pyplot(fig)


# fetching one record from our collection
# one_record = mycollection.find_one()
# print(one_record)

# fetching all the records from our collection
# all_records = mycollection.find()
# print(all_records)
# run a for loop here to extract from cursor
# for row in all_records:
# print(row)

# convert cursor into list
# all_records = mycollection.find()
# print(all_records)
# list_cursor = list(all_records)
# print(list_cursor)
# now we should have a list of dictionaries
# now we should have a dataframe
# df = pd.DataFrame(list_cursor)
# df.head()
# df.tail()
