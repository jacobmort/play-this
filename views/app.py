import cgi
from google.appengine.ext import webapp
from google.appengine.api import users
from google.appengine.ext.webapp.util import run_wsgi_app
from mako.template import Template
from mako.runtime import Context
import simplejson


class Song:
    def __init__(self,id,song,artist):
        self.id = id
        self.name = song
        self.artist = artist
        self.album = 'album'
        self.votes = 0

def encode_song(obj):
    if isinstance(obj, Song):
        return [obj.id, obj.name]
    raise TypeError(repr(o) + " fack")

class Home(webapp.RequestHandler):
    def get(self):
        mytemplate = Template(filename='../templates/index.html')
        songs = []
        songs.append(Song('1','fuck you','ceelo green'))
        songs.append(Song('2','good vibrations','beach boys'))
        songs.append(Song('3','hot like sauce','Pretty Lights'))
        print mytemplate.render(songs=songs)
    
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