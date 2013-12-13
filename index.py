#!/users/mtahmed/bin/python
import cgitb
cgitb.enable

import sys
sys.path.append('/users/mtahmed/.local/lib/python3.3/site-packages')

from pyramid.config   import Configurator
from pyramid.response import Response
from pyramid.view     import view_config

'''
import auth
'''

@view_config(route_name='main')
def main(request):
    response = Response("hello world!")
    response.content_type = 'text/plain'
    return response

@view_config(route_name='logout')
def logout(request):
    import auth
    a = auth.Auth()
    response = Response()
    return a.logout(response)

def make_evote_app():
    '''This function returns a Pyramid WSGI application.
    '''
    config = Configurator()

    # Routes
    config.add_route('main', '')
    config.add_route('logout', '/logout')

    # Scan decorated config
    config.scan()

    return config.make_wsgi_app()

if __name__ == '__main__':
    import wsgiref.handlers
    app = make_evote_app()
    wsgiref.handlers.CGIHandler().run(make_evote_app())
