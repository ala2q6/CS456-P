# import <
from requests import get
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from frontend.layout.feed import feedFunction
from backend.resource import directory, application, bootLink

# >


def frameFunction(pData: dict, pStyle: dict):
    '''  '''

    return (

        # location <
        dcc.Location(id = 'locationId'),

        # >

        # header <
        # divider <
        dbc.Row(

            justify = 'center',
            style = dict(

                **pStyle['gRowStyle'],
                **pStyle['headerRowStyle'],
                backgroundColor = pStyle['gColorWhite']

            ),
            children = html.A(

                href = '/',
                children = html.Img(

                    src = pData['headerImgSrc'],
                    style = pStyle['headerImgStyle']

                )

            )

        ),
        dividerFunction(pStyle = pStyle),

        # >

        # navigation <
        dbc.Row(

            style = dict(

                **pStyle['gRowStyle'],
                backgroundColor = pStyle['gColorWhite']

            ),
            children = [

                dbc.Col(

                    className = 'd-grid gap-2',
                    children = dbc.Button(

                        href = f'/{k}',
                        children = k.replace('-', ' '),
                        color = pStyle['gColorBlack'],
                        style = dict(

                            color = pStyle['gColorBlack'],
                            **pStyle['navigationButtonStyle'],
                            fontFamily = pStyle['gFontFamily'],
                            backgroundColor = pStyle['gColorWhite']

                        )

                    )

                )

            for k, v in pData['navigationDict'].items()]

        ),

        # >

        # divider <
        # body <
        dividerFunction(pStyle = pStyle),
        dbc.Row(

            id = 'bodyRowId',
            justify = 'center',
            style = dict(

                **pStyle['gRowStyle'],
                backgroundColor = pStyle['gColorWhite']

            )

        ),

        # >

        # divider <
        # footer <
        dividerFunction(pStyle = pStyle),
        dbc.Row(

            justify = 'center',
            style = dict(

                **pStyle['gRowStyle'],
                **pStyle['footerRowStyle'],
                backgroundColor = pStyle['gColorWhite']

            ),
            children = html.A(

                href = pData['footerAHref'],
                children = html.Img(

                    src = pData['footerImgSrc'],
                    style = pStyle['footerImgStyle']

                )

            )

        ),

        # >

    )


@application.callback(

    Output('bodyRowId', 'children'),
    Input('locationId', 'pathname')

)
def frameCallback(pKey: str) -> list:
    '''  '''

    # get frame data <
    # get feed style <
    frameData = get(bootLink).json()
    feedStyle = get(frameData['feedStyle']).json()

    # >

    return feedFunction(

        pData = frameData,
        pStyle = feedStyle,
        pKey = pKey.replace('/', '')

    )


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