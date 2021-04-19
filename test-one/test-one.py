import json
import os

#TEST-ONE-A
os.system('./test-one-a.sh')
#TEST-ONE-B
os.system('./test-one-b.sh ')
#TEST-ONE-C
os.system('./test-one-c.sh ')
#TEST-ONE-D
os.system('./test-one-d.sh ')
#TEST-ONE-E
os.system('./test-one-e.sh ')

with open('data.json') as f:
  data = json.load(f)


