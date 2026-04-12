import time

class EventTracker:
    """
    Loggue les alertes et les actions du système.
    """
    def __init__(self):
        self.events = []

    def log_event(self, level, data):
        event = {
            "timestamp": time.time(),
            "level": level,
            "data": data
        }
        self.events.append(event)
        return event
