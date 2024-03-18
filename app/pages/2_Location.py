import pandas as pd
from geopy.geocoders import Nominatim
import folium
import pickle
import streamlit as st
from streamlit_folium import st_folium

import numpy as np
import pandas as pd
import streamlit as st
import folium
from geopy.geocoders import Nominatim
from streamlit_folium import st_folium

df = pd.read_csv("check_file.csv")

def getdfp(inp1):
    n1 = df[df['postcode'] == inp1]
    return n1[['name', 'latitude', 'longitude']].reset_index(drop=True)

def get_coordinates_from_postal_code(inp1):
    geolocator = Nominatim(user_agent="your_app_name")
    location = geolocator.geocode(inp1)
    if location:
        return location.latitude, location.longitude
    else:
        return None, None

def smap(inp1):
    try:
        result1 = getdfp(inp1)
        lat, lot = get_coordinates_from_postal_code(inp1)
        map = folium.Map(location=[lat, lot], zoom_start=4)
        for index, row in result1.iterrows():
            coords = (row['latitude'], row['longitude'])
            folium.Marker(coords, popup=row["name"]).add_to(map)
        return map
    except (ValueError, AttributeError) as e:
        print(f"Error: {e}")
        print(f"Unable to retrieve coordinates for {inp1}")
        return None
    
def getdfla(inp1):
    n1 = df[df['local_authority'] == inp1]
    return n1[['name', 'latitude', 'longitude']].reset_index(drop=True)
def smap2(inp1):
    try:
        result1 = getdfla(inp1)
        lat, lot = get_coordinates_from_postal_code(inp1)
        map = folium.Map(location=[lat, lot], zoom_start=9)
        for index, row in result1.iterrows():
            coords = (row['latitude'], row['longitude'])
            folium.Marker(coords, popup=row["name"]).add_to(map)
        return map
    except (ValueError, AttributeError) as e:
        print(f"Error: {e}")
        print(f"Unable to retrieve coordinates for {inp1}")
        return None
@st.cache_data
def display1(inp1):
    condition1 = df['postcode'] == inp1
    res1 = df.loc[condition1, 'name']
    return pd.DataFrame(res1).reset_index(drop=True)

@st.cache_data
def display2(inp2):
    condition2 = df['local_authority'] == inp2
    res2 = df.loc[condition2, 'name']
    return pd.DataFrame(res2).reset_index(drop=True)

def main():
    st.title('Open Pubs ✨')
    input_type = st.radio("Select input type:", ["Postal Code", "Local Authority"])

    if input_type == "Postal Code":
        inp1 = st.text_input("Enter the Postal code")
        result = ''
        folium_map = smap(inp1)

        if st.button("Display"):
            result = display1(inp1)
            st.write("The list of Pubs\n",result)

    if input_type == "Local Authority":
        inp2 = st.text_input("Enter the Local Authority")
        result = ''
        folium_map = smap2(inp2)
        if st.button("Display"):
            result = display2(inp2)
            st.write("The list of Pubs\n",result)
            
            
            #folium_map = smap(inp2)

    #st.write(result)
    if folium_map is not None:
       st_folium(folium_map, width=725)

if __name__ == '__main__':
    main()
