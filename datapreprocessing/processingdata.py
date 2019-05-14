from cltk.tokenize.sentence import TokenizeSentence
import dataExtraction.datapreprocessing.parser as parser
import dataExtraction.datapreprocessing.stopword as stopword

stop=stopword.stopwords()
stemmer=parser.Stemmer()

def clean(str):
    stop_free = " ".join([i for i in str if i not in stop])
    #punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
    #normalized = " ".join(lemma.lemmatize(word) for word in stop_free.split())
    stemm_line=" ".join(stemmer.stem_word(word) for word in stop_free.split())
    y = stemm_line.split()
    return y

def cleaning_data(str):
    tokenizer = TokenizeSentence('bengali')
    bengali_text_tokenize = tokenizer.tokenize(str)
    # print(bengali_text_tokenize)
    cleaned = clean(bengali_text_tokenize)
    cleaned = ' '.join(cleaned)
    return cleaned

def tokenizer(str):
    tokenizer = TokenizeSentence('bengali')
    bengali_text_tokenize = tokenizer.tokenize(str)
    return bengali_text_tokenize
