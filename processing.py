from plotly import graph_objects as go
import pandas as pd
import nltk
from scipy import signal

nltk.download('punkt')

df=pd.read_csv("migunamiguna_tweets.csv")
df.columns
def getTimePlot():
    df.created_at=[x.replace(" +0000","") for x in df.created_at]
    df.created_at=pd.to_datetime(df.created_at,format="%a %b %d %H:%M:%S %Y")
    tData=df.created_at.dt.strftime("%H:%M").value_counts().to_frame().reset_index()
    tData.columns=["Time of Day","Count"]
    tData=tData.sort_values(by=["Time of Day"]).reset_index(drop=True)
    fig=go.Figure()
    fig.add_trace(
        go.Scatter(
            x=tData["Time of Day"],
            y=tData["Count"],
            mode="markers",
            name="Tweets"
        )
    )
    fig.add_trace(
        go.Scatter(
            x=tData["Time of Day"],
            y=signal.savgol_filter(tData["Count"],
                53, # window size used for filtering
                3), # order of fitted polynomial
            mode="lines",
            marker=dict(
                color="red"
            ),
            text=["<b>Time of Day : <b> {}".format(x) for x in tData["Time of Day"]],
            name="Smoothed Trend line"
        )
    )
    return fig




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


from textgenrnn import textgenrnn

textgen = textgenrnn()
textgen.generate()

textgen_2 = textgenrnn('/weights/hacker_news.hdf5')
textgen_2.generate(3, temperature=1.0)

import tensorflow as tf
tf.config.experimental.list_physical_devices(device_type=None)
tf.config.experimental_list_devices()