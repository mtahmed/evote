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
    
@view_config(route_name='vote', renderer='templates/vote.jinja2')
def vote(request):    
    '''View for Voting page
    - Answer the available questions
    - Verify the answers
    - Cast vote
    '''
    template_data = dict()
    
    a = auth.Auth(user_id=request.remote_user)
    template_data['user_id'] = a.get_user_id()
    
    return template_data
    
@view_config(route_name='create-election', renderer='templates/create-election.jinja2')
def create_election(request):
    '''View for Create election page (this will be an admin page):
    - this page will provide an interface to add new questions for the ballot,
    - select voters list (no idea how this should be done yet, input from others would be nice)
    - set vote period ending date/time
    - add election officers (those who can admin the election)
    - start election
    '''
    template_data = dict()
    
    a = auth.Auth(user_id=request.remote_user)
    template_data['user_id'] = a.get_user_id()
    
    return template_data
