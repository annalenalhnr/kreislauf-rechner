import streamlit as st
import plotly.graph_objects as go  # Plotly für interaktive Diagramme

def plot_results(data, title, xlabel, ylabel):
    # Plotly für Balkendiagramme
    fig = go.Figure([go.Bar(x=list(data.keys()), y=list(data.values()), marker=dict(color='skyblue'))])
    fig.update_layout(
        title=title, 
        xaxis_title=xlabel, 
        yaxis_title=ylabel,
        height=400,  # Höhe des Diagramms
        width=800    # Breite des Diagramms
    )
    
    st.plotly_chart(fig)

def plot_pie_chart(data, title):
    materials = list(data.keys())
    values = list(data.values())
    
    # Plotly Kreisdiagramms
    fig = go.Figure(data=[go.Pie(labels=materials, values=values, hole=0.3, 
                                 hoverinfo="label+percent", textinfo="none", 
                                 marker=dict(colors=['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#19D3F3', '#FF6692']))])

    # Diagrammtitel und Layout-Optionen
    fig.update_layout(
        title=title,
        showlegend=True,
        margin=dict(t=20, b=20, l=20, r=20),  # Abstände für den Diagrammrahmen
        height=400,  # Höhe des Diagramms
        width=800    # Breite des Diagramms
    )

    # Materialnamen und Prozentsätze erscheinen beim Hovern
    st.plotly_chart(fig)