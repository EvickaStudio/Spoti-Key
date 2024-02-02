import logging
from config.config import Config
from spotify.spotify_client import SpotifyClient

if __name__ == "__main__":
    """
    This script adds the currently playing song on Spotify to the user's liked songs.
    It uses the SpotifyClient class from the spotify_client module and reads the configuration
    from the config.ini file using the Config class from the config module.
    """
    config = Config("config.ini")
    client = SpotifyClient(config, log_level=logging.INFO)
    client.add_current_song_to_liked_songs()