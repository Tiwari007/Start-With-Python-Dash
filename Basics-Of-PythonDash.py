import dash
from dash import dcc
from dash import html


app = dash.Dash()

colors = {
    "text" : "gray",
    "plot" : "pink",
    "paper": "skyblue"
}

app.layout = html.Div( 
        children= [
            html.H1("Dashboard"),
            html.P("Welcom to plotly Dashboard apllication"),


            dcc.Graph(
                id = 'Sample-Bar-Graph',
                figure= {
                    'data': [
                        { 'x' : [12, 14, 15, 16], 'y': [23, 25, 26, 27], 'type': 'bar', 'name': 'First Chart' },
                        { 'x' : [12, 14, 15, 16], 'y': [24, 25, 22, -5], 'type': 'line', 'name': 'Second Chart'}
                    ],
                    'layout' : {
                        'plot_bgcolor': colors["plot"],
                        'paper_bgcolor': colors["paper"],
                        'font': {
                            'color': colors["text"]
                            },
                            'title': 'Simple Bar Chart',
                    },
                },
            ),

            dcc.Graph(
                id = 'Sample-Pie-Graph',
                figure= {
                    'data': [
                        { 'x' : [12, 14, 15, 16], 'y': [1798, 1808, 1916, 2023], 'type': 'bar', 'name': 'First Chart' }
                    ],
                    'layout' : {
                        'title': 'Simple Pie Chart',
                        'xaxis': {'title': 'Quantity'},
                        'yaxis': {'title': 'year'}
                    }
                }
            )

        ],
        style={ "textAlign": "center" }
    )




if __name__ == "__main__":
    app.run_server(debug= True)

