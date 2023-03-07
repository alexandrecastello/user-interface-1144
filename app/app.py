import streamlit as st

import numpy as np
import pandas as pd

spell = st.secrets['spell']
key = st.secrets.some_magic_api.key

st.markdown("""# My First Streamlit app
## Use the slider to see the dataframe
Try it out!""")

df = pd.DataFrame({
    'first column': list(range(1, 11)),
    'second column': np.arange(10, 101, 10)
})

st.checkbox('Check me, please!')

# this slider allows the user to select a number of lines
# to display in the dataframe
# the selected value is returned by st.slider
line_count = st.slider('Select a line count', 1, 10, 3)

# and used to select the displayed lines
head_df = df.head(line_count)

head_df