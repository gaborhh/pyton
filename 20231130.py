import PANDAS as pd
import streamlit as st
tabla = {"adatok":[0,1,2,3],
         "adat2":[4,5,6,7]}
kiiras = st.data_editor(pd.dataframe(table))
st.write(kiiras)
