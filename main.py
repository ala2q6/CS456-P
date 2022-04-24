# import <
from dash import html, dcc
import dash_bootstrap_components as dbc

from backend.resource import application, server

# >


# main <
if (__name__ == '__main__'): application.run_server(debug = True)

# >