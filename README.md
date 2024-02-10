# Spoti-Key

Spoti-Key is a Python application that adds the currently playing song on Spotify to your liked songs. It uses the Spotify Web API via the Spotipy library and can be executed via a hotkey on your keyboard.

## Structure

The application mainly consists of two modules:

1. `Config` ([config/config.py](/config/config.py)): This module reads the configuration from a `config.ini` file.
2. `SpotifyClient`([spotify/spotify_client.py](/spotify/spotify_client.py)): This class represents a Spotify client. It authenticates the client using the provided configuration and has a method `add_current_song_to_liked_songs` which adds the currently playing song to the user's liked songs.

## Installation

Details from [spotipy](https://spotipy.readthedocs.io/en/2.22.1/#)

1. Create a new app on the [Spotify Dashboard](https://developer.spotify.com/dashboard).

2. Optional create a virtual environment

3. Install the requirements using pip:

   ```sh
   pip install -r requirements.txt
   ```

4. Fill out the `config.ini` file with your Spotify app credentials:

   ```ini
   [SPOTIFY]
   CLIENT_ID = your-spotify-client-id
   CLIENT_SECRET = your-spotify-client-secret
   REDIRECT_URI = your-app-redirect-url
   ```

You can find the example config [here](/example/example_config.ini). After filling out the info, please move it to the root directory of the project.

## Usage

Run the `main.py` script:

```sh
python main.py

# INFO:root:Adding 'The Beginning' by 'Flawed Mangoes' to liked songs...
# INFO:root:Done!
```

To disable the popping up of the console, rename the `main.py` to `main.pyw`.

This script uses the `SpotifyClient` class from the `spotify_client` module and reads the configuration from the `config.ini` file using the `Config` class from the `config` module. It then adds the currently playing song on Spotify to the user's liked songs.

## Compiling

You can compile this skript using `pyinstaller`:

1. Install PyInstaller:

   ```sh
   pip install pyinstaller
   ```

2. Run the following command:

   `--onfile` Only one file.
   `--noconsole` No console window.

   ```sh
   pyinstaller --onefile --noconsole main.py
   ```

This will create a single executable file in the `dist` directory.

> [!NOTE]
> The implementation of this feature as a hotkey within your hardware/software is up to you.
> I compiled it into an .exe file because Logitech Options does not support .py or .lnk files.
