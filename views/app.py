import cgi
from google.appengine.ext import webapp
from google.appengine.api import users
from google.appengine.ext.webapp.util import run_wsgi_app
from mako.template import Template
from mako.runtime import Context
import simplejson

def serialize(obj):
    """Recursively walk object's hierarchy."""
    if isinstance(obj, (bool, int, long, float, basestring)):
      return obj
    elif isinstance(obj, dict):
      obja = {}#= obj.copy()
      for key in obj:
        obja['"'+str(key)+'"'] = serialize(obj[key])
      return obja
    elif isinstance(obj, list):
      return [serialize(item) for item in obj]
    #elif isinstance(obj, tuple):
    #  return tuple(serialize([item for item in obj]))
    elif hasattr(obj, '__dict__'):
      return serialize(obj.__dict__)
    #else:
    #  return repr(obj) # Don't know how to handle, convert to string


class Song:
    def __init__(self,id,song,artist):
        self.id = id
        self.name = song
        self.artist = artist
        self.album = 'album'
        self.votes =  '0'
    
class Home(webapp.RequestHandler):
    def get(self):
        mytemplate = Template(filename='../templates/index.html')
        songs = []
        songs.append(Song('1','fuck you','ceelo green'))
        songs.append(Song('2','good vibrations','beach boys'))
        songs.append(Song('3','hot like sauce','Pretty Lights'))
        print mytemplate.render(songs=serialize(songs))
    
class VoteAction(webapp.RequestHandler):
    def post(self):
        results = self.request.get('searchquery')
        mytemplate = Template(filename='../templates/index.html')
        songs = dict()

        songs.update(s1=Song('2','good vibrations','beach boys'))
        songs.update(s2=Song('3','hot like sauce','Pretty Lights'))
        songs.update(s3=Song('1','fuck you','ceelo green'))
        self.response.out.write(simplejson.dumps({'s1':Song('2','good vibrations','beach boys')}),default=encode_song)

application = webapp.WSGIApplication(
                                     [('/', Home),
                                      ('/playthis', VoteAction)],
                                     debug=True)
def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()