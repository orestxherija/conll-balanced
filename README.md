# README

This repository is a guide to downloading CoNLL-Balanced data, as well as some data analysis that we included in our blog post.  


# Downloading Data

To generate the full data of CoNLL-Balanced, run the following from the root of the repo:

```
pip install -r requirements.txt
python generate_data.py
```

The three generated data files in the `data/` directory are:
1. `conll-enriched.json`: CoNLL-2003 data enriched with name categories
2. `conll-augment.json`: Our new annotated sentences with over 600 new female names
3. `conll-balanced.json`: CoNLL-Balanced, the combination of CoNLL-Enriched and our additional data

# Notebook Details

The code in the notebook walks through an investigation of the distribution of labels and names in CoNLL and CONLL-Balanced. It also shows an example of training a model on the data, demonstrating the bias of a NER model trained on CoNLL alone. 

Note: We have provided pre-trained models; however, if you train a fresh model on the data there will be some variance in the results. The sample size of female names in the test data set isn't very large so the results will vary, as is expected with most ML models.

# CORPUS LICENSE INFORMATION

Our goal was to measure the bias in a historical NLP dataset on a named-entity recognition model and measure whether enrichment of the dataset would mitigate bias effects in a model trained on the enriched data.  In order to do this, we started out using the Reuters corpus used by the CoNLL-2003. 

The original English data is a collection of news articles from Reuters Corpus available at: https://trec.nist.gov/data/reuters/reuters.html. In order to use this dataset that has enriched annotations of the original CoNLL-2003 data, you will need to obtain the original corpus.

The annotations of the original English data were completed by Erik F Tjong Kim Sang and Fien De Meulder of the Language Technology 
Group at the University of Antwerp.  They have made the original annotations available at: https://www.clips.uantwerpen.be/conll2003/ner/.

In order to enrich the CoNLL-2003 dataset, we used two additional corpora.  First, we used the Reuters-21578 collection. This collection is copyrighted by Reuters Ltd. and Carnegie Group, Inc. You can find more information about the Reuters-21578 collection at: http://kdd.ics.uci.edu/databases/reuters21578/README.txt.  

Second, to enrich the CoNLL-2003 dataset we used the Brown Corpus by W.N. Francis and H. Kucera at Brown University.  Information about the Brown Corpus is available at: https://archive.org/details/BrownCorpus.
