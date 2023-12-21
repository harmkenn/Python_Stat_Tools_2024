import streamlit as st
from multiapp import MultiApp
from apps import a_quant # import your app modules here
st.set_page_config(layout="wide")
app = MultiApp()

# Add all your application here
app.add_app("Quantitative Stats", a_quant.app)

# The main app
app.run()