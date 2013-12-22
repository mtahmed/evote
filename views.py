from pyramid.config   import Configurator
from pyramid.response import Response
from pyramid.view     import view_config

from . import auth

@view_config(route_name='main', renderer='templates/main.jinja2')
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
