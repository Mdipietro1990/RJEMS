import nltk
nltk.download()
doc_list = ['Doc1.txt','Doc2.txt', 'Doc3.txt','Doc4.txt','Doc5.txt']
for i in doc_list:
    file = open(i, 'rt')
    text = file.read()
    file.close()
    # split into words by white space
    words = text.split()
    # convert to lower case
    words = [word.lower() for word in words]
    print(words[:100])
