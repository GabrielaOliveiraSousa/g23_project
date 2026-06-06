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
  top_convidados = df['name'].value_counts().head(10).reset_index()
  top_convidados.columns = ['Convidado', 'Participações']
    
  fig_participacoes = px.bar(top_convidados,x='Participações', y='Convidado', orientation='h',title='Top 10 Convidados com Mais Participações no Podcast',labels={'Participações': 'Número de Episódios', 'Convidado': 'Nome do Convidado'},color='Participações',color_continuous_scale='Tealgrn')
  
  fig_participacoes.update_layout(yaxis={'categoryorder': 'total ascending'}, showlegend=False,template='plotly_white')
  fig_participacoes.update_traces(texttemplate='%{x}', textposition='outside')

  plot_div = fig_participacoes.to_html(full_html=False, div_id='my-plot')


  return render_template("plotly.html", plot_div=plot_div, ulogin=session.get("user"))
