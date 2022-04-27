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

        # location <
        dcc.Location(id = 'locationId'),

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

                href = '/',
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

            justify = 'evenly',
            style = dict(

                **frameStyle['gRowStyle'],
                backgroundColor = frameStyle['gColorWhite']

            ),
            children = [

                dbc.Col(

                    # width = 'auto',
                    # align = 'center',
                    className = 'd-grid gap-2',
                    children = dbc.Button(

                        href = k,
                        color = frameStyle['gColorBlack'],
                        children = k.replace('-', ' '),
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

            ),
            children = dbc.Col(

                id = 'bodyColId',
                style = frameStyle['bodyColStyle']

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

    Output('bodyColId', 'children'),
    Input('locationId', 'pathname')

)
def frameCallback(pLocationPathname):
    '''  '''

    print(pLocationPathname) # remove

    return (

        html.H1('ok')

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