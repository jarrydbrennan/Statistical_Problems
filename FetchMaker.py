# Import libraries
import numpy as np
import pandas as pd
import codecademylib3
from scipy.stats import binom_test
from scipy.stats import f_oneway
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from scipy.stats import chi2_contingency

# Import data
dogs = pd.read_csv('dog_data.csv')
print(dogs.head())

#Are whippets more or less likely than other dogs to be rescue (8%)
whippet_rescue = dogs.is_rescue[dogs.breed == 'whippet']
num_whippet_rescues = np.sum(whippet_rescue == 1)
print(num_whippet_rescues)
num_whippet = len(whippet_rescue)
print(num_whippet)
#binomal test of significance
p_value = binom_test(num_whippet_rescues, num_whippet, .08)
print('With a P Value of',p_value,'the proportion of whippets who are rescues does not significantly differ from 8%')

# Subset to just whippets, terriers, and pitbulls
dogs_wtp = dogs[dogs.breed.isin(['whippet', 'terrier', 'pitbull'])]

#weight averages of mid-sized dogs
wt_whippets = dogs.weight[dogs.breed == 'whippet']
wt_terriers = dogs.weight[dogs.breed == 'terrier']
wt_pitbulls = dogs.weight[dogs.breed == 'pitbull']
#ANOVA
fstat,pval = f_oneway(wt_whippets,wt_terriers,wt_pitbulls)
print('With a P Value of',pval,'there is at least one pair of dogs that are significantly different in weight than another.')
#Tukey's Range Test
tukey_result = pairwise_tukeyhsd(dogs_wtp.weight, dogs_wtp.breed, 0.05)
print(tukey_result)
print("Pitbulls and Whippets weigts are not significantly different. However, the weights of Pitbulls & Terriers and Whippets & Terriers are significantly different.")

# Subset to just poodles and shihtzus
dogs_ps = dogs[dogs.breed.isin(['poodle', 'shihtzu'])]

Xtab = pd.crosstab(dogs_ps.breed, dogs_ps.color)
print(Xtab)
#Chi2 Test
chi2,pval,dof,expected = chi2_contingency(Xtab)
print('With a P Value of',pval,'poodles and shihtzus come in significantly different colors')

