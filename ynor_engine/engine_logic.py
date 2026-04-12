# ==============================================================================
# 🔺 CORE ENGINE : YNOR GEO-EDITION (V15.0)
# ==============================================================================

import requests
import json
import os
import re
from datetime import datetime
from ynor_geo_sentiment import YnorGeoSentimentEngine

class YnorEconomicSentinel:
    def __init__(self, calendar_path, report_path):
        self.report_path = report_path
        self.geo_engine = YnorGeoSentimentEngine()

    def get_geo_alpha(self, asset):
        try:
            with open(self.report_path, 'r') as f:
                report = json.load(f)
                news = report.get("top_news", [])
                
                # Analyse multi-langue
                global_sentiment = sum([self.geo_engine.analyze_global_feed(n) for n in news])
                alpha = global_sentiment / (len(news) if news else 1)
                
                # Bouclier Black Swan
                # Si le sentiment est trop extrême, on alerte
                if abs(alpha) > 7.0:
                    print("⚠️ [GEO-ALERTE] ANOMALIE DÉTECTÉE")
                
                return round(alpha, 2)
        except: return 0.0

class YnorNewsScraper:
    def __init__(self, report_path):
        self.report_path = report_path
        self.sources = [
            "https://www.investing.com/rss/news_285.rss", # US
            "https://www.investing.com/rss/market_overview.rss", # Global
            "https://fr.investing.com/rss/news_285.rss" # FR
        ]

    def update_report(self):
        all_news = []
        for url in self.sources:
            try:
                res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=5)
                titles = re.findall(r'<title>(.*?)</title>', res.text)
                all_news.extend(titles[1:5])
            except: continue
        
        report = {"timestamp": datetime.now().isoformat(), "top_news": list(set(all_news))}
        with open(self.report_path, 'w') as f:
            json.dump(report, f, indent=4)
