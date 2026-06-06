from flask import render_template, session
import pandas as pd
import plotly.express as px

@app.route('/plotly')
def apps_plotly():

    df = pd.read_csv('g23_Podcasts_Guests.csv', sep=';', header=1)
    df.columns = df.columns.str.strip()

    print(df.columns.tolist())  # para verificar as colunas

    df['date'] = pd.to_datetime(df['date'], dayfirst=True, errors='coerce')
    df['creation_date'] = pd.to_datetime(df['creation_date'], dayfirst=True, errors='coerce')

    top_convidados = df['name'].value_counts().head(10).reset_index()
    top_convidados.columns = ['Convidado', 'Participações']

    fig = px.bar(
        top_convidados,
        x='Participações',
        y='Convidado',
        orientation='h',
        title='Top 10 Convidados com Mais Participações no Podcast',
        labels={
            'Participações': 'Número de Episódios',
            'Convidado': 'Nome do Convidado'
        },
        color='Participações',
        color_continuous_scale='Tealgrn'
    )

    fig.update_layout(
        yaxis={'categoryorder': 'total ascending'},
        template='plotly_white',
        showlegend=False
    )

    fig.update_traces(
        texttemplate='%{x}',
        textposition='outside'
    )

    plot_div = fig.to_html(full_html=False)

    return render_template(
        'plotly.html',
        plot_div=plot_div,
        ulogin=session.get("user")
    )
