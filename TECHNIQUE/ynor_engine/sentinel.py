import json
import os

class YnorEconomicSentinel:
    def __init__(self, calendar_path, report_path):
        self.report_path = report_path

    def get_geo_alpha(self, asset):
        try:
            if os.path.exists(self.report_path):
                with open(self.report_path, 'r') as f:
                    report = json.load(f)
                    # Logic simplifiée pour la prod
                    return 0.5 
            return 0.5
        except:
            return 0.5
