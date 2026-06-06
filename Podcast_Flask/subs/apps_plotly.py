from flask import render_template, session
from classes.podcast import Podcast
from classes.sponsor import Sponsor
from classes.theme import Theme
from classes.participation import Participation
from classes.guest import Guest
from datafile import filename

import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px

def apps_plotly():

    engine = create_engine('sqlite:///' + filename + 'podcast.db')

    df_guest = pd.read_sql('Guest', con=engine)
    df_participation = pd.read_sql('Participation', con=engine)

    participacoes = (
        df_participation
        .groupby('guest_id')
        .size()
        .reset_index(name='Participações')
    )

    participacoes = participacoes.merge(
        df_guest[['id', 'name']],
        left_on='guest_id',
        right_on='id'
    )

    top_convidados = participacoes.nlargest(10, 'Participações')

    fig = px.bar(
        top_convidados,
        x='Participações',
        y='name',
        orientation='h',
        title='Top 10 Convidados com Mais Participações'
    )

    plot_div = fig.to_html(full_html=False, div_id='my-plot')

    return render_template(
        "plotly.html",
        plot_div=plot_div,
        ulogin=session.get("user")
    )
