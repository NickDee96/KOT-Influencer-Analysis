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
from scipy import signal

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

def getTimePlot():
    df.created_at=[x.replace(" +0000","") for x in df.created_at]
    df.created_at=pd.to_datetime(df.created_at,format="%a %b %d %H:%M:%S %Y")
    tData=df.created_at.dt.strftime("%H:%M").value_counts().to_frame().reset_index()
    tData.columns=["Time of Day","Count"]
    tData=tData.sort_values(by=["Time of Day"]).reset_index(drop=True)
    fig=go.Figure()
    fig=fig.add_trace(
        go.Scatter(
            x=tData["Time of Day"],
            y=tData["Count"],
            mode="markers",
            name="Tweets"
        )
    )
    fig=fig.add_trace(
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
    ]),
    dbc.Row([
        dbc.Col([
            html.H3(
                children="Tweet Frequency across the day"
            ),
            html.Div([
                dcc.Graph(
                    id="time_plot",
                    figure=getTimePlot()
                )
            ])
        ])
    ])
])
if __name__=="__main__":
    app.run_server(debug=True)