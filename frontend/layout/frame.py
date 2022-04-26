# import <
from os import listdir
from dash import html, dcc
import dash_bootstrap_components as dbc

from backend.resource import directory
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

            justify = 'evenly',
            style = dict(

                **frameStyle['gRowStyle'],
                backgroundColor = frameStyle['gColorWhite']

            ),
            children = [

                dbc.Col(

                    width = 'auto',
                    children = dbc.Button(

                        children = k,
                        color = frameStyle['gColorBlack']

                    )

                )

            for k, v in frameData['navigationDict'].items()]

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

        )

        # >

    )


# callback for link redirects here #


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