import streamlit as st
from streamlit_option_menu import option_menu
from apps import home, gjilan_buildings, upload, trashegimia_kulturore, pronat_e_legalizuara  

st.set_page_config(page_title="Streamlit Geospatial", layout="wide", )

# A dictionary of apps in the format of {"App title": "App icon"}

apps = [
    {"func": home.app, "title": "Home", "icon": "house"},
    {"func": upload.app, "title": "Upload", "icon": "cloud-upload"},
    {"func": trashegimia_kulturore.app, "title": "Objektet në mbrojtje", "icon": "house"},
     {"func": pronat_e_legalizuara.app, "title": "Ndërtesat në Gjilan", "icon": "map"},
]

titles = [app["title"] for app in apps]
titles_lower = [title.lower() for title in titles]
icons = [app["icon"] for app in apps]

params = st.experimental_get_query_params()

if "page" in params:
    default_index = int(titles_lower.index(params["page"][0].lower()))
else:
    default_index = 0

with st.sidebar:
    selected = option_menu(
        "Menu:",
        options=titles,
        icons=icons,
        menu_icon="cast",
        default_index=default_index,
    )

    st.sidebar.title("Kontakte:")
    st.sidebar.info(
        """
        Punimi në lëndën WebGis

        Punoi: Elonë Zeqiri
         elone.zeqiri@gmail.com

        Profesor i lëndës: Bashkim Idrizi
          bashkim.idrizi@uni-pr.edu

        """
    )
    
    st.sidebar.title("Referenca:")

    st.sidebar.write('[Gjeoportali shtetëror i Kosovës](http://geoportal.rks-gov.net)')
    st.sidebar.write('[Agjencioni Kadastral i Kosovës](https://akk.rks-gov.net/sq)')
    st.sidebar.write('[Objektet në mbrojtje të përkohshme](https://www.mkrs-ks.org/repository/docs/Vendim_i_Ministrit_MKRS_per_Mbrojtje_te_Perkohshme_2022-2023.pdf)')
    
for app in apps:
    if app["title"] == selected:
        app["func"]()
        break
