# Gapminder Panel App

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/panel-demos/gapminder/master?urlpath=/proxy/5006/app)

This repo contains:

- `environment.yml` installing bokeh and nbserverproxy
- a custom serverextension (`bokehserverextension.py`) that launches bokeh server
- a `postBuild` script to enable the server extensions and install the local one
  (this last step would go away if the local extension became a proper package)
- A [panel](https://github.com/pyviz/panel) displaying the gapminder data using a number of libraries
