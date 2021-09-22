import streamlit as st

import numpy as np
import pandas as pd

st.title("GPA PREDICTOR 🎯!")

df = pd.DataFrame({
  'COURSE': ['IPE 2207', 'IPE 2229', 'EEE 2211', 'ME 2213', 'ME 2215' ],
  'CREDIT': ['3','3','3','3','4']
})

cols = st.columns(9)

total_credit=19.75

page_names = [4,3.75,3.50,3.25,3.00,2.75,2.50,2.25,2.00,0]


stat =     cols[0].radio('Probability & Stat', page_names, index=1)
law =      cols[1].radio('Psychology & Law', page_names, index=1)
eee =      cols[2].radio('Electronics', page_names, index=1)
solid =    cols[3].radio('Mechanics of Solid', page_names, index=1)
heat =     cols[4].radio('Heat & Thermal', page_names, index=1)
cad =      cols[5].radio('AutoCad', page_names, index=1)
eeel =     cols[6].radio('Electrolics Lab', page_names, index=1)
solidl =   cols[7].radio('Mechanics Lab', page_names, index=1)
heatl =    cols[8].radio('Heat Lab', page_names, index=1)

gpa = (stat*3+ law*3+eee*3+solid*3+heat*4+cad*.75+eeel*.75+solidl*.75+heat*1.5)/total_credit

limit_gpa = round(gpa, 2)


st.write("GPA ::", limit_gpa)






