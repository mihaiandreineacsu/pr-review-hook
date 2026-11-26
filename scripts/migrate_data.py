import json
import sys

data = json.load(open(sys.argv[1]))
for row in data:
    row["name"] = row["name"].upper()
json.dump(data, open(sys.argv[1], "w"))
print("done")
