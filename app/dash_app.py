import pandas as pd
import dash
from dash import dcc
from dash import html
import plotly.express as px
from dash.dependencies import Input, Output
import dash_table

data_path = "../Data/Parks_and_Open_Space_20240311.csv"
df = pd.read_csv(data_path)

# Create the Dash app
app = dash.Dash(__name__)

# Create a plotly express bar chart
fig = px.bar(df.head(20), x="Park Name", y=["Total Area in Hectares", "Water Area in Hectares", "Land Area in Hectares"],
             title="Park Areas Comparison", barmode='group')

# App layout including the table and the graph
app.layout = html.Div(children=[
    html.H1('Interactive API 2'),
        html.H2('Showing Data Set using Dash'),
        html.P('This is a simple web application that allows you to see dataset from a CSV file using Dash.'),
    
    html.H2(children='Park Information and Areas Comparison'),
    
    html.H3(children='Park Data Table'),
    dash_table.DataTable(
        id='table',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.head(20).to_dict('records'),
        style_table={'height': '300px', 'overflowY': 'auto'}
    ),
    
    html.H3(children='Park Areas Graph'),
    dcc.Graph(
        id='graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)