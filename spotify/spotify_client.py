import spotipy
import logging
from spotipy.oauth2 import SpotifyOAuth


class SpotifyClient:
    """
    A class representing a Spotify client.

    Args:
        config (ConfigParser): The configuration object containing Spotify credentials.
        log_level (int, optional): The logging level. Defaults to logging.WARNING.
    """

    def __init__(self, config, log_level=logging.WARNING):
        self.spotify = self._authenticate(config)
        logging.basicConfig(level=log_level)

    def _authenticate(self, config):
        """
        Authenticates the Spotify client using the provided configuration.

        Args:
            config (ConfigParser): The configuration object containing Spotify credentials.

        Returns:
            spotipy.Spotify: The authenticated Spotify client.
        """
        client_id = config.get("SPOTIFY", "CLIENT_ID")
        client_secret = config.get("SPOTIFY", "CLIENT_SECRET")
        redirect_uri = config.get("SPOTIFY", "REDIRECT_URI")
        scope = "user-read-currently-playing, user-library-modify"

        return spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                client_id=client_id,
                client_secret=client_secret,
                redirect_uri=redirect_uri,
                scope=scope,
            )
        )

    def add_current_song_to_liked_songs(self):
        """
        Adds the currently playing song to the user's liked songs.

        This method retrieves the currently playing song from Spotify, extracts its name,
        artists, and ID, and adds it to the user's liked songs.

        Raises:
            spotipy.SpotifyException: If there is an error adding the song to the liked songs.
        """
        current_song = self.spotify.current_user_playing_track()
        track_name = current_song["item"]["name"]
        track_artists = [artist["name"] for artist in current_song["item"]["artists"]]
        track_id = current_song["item"]["id"]

        logging.info(
            f"Adding '{track_name}' by {', '.join(track_artists)}' to liked songs..."
        )
        self.spotify.current_user_saved_tracks_add([track_id])
        logging.info("Done!")

    # For testing purposes
    def get_song_info(self, song_id):
        """
        Get information about a song by its ID.

        Args:
            song_id (str): The ID of the song.

        Returns:
            dict: A dictionary containing information about the song.
        """
        return self.spotify.track(song_id)
