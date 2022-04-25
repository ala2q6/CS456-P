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

    fluid = 'sm',
    id = 'containerId'

)

# >


@application.callback(

    Output('containerId', 'style'),
    Output('containerId', 'children'),
    Input('containerId', 'children')

)
def mainCallback(containerChildren: None):
    '''  '''

    # local <
    frameStyle = jsonLoad(file = '/frontend/style/frame.json')

    # >

    return (

        # style <
        # children <
        dict(

            frameStyle['containerStyle'],
            backgroundColor = frameStyle['gColorWhite']

        ),
        frameFunction()

        # >

    )


# main <
if (__name__ == '__main__'): application.run_server(debug = True)

# >