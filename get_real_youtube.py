import urllib.request
import urllib.parse
import re

experts = [
    ("justin-welsh.md", "Justin Welsh LinkedIn"), 
    ("chris-walker.md", "Chris Walker B2B podcast"), 
    ("dave-gerhardt-exitfive.md", "Dave Gerhardt B2B podcast"), 
    ("jason-lemkin-saastr.md", "Jason Lemkin SaaStr"),
    ("april-dunford.md", "April Dunford positioning"), 
    ("elena-verna.md", "Elena Verna product led growth"), 
    ("anthony-pierri.md", "Anthony Pierri FletchPMM homepage"),
    ("morgan-ingram.md", "Morgan Ingram B2B sales LinkedIn"), 
    ("sangram-vajre.md", "Sangram Vajre B2B"), 
    ("kyle-poyar.md", "Kyle Poyar PLG")
]

for filename, expert in experts:
    query_string = urllib.parse.urlencode({"search_query": expert})
    
    req = urllib.request.Request(
        "https://www.youtube.com/results?" + query_string,
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    
    try:
        html_content = urllib.request.urlopen(req).read().decode('utf-8')
    except Exception as e:
        print(f"Failed to fetch search for {expert}: {e}")
        continue
        
    # YouTube's initial data contains the search results
    # We can use regex to find videoId and title
    # Format typically: "videoId":"xyz","thumbnail":{...},"title":{"runs":[{"text":"Real Title Here"}]}
    
    matches = re.finditer(r'"videoId":"([^"]{11})".*?"title":\{"runs":\[\{"text":"(.*?)"\}\]', html_content)
    
    videos = []
    seen = set()
    for m in matches:
        vid = m.group(1)
        title = m.group(2)
        if vid not in seen and "{" not in title and len(title) > 5:
            seen.add(vid)
            # Unescape some basic unicode
            title = title.encode('utf-8').decode('unicode_escape')
            videos.append((vid, title))
            if len(videos) == 2:
                break
                
    print(f"\nFile: {filename}")
    for i, (vid, title) in enumerate(videos):
        print(f"Video {i+1}: {title}")
        print(f"URL: https://www.youtube.com/watch?v={vid}")
