#!/usr/bin/env python3

import sys
sys.path.append('/users/mtahmed/.local/lib/python3.2/site-packages')

import webob
import auth

def election(environ, start_response):
    a = auth.Auth()
    logout_button = (
'''<!DOCTYPE HTML>
<html>
<body>
  [<a href='?logout'>LOGOUT</a>]
</body>
</html>
''')
    request = webob.Request(environ)
    response = webob.Response()
    if 'logout' in request.params:
        response = a.logout(response)
    else:
        response.text = 'Logged in as %s' % a.user_id
        response.text += logout_button

    return response(environ, start_response)

if __name__ == '__main__':
    import wsgiref.handlers
    wsgiref.handlers.CGIHandler().run(election)
