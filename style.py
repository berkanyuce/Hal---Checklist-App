import streamlit as st

def change_background():
    style_markdown = st.markdown(
        """
    <style>
    .reportview-container .markdown-text-container {
        font-family: monospace;
    }
    .sidebar .sidebar-content {
        background-image: linear-gradient(white,white);
        color: white;
    }
    .Widget>label {
        color: black;
        font-family: monospace;
    }
    [class^="st-b"]  {
        color: black;
        font-family: monospace;
    }
    .st-bb {
        background-color: transparent;
    }
    .st-at {
        background-color: white;
    }footer {
        font-family: monospace;
    }
    .reportview-container .main footer, .reportview-container .main footer a {
        color: #0c0080;
    }
    header .decoration {
        background-image: none;
    }
    
    </style>
    """,
        unsafe_allow_html=True,
    )