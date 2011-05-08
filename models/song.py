import datetime
from google.appengine.ext import db
from google.appengine.api import users

class Song(db.Model):
    id = db.IntegerProperty()
    name = db.StringProperty(required=True)
    artist = db.StringProperty(required=True)
    album = db.StringProperty(required=False)
    votes = db.IntegerProperty()
    time = db.DateProperty(auto_now=True)
    
    def jsonify(self):
        response = {"SongID" : str(self.id),
                "SongName" : str(self.name),
                "ArtistName" : str(self.artist),
                "AlbumName" : str(self.album),
                "votes" : str(self.votes) };
        return response


def jsonifySongs(songs):
    s = len(songs) - 1
    i = 0
   # result = '{'
    result = []
    for song in songs:
        result.append(Song.jsonify(song))
        #if i<s :
        #    result += ', '

        i += 1

    #result += '}'
    return result;

