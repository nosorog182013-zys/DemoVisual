import plotly.express as px

fig = px.bar(x=["a", "b", "c", "d", "e", "f"], y=[1, 3, 2, 7, 5, 4])
fig.write_html('first_figure.html', auto_open=True)
