from secrets import spotify_user_id, spotify_token
import json
import


class CreatePlaylist:
    def __init__(self):
        self.user_id = spotify_user_id

    def get_youtube_Client(self):
        pass

    def get_liked_video(self):
        pass

    def create_playlist(self):
        request_body = json.dumps({
            "name": "Youtube Liked Vids",
            "description": "All Liked Youtube Videos",
            "public": false
        })

        query = "https://api.spotify.com/v1/users/{}/playlists".format(
            self.user_id)
        response = requests.post(
            query,
            data=request_body,
            headers={"Content-Type": "application/json",
                     "Authorization": "Bearer {}".format(spotify_token)}
        )

    def get_spotify_uri(self):
        pass

    def add_song_to_playlist(self):
        pass
