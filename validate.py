#!/usr/bin/env python3
import json

records = json.load(open('novels-project-identifiers.json'))
num_valid = 0
for k, v in records.items():
    if int(k) != v['novels-project']:
        raise ValueError("Record {} invalid.".format(k))
    num_valid += 1
print("All {} records valid.".format(num_valid))
