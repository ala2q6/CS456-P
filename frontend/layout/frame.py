# import <
from dash import html, dcc
import dash_bootstrap_components as dbc


from backend.resource import jsonLoad # remove

# >


# global <
frameStyle = jsonLoad(file = '/frontend/style/frame.json') # update

# >


def frameFunction():
    '''  '''

    return (

        html.H1('ok')

    )