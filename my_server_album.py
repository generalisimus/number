from bottle import route
from bottle import run
from bottle import HTTPError

import my_user_album

@route("/albums/<album>")
def len_album(len_a):
    len_as = my_user_album.find(album)
    if album in albums_list:
        len_f = len(album)
    return len_f

@route("/albums/<artist>")
def albums(artist):
    albums_list = my_user_album.find(artist)
    if not albums_list:
        message = "Альбомов {} не найдено".format(artist)
        result = HTTPError(404, message)
    else:
        album_names = [my_user_album.album for my_user_album in albums_list]
        result = "Список альбомов {}, всего альбомов {}: ".format(artist, len_f)
        result += ", ".join(album_names)
    return result

if __name__ == "__main__":
    run(host="localhost", port=8080, debug=True)
