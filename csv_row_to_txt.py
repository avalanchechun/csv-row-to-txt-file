# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 02:35:23 2020

@author: PAULHUANG
"""
import csv
import pandas as pd
reader = pd.read_excel('C:/Users/paul3/Desktop/NRCLex-master/Dataset detecting Insults in Social Commentary/train_cleaned1513justtext.xlsx', encoding='utf-8')
rownumber = 0
for row in reader.values:
    g=open("C:/Users/paul3/Desktop/Big 5 personality traits using ibm watson/Tweets_Texts/anyfile"+str(rownumber)+".txt","w")
    g.write(str(row)[2:-2])
    rownumber = rownumber + 1
    g.close()
        
        
        
