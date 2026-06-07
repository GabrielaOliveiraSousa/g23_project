from flask import render_template, session
from datafile import filename

import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px


PINK_SCALE = [[0.0, '#ffd9e6'], [0.5, '#ff9cbb'], [1.0, '#ff6595']]
PINK_DISCRETE = ['#ff6595', '#ff9bb6', '#ffd0dd']
FONT_FAMILY = "Segoe UI, system-ui, -apple-system, sans-serif"
TEXT_COLOR = '#4a3e41'
ACCENT = '#ff6595'

PLOT_CONFIG = {'responsive': True, 'displayModeBar': False}


def _style(fig):
    fig.update_layout(
        template='plotly_white',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(family=FONT_FAMILY, color=TEXT_COLOR, size=11),
        title=dict(font=dict(color=ACCENT, size=14, family=FONT_FAMILY),
                   x=0.5, xanchor='center'),
        margin=dict(l=60, r=20, t=46, b=36),
        autosize=True,
    )
    fig.update_xaxes(gridcolor='#ffe4ec', zerolinecolor='#ffe4ec')
    fig.update_yaxes(gridcolor='#ffe4ec', zerolinecolor='#ffe4ec')
    return fig


def _to_html(fig, div_id, first=False):
    return fig.to_html(
        full_html=False,
        include_plotlyjs=True if first else False,
        div_id=div_id,
        default_height='100%',
        default_width='100%',
        config=PLOT_CONFIG,
    )


def apps_plotly():

    DATABASE = filename + "DadaBase_Podcast.db"
    engine = create_engine(f"sqlite:///{DATABASE}")

# GRÁFICO 1 
    Y_LABEL = "Participações"
    GRAPH_TITLE = "Top 10 Convidados com Mais Participações"

    df_participation = pd.read_sql("SELECT * FROM Participation", con=engine)
    df_guests = pd.read_sql("SELECT * FROM Guest", con=engine)

    df_combined = pd.merge(df_participation, df_guests, on='guest_id')

    # 3. Agrupar por nome e contar podcasts únicos 
    dados = (
        df_combined.groupby('name')['podcast_id']
        .nunique()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )
    dados.columns = ['guest_name', Y_LABEL]

  
    dados = dados.sort_values(by=Y_LABEL, ascending=True)
    name_order = dados['guest_name'].tolist()

  
    fig1 = px.bar(
        dados, x=Y_LABEL, y='guest_name', orientation='h',
        title=GRAPH_TITLE, color=Y_LABEL, color_continuous_scale=PINK_SCALE,
    )
    
    fig1.update_layout(
        showlegend=False,
        coloraxis_showscale=False,
        bargap=0.12,
        yaxis=dict(
            categoryorder='array', 
            categoryarray=name_order,
            title=None
        )
    )
    
    fig1.update_traces(texttemplate='%{x}', textposition='outside', cliponaxis=False)
    _style(fig1)
    plot_div1 = _to_html(fig1, 'my-plot1', first=True)

    # GRÁFICO 2
    df2 = pd.read_sql("""
        SELECT t.subject, p.amount
        FROM Participation p
        JOIN Theme t ON p.podcast_id = t.podcast_id
    """, con=engine)

    df_metricas = (
        df2.groupby('subject')['amount']
        .agg(['mean', 'max', 'min'])
        .reset_index()
    )
    df_metricas.columns = ['Tema', 'Média', 'Máximo', 'Mínimo']

    df_melt = df_metricas.melt(
        id_vars='Tema', value_vars=['Média', 'Máximo', 'Mínimo'],
        var_name='Métrica', value_name='Valor',
    )

    fig2 = px.bar(
        df_melt, x='Tema', y='Valor', color='Métrica', barmode='group',
        title='Análise por Tema: Média, Máximo e Mínimo',
        color_discrete_sequence=PINK_DISCRETE,
    )
    fig2.update_layout(
        legend=dict(orientation='h', yanchor='bottom', y=1.0,
                    xanchor='right', x=1, title=None),
        yaxis=dict(range=[0, df_melt['Valor'].max() * 1.15], title=None),
        xaxis=dict(title=None),
    )
    _style(fig2)
    plot_div2 = _to_html(fig2, 'my-plot2')

    # GRÁFICO 3 
    df3 = pd.read_sql("""
        SELECT
            t.subject,
            COUNT(p.guest_id) AS total_participantes
        FROM Participation p
        JOIN Theme t ON p.podcast_id = t.podcast_id
        GROUP BY t.subject
        ORDER BY total_participantes DESC
    """, con=engine)

    fig3 = px.bar(
        df3, x='subject', y='total_participantes',
        title='Número Total de Participantes por Tema',
        color='total_participantes', color_continuous_scale=PINK_SCALE,
        text_auto=True,
    )
    fig3.update_traces(width=0.6, textposition='outside', cliponaxis=False)
    fig3.update_layout(
        xaxis_title=None,
        yaxis_title=None,
        yaxis=dict(range=[0, df3['total_participantes'].max() * 1.15]),
        coloraxis_showscale=False,
    )
    _style(fig3)
    plot_div3 = _to_html(fig3, 'my-plot3')

    # GRÁFICO 4
    df4 = pd.read_sql("SELECT * FROM Podcast", con=engine)

    top_categorias = (
        df4['category']
        .value_counts()
        .head(5)
        .reset_index(name='Total')
    )

    fig4 = px.bar(
        top_categorias, x='Total', y='category', orientation='h',
        title='As 5 Categorias Mais Comuns no Projeto',
        labels={'Total': 'Número de Podcasts', 'category': 'Categoria'},
        color='Total', color_continuous_scale=PINK_SCALE,
    )
    fig4.update_layout(
        showlegend=False,
        coloraxis_showscale=False,
        yaxis={'categoryorder': 'total ascending', 'title': None},
    )
    fig4.update_traces(texttemplate='%{x}', textposition='outside',
                       cliponaxis=False)
    _style(fig4)
    plot_div4 = _to_html(fig4, 'my-plot4')

    return render_template(
        "plotly.html",
        plot_div1=plot_div1,
        plot_div2=plot_div2,
        plot_div3=plot_div3,
        plot_div4=plot_div4,
        ulogin=session.get("user"),
    )
