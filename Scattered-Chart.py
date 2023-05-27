import dash
from dash import dcc
from dash import html
import numpy as np
import plotly.graph_objs as go


app = dash.Dash()

colors = {
    "text" : "gray",
    "plot" : "pink",
    "paper": "skyblue"
}


np.random.seed(50)
x_rand = np.random.randint(1, 61, 60)
y_rand = np.random.randint(1, 61, 60)


app.layout = html.Div( 
        children= [
            html.H1("Dashboard"),
            html.P("Welcom to plotly Dashboard apllication"),


            dcc.Graph(
                id = 'Scattered Chart',
                figure= {
                    'data': [
                        go.Scatter(
                            x = x_rand,
                            y = y_rand,
                            mode = 'markers'
                        )
                    ],
                    'layout': go.Layout(
                        title= 'Scattered plot of random 60 points',
                        xaxis= {'title': 'Random X'},
                        yaxis= {'title': 'Random Y'}
                    )
                }
            ),

        ],
        style={ "textAlign": "center" }
    )




if __name__ == "__main__":
    app.run_server(debug= True)

