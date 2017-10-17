#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 15:21:36 2017

@author: nanthini
"""
import pandas as pd 
import seaborn as sns 
all_salaries = pd.read_csv('data/salaries-by-college-type.csv')
all_salaries.columns = ['School','Type','Starting','Mid', 'Mid_10', 'Mid_25', 'Mid_75', 'Mid_90']
#Remove all $'s
for x in all_salaries.columns:
    if x != 'School' and x!='Type':
        salary = all_salaries[x].str.replace("$", "")
        salary = salary.str.replace(",", "")
        all_salaries[x] = pd.to_numeric(salary)

#Change the sort_by and get graphs for Starting, Mid, Mid_10, etc.
sort_by = 'Mid_90'
top_degrees = all_salaries.nlargest(10, sort_by).reset_index()
#Bar chart view of the data
sns.barplot(sort_by,'School', data=top_degrees)