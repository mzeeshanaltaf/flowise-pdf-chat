from streamlit_navigation_bar import st_navbar
from home import *
from about import *

# INITIALIZE STREAMLIT APP
page_title = "Chat with PDF"
page_icon = "📄"
st.set_page_config(page_title=page_title, page_icon=page_icon, layout="centered")

styles = {
    "nav": {
        "background-color": "rgb(123, 209, 146)",
    },
    "div": {
        "max-width": "32rem",
    },
    "span": {
        "border-radius": "0.5rem",
        "color": "rgb(49, 51, 63)",
        "margin": "0 0.125rem",
        "padding": "0.4375rem 0.625rem",
    },
    "active": {
        "background-color": "rgba(255, 255, 255, 0.25)",
    },
    "hover": {
        "background-color": "rgba(255, 255, 255, 0.35)",
    },
}
options = {
    "use_padding": False,
    "show_menu": True,
    "show_sidebar": True,
}

page = st_navbar(["Home", "About"], styles=styles, options=options,)

if page == "Home":
    show_home()

if page == "About":
    show_about()
