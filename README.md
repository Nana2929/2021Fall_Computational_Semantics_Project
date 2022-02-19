# 2021Fall Computational Semantics Term Project
1. Topic: Wiki-based Chinese WSD 
2. Data: 
  * Crawled from Wikipedia, cleaned and preprocessed by myself
  * 164 words with # of fine-grained senses >=2
3. Phrase list: https://gist.github.com/indiejoseph/eae09c673460aa0b56db
4. The experimented WSD algorithms: 
(1) tfidf (inspired by https://www.itread01.com/hkyecfy.html)
(2) Lesk++ (inspired by [Simple Embedding-Based
Word Sense Disambiguation](https://aclanthology.org/2018.gwc-1.30/)) 
5. Result: 
(1) tfidf
* Train: Test = 1:1, Total TestSize = 28,517 // No randomization
*  Total CAcc: 46.6% // Coarse-grained Accuracy
(2) Lesk++ 
* Train: Test = 7:3, Total TestSize = 8,576 // with randomization
* Total Accuracy: 59.34 %  // Coarse-grained Accuracy

Check [doc](doc) for more details.
