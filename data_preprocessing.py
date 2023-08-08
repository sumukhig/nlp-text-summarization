import glob
import json
import xml.etree.ElementTree as ET

data_directory = './data/scisummnet_release1.1__20190413/top1000_complete'

for doc in glob.glob(data_directory+'/*')[0:2]:
    citing_sentences = glob.glob(doc + '/*.json')[0]
    article = glob.glob(doc + '/*_xml/*.xml')[0]
    summary = glob.glob(doc + '/summary/*.txt')[0]
    
    a = ET.parse(article)
    article_content = 

    with open(summary) as s:
        summary_content = s.read()

    with open(citing_sentences) as cs:
        citing_sentences_content = json.loads(cs.read().decode('utf-8'))

    print(summary_content)