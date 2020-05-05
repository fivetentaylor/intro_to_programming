import json
import sys

max_buy = float('-inf')
min_sell = float('inf')
for line in sys.stdin:
    rec = json.loads(line.strip())
    if 'price' not in rec:
        continue

    if rec['side'] == 'sell':
        min_sell = min(min_sell, float(rec['price']))
    else:
        max_buy = max(max_buy, float(rec['price']))

    print('max_buy: %s, min_sell: %s' % (max_buy, min_sell))
