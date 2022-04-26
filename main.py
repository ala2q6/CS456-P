# import <
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from frontend.layout.frame import frameFunction
from backend.resource import application, server

from backend.resource import jsonLoad # remove

# >


# global <
application.layout = dbc.Container(

    id = 'containerId',
    children = [

        dbc.Row(

            justify = 'center',
            children = [

                dbc.Col(html.Div('ok')),
                dbc.Col(html.Div('ok')),
                dbc.Col(html.Div('ok'))

            ]

        )

    ]

)

# >


# @application.callback(
#
#     Output('containerId', 'style'),
#     Output('containerId', 'children'),
#     Input('containerId', 'children')
#
# )
# def mainCallback(containerChildren: None) -> (list, dict):
#     '''  '''
#
#     # local <
#     frameStyle = jsonLoad(file = '/frontend/style/frame.json')
#
#     # >
#
#     return (
#
#         # style <
#         # children <
#         dict(
#
#             frameStyle['containerStyle'],
#             backgroundColor = frameStyle['gColorBlack']
#
#         ),
#         frameFunction()
#
#         # >
#
#     )


# main <
if (__name__ == '__main__'): application.run_server(debug = True)

# >