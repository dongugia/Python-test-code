from sklearn.feature_extraction.text import CountVectorizer
import os
vectorizer = CountVectorizer(min)
print(vectorizer)
#CountVectorizer(analyzer= word, binary = False, charset = utf-8, charset_error = strict, dtype =<type 'long'>, input = content, lowercase = True,
               # max_df= 1.0 ,max_df=1.0,max_features=None, max_n=None,
               # min_df=1, min_n=None, ngram_range=(1, 1), preprocessor=None,
               # stop_words=None, strip_accents=None, token_pattern=(?u)\b\w\w+\b,
               # tokenizer=None, vocabulary=None)

content = ["How to format my hard disk", "Hard disk format problems"]
X = vectorizer.fit_transform(content)
vectorizer.get_feature_names()
[u'disk',u'format', u'hard', u'how',u'my', u'proplems', u'to']

print(X.toarray().transpose())
DIR = r"C:\Users\DK0626\Desktop\仕事"
posts = [open(os.path.join(DIR, f)).read() for f in os.listdir(DIR)]
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer(min_df = 1)
X_train = vectorizer.fit_transform(posts)
num_samples, num_features = X_train.shape
print("#samples: %d, #features: %d" % (num_samples,num_features)) #samples: 5, #features: 25
print(vectorizer.get_feature_names())