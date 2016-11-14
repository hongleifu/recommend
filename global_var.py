#!/usr/bin/python
import gensim
MODEL_FILE="./word_2_vector.model"
print "now load model...",MODEL_FILE
MODEL=gensim.models.Word2Vec.load(MODEL_FILE)
