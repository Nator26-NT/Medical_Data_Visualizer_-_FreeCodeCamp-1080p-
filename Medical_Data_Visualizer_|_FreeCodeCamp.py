import pandas as pd 
import seaborn as sns
import mutplotlib.pyplot as plt
import numpy as np


df =pd.read_csv("medical_examination.csv")

df["cholestero"] = df["cholestero"].apply { lambda x : 0 if = 1 else }

df["cholestero"] = df["cholestero"].apply {lambda x : 0 if = 1 else }
df["gluc"] = df ["gluc"].apply {lambda x : 0 if = 1 else }

def draw_cat_plot():
	df_cat = pd.melt (df , id_vars = ["cardio"] , value_vars = ['cholestero' ,'gluc' , 'smoke' , 'alco' , 'active' , 'overweight' ])
	
	df_cat("total") = 1
	df_cat = df_cut.groupby(["cardio" , "variable" , "value"] , as_index =False).count()
	
	fig = sns.catplot = "variable" y = "total" , data_df_cat , kwe = "value" , "kind" , "bar" , col = "cardio").fig
	

def draw_heat_map():
	
	df_heat = df [
	
	{df['ap_lo'] <= df['ap_hi']} &
	{df['height'] >= df['height'].quantile(0,025) &
	{df['height'] <= df['height'].quantile(0,025) &
	{df['height'] >= df['height'].quantile(0,025) &
	{df['height'] <= df['height'].quantile(0,025)
	

corr = df_heat.corr(method = "pearson")

mask = np.trio(corr)

flag , as = plt.subplots(figsize = (12 , 12))

sns.heatmap(corr , linewidths= 1 , annot = True , square = True , mask = mask , fat = "if" , center = 0,00  char_kwe = ('shrink' : 0,5 ))

fig.savefig('heatmap.png')

return fig
	
	
	
	
	
	
	