import glob
import gzip
import json

data_directory = './data/Multi-XScience/data/*'

for file in glob.glob(data_directory):
    print(file)
    f = gzip.open(file, 'r')
    data = json.loads(f.read().decode('utf-8'))
    print(data[0])
