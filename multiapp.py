"""Frameworks for running multiple Streamlit applications as a single app.
"""
import streamlit as st

class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        """Adds a new application.
        Parameters
        ----------
        func:
            the python function to render this app.
        title:
            title of the app. Appears in the dropdown in the sidebar.
        """
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):

        st.sidebar.title("Python Stat Tools v2024.1")
        st.sidebar.subheader("by Ken Harmon")
        st.session_state.gs_URL = st.sidebar.text_input("Public Google Sheet URL:","https://docs.google.com/spreadsheets/d/1tuQPjJbLV9e2F1abxs2HVJsZO0xaitc9KtcKJD1acXQ/edit#gid=182521220") 
               
        app = st.sidebar.radio(
            '',
            self.apps,
            format_func=lambda app: app['title'])

        app['function']()