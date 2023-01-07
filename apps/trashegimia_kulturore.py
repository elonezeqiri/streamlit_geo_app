import streamlit as st
import leafmap.foliumap as leafmap
from folium.plugins import LocateControl
import pandas as pd
import geopandas as gpd
import os

def app():
    st.title("Vendet e klasifikuara si trashegimi kulturore ne Gjilan")

    st.markdown(
        "....."
    )

    dataset = pd.read_pickle('data/zonat_e_mbrojtura.pkl')
    
    m = leafmap.Map(minimap = True, draw_export = True, png_enabled = True)
    
    m.add_basemap("HYBRID")

    m.add_gdf(dataset, info_mode = 'on_click')
    
    m.fit_bounds(m.get_bounds(), padding=(30, 30))

    LocateControl(auto_start=False).add_to(m)
    m.to_streamlit(height=700)
