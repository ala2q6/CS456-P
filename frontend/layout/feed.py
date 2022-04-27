# import <
from dash import html, dcc
import dash_bootstrap_components as dbc

from backend.resource import directory, application
from backend.resource import jsonLoad # remove

# >


def feedFunction(pKey: str, pData: dict) -> list:
    '''  '''

    # local <
    linkStr = pData[pKey] if (pKey in pData.keys()) else pData['default']

    # >

    return (



    )