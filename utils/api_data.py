import requests


baseUrl = "https://hacker-news.firebaseio.com/v0"
storiesUrl = f"{baseUrl}/topstories.json"
itemUrl = f"{baseUrl}/item/"
    
def get_stories():
    try:
        stories_data = requests.get(storiesUrl, timeout=(10, 10))
        stories_data.raise_for_status()
        return stories_data.json()
    except Exception as err:
        return False
    
    
def get_item(item_id):
    try:
        item_data = requests.get(f"{itemUrl}{item_id}.json", timeout=(10, 10))
        item_data.raise_for_status()
        return item_data.json()
    except Exception as err:
        return False
    
    
def get_stories_data():
    stories_data = get_stories()
    stories = []
    if not stories_data:
        return False
    for story_id in stories_data:
        item = get_item(story_id)
        stories.append(item)
    return stories
