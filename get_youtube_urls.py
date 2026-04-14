import urllib.request
import urllib.parse
import re

experts = [
    ("justin-welsh.md", "Justin Welsh"), 
    ("chris-walker.md", "Chris Walker B2B"), 
    ("dave-gerhardt-exitfive.md", "Dave Gerhardt"), 
    ("jason-lemkin-saastr.md", "Jason Lemkin SaaStr"),
    ("april-dunford.md", "April Dunford positioning"), 
    ("elena-verna.md", "Elena Verna product led growth"), 
    ("anthony-pierri.md", "Anthony Pierri FletchPMM"),
    ("morgan-ingram.md", "Morgan Ingram B2B sales"), 
    ("sangram-vajre.md", "Sangram Vajre B2B"), 
    ("kyle-poyar.md", "Kyle Poyar PLG")
]

for filename, expert in experts:
    query_string = urllib.parse.urlencode({"search_query": expert})
    html_content = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'"videoId":"(.*?)"', html_content.read().decode())
    
    videos = []
    for vid in search_results:
        if len(vid) == 11 and vid not in videos:
            videos.append(vid)
            if len(videos) == 2:
                break
    
    print(f"File: {filename}")
    for i, vid in enumerate(videos):
        try:
            vid_html = urllib.request.urlopen(f"https://www.youtube.com/watch?v={vid}").read().decode()
            title = re.search(r'<title>(.*?)</title>', vid_html).group(1).replace(" - YouTube", "")
            title = title.replace('&#39;', "'").replace('&amp;', '&').replace('&quot;', '"')
            print(f"Video {i+1}: {title}")
            print(f"URL: https://www.youtube.com/watch?v={vid}")
        except Exception as e:
            print(f"Video {i+1}: URL=https://www.youtube.com/watch?v={vid} (Fetch failed)")

