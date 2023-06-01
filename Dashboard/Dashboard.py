import dash
from dash import html, dcc

external_stylesheets = [
    'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.3.0/css/all.min.css'
]


app = dash.Dash(__name__, external_stylesheets=external_stylesheets, meta_tags = [
    {
        'name': 'description',
        'content': 'dashboard for showing data. where you can interact with datas and charts.'
    },
    {
        'name': 'author',
        'content': 'BuckyAlita'
    },
    {
        'charset': 'utf-8'
    }
], title="Dashboard")

colors = {
    "text" : "gray",
    "plot" : "pink",
    "paper": "skyblue"
}


app.layout = html.Div(
    children = [
        #  Header
        html.Div(
            className = 'dashbord--header',
            children = html.Div(
                className = 'dashbord--header--Navigation',
                children = [
                    html.A("Home"),
                    html.A("Player"),
                    html.A("Level"),
                    html.A("About Game"),
                    html.A("Boss Level"),
            ]
        )
        ),

        # ScoreBoard
        html.Div(
            className = 'dashboard--scoreboard',
            children = html.H1(
                children = "Points Table"
            )
        ),

        # Graph
        html.Div(
            className = 'dashboard--graph',
            children = [
                dcc.Graph(
                id = 'Points-table-line',
                figure= {
                    'data': [
                        { 'x' : ["Vivek", "Rohan", "Piya", "Alita"], 'y': [44, 67, 83, 92], 'type': 'line', 'name': 'Scoreboard' },
                        # { 'x' : [12, 14, 15, 16], 'y': [24, 25, 22, -5], 'type': 'line', 'name': 'Second Chart'}
                    ],
                    'layout' : {
                        # 'plot_bgcolor': colors["plot"],
                        # 'paper_bgcolor': colors["paper"],
                        # 'font': {
                        #     'color': colors["text"]
                        #     },
                            'title': 'Points',
                            'xaxis': {'title': 'name'},
                            'yaxis': {'title': 'points'}
                    },
                },
            ),
            dcc.Graph(
                id = 'points-table-bar',
                figure= {
                    'data': [
                        { 'x' : ["Vivek", "Rohan", "Piya", "Alita"], 'y': [44, 67, 83, 92], 'type': 'bar', 'name': 'Scoreboard' },
                        # { 'x' : [12, 14, 15, 16], 'y': [24, 25, 22, -5], 'type': 'line', 'name': 'Second Chart'}
                    ],
                    'layout' : {
                        # 'plot_bgcolor': colors["plot"],
                        # 'paper_bgcolor': colors["paper"],
                        # 'font': {
                        #     'color': colors["text"]
                        #     },
                            'title': 'Points',
                            'xaxis': {'title': 'name'},
                            'yaxis': {'title': 'points'}
                    },
                },
            )
            ]
        ),

        # Table
        # html.Div(
        #     className = 'dashboard--table',
        #     children = "Main Container"
        # ),

        # Footer
    html.Footer(
        className = "dashboard--footer",
            id="contact_us",
            children=[
                html.Ul(
                    className="wrapper",
                    children=[
                        html.Li(
                            className="icon discord",
                            children=[
                                html.Span(className="tooltip", children="Discord"),
                                html.A(
                                    href="#",
                                    target="_blank",
                                    children=[html.Span(html.I(className="fab fa-discord"))]
                                )
                            ]
                        ),
                        html.Li(
                            className="icon twitter",
                            children=[
                                html.Span(className="tooltip", children="Twitter"),
                                html.A(
                                    href="#",
                                    target="_blank",
                                    children=[html.Span(html.I(className="fab fa-twitter"))]
                                )
                            ]
                        ),
                        html.Li(
                            className="icon instagram",
                            children=[
                                html.Span(className="tooltip", children="Instagram"),
                                html.A(
                                    href="#",
                                    target="_blank",
                                    children=[html.Span(html.I(className="fab fa-instagram"))]
                                )
                            ]
                        ),
                        html.Li(
                            className="icon github",
                            children=[
                                html.Span(className="tooltip", children="Github"),
                                html.A(
                                    href="#",
                                    target="_blank",
                                    children=[html.Span(html.I(className="fab fa-github"))]
                                )
                            ]
                        ),
                        html.Li(
                            className="icon youtube",
                            children=[
                                html.Span(className="tooltip", children="Youtube"),
                                html.A(
                                    href="#",
                                    target="_blank",
                                    children=[html.Span(html.I(className="fab fa-youtube"))]
                                )
                            ]
                        )
                    ]
                ),
                html.Div(
                    className="footer--menu",
                    children=[
                        html.P(
                            children=[
                                html.Span("Home"),
                                " / ",
                                html.Span("Level"),
                                " / ",
                                html.Span("Player"),
                                " / ",
                                html.Span("About Game"),
                                " / ",
                                html.Span("Boss Level")
                            ]
                        )
                    ]
                ),
                html.Div(
                    className="footer-copyright",
                    children=[
                        html.P("© 2023 BuckyAlita. All Rights Reserved.")
                    ]
                )
            ]
        )
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
