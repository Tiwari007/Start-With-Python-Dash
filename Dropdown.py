import dash
from dash import dcc
from dash import html


app = dash.Dash()

app.layout = html.Div(
    children=[
        html.Label('Choose A City'),
        dcc.Dropdown(
            style ={"width": "80%", "margin":"0px auto"},
            id = "country_dropdown",
            options = [
                {"label": "New York City", "value": "NYC"},
                {"label": "San Francisco", "value": "SF"},
                {"label": "Tokyo City", "value": "TC", "disabled": True}
            ],
            # value= "NYC",
            # To choose multiple options from dropdown
            # multi = True,

            # placeholder
            placeholder="Select a city"
        )
    ]
)




if __name__ == "__main__":
    app.run_server(debug = True)