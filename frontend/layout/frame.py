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

    return [

        # logo <
        dbc.Row(

            #
            dbc.Row(

                justify = 'center',
                style = {'backgroundColor' : "rgb(248, 240, 227)"},
                children = [

                    dbc.Col(

                        children = [

                            dbc.Col(html.H1('ok')),
                            dbc.Col(html.H1('ok')),
                            dbc.Col(html.H1('ok'))

                        ]

                    )

                ]

            )

        ),

        # >

        # footer <
        dbc.Row(

            #

        )

        # >

    ]