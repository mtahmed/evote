import os


class Auth:
    '''This class will provide the voter authentication.

    Right now it uses the uWaterloo CAS to provide authentication.
    '''
    def __init__(self):
        self.user_id = os.environ['REMOTE_USER']
        # The user is denied if auth fails before they get here so the user must
        # already be authenticated.
        self.is_authed = True

    def get_user_id(self):
        return self.user_id

    def logout(self):
        '''Logout the currently logged in user.
        '''
        
        self.is_authed = False;
        self.user_id = None;
        
        
        
