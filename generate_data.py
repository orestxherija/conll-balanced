import json
import hashlib
import requests

RAW_URLS = [
  'https://raw.githubusercontent.com/Franck-Dernoncourt/NeuroNER/master/neuroner/data/conll2003/en/train.txt',
  'https://raw.githubusercontent.com/Franck-Dernoncourt/NeuroNER/master/neuroner/data/conll2003/en/test.txt',
  'https://raw.githubusercontent.com/Franck-Dernoncourt/NeuroNER/master/neuroner/data/conll2003/en/valid.txt',
]
INPUT_FILE = 'data/conll-balanced-hashed.json'
OUTPUT_FILE = 'data/conll-balanced.json'
CONLL_OUTPUT_FILE = 'data/conll-enriched.json'

def get_hash_str(text):
  return hashlib.md5(text.encode(encoding='UTF-8', errors='strict')).hexdigest()

def get_sentences_from_text(text):
  sentences = []
  cur_words = []
  for line in text.split('\n'):
    line = line.strip()
    doc_start = line.startswith('-DOCSTART-')
    if (len(line) == 0 or doc_start):
      if len(cur_words) > 0:
        sentences.append(' '.join(cur_words))
        cur_words = []
      continue
    cur_words.append(line.split(' ')[0])
  sentences.append(' '.join(cur_words))
  return sentences

def inflate_annotation(text, annot):
  vals = {
    'start': annot['start'],
    'end': annot['end'],
    'label': annot['label'],
    'text': text[annot['start'] : annot['end']],
  }
  if 'name_category' in annot:
    vals['name_category'] = annot['name_category']
  return vals

def transform_entry(entry):
  return (entry['text'], entry['annotations'])


def main():
  sentences = []
  for url in RAW_URLS:
    text = requests.get(url).text
    sentences += get_sentences_from_text(text)

  textByHash = {
    get_hash_str(sent): sent for sent in sentences
  }

  with open(INPUT_FILE, 'r') as infile:
    raw_data = json.load(infile)

  full_data = []
  conll_data = []
  for entry in raw_data:
    if 'textHash' in entry:
      hash_str = entry['textHash']
      text = textByHash[hash_str]
      inflated_entry = transform_entry({
        'text': textByHash[hash_str],
        'annotations': [
          inflate_annotation(text, annot)
          for annot in entry['annotations']
        ],
      })
      full_data.append(inflated_entry)
      conll_data.append(inflated_entry)
    else:
      full_data.append(transform_entry(entry))

  with open(OUTPUT_FILE, 'w') as outfile:
    outfile.write(json.dumps(full_data))
  with open(CONLL_OUTPUT_FILE, 'w') as outfile:
    outfile.write(json.dumps(conll_data))

  print('[Done]')

main()
