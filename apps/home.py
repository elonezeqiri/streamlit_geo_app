import streamlit as st
import leafmap.foliumap as leafmap
from folium.plugins import LocateControl
import geopandas as gpd

def app():
    st.title("Home")

    st.markdown(
        """
    insert text here____

    """
    )

    m = leafmap.Map(location = [42.569264,20.901489], zoom_start=8, )
    m.add_geojson('data/kufiri_ks.geojson', info_mode = 'on_click')
    m.fit_bounds(m.get_bounds(), padding=(30, 30))

    m.add_basemap("HYBRID")

    LocateControl(auto_start=False).add_to(m)
    m.to_streamlit(height=700)
