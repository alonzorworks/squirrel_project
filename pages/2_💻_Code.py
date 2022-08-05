import streamlit as st 
import pandas as pd  
import requests
from streamlit_lottie import st_lottie


st.set_page_config(
    page_title = "Code Review",
    page_icon = "💻"
)

# NOTE Allow pictures to be put into the document. 
def load_lottieurl(url):
    """If the lottie file does not display the image return nothing. This will prevent errors when trying to display the Lottie Files.
    Requires importing packages streamlit_lottie and requests"""
    r = requests.get(url)
    if r.status_code != 200:
        return None 
    return r.json()


def lottie_credit(credit):
    return st.markdown(f"<p style='text-align: center; color: gray;'>{credit}</p>", unsafe_allow_html=True)


st.title("About This Project")
run_sq = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_dedxlrqc.json")
st_lottie(run_sq, width = 300)
lottie_credit("Run Squirrel Syed Mubarak")


st.write("""I originally created a similar project to this in Jupyter Notebooks. Instead of simply transliterating the code from the orinal code I did, I enchanced the project in many different ways.\n
Below the code utilized in the main page is posed below.
""")

st.code('''
from turtle import width
import pandas as pd 
import numpy as np
import folium
from folium.plugins import MarkerCluster
import streamlit as st 
from streamlit_folium import folium_static
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from iteration_utilities import duplicates
from folium.plugins import HeatMap
from PIL import Image
import requests
from streamlit_lottie import st_lottie
# from math import pi
# import bokeh
# from collections import Counter

st.set_page_config(
    page_title = "Home Page",
    page_icon = "🏡"
)

# NOTE Allow pictures to be put into the document. 
def load_lottieurl(url):
    """If the lottie file does not display the image return nothing. This will prevent errors when trying to display the Lottie Files.
    Requires importing packages streamlit_lottie and requests"""
    r = requests.get(url)
    if r.status_code != 200:
        return None 
    return r.json()


def lottie_credit(credit):
    return st.markdown(f"<p style='text-align: center; color: gray;'>{credit}</p>", unsafe_allow_html=True)

st.title("Squirrel Census Central Park 2018 :chestnut: :deciduous_tree:")



df = pd.read_csv("central_sqrl_2018.csv")



image = Image.open("central_park_sq.PNG")

st.image(image, caption = "Photographs provided by rawpixel.com")

df

st.subheader("Written Analysis")

with st.expander("Click here to expand."):
    st.write(""" 
    The data was provided by New York City. More specifically NYC Open Data and The New York Department of Data. They were mostly looking for Eastern gray squirrels (Sciurus carolinensis). The data was collected by volunteers in 2018.
    \nBased on the sample, it is evident that the squirrel population is likely aging. 88% of the squirrels are adults, leaving only 12% of the population as juveniles ignoring the negligible number of animals of unknown age. The sample contains over 3,000 entries, that were collected over a two-week period from October 6th, 2018, until October 20th, 2018. There were only five squirrels that were sampled multiple times, during the duration of the study. Fifty-five percent of the data was collected in the daytime, while 45% of the data was collected during the evening.

The squirrels vary phenotypically. A vast majority of the squirrels are primarily gray. The secondary colors of the squirrels vary more dramatically. This may suggest that the squirrels are different species or vary in color for some other unspecified reasons.

The maps were the most elucidating aspect of this project. The breadths (width) of the rectangular park have the most squirrel activity overall. Central Park South is teeming with life, commerce, and human traffic. In addition to these, locals, and tourists alike, patronize food trucks at the border of the park. Additionally, there is a large mall and several restaurants where people will bring food and eat near the border of the park. It is not uncommon for people to drop food intentionally and unintentionally dropped by people on their leisurely stroll. There is even more activity in this area of the park near Central Park North. This is somewhat surprising considering Central Park North has considerably fewer things to do and is less remarkable. However, the heatmap reveals that Columbus’s circle is busier than any other frontier along the width. The whole park is filled with unique squirrel sightings. This helps show that park is a vital biome to the city. However, there is some considerable activity near certain bodies of water, especially “The Lake”. Certain areas of the park are devoid of squirrel activity such as the playground, which shows that squirrels still respect certain spaces that humans frequent likely due to lack of foraging opportunities.

Unfortunately, the activity facet of the squirrels of central park is somewhat limited. Most of the behavior’s researchers looked for within their ethogram were false, in the true/false section. It would have been immensely difficult for researchers to write down their other observations after already noting some other information. To get a better grasp of animal behavior, fewer squirrels would have to be observed to describe them in more vivid detail.

Much of this information comes from the writer/analyst repertoire. He took a course in animal behavior and interned in New York City. He has also spent several hours walking through the park. - Alonzo R. 
    
    """)


st.header("Graphing Section")
team = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_fu91tpxl.json")
st_lottie(team, width =700)
lottie_credit("Irfan Munawar 3D Product Launch Product Launch")


# NOTE Pie Charts 

def pie(column_name):
    pie_maker = px.pie(df, values = df[column_name].value_counts().values , names = df[column_name].value_counts().index)

    return st.plotly_chart(pie_maker)


def bar(column_name):
    # Should be bar not scatter but that is not worth renaming
    x_name = df[column_name].value_counts().index
    scatter = px.bar(df, y = df[column_name].value_counts().values , x = df[column_name].value_counts().index, color = df[column_name].value_counts().index, text_auto = True, width = 1000)
    return st.plotly_chart(scatter)

st.subheader("Bar Chart of Squirrel Primary Fur Color")
bar("Primary Fur Color")


st.subheader("Primary Fur Color")
pie("Primary Fur Color")

st.subheader("Bar Chart for Secondary Fur Color")
bar("Highlight Fur Color")
st.write("Note that fur highlight and secondary fur color is used interchangeably.")

st.subheader("Secondary Fur Color")
pie("Highlight Fur Color")

st.subheader("Bar Chart Squirrels' Age")
bar("Age")
st.subheader("Age of the Squirrels")
pie("Age")

st.subheader("Location of the Squirrels")
bar("Location")
pie("Location")

#NOTE Section of Boolean
st.header("Boolean Behaviors")
st.write("These are behaviors that were either observed (True) or not observed (False) while viewing the squirrels. In most cases these behaviors were not observed.")

# Get a df of true or false columns on a dataframe 
# Gets a name of their columns and turn it into a list. 
# Delete the non boolean column name within the data frame. 
# Use a for loop to call the bar and pie charts to graph them quickly. 
boolean_list = df.iloc[:,15:24].columns.tolist()
del boolean_list[5]

man = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_QIvVpl.json")


st_lottie(man)
lottie_credit("Man in Park Abdul Latif - LottieFiles")


with st.expander("Click here to see Boolean Charts"):
    for i in boolean_list:
        st.subheader(f"Boolean Chart for {i}")
        bar(i)
        pie(i)





# NOTE Maps 
# Lattitude then longitude
# cp stands for central park

# Map Section start (That is visual to the user, pre-req code starts before).



st.header("Mapping Section")
st.write("Note that the maps are interactive.")
map_zoom = load_lottieurl("https://assets10.lottiefiles.com/private_files/lf30_noclpt6t.json")
st_lottie(map_zoom)
lottie_credit("Loupe on map by Иван Шаршапин (Ivan Sharshapin) on LottieFiles.")

sleep = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_KhUhak.json")


sq_nut = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_9tswl7vw.json")

sql_nut = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_9tswl7vw.json")

sq1, sq2 = st.columns(2)

with sq2:
    st_lottie(sleep, key = "sleep")
    lottie_credit("Squirrel Sleeping - Johnathan Ferreria LottieFiles")
with sq1:
    st_lottie(sq_nut, key = "sq_pair")
    lottie_credit("Two Squirrels Bojan MItevski on LottieFiles.")


cp = folium.Map(location=[40.781832, -73.966714], zoom_start = 14)

st.subheader("Map of Central Park")
folium_static(cp)

st.write("Number of unique Squirrel IDs", df["Unique Squirrel ID"].nunique())
st.code(df["Unique Squirrel ID"].nunique())

repeats = list(duplicates(df["Unique Squirrel ID"]))
st.write("Number of Squirrels who showed up more than once." , repeats)


location = []

for animal in range(len(df) - 1):
    lat = df.iloc[animal]["X"] 
    long = df.iloc[animal]["Y"]
    
    tup = [lat, long]
    
    location.append(tup)

    cp2 = cp

    mapit = cp2

for point in range(len(location) -1):
    folium.Marker(location = [location[point][0], location[point][1] ],  fill_color='#43d9de', radius=8, popup= "<i>Animal</i>").add_to(cp2)

sq_list = df[["Y","X"]].values.tolist()
sq_list_size = len(sq_list)


cp2 = folium.Map(location=[40.781832, -73.966714],  zoom_start = 14)

for point in range(0, sq_list_size - 3000):
    folium.Marker(sq_list[point]).add_to(cp2)


st.write("This is the first 23 points in the dataset. There are over 3,000 recorded sightings of squirrels in this dataset. Each blue marker represents a single sighting.")
folium_static(cp2)

st.write("Cluster Map of Squirrel Sightings")
cp3 = folium.Map(location=[40.781832, -73.966714],  zoom_start = 14)
marker_cluster = folium.plugins.MarkerCluster().add_to(cp3)
for point in range(0, sq_list_size):
    folium.Marker(sq_list[point]).add_to(cp3).add_to(marker_cluster)
folium_static(cp3)


st.write("Cluster Map of Squirrel Sightings - State Terrain")
cp4 = folium.Map(location=[40.781832, -73.966714], tiles="Stamen Terrain",  zoom_start = 14)
marker_cluster4 = folium.plugins.MarkerCluster().add_to(cp4)

for point in range(0, sq_list_size):
    folium.Marker(sq_list[point]).add_to(cp4).add_to(marker_cluster4)

folium_static(cp4)

# Heatmap 
st.write("Heatmap of the Squirrel Sightings")
cp5 = folium.Map(location=[40.781832, -73.966714], tiles="Stamen Toner",  zoom_start = 14)
HeatMap(sq_list).add_to(cp5)
folium_static(cp5)

# Cp6 
st.write("Heatmap of the Squirrel Sightings - State Terrain")
cp6 = folium.Map(location=[40.781832, -73.966714], tiles="Stamen Terrain",  zoom_start = 14)
HeatMap(sq_list).add_to(cp6)
folium_static(cp6)

# Sightings in Time of Day 
sum =  df.loc[df["Shift"] == "AM"].X.count() + df.loc[df["Shift"] == "PM"].X.count()

st.write("Sighting in the AM.", df.loc[df["Shift"] == "AM"].X.count(),  df.loc[df["Shift"] == "AM"].X.count()/ sum * 100, "%")

st.write("Sightings in the PM", df.loc[df["Shift"] == "PM"].X.count(), df.loc[df["Shift"] == "PM"].X.count() / sum * 100, "%")

run_sq = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_dedxlrqc.json")
st_lottie(run_sq)
lottie_credit("Run Squirrel Syed Mubarak")


''')