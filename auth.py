import os

class Auth:
    '''This class will provide the voter authentication.

    Right now it uses the uWaterloo CAS to provide authentication.
    '''
    CAS_LOGOUT_URL='https://cas.uwaterloo.ca/cas/logout'

    def __init__(self):
        self.user_id = os.environ['REMOTE_USER']
        # The user is denied if auth fails before they get here so the user must
        # already be authenticated.
        self.is_authed = True

    def get_user_id(self):
        return self.user_id

    def logout(self, response):
        '''Logout the currently logged in user.

        :param response: The Response object to be filled.
        '''
        response.location = self.CAS_LOGOUT_URL

        return response
