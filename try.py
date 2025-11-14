
results={
  "tracks": {
    "href": "https://api.spotify.com/v1/search?query=God%27s+Plan&type=track&offset=0&limit=2",
    "items": [
      {
        "album": {
          "album_type": "album",
          "artists": [
            {"name": "Drake", "id": "3TVXtAsR1Inumwj472S9r4"}
          ],
          "name": "Scorpion",
          "release_date": "2018-06-29",
        },
        "artists": [
          {"name": "Drake", "id": "3TVXtAsR1Inumwj472S9r4"}
        ],
        "name": "God's Plan",
        "id": "6DCZcSspjsKoFjzjrWoCdn",
        "uri": "spotify:track:6DCZcSspjsKoFjzjrWoCdn",
        "popularity": 95,
        "preview_url": "https://p.scdn.co/mp3-preview/..."
      },
      {
        "album": {
          "album_type": "single",
          "artists": [
            {"name": "Drake", "id": "3TVXtAsR1Inumwj472S9r4"}
          ],
          "name": "God's Plan - Remix",
          "release_date": "2018-07-01",
        },
        "artists": [
          {"name": "Drake", "id": "3TVXtAsR1Inumwj472S9r4"},
          {"name": "Future", "id": "1RyvyyTE3xzB2ZywiAwp0i"}
        ],
        "name": "God's Plan - Remix",
        "id": "7lPN2DXiMsVn7XUKtOW1CS",
        "uri": "spotify:track:7lPN2DXiMsVn7XUKtOW1CS",
        "popularity": 80,
        "preview_url": "https://p.scdn.co/mp3-preview/..."
      }
    ],
    "limit": 2,
    "next": "https://api.spotify.com/v1/search?query=God%27s+Plan&type=track&offset=2&limit=2",
    "offset": 0,
    "previous": null,
    "total": 50
  }
}
print(results)

