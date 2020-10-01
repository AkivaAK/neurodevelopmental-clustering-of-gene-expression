import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


gene_df=pd.read_csv("brainlipo.csv")


means=[]
for x in range(5,len(gene_df.columns)):

    means.append(gene_df.iloc[:,x].mean())

sd=[]
for y in range(5,len(gene_df.columns)):

    sd.append(gene_df.iloc[:,y].std())

print(means)
print(sd)
histplot=means
histplot2=sd
plt.hist(histplot,bins = 10, label="mean",alpha=1)
plt.hist(histplot2,bins=10,label="sd",alpha=0.5)
plt.legend(loc='best')
plt.xlabel('sd and mean')
plt.ylabel('patients')
plt.show()
