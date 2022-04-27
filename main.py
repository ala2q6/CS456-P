# import <
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from backend.resource import jsonLoad # remove
from frontend.layout.frame import frameFunction
from backend.resource import server, application

# >


def mainFunction(pKey: str):
    '''  '''

    # if (children) then return list <
    # elif (style) then return dict <
    if (pKey == 'children'): return frameFunction()
    elif (pKey == 'style'):

        # load style <
        # return style <
        frameStyle = jsonLoad(file = '/frontend/style/frame.json')
        return dict(

            **frameStyle['containerStyle'],
            backgroundColor = frameStyle['gColorBlack']

        )

        # >

    # >


# main <
if (__name__ == '__main__'):

    # set layout <
    # run <
    application.layout = dbc.Container(

        fluid = True,
        id = 'containerId',
        style = mainFunction('style'),
        children = mainFunction('children')

    )

    application.run_server(debug = True)

    # >

# >