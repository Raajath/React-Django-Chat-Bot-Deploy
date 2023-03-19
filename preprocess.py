# cleaning
import re 
# module for matching regular expressions
# s="Hi , i am rajath and i am ||| running coding in between"
s="Give me the better of Roshan Sir's cabin"

s=re.sub(r'[^\w\s]','',s)

#\w-- word
# ^-not 
# \s-space character 

# this code for to allow only space and words (whichever is not a word or space characater replace it with '')
print("This removes all unwanted punctuations...: ",s)

#tokenization 
#alternate use split

#this is standard
import nltk
nltk.download('punkt')
nltk.download('wordnet')#dependencies 

tokens=nltk.word_tokenize(s)
print(tokens)

#removing unwanted words

from nltk.corpus import stopwords 
# eg 'or' 'and'  'conjunctions' 'the'
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
  
  

stop_words = set(stopwords.words('english'))
print("Stop word : ",stop_words)


# converts the words in word_tokens to lower case and then checks whether 
#they are present in stop_words or not
# geeks code needs improvement tommorow discussion
# filtered_sentence = [w for w in tokens if not w.lower() in stop_words]
#with no lower case conversion
filtered_sentence = []
  
for w in tokens:
    if w not in stop_words:
        filtered_sentence.append(w)
  
print(tokens)
print(filtered_sentence)

#stemming we will not use

# lemmatization 

from nltk.stem import WordNetLemmatizer
  
lemmatizer = WordNetLemmatizer()


from nltk.stem import PorterStemmer
# create an object of class PorterStemmer
porter = PorterStemmer()

lemma=[]
st=[]

for i in range(len(filtered_sentence)):
    lemma.append(lemmatizer.lemmatize(filtered_sentence[i],'a'))
    st.append(porter.stem(filtered_sentence[i]))

print("Lemmatized string : \n\n",lemma)  
print("Stemming pattern : \n",st) 

# tags to tell if noun or verb so on POS
from nltk import pos_tag
nltk.download('averaged_perceptron_tagger')
tags = tokens_tag = pos_tag(filtered_sentence)
print(tags)

#tags meaning

"""
CC: It is the conjunction of coordinating
CD: It is a digit of cardinal
DT: It is the determiner
EX: Existential
FW: It is a foreign word
IN: Preposition and conjunction
JJ: Adjective
JJR and JJS: Adjective and superlative
LS: List marker
MD: Modal
NN: Singular noun
NNS, NNP, NNPS: Proper and plural noun
PDT: Predeterminer
WRB: Adverb of wh
WP$: Possessive wh
WP: Pronoun of wh
WDT: Determiner of wp
VBZ: Verb
VBP, VBN, VBG, VBD, VB: Forms of verbs
UH: Interjection
TO: To go
RP: Particle
RBS, RB, RBR: Adverb
PRP, PRP$: Pronoun personal and professional
"""





