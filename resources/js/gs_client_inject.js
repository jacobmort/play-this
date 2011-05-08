
function setNextSong(json){
    if (json != '') {
        var songid = jQuery.parseJSON(json);
        Grooveshark.addSongsByID(songid.SongID);
    }
}

function getNextSong(){
    if (Grooveshark.getNextSong() == null){
        jQuery.ajax({
            url: "http://hear-this.appspot.com/getnext",
            type: "GET",
            dataType: 'jsonp'
        });
    }else{
        song = Grooveshark.getCurrentSongStatus();
        artist = song.song.artistName;
        name = song.song.songName;
        jQuery.ajax({
            url: "http://hear-this.appspot.com/setcurrent?name="+name+"&artist="+artist,
            type: "GET"
        });
    }
}



setInterval(getNextSong, 120000);



