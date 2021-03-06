# Vizify
## Audio-Visualization Utilizing Spotify Song Data
Authors: Alex Scott, David Tarazi, Harrison Mintz

### Description:

The purpose of this code is to create engaging visualizations that play
alongside a user's Spotify music. These visualizations utilize different
quantitative descriptions of a song, such as its tempo, intensity, and danceability,
to ensure the vibe of the visualization matches the vibe of the song. The user can
either enable the program to create a visual for whatever song they are currently
listening to or search for a song using the interactive display; both of these
options lead to the audio visualization.

### Getting Stared:

To run, you must have Spotipy installed. You can do this with pip:

$ pipenv install git+https://github.com/plamere/spotipy.git#egg=spotipyp

You must also create your own client id and place it in a file called config.py
so that the script can access spotify data. There is a template file named
config_template.py which can be edited once you have your own Spotify web API
client id and username. You can set up your clients by visiting [this page.](https://developer.spotify.com/dashboard/)
Once you are on this page, you can login and click "CREATE A CLIENT ID".

To run, you must also have pygame installed. You can do this with:

$ pip install -U pygame --user

### Usage:
Once you have done the setup, you can begin playing a Spotify song on any player 
and in the terminal from the repository folder, you can run the script with:

$ python vizify.py

You don't need to pass any arguments; this will pull up a GUI explaining how to
interact with the software.

### License:

This project is licensed under the GNU APGLv3 license.
For more details regarding this license, please see the LICENSE.md file

### Tip Jar:

If you love our code SO much, are a big fan of our trippy music visualizations,
or perhaps just want to help out some broke college students then it is your 
lucky day because we accept tips!

You can Venmo any of us at @HarrisonMintz and @David-Tarazi

Thank you :)
