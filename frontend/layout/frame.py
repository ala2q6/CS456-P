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
        dbc.Row(

            justify = 'center',
            style = dict(

                **frameStyle['gRowStyle'],
                **frameStyle['headerRowStyle'],
                backgroundColor = frameStyle['gColorWhite']

            ),
            children = [

                # header <
                # divider <
                html.A(

                    href = '/',
                    children = html.Img(

                        src = frameData['headerImgSrc'],
                        style = frameStyle['headerImgStyle']

                    )

                ),
                html.Hr(style = dict(backgroundColor = frameStyle['gColorBlack']))

                # >

            ]

        ),

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
                    align = 'center',
                    style = {'backgroundColor' : '#FFFFFF'},
                    children = html.Button(

                        children = k,
                        style = {'display' : 'block'}

                    )

                    # children = dbc.Button(
                    #
                    #     href = v,
                    #     className = 'me-1',
                    #     children = k,
                    #     color = frameStyle['gColorBlack'],
                    #     style = {'backgroundColor' : '#FFFFFF'}
                    #
                    # )

                )

            for k, v in frameData['navigationDict'].items()]

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


# callback for link redirects here #