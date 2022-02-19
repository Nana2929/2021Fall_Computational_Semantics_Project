import numpy as np
import pandas as pd
def word_tfidf(target, docs):
    '''
    doc: a list of sentences
    docs: a collection of list of sentences
    target: a string (a word)
    '''
    Dcount = len(docs)
    cache = [0 for i in range(len(docs))]
    numerators = [-1 for i in range(len(docs))]
    denominators = [-1 for i in range(len(docs))]
    tfvalues = [-1 for i in range(len(docs))]
    for idx, doc in enumerate(docs):
        # flatten
        flatdoc = [token for sentence in doc for token in sentence]
        # count
        doclen = len(flatdoc)
        tcount = flatdoc.count(target)
        statemsg = 'OK'
        # tf
        try:
            tf = tcount/doclen
        except ZeroDivisionError:
            tf = -1    
            statemsg = f'--- Doc {idx} of {target} is missing.'
        numerators[idx] = tf
        if tcount > 0:
          cache[idx] = 1 # 有出現
          
    for idx, doc in enumerate(docs):
        # idf
        selfhasoccur = cache[idx]
        occ = sum(cache) - selfhasoccur
        denominators[idx] = np.log((Dcount+1)/(occ+1))
        tfvalues[idx] = numerators[idx] / denominators[idx]
    return statemsg, tfvalues

def TFIDF(testsent, docs, sensenames, wsdword, minlen = 2):
    '''只算兩個字（含）以上的詞'''
    # print("* cleaned test sentence:\n", testsent)
    tfs = {}
    for word in testsent:
      if word != wsdword and len(word) >= minlen:
        statemsg, tfval = word_tfidf(word, docs)
        tfs[word] = tfval
        if statemsg != 'OK': print(statemsg)
   
    df = pd.DataFrame(tfs, index = sensenames)
    df["Tfidf_sum"] = df.sum(axis=1)
    # reordering, move tfidf-sum to front
    cols = list(df.columns.values)
    cols = cols[-1:] + cols[:-1]
    df = df[cols]
    return df["Tfidf_sum"].idxmax(), df