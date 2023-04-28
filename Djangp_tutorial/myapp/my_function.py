def my_function(s):
    # do something with the text here
    # cleaning
    import re 
# module for matching regular expressions
    

    s=re.sub(r'[^\w\s]','',s)
# this code for to allow only space and words (whichever is not a word or space characater replace it with '')


#tokenization 
#alternate use split

#this is standard
    import nltk
    nltk.download('punkt')
    nltk.download('wordnet')

    tokens=nltk.word_tokenize(s)


#removing unwanted words

    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize
    nltk.download('stopwords')
  

  
    stop_words = set(stopwords.words('english'))
  

# converts the words in word_tokens to lower case and then checks whether 
#they are present in stop_words or not
# geeks code needs improvement tommorow discussion
    filtered_sentence = [w for w in tokens if not w.lower() in stop_words]
#with no lower case conversion
    filtered_sentence = []
  
    for w in tokens:
        if w not in stop_words:
            filtered_sentence.append(w)
  

#stemming we will not use ....


# lemmatization 

    from nltk.stem import WordNetLemmatizer
  
    lemmatizer = WordNetLemmatizer()


    lemma=[]


    for i in range(len(filtered_sentence)):
        lemma.append(lemmatizer.lemmatize(filtered_sentence[i],'v'))
  

    return lemma 


