# import <
from os import path
from dash import Dash
from json import load, dump
import dash_bootstrap_components as dbc

# >

# global <
realpath = path.realpath(__file__)
directory = ('/'.join(realpath.split('/')[:-2]))
application = Dash(

    suppress_callback_exceptions = True,
    external_stylesheets=[dbc.themes.GRID]

)
server = application.server

# >


def jsonLoad(file: str) -> dict:
    '''  '''

    # read file <
    # get data <
    with open(f'{directory}{file}', 'r') as fileIn:

        return load(fileIn)

    # >