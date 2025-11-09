import streamlit as st

counter = 0



if "counter" not in st.session_state:
    st.session_state.counter = 0

if st.button("Increase Counter"):
    st.session_state.counter += 1
    st.write(f"Counter value: {st.session_state.counter}")
else:
    st.write(f" Counter stays at {st.session_state.counter}")

if st.button("Reset Counter"):
    st.session_state.counter = 0
    st.write("Counter reset to 0")



