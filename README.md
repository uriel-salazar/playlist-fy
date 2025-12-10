# Playlist-fy 🎵
Playlist-fy is a CLI program designed with spotipy API. 
## Description 
After log in with Spotify (by PKCE OAuth flow), you can search your own playlists, add news songs to your playlists and see your top of artists and music 
## Tech used 
- ![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
- ![CLI](https://img.shields.io/badge/Command%20Line-000000?style=flat&logo=terminal)
- ![Spotify API](https://img.shields.io/badge/Spotify%20API-1DB954?logo=spotify&logoColor=white)
- ![Requests](https://img.shields.io/badge/Requests-202020?style=flat&logo=requests&logoColor=white)
![OAuth2 PKCE](https://img.shields.io/badge/OAuth2%20PKCE-4A90E2?logo=oauth&logoColor=white)

# Getting started 
## Prerequisites
- Python 3.10+
- pip installed
- Spotify Developer Account
- A Spotify App configured for PKCE
  Ensure your Redirect URI matches your script ("http://127.0.0.1:46666/callback")
## Installation 
*1*. **Clone repository**
```bash
https://github.com/uriel-salazar/playlist-fy
```
*2*. **Install dependencies**
```bash
  pip install -r requirements.txt
```
*3*. **Configuration for PKCE**
(Create a .env file with this information)
```bash
SPOTIPY_CLIENT_ID=your_client_id_here
SPOTIPY_REDIRECT_URI=http://localhost:8080/callback
```
*4* **Running**
```bash
  python playlist_fy.py
```
## Overview *Screenshots*








