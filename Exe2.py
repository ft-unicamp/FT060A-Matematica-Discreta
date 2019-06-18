from nltk import word_tokenize, pos_tag
from nltk.corpus import wordnet as wn
 
def penn_to_wn(tag):
    """ Convert between a Penn Treebank tag to a simplified Wordnet tag """
    if tag.startswith('N'):
        return 'n'
 
    if tag.startswith('V'):
        return 'v'
 
    if tag.startswith('J'):
        return 'a'
 
    if tag.startswith('R'):
        return 'r'
 
    return None
 
def tagged_to_synset(word, tag):
    wn_tag = penn_to_wn(tag)
    if wn_tag is None:
        return None
 
    try:
        return wn.synsets(word, wn_tag)[0]
    except:
        return None
 
def sentence_similarity(sentence1, sentence2):
    """ compute the sentence similarity using Wordnet """
    # Tokenize and tag
    sentence1 = pos_tag(word_tokenize(sentence1))
    sentence2 = pos_tag(word_tokenize(sentence2))
 
    # Get the synsets for the tagged words
    synsets1 = [tagged_to_synset(*tagged_word) for tagged_word in sentence1]
    synsets2 = [tagged_to_synset(*tagged_word) for tagged_word in sentence2]
 
    # Filter out the Nones
    synsets1 = [ss for ss in synsets1 if ss]
    synsets2 = [ss for ss in synsets2 if ss]
 
    score, count = 0.0, 0
    
    # For each word in the first sentence
    for synset in synsets1:
        
        best_score = None
        # Get the similarity value of the most similar word in the other sentence
        if ss is not None:
            best_score = max([synset.wup_similarity(ss) for ss in synsets2])                    
 
        # Check that the similarity could have been computed
        if best_score is not None:
            score += best_score
            count += 1
 
    # Average the values
    if count is not 0 :
        score /= count
    
    
    return score
def similarity(value1, value2):
    m = []
    for v1 in value1:
        linha = []
        for v2 in value2:
            linha.append(sentence_similarity(v1, v2))
            print "Similarity(\"%s\", \"%s\") = %s" % (v1, v2, sentence_similarity(v1, v2))
        m.append(linha)
    
    return m

def functionVA(alpha, x, S):
    soma = 0.0
   
    for i in range(len(x)):
        for j in range(len(S)):
            soma = soma + (1-abs(x[i][j] - S[i][j]))
            print soma

    return soma

def CMGIP(alpha,X_N,X_E,N1,N2,E1,E2):
    #similarityVM = similarity(N1,N2)
    #similarityAM = similarity(E1,E2)

    similarityVM = [[0.3704,0.2,0.3333,0.3846],[0.3704,0.2,0.3333,0.3846],[0.1739,0.375,0.2857,0.2105],[0.2857,	0.2857,0.8333,0.3529]]
    similarityAM =[[0.4,1,0.2857,0.5], [0.4,1,0.2857,0.5], [0.4,1,0.2857,0.5], [0.4,0.5,0.2857,0.5]]


    valueFv = functionVA(alpha,X_N,similarityVM)
    valueFa = functionVA(alpha,X_E,similarityAM)

    fx = (((alpha/(len(N1)*len(N2))) * valueFv) +  (((1-alpha)/(len(E1)*len(E2))) * valueFa))
    
    return fx

alpha = 0.2

X_N = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]

X_E = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]

N1	= ["Cat", "Family","Food","Father"]

N2	= ["Truck", "Wheel","Price","Fuel"]

E1 = ["like", "have","feed","acquire"]

E2 = ["have", "have","have","need"]


valueFx = CMGIP(alpha,X_N,X_E,N1,N2,E1,E2)

print "Similarity F(X) = (\"%s\")" % (valueFx)

print "Alpha = (\"%s\")" % (alpha)



