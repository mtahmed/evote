from pyramid.config   import Configurator
from pyramid.response import Response
from pyramid.view     import view_config

from . import auth

@view_config(route_name='main', renderer='templates/base.jinja2')
def main(request):
    '''View for the main landing page.
    '''
    template_data = dict()

    a = auth.Auth(user_id=request.remote_user)
    template_data['user_id'] = a.get_user_id()

    return template_data

@view_config(route_name='logout')
def logout(request):
    '''View for the logout page. Only redirects to the logout page.
    '''
    a = auth.Auth(user_id=request.remote_user)
    response = Response()

    return a.logout(response)

def make_wsgi_app():
    '''This function returns a Pyramid WSGI application.
    '''
    config = Configurator()

    # Routes
    config.add_route('main', '')
    config.add_route('logout', '/logout')

    # Scan decorated config.
    config.scan()

    # Enable jinja2 templating.
    config.include('pyramid_jinja2')

    return config.make_wsgi_app()
