
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
    }
}



setInterval(getNextSong, 120000);



