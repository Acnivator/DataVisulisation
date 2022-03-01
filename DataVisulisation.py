import pandas as pd
import plotly_express as px

df = pd.read_csv("Covid-19.csv")
fig = px.scatter(df,x = "date",y = "cases",color = "country",title = "Covid cases per country")
fig.show()