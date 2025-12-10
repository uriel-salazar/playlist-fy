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
## 📌 Main Menu
<p align="center">
  <img src="https://github.com/user-attachments/assets/c9d08d38-69c3-4933-84d6-227bc3db627d" width="700">
</p>

---

## 🎵 Playlists Menu
<p align="center">
  <img src="https://github.com/user-attachments/assets/b92f5239-a81b-47e6-ba3b-d54f081c430e" width="450">
</p>

---

## Select a Playlist
<p align="center">
  <img src="https://github.com/user-attachments/assets/bc43e56b-110f-4a72-b114-79260b105938" width="450">
</p>

---

##  Songs from Playlist
<p align="center">
  <img src="https://github.com/user-attachments/assets/6bef00ca-2be6-40c3-9140-839f9fae9a5a" width="750">
</p>

---

##  Top Songs
<p align="center">
  <img src="https://github.com/user-attachments/assets/f5be91b7-8022-40c7-9673-746d2edf08c5" width="450">
</p>

  - **Note: The screenshots use my personal Spotify account only for demonstration purposes.**
    
 # Features
- Authenticate with Spotify using PKCE
- View your playlists
- View songs inside any playlist
- See your top tracks and artists
- Switch playlists
- Add songs to your playlist
- CLI interface

 ## Known Bugs / Errors🐛
- If the user denies the PKCE login, the program goes back to the main menu. However, if you want to try the authorization again, the program freezes.

- Token expiration: If the Spotify token expires, the user must re-authenticate. This is normal behavior with PKCE.

- Playback control: Some playback actions may fail if the user does not have Spotify Premium.

- Rate limits: The Spotify API may temporarily block requests if too many are made in a short time.

- Environment differences: Behavior can vary depending on the platform or browser used during authentication.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing
Contributions are welcome! If you find a bug or have a feature request, please open an issue or submit a pull request.

