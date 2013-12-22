from pyramid.config   import Configurator
from pyramid.response import Response
from pyramid.view     import view_config

from . import views

def make_wsgi_app():
    '''This function returns a Pyramid WSGI application.
    '''
    config = Configurator()
    
    # Static files
    config.add_static_view(name='static', path='evote:static')
    
    # Routes
    config.add_route('main', '')
    config.add_route('logout', '/logout')

    # Scan decorated config.
    config.scan()

    # Enable jinja2 templating.
    config.include('pyramid_jinja2')

    return config.make_wsgi_app()
