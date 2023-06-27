import dash
from dash import html, dcc

app = dash.Dash()

app.layout = html.Div(
    className = "input__fields",
    children = [
        html.Label("Enter Your Name: "),
        dcc.Input(
        placeholder = 'Name',
        type = 'text',
        value = ""
    ),
    html.Br(),
    html.Label("Enter Your Message: "),
        dcc.Textarea(
        placeholder = 'Your Message',
        value = "",
        style = {'width' : '50%'}
    ),
    html.Br(),
    html.Br(),
    html.Button('Submit', id= 'submit-form')
    
    ]
)


if __name__ == "__main__":
    app.run_server(debug = True)