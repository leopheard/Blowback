from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()
url1 = "https://www.omnycontent.com/d/playlist/aaea4e69-af51-495e-afc9-a9760146922b/4a3ca742-9a68-4850-a727-ab790176c0e9/bf57384a-96e6-402e-90c6-ab790178fd59/podcast.rss"
@plugin.route('/')
def main_menu():
    items = [
        {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('episodes1'),
            'thumbnail': "https://www.omnycontent.com/d/programs/aaea4e69-af51-495e-afc9-a9760146922b/4a3ca742-9a68-4850-a727-ab790176c0e9/image.jpg"},
        {
            'label': plugin.get_string(30002),
            'path': plugin.url_for('episodes2'),
            'thumbnail': "https://www.omnycontent.com/d/programs/aaea4e69-af51-495e-afc9-a9760146922b/4a3ca742-9a68-4850-a727-ab790176c0e9/image.jpg"},
    ]
    return items

@plugin.route('/episodes1/')
def episodes1():
    soup1 = mainaddon.get_soup1(url1)
    playable_podcast1 = mainaddon.get_playable_podcast1(soup1)
    items = mainaddon.compile_playable_podcast1(playable_podcast1)
    return items

@plugin.route('/episodes2/')
def episodes2():
    soup1 = mainaddon.get_soup1(url1)
    playable_podcast2 = mainaddon.get_playable_podcast2(soup1)
    items = mainaddon.compile_playable_podcast2(playable_podcast2)
    return items

if __name__ == '__main__':
    plugin.run()
