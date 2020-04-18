

def stopwords():
    stop = []
    with open("dataExtraction/datapreprocessing/stopwords-bn.txt", "r") as ins:
        for line in ins:
            stop.append(line.strip('\n'))
    #print(stop)
    return stop

# import  codecs
# def stopwords():
#     stop = []
#     fname = str('C:/Users/BR450s8g180h/Documents/backend/DataExtractionModule/dataExtraction/datapreprocessing/stopwords-bn.txt')
#     with codecs.open(fname, encoding='utf-8') as f:
#         for line in f:
#             stop.append(line.strip('\n'))
#     return stop

#print((stopwords()))