import streamlit as st

from database import query_db
from plot import plot_wells

def app():
    st.title('This is my app')
    
    st.markdown('This is text with **bold** and _italic_.')
    
    depth = st.number_input('Min depth', 0, 10000, value=5000, step=500)
    gradient = st.number_input('Min gradient', 0., 0.1, value=0.01, step=0.005,
                               format='%0.3f')
    
    st.write(f'Looking for depth of {depth} and gradient of {gradient}')
    
    data = query_db(depth, gradient)
    st.write(plot_wells(data))
    
if __name__ == '__main__':
    app()
