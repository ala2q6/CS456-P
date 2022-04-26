# import <
from os import listdir
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from backend.resource import directory, application
from backend.resource import jsonLoad # remove

# >


# global <


# >


def frameFunction():
    '''  '''

    # local <
    frameData = jsonLoad(file = '/frontend/data/frame.json')
    frameStyle = jsonLoad(file = '/frontend/style/frame.json')

    # >

    return (

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

                href = '/',
                children = html.Img(

                    src = frameData['headerImgSrc'],
                    style = frameStyle['headerImgStyle']

                )

            )

        ),
        dividerFunction(gStyle = frameStyle),

        # >

        # navigation <
        dbc.Row(

            justify = 'between',
            style = dict(

                **frameStyle['gRowStyle'],
                backgroundColor = frameStyle['gColorWhite']

            ),
            children = [

                dbc.Col(

                    className = 'd-grid gap-2',
                    children = dbc.Button(

                        children = k,
                        color = frameStyle['gColorBlack'],
                        style = dict(

                            href = v,
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
        dividerFunction(gStyle = frameStyle),
        dbc.Row(

            id = 'bodyRowId',
            justify = 'center',
            style = dict(

                **frameStyle['gRowStyle'],
                backgroundColor = frameStyle['gColorWhite']

            ),
            children = dbc.Col(

                id = 'bodyColId',
                style = frameStyle['bodyColStyle']

            )

        ),

        # >

        # divider <
        # footer <
        dividerFunction(gStyle = frameStyle),
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

#


def dividerFunction(gStyle: dict) -> list:
    '''  '''

    return dbc.Row(

        style = dict(

            **gStyle['gRowStyle'],
            backgroundColor = gStyle['gColorWhite']

        ),
        children = html.Hr(

            style = dict(

                **gStyle['gHrStyle'],
                backgroundColor = gStyle['gColorBlack']

            )

        )

    )