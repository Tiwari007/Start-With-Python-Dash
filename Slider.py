import dash
from dash import html, dcc

app = dash.Dash()

app.layout = html.Div(
    className = "slider",
    children = [
        html.Label('Slider'),
        dcc.Slider(
            # name='Polynomial Degree',
            # id='slider-polynomial-degree',
            min=1,
            max=10,
            step=.5,
            value=1,
            marks={i: str(i) for i in range(1, 11)},

    )
])

if __name__ == "__main__":
    app.run_server(debug= True)