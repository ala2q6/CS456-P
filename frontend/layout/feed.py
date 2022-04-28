# import <
from requests import get
from dash import html, dcc
import dash_bootstrap_components as dbc

from backend.resource import directory, application

# >


def imageFunction(v: dict, feedStyle: dict, frameStyle: dict):
    '''  '''

    return dbc.CardImg(

        src = v,
        style = dict(

            **feedStyle['gCardBodyStyle'],
            backgroundColor = frameStyle['gColorBlack']

        )

    )


def linkFunction(v: dict, feedStyle: dict, frameStyle: dict):
    '''  '''

    return dbc.CardLink(

        href = v['href'],
        children = v['name'],
        style = dict(

            **feedStyle['linkStyle'],
            **feedStyle['gCardBodyStyle'],
            color = frameStyle['gColorWhite'],
            fontFamily = frameStyle['gFontFamily'],
            backgroundColor = frameStyle['gColorBlack']

        )

    )


def bodyFunction(v: dict, feedStyle: dict, frameStyle: dict):
    '''  '''

    return dbc.CardBody(

        style = dict(

            **feedStyle['gCardBodyStyle'],
            backgroundColor = frameStyle['gColorBlack']

        ),
        children = [

            # title <
            # subtitle <
            # text <
            html.H4(

                children = v['title'],
                style = dict(

                    **feedStyle['titleStyle'],
                    color = frameStyle['gColorWhite'],
                    fontFamily = frameStyle['gFontFamily'],
                    backgroundColor = frameStyle['gColorBlack']

                )

            ),
            html.H6(

                children = v['subtitle'],
                style = dict(

                    **feedStyle['subtitleStyle'],
                    color = frameStyle['gColorWhite'],
                    fontFamily = frameStyle['gFontFamily'],
                    backgroundColor = frameStyle['gColorBlack']

                )

            ),
            html.P(

                children = v['text'],
                style = dict(

                    **feedStyle['textStyle'],
                    color = frameStyle['gColorWhite'],
                    fontFamily = frameStyle['gFontFamily'],
                    backgroundColor = frameStyle['gColorBlack']

                )

            )

            # >

        ]

    )


def feedFunction(pKey: str, pData: dict, pStyle: dict) -> list:
    '''  '''

    # if (button) then subject else then default <
    # init output list and get feed data <
    # get frame style <
    data = pKey if (pKey in pData['navigationDict'].keys()) else 'Default'
    outputList, feedData = [], get(pData['navigationDict'][data]).json()
    frameStyle = get(pData['frameStyle']).json()

    # >

    # header <
    outputList.append(dbc.CardHeader(style = dict(

        **pStyle['gCardBodyStyle'],
        **pStyle['cardHeaderStyle'],
        backgroundColor = frameStyle['gColorBlack']

    )))

    # >

    # body <
    # iterate element in data <
    for k, v in feedData.items():

        # if (body) <
        # if (link) <
        # if (image) <
        if ('body' in k): outputList.append(bodyFunction(v, pStyle, frameStyle))
        if ('link' in k): outputList.append(linkFunction(v, pStyle, frameStyle))
        if ('image' in k): outputList.append(imageFunction(v, pStyle, frameStyle))

        # >

    # >

    # footer <
    outputList.append(dbc.CardFooter(style = dict(

        **pStyle['gCardBodyStyle'],
        **pStyle['cardFooterStyle'],
        backgroundColor = frameStyle['gColorBlack']

    )))

    # >

    return outputList