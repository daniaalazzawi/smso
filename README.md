# Smart Media Storage Optimizer (SMSO)

SMSO is an AI-enhanced tool that scans multiple storage drives to find duplicate media files, predict file usage patterns, and intelligently optimize where files are stored based on speed, space, and access frequency.

---

## Project Structure

```text
SMSO/
sms_optimizer.py
usage_predictor.py
main.py
requirements.txt
```

---

## Features

- Detects exact and near-duplicate photos/videos
- Learns file access patterns via ML stub
- Scores and ranks storage drives
- Plans file relocations to optimize speed and space
- Fault tolerant: handles inaccessible drives

---

## How to Run

### 1. **Clone the Repository**
```bash
git clone
cd SMSO
```

### 2. **Run the Optimizer**
```bash
python main.py /mnt/ssd /mnt/hdd1 /mnt/hdd2
```
Replace the paths with real directories you want scanned.

### 3. **Sample Output**
```text
Move '/mnt/hdd1/photo1.jpg' to '/mnt/ssd'
Move '/mnt/hdd2/video3.mp4' to '/mnt/hdd1'
...
```

---

## Requirements

For this basic version, no external libraries are required beyond Python 3.8+.

If needed, create `requirements.txt`:

Install with:
```bash
pip install -r requirements.txt
```
