import pandas as pd
import numpy as np
import plotly
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import dash_bootstrap_components as dbc

from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
import nltk
nltk.download("stopwords")

df=pd.read_csv("migunamiguna_tweets.csv")


def getTfIdf(series):
    stpwds=set(stopwords.words('english'))
    vectorizer = TfidfVectorizer(stop_words=stpwds,ngram_range=(2,3),max_features=20)
    vectorizer.fit_transform(series)
    return vectorizer.get_feature_names()



def get_top_references(series,sign):
    combtext=" ".join(series)
    tokenized=combtext.split(" ")
    handles=[]
    for i in tokenized:
        if i.startswith(sign):
            handles.append(i)
    handledf=pd.DataFrame(data={"handle":handles}).handle.value_counts().to_frame().reset_index()
    handledf.columns=["handle","count"]
    return handledf.head(20)["handle"]


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

server = app.server
## Setting up the DashBoard layout
app.layout = html.Div([
    dbc.Row([
        dbc.Col([
            html.H1(
                children="Miguna Miguna tweet analysis",
                style={
                    'text-align': 'center'
                }
            ),
            html.P(
                children="This is an analysis of Miguna Miguna's latest 3200 tweets.",
                style={
                    'text-align': 'center'
                }
            )
        ])
    ]),
    dbc.Row([
        dbc.Col([
            html.Div([
                dbc.Card([
                   dbc.CardBody([
                       html.H3(
                           children="Most Used #tags"
                       ),
                       html.Ul(
                           [html.Ul(x) for x in get_top_references(df.text,"#")]
                       )
                   ]) 
                ])
            ])
        ],width=4),
        dbc.Col([
            html.Div([
                dbc.Card([
                   dbc.CardBody([
                       html.H3(
                           children="Most referenced twitter users"
                       ),
                       html.Ul(
                           [html.Ul(x) for x in get_top_references(df.text,"@")]
                       )
                   ]) 
                ])
            ])
        ],width=4),
        dbc.Col([
            html.Div([
                dbc.Card([
                   dbc.CardBody([
                       html.H3(
                           children="Most used phrases"
                       ),
                       html.Ul(
                           [html.Ul(x) for x in getTfIdf(df.text)]
                       )
                   ]) 
                ])
            ])
        ],width=4)
    ])
])
if __name__=="__main__":
    app.run_server(debug=True)