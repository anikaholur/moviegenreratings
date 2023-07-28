import pymongo
from pymongo import MongoClient
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings("ignore")


# establishing the connection between MongoDB and Python
#@st.experimental_singleton(suppress_st_warning=True)
#def init_connection():
    #return pymongo.MongoClient("mongodb+srv://st.secrets.db_username:st.secrets.db_pswd@st.secrets.cluster_name.qrqm7sw.mongodb.net/?retryWrites=true&w=majority")
@st.cache_resource
def init_connection():
    return pymongo.MongoClient("mongodb+srv://anikaholur8:Sarcasm_1234@mymcluster.qrqm7sw.mongodb.net/?retryWrites=true&w=majority")


client = init_connection()


# identifying the database we want to read from
db = client["fakedata"]

# identifying the collection we want to read from
myCollection = db["movies"]

# saving data in Pandas dataframe
df = pd.DataFrame(list(myCollection.find()))

# getting rid of the id field
df1 = df.drop(['_id'], axis=1)

# data is ready to go in a Pandas dataframe: we just need to visualize it on Streamlit!

# setting screen size
#st.set_page_config(layout="wide", page_title="Netflix Movies and TV Shows")

# main title
st.title("Ratings Across Movie Genres")
st.subheader("A simple web app that shows statistics on Netflix Movies and TV Shows over the years")

st.write(df1.describe())
st.dataframe(df1)

# creating a bar chart using seaborn
sns.set_theme(style='darkgrid', rc={'figure.dpi': 147},
              font_scale=0.7)
fig, ax = plt.subplots(figsize=(7, 2))
ax.set_title("Ratings Across Various Genres")
chart = sns.barplot(x='Genre', y='Rating', data=df1, ci=None)
ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
plt.xticks(fontsize=7)
# ax.figure
for p in chart.patches:
    chart.annotate("%.1f" % p.get_height(), (p.get_x() + p.get_width() / 2., p.get_height()),
                   ha='center', va='center', fontsize=5, color='black', xytext=(0, 10),
                   textcoords='offset points')

st.pyplot(fig)

