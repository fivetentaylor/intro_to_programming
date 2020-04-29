import sys
import json
import yaml

for line in sys.stdin:
    rec = line.strip().split(",")
    rec = [int(s) for s in rec]
    rec.append(rec[0] + rec[1])
    print(json.dumps(rec))
