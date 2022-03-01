import pandas as pd
import plotly.express as px
df=pd.read_csv("data.csv")
print(df.groupby("level")["attempt"].mean())
figure=px.scatter(x=df.groupby("level")["attempt"].mean(),y=['level 1','level 2','level 3','level 4'],orientation='h')
figure.show()