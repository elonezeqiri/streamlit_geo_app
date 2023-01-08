import streamlit as st
import leafmap.foliumap as leafmap
from folium.plugins import LocateControl
import pandas as pd
import geopandas as gpd
import os

def app():
    st.title("Objektet në mbrojtje të përkohshme")

    st.markdown(
        "Bazuar në Vendimin nr.149/2022, dt.07.10.22, Objektet të cilat janë në mbrojtje të përkohshme brenda komunës së Gjilanit janë të paraqitura në hartën në vijim. Klikoni mbi markerin blu dhe do keni të dhëna shtesë për këto objekte."
    )

    dataset = pd.read_pickle('data/zonat_e_mbrojtura.pkl')
    
    m = leafmap.Map(minimap = True, draw_export = True, png_enabled = True)
    
    m.add_basemap("HYBRID")

    m.add_gdf(dataset, info_mode = 'on_click')
    
    m.fit_bounds(m.get_bounds(), padding=(30, 30))

    LocateControl(auto_start=False).add_to(m)
    m.to_streamlit(height=700)
