from flask import render_template, session
from datafile import filename

import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px


def apps_plotly():

    

    DATABASE = filename + "DadaBase_Podcast.db"

    TABLE_1= "Participation"

    engine = create_engine(f"sqlite:///{DATABASE}")

    X_COLUMN = "guest_id"      
    Y_LABEL = "Participações"

    GRAPH_TITLE = "Top 10 Convidados com Mais Participações"


    df1 = pd.read_sql(f"SELECT * FROM {TABLE_1}", con=engine)

    #GRÁFICO 1
    dados = (
        df1[X_COLUMN]
        .value_counts()
        .head(10)
        .reset_index()
    )

    dados.columns = [X_COLUMN, Y_LABEL]

    fig1 = px.bar(
        dados,
        x=Y_LABEL,
        y=X_COLUMN,
        orientation='h',
        title=GRAPH_TITLE,
        color=Y_LABEL,
        color_continuous_scale='Tealgrn'
    )

    fig1.update_layout(
        template='plotly_white',
        showlegend=False,
        yaxis={'categoryorder': 'total ascending'},
        height=700,
        bargap=0.15,
        margin=dict(l=120,r=40,t=80,b=40)
    )


    fig1.update_traces(
        texttemplate='%{x}',
        textposition='outside'
    )

    plot_div1 = fig1.to_html(
        full_html=False,
        div_id='my-plot1'
    )

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
    
    df_metricas.columns = [
        'Tema',
        'Média',
        'Máximo',
        'Mínimo'
    ]
    
    df_melt = df_metricas.melt(
        id_vars='Tema',
        value_vars=['Média', 'Máximo', 'Mínimo'],
        var_name='Métrica',
        value_name='Valor'
    )
    
    fig2 = px.bar(
        df_melt,
        x='Tema',
        y='Valor',
        color='Métrica',
        barmode='group',
        text_auto='.0f',
        title='Análise por Tema: Média, Máximo e Mínimo',
        color_discrete_sequence=[
            'hotpink',
            'deeppink',
            'lightpink'
        ]
    )
    
    fig2.update_traces(
        textposition='outside'
    )
    
    fig2.update_layout(
        template='plotly_white',
        height=650,
        margin=dict(
            t=100,
            b=50,
            l=50,
            r=50
        ),
        yaxis=dict(
            range=[0, df_melt['Valor'].max() * 1.15]
        )
    )
    
    plot_div2 = fig2.to_html(
        full_html=False,
        div_id='my-plot2'
    )
    

    # GRÁFICO 3
    df3=pd.read_sql("""
        SELECT t.subject, COUNT(*) as total_participantes
        FROM Participation p
        JOIN Theme t ON p.podcast_id = t.podcast_id
        GROUP BY t.subject
        ORDER BY total_participantes DESC
    """, con=engine)
    
    df_participantes = (
        df3.groupby('subject')
        .size()
        .reset_index(name='total_participantes')
    )
    
    df_participantes = df_participantes.sort_values(
        by='total_participantes',
        ascending=False
    )
    
    fig3 = px.bar(
        df_participantes,
        x='subject',
        y='total_participantes',
        title='Número Total de Participantes por Tema',
        color='total_participantes',
        color_continuous_scale='Bluered',
        text_auto=True
    )
    
    fig3.update_traces(
        width=0.6,
        textposition='outside'
    )
    
    fig3.update_layout(
        template='plotly_white',
        height=550,
        margin=dict(
            t=100,
            b=50,
            l=50,
            r=50
        ),
        xaxis_title="Tema",
        yaxis_title="Total de Participantes",
        yaxis=dict(
            range=[
                0,
                df_participantes['total_participantes'].max() * 1.15
            ]
        ),
        coloraxis_showscale=False
    )
    
    plot_div3 = fig3.to_html(
        full_html=False,
        div_id='my-plot3'
    )


    # GRÁFICO 4
    TABLE_4= "Podcast"
    df4 = pd.read_sql(f"SELECT * FROM {TABLE_4}", con=engine)


    top_categorias = (
        df4['category']
        .value_counts()
        .head(5)
        .reset_index(name='Total')
    )
    
    fig4 = px.bar(
        top_categorias,
        x='Total',
        y='category',
        orientation='h',
        title='As 5 Categorias Mais Comuns no Projeto',
        labels={
            'Total': 'Número de Podcasts',
            'category': 'Categoria'
        },
        color='Total',
        color_continuous_scale='Blues'
    )
    
    fig4.update_layout(
        template='plotly_white',
        yaxis={'categoryorder': 'total ascending'},
        showlegend=False,
        height=550,
        margin=dict(
            t=80,
            b=50,
            l=120,
            r=50
        )
    )
    
    fig4.update_traces(
        texttemplate='%{x}',
        textposition='outside'
    )
    
    plot_div4 = fig4.to_html(
        full_html=False,
        div_id='my-plot4'
    )
    return render_template(
        "plotly.html",
        plot_div1=plot_div1,
        plot_div2=plot_div2,
        plot_div3=plot_div3,
        plot_div4=plot_div4,
        ulogin=session.get("user")
    )

