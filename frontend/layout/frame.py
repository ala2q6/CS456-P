# import <
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from backend.resource import jsonLoad # remove
from frontend.layout.feed import feedFunction
from backend.resource import directory, application

# >


def frameFunction():
    '''  '''

    # local <
    frameData = jsonLoad(file = '/frontend/data/frame.json')
    frameStyle = jsonLoad(file = '/frontend/style/frame.json')

    # >

    return (

        # location <
        dcc.Location(id = 'locationId', refresh = False),

        # >

        # header <
        # divider <
        dbc.Row(

            justify = 'center',
            style = dict(

                **frameStyle['gRowStyle'],
                **frameStyle['headerRowStyle'],
                backgroundColor = frameStyle['gColorWhite']

            ),
            children = html.A(

                href = '/header',
                children = html.Img(

                    src = frameData['headerImgSrc'],
                    style = frameStyle['headerImgStyle']

                )

            )

        ),
        dividerFunction(pStyle = frameStyle),

        # >

        # navigation <
        dbc.Row(

            style = dict(

                **frameStyle['gRowStyle'],
                backgroundColor = frameStyle['gColorWhite']

            ),
            children = [

                dbc.Col(

                    className = 'd-grid gap-2',
                    children = dbc.Button(

                        href = f'/{k}',
                        children = k.replace('-', ' '),
                        color = frameStyle['gColorBlack'],
                        style = dict(

                            color = frameStyle['gColorBlack'],
                            **frameStyle['navigationButtonStyle'],
                            fontFamily = frameStyle['gFontFamily'],
                            backgroundColor = frameStyle['gColorWhite']

                        )

                    )

                )

            for k, v in frameData['navigationDict'].items()]

        ),

        # >

        # divider <
        # body <
        dividerFunction(pStyle = frameStyle),
        dbc.Row(

            id = 'bodyRowId',
            justify = 'center',
            style = dict(

                **frameStyle['gRowStyle'],
                backgroundColor = frameStyle['gColorWhite']

            )

        ),

        # >

        # divider <
        # footer <
        dividerFunction(pStyle = frameStyle),
        dbc.Row(

            justify = 'center',
            style = dict(

                **frameStyle['gRowStyle'],
                **frameStyle['footerRowStyle'],
                backgroundColor = frameStyle['gColorWhite']

            ),
            children = html.A(

                href = frameData['footerAHref'],
                children = html.Img(

                    src = frameData['footerImgSrc'],
                    style = frameStyle['footerImgStyle']

                )

            )

        ),

        # >

    )


@application.callback(

    Output('bodyRowId', 'children'),
    Input('locationId', 'pathname')

)
def frameCallback(pLocation: str) -> list:
    '''  '''

    # get data <
    # return feed <
    navData = jsonLoad(file = '/frontend/data/frame.json')['navigationDict']
    return feedFunction(pKey = pLocation, pData = navData)

    # >



def dividerFunction(pStyle: dict) -> list:
    '''  '''

    return dbc.Row(

        style = dict(

            **pStyle['gRowStyle'],
            backgroundColor = pStyle['gColorWhite']

        ),
        children = html.Hr(

            style = dict(

                **pStyle['gHrStyle'],
                backgroundColor = pStyle['gColorBlack']

            )

        )

    )