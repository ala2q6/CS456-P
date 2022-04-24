# import <
import dash_bootstrap_components as dbc

# >

from backend.resource import jsonLoad
frameStyle = jsonLoad(file = '/frontend/resource/style.json')


application.layout = dbc.Container(

    fluid = True,
    style = style['containerStyle'],
    children = [

        html.H1("ok")

    ]

)