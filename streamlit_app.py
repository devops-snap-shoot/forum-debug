import streamlit as st

html='<iframe src="https://www.w3schools.com" title="W3Schools Free Online Web Tutorials"></iframe>'

st.components.v1.html(html, width=None, height=None, scrolling=False)
