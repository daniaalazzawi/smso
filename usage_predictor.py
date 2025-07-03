class UsagePredictor:
    def analyze_patterns(self, files):
        # Dummy logic
        usage = {}
        for f in files:
            usage[f.path] = 1.0 / (1 + f.modified_time)
        return usage
