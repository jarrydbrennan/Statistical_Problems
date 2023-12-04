# Import libraries
import pandas as pd
import numpy as np
from scipy.stats import ttest_1samp
from scipy.stats import ttest_ind
from scipy.stats import chi2_contingency

# Load datasets
lifespans = pd.read_csv('familiar_lifespan.csv')
iron = pd.read_csv('familiar_iron.csv')

print(lifespans.head())

vein_pack_lifespans = lifespans.lifespan[lifespans.pack == 'vein']
print('Average lifespan for Vein Pack:', np.mean(vein_pack_lifespans))

tstat, pval = ttest_1samp(vein_pack_lifespans, 73)
print('A 1 sided t-test for Vein Pack lifespans has a P value of',pval,'showing a significant difference compared to the average lifespan of 73.')

artery_pack_lifespans = lifespans.lifespan[lifespans.pack == 'artery']
print('Average lifespan for Artery Pack:', np.mean(artery_pack_lifespans))

tstat,pval = ttest_ind(artery_pack_lifespans,vein_pack_lifespans)
print('The difference in lifespans between the Artery Pack and the Vein pack is not significant due to a P Value of',pval)

print(iron.head())

Xtab = pd.crosstab(iron.pack, iron.iron)
print(Xtab)

chi2,pval,dof,expected = chi2_contingency(Xtab)
print('With a P Value of',pval,'there is a significant difference between packs and iron levels.')

