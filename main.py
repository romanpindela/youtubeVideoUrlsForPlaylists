# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import googleapiclient.discovery
from urllib.parse import parse_qs, urlparse

# FILE_PLAYLISTS = "playlists.txt"
# FILE_OUTPUT = "urls_videos_for_playlists.txt"


def main():

    # extract playlist id from url
    url = 'https://www.youtube.com/watch?v=Ilt7n76kOyc&list=UUiOxbbkbhn2wXPo0zIrc1mA&index=1'

    query = parse_qs(urlparse(url).query, keep_blank_values=True)
    playlist_id = query["list"][0]

    print(f'get all playlist items links from {playlist_id}')
    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey="AIzaSyAIwlhxzClXrRyZBxqgUGKFzSslj9HrtgY")

    request = youtube.playlistItems().list(
        part="snippet",
        playlistId=playlist_id,
        maxResults=50
    )
    response = request.execute()

    playlist_items = []
    while request is not None:
        response = request.execute()
        playlist_items += response["items"]
        request = youtube.playlistItems().list_next(request, response)

    print(f"total: {len(playlist_items)}")

    urls = [
        f'https://www.youtube.com/watch?v={t["snippet"]["resourceId"]["videoId"]}&list={playlist_id}&t=0s'
        for t in playlist_items]

    for url in urls:
        print(url)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
