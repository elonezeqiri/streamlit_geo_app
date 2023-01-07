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

    file_names = [f'data/ndertesat/{file}' for file in os.listdir('data/ndertesat') if file.endswith(".geojson")]

    file_ref = [int(x.split('.')[0].split('/')[-1]) for x in file_names]

    filepaths = dict(zip(file_ref, file_names))
    
    kati = st.slider(label = 'caktoni katin', min_value = 1, max_value = len(filepaths), step = 1, )

    st.text(filepaths)

    m = leafmap.Map(minimap = True, draw_export = True, png_enabled = True)
    m.add_geojson(filepaths[kati], info_mode = 'on_click', layer_name = f'kati {kati}')
    # m.add_marker([42.421164, 21.421052])
    
    m.fit_bounds(m.get_bounds(), padding=(30, 30))
    # m.add_basemap("HYBRID")




    # # m.
    # LocateControl(auto_start=False).add_to(m)
    m.to_streamlit(height=700)
