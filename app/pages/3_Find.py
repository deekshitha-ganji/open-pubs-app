import pandas as pd
from geopy.geocoders import Nominatim
import folium
import pickle
import streamlit as st
from streamlit_folium import st_folium

#df = pd.read_csv("check_file.csv")

def nearest(lat,lot):
    df = pd.read_csv("check_file.csv")
    df['Distance'] = df.apply(lambda row: ((row['latitude'] - lat)**2 + (row['longitude'] - lot)**2)**0.5, axis=1)
    df = df.sort_values(by='Distance')
    nearest_pubs = df.head(5)
    return(nearest_pubs[['name', 'Distance']].reset_index(drop=True),nearest_pubs[['name', 'Distance','latitude','longitude']].reset_index(drop=True))


def show_map(lat,lot):
    map = folium.Map(location = [lat,lot], zoom_start=4)
    result1,result2 = nearest(lat,lot)
    for index, row in result2.iterrows():
        coords = (row['latitude'],row['longitude'])
        folium.Marker(coords, popup = row["name"]).add_to(map)
    m = map
    return(m)


def main():
    st.title('Find the nearest Pubs😁')
    #df = pd.read_csv("check_file.csv")
    #Getting the input from the user
    lat = st.number_input("Enter the Latitude")
    lot = st.number_input("Enter the Longitude")
    #try:
     #    lat = float(u1)
      #   lot = float(u2)
       #  st.write("You entered:", u1,u2)
    #except ValueError:
     #    st.write("Please enter a valid float.")
    
    result1 = ''
    result2 = ''
    folium_map = show_map(lat,lot)
    ####m = folium.Map(location=[lat,lot], zoom_start=12)
    # Creating a button
    if st.button('Find'):
        st.subheader("The nearest Pubs are:\n")
        result1,result2 = nearest(lat,lot)

    st.write(result1)
    st.subheader("Map")
    st_data = st_folium(folium_map, width=725)

if __name__ == '__main__':
    main()