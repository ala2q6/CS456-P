# import <
from os import path
from dash import Dash
from dash_bootstrap_components import themes

# >


# global <
realpath = path.realpath(__file__)
directory = ('/'.join(realpath.split('/')[:-2]))
bootLink = 'https://raw.githubusercontent.com/ala2q6/CS456-P/main/frontend/data/frame.json'
application = Dash(

    suppress_callback_exceptions = True,
    external_stylesheets = [themes.GRID]

)
server = application.server

# >