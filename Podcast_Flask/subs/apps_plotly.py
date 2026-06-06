from flask import render_template, session
from datafile import filename

import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px


def apps_plotly():

    

    DATABASE = "DadaBase_Podcast.db"

    TABLE = "Participation"

    X_COLUMN = "guest_id"      
    Y_LABEL = "Participações"

    GRAPH_TITLE = "Top 10 Convidados com Mais Participações"

    

    engine = create_engine(f"sqlite:///{DATABASE}")

    df = pd.read_sql(f"SELECT * FROM {TABLE}", con=engine)

    dados = (
        df[X_COLUMN]
        .value_counts()
        .head(10)
        .reset_index()
    )

    dados.columns = [X_COLUMN, Y_LABEL]

    fig = px.bar(
        dados,
        x=Y_LABEL,
        y=X_COLUMN,
        orientation='h',
        title=GRAPH_TITLE,
        color=Y_LABEL,
        color_continuous_scale='Tealgrn'
    )

    fig.update_layout(
        template='plotly_white',
        showlegend=False,
        yaxis={'categoryorder': 'total ascending'},
        height=700,
        bargap=0.15,
        margin=dict(l=120,r=40,t=80,b=40
    )


    fig.update_traces(
        texttemplate='%{x}',
        textposition='outside'
    )

    plot_div = fig.to_html(
        full_html=False,
        div_id='my-plot'
    )

    return render_template(
        "plotly.html",
        plot_div=plot_div,
        ulogin=session.get("user")
    )
