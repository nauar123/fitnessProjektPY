import streamlit as st


st.title("Fitness tracker")


name = "Nauar"
st.write(f"Velkommen, {name}!") 


#funktionerne i appen
#st.markdown bruges til at formatere teksten i markdown format, som gør det nemmere at læse og forstå.
st.markdown( """
              
* Register øvelser 
* Se vægt og gentagelser
* Følg din udvikling over tid
""")


