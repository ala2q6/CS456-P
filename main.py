# import <
from requests import get
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from frontend.layout.frame import frameFunction
from backend.resource import server, application, bootLink

# >


def mainFunction() -> tuple:
    '''  '''

    # get frame data <
    # get frame style <
    frameData = get(bootLink).json()
    frameStyle = get(frameData['frameStyle']).json()

    # >

    # filter data <
    del frameData['navigationDict']['Default']

    # >

    return (

        # children <
        # style <
        frameFunction(

            pData = frameData,
            pStyle = frameStyle

        ),
        dict(

            **frameStyle['containerStyle'],
            backgroundColor = frameStyle['gColorBlack']

        )

        # >

    )

    # # if (children) then return list <
    # # elif (style) then return dict <
    # if (pProperty == 'children'): return frameFunction()
    # elif (pProperty == 'style'):
    #
    #     # load style <
    #     # return style <
    #     frameStyle = jsonLoad(file = '/frontend/style/frame.json')
    #     return dict(
    #
    #         **frameStyle['containerStyle'],
    #         backgroundColor = frameStyle['gColorBlack']
    #
    #     )
    #
    #     # >
    #
    # # >


# main <
if (__name__ == '__main__'):

    # boot <
    # set layout <
    # run application <
    mainChildren, mainStyle = mainFunction()
    application.layout = dbc.Container(

        fluid = True,
        style = mainStyle,
        id = 'containerId',
        children = mainChildren,

    )

    application.run_server(debug = True)

    # >

# >