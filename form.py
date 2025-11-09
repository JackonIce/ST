import streamlit as st

st.title("User Information Form")
st.snow()
st.balloons()

form_values = {
    "name": None,
    "age": None
}

with st.form(key="Mein Form", clear_on_submit=True):
    form_values["name"] = st.text_input("Enter your name")
    form_values["age"] = st.number_input("Enter your Age")
    submitted = st.form_submit_button("Submit")
    print(form_values["name"], form_values["age"])
    if submitted:
        if not all(form_values.values()):
            st.warning("Please fill in all fields.")
        else:
            st.success("Form submitted successfully!")
            st.write("## Info")
            st.write(f"Name: {form_values['name']}")
