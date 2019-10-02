# python-music-player-with-database
Python music player with GUI and Database connectivity to save playlist data. Tkinter library is user for GUI and MySQL is used to store music playlist.


## Features of music player

### Add Songs - This will add songs to database and update playlist from database.
### Clear Playlist - This will clear the database and remove all the songs from playlist.
### Play - This will play the song.
### Next Song - This will play next song.
### Privious Song - This will play privious song.
### Stop - This Will Stop music.
### Current playing song will be displayed.
### All the song in playlist is displayed in playlist.




## Configure Your Music Player in music-player.py

mydb = mysql.connector.connect(
  host="INSERT_HOST_NAME_HERE",
  user="INSERT_USERNAME_HERE",
  passwd="INSERT_PASSWORD_HERE",
  database="ENTER DATABASE NAME HERE"
)




## Setup database and music table

Open your mysql console
Create database
Create table with name musiclist and 2 attribute as id, path and name (Use the below query to create table in databse)
CREATE TABLE musiclist(id int primary key not null auto_increament, path varchar(500), name varchar(500));


## Install Libraries


### Tkinter - Install Tkinter using command
pip install python-tkinter


### pygame - Install Pygame using command
pip install pygame


### mysql - Install mysql interface
pip install mysql-connector


### Install Mutagen from python console.


## Run your music player - Hit the command
python music-player.py

Done. Enjoy Your Music Player Project.
