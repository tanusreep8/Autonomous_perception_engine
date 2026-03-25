import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def plot_bar(df):
    fig = px.bar(df['label'].value_counts(),
                 title="Object Count",
                 labels={'value': 'Count'})
    return fig

def plot_pie(df):
    fig = px.pie(df, names='label', title="Distribution")
    return fig

def seaborn_plot(df):
    fig, ax = plt.subplots()
    sns.countplot(x='label', data=df, ax=ax)
    return fig