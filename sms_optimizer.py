import os
import time
import hashlib
import shutil
from collections import defaultdict
from usage_predictor import UsagePredictor

class FileObject:
    def __init__(self, path, resolution=(0, 0), modified_time=None):
        self.path = path
        self.resolution = resolution
        self.modified_time = modified_time or os.path.getmtime(path)

class SMSOOptimizer:
    def __init__(self):
        self.ai_rules_engine = AIRulesEngine()
        self.usage_predictor = UsagePredictor()

    def scan_drive(self, drive_path):
        files = []
        for root, _, filenames in os.walk(drive_path):
            for fname in filenames:
                path = os.path.join(root, fname)
                resolution = (1920, 1080) if fname.lower().endswith(('.jpg', '.png', '.mp4')) else (0, 0)
                files.append(FileObject(path, resolution))
        return files

    def compute_hash(self, path):
        h = hashlib.sha256()
        try:
            with open(path, 'rb') as f:
                while chunk := f.read(8192):
                    h.update(chunk)
            return h.hexdigest()
        except:
            return path

    def profile_drive(self, drive_path):
        try:
            total, used, free = shutil.disk_usage(drive_path)
            return {
                'free_space': free,
                'is_ssd': 'ssd' in drive_path.lower()
            }
        except Exception as e:
            print(f"Error accessing drive {drive_path}: {e}")
            return {
                'free_space': 0,
                'is_ssd': False
            }

    def find_duplicates_with_ai(self, files):
        hash_groups = defaultdict(list)
        for file in files:
            hash_groups[self.compute_hash(file.path)].append(file)

        duplicates = []
        for group in hash_groups.values():
            if len(group) > 1:
                best = self.ai_rules_engine.select_best_duplicate(group)
                group_copy = [f for f in group if f != best]
                duplicates.append({'keep': best, 'remove': group_copy})
        return duplicates

    def optimize_storage(self, drive_paths):
        all_files = [f for drive in drive_paths for f in self.scan_drive(drive)]
        duplicates = self.find_duplicates_with_ai(all_files)
        usage_patterns = self.usage_predictor.analyze_patterns(all_files)
        drive_profiles = {d: self.profile_drive(d) for d in drive_paths}
        return self.ai_rules_engine.generate_plan(all_files, duplicates, usage_patterns, drive_profiles)

class AIRulesEngine:
    def select_best_duplicate(self, duplicates):
        return max(duplicates, key=lambda f:
            (f.resolution[0] * f.resolution[1]) +
            (time.time() - f.modified_time) / (365 * 24 * 3600) +
            (10 if '/organized/' in f.path.lower() else 0))

    def generate_plan(self, files, duplicates, usage_patterns, drive_profiles):
        plan = []
        for file in files:
            usage = usage_patterns.get(file.path, 0)
            target_drive = max(drive_profiles.items(), key=lambda d: (d[1]['is_ssd'], usage))
            plan.append({'file': file.path, 'target_drive': target_drive[0]})
        return plan
