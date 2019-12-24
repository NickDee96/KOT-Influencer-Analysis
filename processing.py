from plotly import graph_objects as go
import pandas as pd
import nltk
nltk.download('punkt')

df=pd.read_csv("migunamiguna_tweets.csv")
df.columns
df.created_at=[x.replace(" +0000","") for x in df.created_at]
df.created_at=pd.to_datetime(df.created_at,format="%a %b %d %H:%M:%S %Y")
df.text

df.created_at[1]

b'{}.format(cnDf["text"][0].decode("utf-8"))
by country
t=cnDf["text"][0].
(b t).encoding()
how are turing developeres paid

combtext=" ".join(df.text)

tokenized=combtext.split(" ")
len(tokenized)

tokenized[2]

handles=[]
for i in tokenized:
    if i.startswith("@"):
        handles.append(i)

handledf=pd.DataFrame(data={"handle":handles}).handle.value_counts().to_frame().reset_index()
handledf.columns=["handle","count"]
handledf.head(20)


df["text"][5]

def gettags(series,sign):
    combtext=" ".join(series)
    combtext=combtext.replace("\n"," ")
    tokenized=combtext.split(" ")
    handles=[]
    for i in tokenized:
        if i.startswith(sign):
            handles.append(i)
    handledf=pd.DataFrame(data={"handle":handles}).handle.value_counts().to_frame().reset_index()
    handledf.columns=["handle","count"]
    return handledf.head(20)

get_top_references(df.text)

from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
def getTfIdf(series):
    stpwds=set(stopwords.words('english'))
    vectorizer = TfidfVectorizer(stop_words=stpwds,ngram_range=(2,3),max_features=20)
    vectorizer.fit_transform(series)
    return vectorizer.get_feature_names()



from textblob import TextBlob
blob=TextBlob("I am. Are you a capitalist (in your delusions) without owning the means of pro")
df.text[250]
blob.sentiment

for  i in df.text:
    blob=TextBlob("I am. Are you a capitalist (in your delusions) without owning the means of pro")
    print(blob.sentiment)