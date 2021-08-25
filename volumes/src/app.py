import streamlit as st
import pandas as pd

st.set_page_config(
        page_title="Ex-stream-ly Cool App",
        page_icon=":smiley:",
        layout="wide",
        # initial_sidebar_state="expanded"
        )


st.button('Say hello Josh')

agree = st.checkbox('I agree')

if agree:
    st.write('Great!')


st.title('My first app 2666777')

# Add title on the page
st.title("ZEN Group - Josh")

st.write("ZEN Journey \
    consumer's dynamic" )
    
df = pd.DataFrame({'col1': [1,2,3]})
df  # <-- Draw the dataframe