import streamlit as st

st.title('This is a title')

st.write('This is a **text** :books:')

st.button('Reset', type="primary")
if st.button('Say Hello'):
  st.write("Why Hello There")
else:
  st.write("Goodbye")