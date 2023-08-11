# nlp-text-summarization
Project for CS 6120 - Group 10

Team members:
  LeAnn Marie Mendoza
  Sindhu Swaroop
  Sumukhi Ganesan

Path to data: nlp-text-summarization/data/scisummnet_release1.1__20190413/

TextRank method: 
* summarization_using_textrank.ipynb

Clustering method: 
* NLP-Project_Group10-Clustering.ipynb

BART method:
* fine-tuned bart model: generation_config.json, config.json
* code: nlp_project_group10_finetunedbart.py, nlp_project_group10_pretrainedbart.py
* result data: rouge-bartfinetuned.csv, rouge_bartpretrained.csv

Text summarization is the task of producing a concise and fluent summary of a text document while preserving its key information and overall meaning. This task requires the summarizer to understand the text, identify its context, and then generate a new text that captures the content. There are two main approaches to text summarization: extractive and abstractive. Extractive summarization methods identify important sentences or phrases from the text and then combine them to form a summary. Abstractive summarization attempts to learn the context, semantics and relationships of different parts of a text using machine learning and generates summaries consisting of novel sentences that might not appear in the original content.

Research paper summarization is a unique task in the realm of summarization due to the dense, technical, and multifacted nature of scientific literature. As the volume of publications grow, it becomes an increasing challenge for academic professionals to keep up to date with the latest findings. Accurate summaries of research can assist in sifting through volumes of intricate details while maintaining the core competencies of the research publication.

In this project, we explored several different approaches to extractive as well as abstractive text summarization of research papers utilizing the ScisummNet dataset [1]. We will compare the performance of a state-of-the-art text summarization transformer, BART [2] with our devised text summarization methods, TextRank based summarization, Clustering based summarization, and a fine-tuned BART model.

