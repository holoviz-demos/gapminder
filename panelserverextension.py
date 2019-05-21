from subprocess import Popen

def load_jupyter_server_extension(nbapp):
    """serve the gapminder.ipynb directory with bokeh server"""
    Popen(["panel", "serve", "gapminder.ipynb", "--allow-websocket-origin=*"])
