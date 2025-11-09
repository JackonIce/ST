import streamlit as st
import pandas as pd
import os
import time
import matplotlib.pyplot as plt
import altair as alt
import plotly.express as px
from bokeh.plotting import figure

# --- Grundelemente ---
st.write({"name": "value"})
st.write(123)

pressed = st.button("Press me")
print('First:', pressed)

pressed2 = st.button("Press me 2")
print('Second:', pressed2)

st.title("My Streamlit App")
st.header("This is a header")
st.subheader("This is a subheader")
st.markdown("This is a **markdown** text with *formatting*.")
st.caption("small test")

code_example = """
def greet(name):
    print('hello', name)
"""
st.code(code_example, language='python')
st.divider()

# --- Bild ---
img_path = os.path.join(os.getcwd(), "static", "bg.jpg")
if os.path.exists(img_path):
    st.image(img_path)
else:
    st.info(f"Bild nicht gefunden: {img_path}")

# --- DataFrame ---
st.subheader("Data Editor")
df = pd.DataFrame({
    'Column 1': [1, 2, 3, 4],
    'Column 2': ['A', 'B', 'C', 'D']
})
editable_df = st.data_editor(df)
print(editable_df)

# --- Metrics ---
st.subheader("Metrics")
st.metric(label="Total Rows", value=len(df))

# --- Eingebaute Charts ---
st.area_chart(df.set_index('Column 2')['Column 1'])
st.bar_chart(df.set_index('Column 2')['Column 1'])
st.line_chart(df.set_index('Column 2')['Column 1'])

# --- Karte ---
st.map(pd.DataFrame({
    'lat': [37.76, 37.77, 37.78],
    'lon': [-122.40, -122.41, -122.42]
}))

# --- Matplotlib ---
fig, ax = plt.subplots()
ax.plot(df['Column 1'], df['Column 1'], marker='o')
ax.set_xlabel('Column 1')
ax.set_ylabel('Value')
ax.set_title('Matplotlib Line')
st.pyplot(fig)

# --- Vega-Lite ---
st.vega_lite_chart(
    df,
    {
        'mark': 'point',
        'encoding': {
            'x': {'field': 'Column 1', 'type': 'quantitative'},
            'y': {'field': 'Column 2', 'type': 'nominal'}
        }
    },
    use_container_width=True
)

# --- Altair ---
chart = alt.Chart(df).mark_bar().encode(x='Column 2', y='Column 1')
st.altair_chart(chart, use_container_width=True)

# --- Plotly ---
fig_plotly = px.bar(df, x='Column 2', y='Column 1', title='Plotly Bar')
st.plotly_chart(fig_plotly, use_container_width=True)

# --- Bokeh ---
bk = figure(title="Bokeh VBar", x_range=list(df['Column 2']))
bk.vbar(x=df['Column 2'], top=df['Column 1'], width=0.6)
st.bokeh_chart(bk, use_container_width=True)

# --- Graphviz ---
st.graphviz_chart("""
    digraph {
        A -> B
        B -> C
        C -> A
    }
""")

# --- Echo (Kontextmanager) ---
with st.echo():
    st.write("Diese Zeile wird ausgeführt und gleichzeitig als Code angezeigt.")

# --- LaTeX ---
st.latex(r"E = mc^2")

# --- JSON ---
st.json({
    "name": "Streamlit",
    "type": "Web Framework",
    "language": "Python"
})

# --- Fun-Elemente ---
st.snow()
st.balloons()

# --- Fortschrittsbalken ---
progress = st.progress(0)
for i in range(0, 101, 20):
    time.sleep(0.1)
    progress.progress(i)

# --- Spinner (Kontextmanager) ---
with st.spinner("Loading..."):
    time.sleep(0.5)
st.success("Fertig!")

