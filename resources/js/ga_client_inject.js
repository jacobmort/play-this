
function setNextSong(json){
    var songid = jQuery.parseJSON(json);
    Grooveshark.addSongsByID(songid.SongID);
}

function getNextSong(){
    if (Grooveshark.getNextSong() == null){
        jQuery.ajax({
            type: "GET",
            url: 'http://hear-this.appspot.com/getnext',
            data:"format=json",
            dataType: "jsonp"
        });
    }
}



setTimeout(getNextSong, 120000);
