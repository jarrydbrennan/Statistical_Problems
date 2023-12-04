# Import libraries
import codecademylib3
import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency
from scipy.stats import binom_test

# Read in the `clicks.csv` file as `abdata`
abdata = pd.read_csv('clicks.csv')

print(abdata.head())
#Two Categorical variables thus Chi2 Test for A/B effectiveness
Xtab = pd.crosstab(abdata.group, abdata.is_purchase)
print(Xtab)

chi2,pval,dof,expected = chi2_contingency(Xtab)
print("With a P Value of",pval,"there is significant difference in purchase rate for groups A,B,C.")

#Number of visitors
num_visits = len(abdata)
print(num_visits)
#Number of purchases at each test price to hit sales goals
num_sales_needed_099 = 1000/.99
print(num_sales_needed_099)
p_sales_needed_099 = num_sales_needed_099/num_visits#*100
print((p_sales_needed_099),'percent of visitors would need to make a purchase at 99cents to hit $1k in sales')

num_sales_needed_199 = 1000/1.99
print(num_sales_needed_199)
p_sales_needed_199 = num_sales_needed_199/num_visits#*100
print((p_sales_needed_199),'percent of visitors would need to make a purchase at 1.99 to hit $1k in sales')

num_sales_needed_499 = 1000/4.99
print(num_sales_needed_499)
p_sales_needed_499 = num_sales_needed_499/num_visits#*100
print((p_sales_needed_499),'percent of visitors would need to make a purchase at 4.99 to hit $1k in sales')
#sample size for each Group
samp_size_099 = np.sum(abdata.group == 'A')
sales_099 = np.sum((abdata.group == 'A') & (abdata.is_purchase == 'Yes'))

samp_size_199 = np.sum(abdata.group == 'B')
sales_199 = np.sum((abdata.group == 'B') & (abdata.is_purchase == 'Yes'))

samp_size_499 = np.sum(abdata.group == 'C')
sales_499 = np.sum((abdata.group == 'C') & (abdata.is_purchase == 'Yes'))

#Is it significant?
pvalueA = binom_test(sales_099, samp_size_099, p_sales_needed_099, alternative = 'greater')
print(pvalueA, "for Group A vs proportion needed")
pvalueB = binom_test(sales_199, samp_size_199, p_sales_needed_199, alternative = 'greater')
print(pvalueB, "for Group B vs proportion needed")
pvalueC = binom_test(sales_499, samp_size_499, p_sales_needed_499, alternative = 'greater')
print(pvalueC, "for Group C vs proportion needed")
print('To hit the minimum revenue target, Group C is the only group with a purchase rate significantly higher than what is needed to hit the target. Therefore, Brian should charge 4.99 for the upgrade.')
