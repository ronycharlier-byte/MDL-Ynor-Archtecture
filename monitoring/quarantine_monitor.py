import numpy as np

class QuarantineMonitor:
    """
    MDL YNOR - QUARANTINE MONITOR V1.6.1
    Surveille la purete cognitive et le Ghost Drift Index.
    """
    def __init__(self, s1_threshold=0.15, p_threshold=0.05):
        self.s1_threshold = s1_threshold
        self.p_threshold = p_threshold
        self.status = "STABLE"
        self.history = []

    def update(self, s1, rayleigh_p):
        self.history.append(s1)
        
        if s1 > self.s1_threshold or rayleigh_p < self.p_threshold:
            self.status = "QUARANTINE"
        elif s1 > 0.10:
            self.status = "MONITORING"
        else:
            self.status = "STABLE"
            
        return self.status

    def get_gdi(self):
        """ Ghost Drift Index """
        if len(self.history) < 2: return 0.0
        return abs(self.history[-1] - self.history[-2])
