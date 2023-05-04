
"""def db(ele):
    import pyodbc 
    import nltk
    import json
    server = 'LAPTOP-LFH0VJ0R'  # Replace with your server name
    database = 'vp'  # Replace with your database name
#username = 'LAPTOP-LFH0VJ0R\Admin(52)'  # Replace with your username
#password = 'rajathn14'  # Replace with your password
#windows authentication so  no need
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database)

    cursor = cnxn.cursor()
    sn=ele
    pat='%'
    sn=pat+sn+pat
#used placeholder
# Execute a SELECT query to retrieve data from the database
    query = "SELECT * FROM entries WHERE identifier like ?;"
    params = (sn,)
    cursor.execute(query,params)

    results = cursor.fetchall()
    row_list = list(results)
    json_data = json.dumps(row_list)
 
# Iterate over the query results and print them out
    #ans=""
    #for row in results:
   

        
        
    
# Close the cursor and connection to release resources
    cursor.close()

    return json_data
    """

def db(ele):
    import pyodbc 
    import nltk
    import json
    server = 'LAPTOP-LFH0VJ0R'  # Replace with your server name
    database = 'vp'  # Replace with your database name
    #username = 'LAPTOP-LFH0VJ0R\Admin(52)'  # Replace with your username
    #password = 'rajathn14'  # Replace with your password
    #windows authentication so  no need
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database)

    cursor = cnxn.cursor()
    sn = ele
    pat = '%'
    sn = pat + sn + pat

    #used placeholder
    # Execute a SELECT query to retrieve data from the database
    query = "SELECT * FROM entries WHERE identifier like ?;"
    params = (sn,)
    cursor.execute(query, params)

    # Convert the rows to dictionaries
    columns = [column[0] for column in cursor.description]
    results = []
    for row in cursor.fetchall():
        results.append(dict(zip(columns, row)))
    json_data=""
    if results:
        json_data = json.dumps(results)

    # Close the cursor and connection to release resources
    cursor.close()

    return json_data


"""
def db(st):
    from myapp.models import Table

# Get the first Table object with id_name = 'example_id_name'
    table = Table.objects.filter(id_name__icontains=st)


# If the table variable is not None, it means a Table object with id_name = 'example_id_name' was found
    if table:
       
        return table.values_list
    else:
        return 'not found'

"""





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
  

#stemming we will not use


# lemmatization 

    from nltk.stem import WordNetLemmatizer
  
    lemmatizer = WordNetLemmatizer()


    lemma=[]


    for i in range(len(filtered_sentence)):
        lemma.append(lemmatizer.lemmatize(filtered_sentence[i],'v'))

    
    
    for i in lemma:
            ch=db(i)
           
            if ch:
                return ch
  
    import json
    empty=json.dumps("No such name exists")

    return empty
    







