# import <
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from backend.resource import jsonLoad # remove
from frontend.layout.frame import frameFunction
from backend.resource import server, application

# >


# global <
application.layout = dbc.Container(

    fluid = True,
    id = 'containerId'

)

# >


@application.callback(

    Output('containerId', 'style'),
    Output('containerId', 'children'),
    Input('containerId', 'children')

)
def mainCallback(pContainerChildren: None) -> (list, dict):
    '''  '''

    # local <
    frameStyle = jsonLoad(file = '/frontend/style/frame.json')

    # >

    return (

        # style <
        # children <
        dict(

            frameStyle['containerStyle'],
            backgroundColor = frameStyle['gColorBlack']

        ),
        frameFunction(),
        # dcc.Location(id = 'locationId')

        # >

    )


# main <
if (__name__ == '__main__'): application.run_server(debug = True)

# >