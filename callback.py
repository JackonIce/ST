import streamlit as st

if "step" not in st.session_state:
    st.session_state.step = 1

if "info" not in st.session_state:
    st.session_state.info = {}

if st.session_state.step == 1:
    st.header("Part 1: Info")

    name =st.text_input("Name", value=st.session_state.info.get("name", ""))

    if st.button("Next"):
        st.session_state.info["name"] = name
        st.session_state.step = 2



elif st.session_state.step == 2:
    st.header("Part 2: Review")
    st.subheader("Please review your information:")
    st.write(f"Name: {st.session_state.info.get('name', '')}")
    
    if st.button("Submit"):
        st.success("Form submitted successfully!")
        st.balloons()
        st.session_state.step = 1
        st.session_state.info = {}

