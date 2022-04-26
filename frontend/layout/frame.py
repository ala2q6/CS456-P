# import <
from dash import html, dcc
import dash_bootstrap_components as dbc

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

        # logo <
        dbc.Row(

            justify = 'center',
            style = dict(

                **frameStyle['gRowStyle'],
                **frameStyle['logoRowStyle'],
                backgroundColor = frameStyle['gColorWhite']

            ),
            children = [

                # logo <
                # divider <
                html.A(

                    href = '/',
                    children = html.Img(

                        src = frameData['logoImgSrc'],
                        style = frameStyle['logoImgStyle']

                    )

                ),
                html.Hr(style = dict(backgroundColor = frameStyle['gColorBlack']))

                # >

            ]

        ),

        # >

        # footer <
        dbc.Row(

            justify = 'center',
            style = dict(

                **frameStyle['gRowStyle'],
                **frameStyle['footerRowStyle'],
                backgroundColor = frameStyle['gColorWhite']

            ),
            children = [

                # divider <
                # footer <
                html.Hr(style = dict(backgroundColor = frameStyle['gColorBlack'])),
                html.A(

                    href = frameData['footerAHref'],
                    children = html.Img(

                        src = frameData['footerImgSrc'],
                        style = frameStyle['footerImgStyle']

                    )

                )

                # >

            ]

        )

        # >

    )