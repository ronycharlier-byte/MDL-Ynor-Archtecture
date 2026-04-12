import requests
import json
import re
from datetime import datetime

class YnorNewsScraper:
    def __init__(self, report_path):
        self.report_path = report_path
        self.sources = ["https://www.investing.com/rss/news_285.rss"]

    def update_report(self):
        all_news = []
        for url in self.sources:
            try:
                res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=5)
                titles = re.findall(r'<title>(.*?)</title>', res.text)
                all_news.extend(titles[1:5])
            except:
                continue
        report = {"timestamp": datetime.now().isoformat(), "top_news": list(set(all_news))}
        with open(self.report_path, 'w') as f:
            json.dump(report, f, indent=4)
