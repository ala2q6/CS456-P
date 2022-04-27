# import <
from requests import get
from json import load # remove
from dash import html, dcc
import dash_bootstrap_components as dbc

from backend.resource import directory, application

# >


with open(f'{directory}/frontend/style/feed.json', 'r') as f: # remove

    feedStyle = load(f) # remove


def feedFunction(pKey: str, pData: dict, pStyle) -> list:
    '''  '''

    # if (button) then subject else then default <
    # init output list and get data <
    data = pKey if (pKey in pData['navigationDict'].keys()) else 'Default'
    outputList, feedData = [], get(pData['navigationDict'][data]).json()

    # >

    # iterate element in data <
    for k, v in feedData.items():

        pass
        # header
        # subheader
        # subject
        # text

        # image

        # https://dash-bootstrap-components.opensource.faculty.ai/docs/components/card/

    # >

    return outputList