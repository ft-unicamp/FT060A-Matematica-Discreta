from nltk.corpus import wordnet as wn
 
print wn.synsets('cat', 'n')
# [Synset('cat.n.01'), Synset('guy.n.01'), Synset('cat.n.03'), Synset('kat.n.01'), Synset('cat-o'-nine-tails.n.01'), Synset('caterpillar.n.02'), Synset('big_cat.n.01'), Synset('computerized_tomography.n.01')]
 
print wn.synsets('dog', 'n')
# [Synset('dog.n.01'), Synset('frump.n.01'), Synset('dog.n.03'), Synset('cad.n.01'), Synset('frank.n.02'), Synset('pawl.n.01'), Synset('andiron.n.01')]
 
print wn.synsets('feline', 'n')
# [Synset('feline.n.01')]
 
print wn.synsets('house', 'n')
# [Synset('mammal.n.01')]
 
print wn.synsets('acquire', 'v')
 
 
# It's important to note that the `Synsets` from such a query are ordered by how frequent that sense appears in the corpus
 
# You can check out how frequent a lemma is by doing:
cat = wn.synsets('family', 'n')[0]     # Get the most common synset
print cat.lemmas()[0].count()       # Get the first lemma => 18
 
 
 
dog = wn.synsets('dog', 'n')[0]           # Get the most common synset
feline = wn.synsets('feline', 'n')[0]     # Get the most common synset
mammal = wn.synsets('mammal', 'n')[0]
house = wn.synsets('house', 'n')[0]

 
 
 
# You can read more about the different types of wordnet similarity measures here: http://www.nltk.org/howto/wordnet.html
for synset in [dog, feline, mammal,house]:
    print "Similarity(%s, %s) = %s" % (cat, synset, cat.wup_similarity(synset))
 
# Similarity(Synset('cat.n.01'), Synset('dog.n.01')) = 0.2
# Similarity(Synset('cat.n.01'), Synset('feline.n.01')) = 0.5
# Similarity(Synset('cat.n.01'), Synset('mammal.n.01')) = 0.2