# evote

A simple evoting system.

Right now, we will assume that the _election officers_ are trusted and so is the
server the election is being hosted on. We will also assume that the CAS auth
we are using right now is secure. Having made these assumptions, all we need is
a simple, unencrypted tally and an unencrypted vote stored on the server (or the
vote not stored at all). This should later be improved with some basic method of
preserving the vote anonymity, keeping it on the server, and implementing some
way of letting the voter verify their vote and the integerity of the overall
tally.

## Usage

Simply clone the evote repository:

```bash
git clone git@github.com:mtahmed/evote.git
```

Then import from another script and run as a WSGI app:

```python
import evote
from wsgiref.simple_server import make_server

app = evote.make_wsgi_app()
server = make_server('', 8000, app)
server.serve_forever()
```

## Frontend

The frontend right now is intended to be html+javascript pages where users will
need to login through some trusted authentication provider (CAS in this case).

## Backend

The backend right now is intended to be pyramid serving a WSGI app, and
sqlalchemy with a mysql database as the storage layer.

# License

Copyright (C) 2013  Muhammad Tauqir Ahmad

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
