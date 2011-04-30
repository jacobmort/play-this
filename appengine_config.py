from gaesessions import SessionMiddleware
from os import urandom
def webapp_add_wsgi_middleware(app):
    app = SessionMiddleware(app, cookie_key="2458ualsngq3op45uyapsdkfhjaslkjt3420q85halsgnasfafasdf",no_datastore=True)
    return app