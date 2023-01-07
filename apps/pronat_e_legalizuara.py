import streamlit as st
import leafmap.foliumap as leafmap
from folium.plugins import LocateControl
import geopandas as gpd
import os

def app():
    st.title("Ndertesat e legalizuara ne Gjilan")

    st.markdown(
        "Add description Here!"
    )

    file_paths = [f'data/ndertesat_data/{file}' for file in os.listdir('data/ndertesat_data') if file.endswith(".shp")]

    file_names = [x.split('/')[-1].split('.')[0] for x in file_paths]

    buildings_dict = {}
    for file_name in file_paths:
        buildings_dict[file_name.split('/')[-1].split('.')[0]] = gpd.read_file(file_name)


    kati = st.selectbox(label = 'caktoni katin', options=file_names)

    m = leafmap.Map(minimap = True, draw_export = True, png_enabled = True)
    m.add_gdf(buildings_dict[kati], info_mode = 'on_click', layer_name = f'Kati {kati}')
    # m.add_marker([42.421164, 21.421052])
    
    m.fit_bounds(m.get_bounds(), padding=(30, 30))
    # m.add_basemap("HYBRID")




    # # m.
    # LocateControl(auto_start=False).add_to(m)
    m.to_streamlit(height=700)
