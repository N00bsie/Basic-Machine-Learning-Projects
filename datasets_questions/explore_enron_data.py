#!/usr/bin/python
""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import pandas as pd
import numpy as np

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))
print("Length of the dictionary is " + str(len(enron_data)))
dictionary_length = len(enron_data)
#for all counts
poi_count  = 0
quantified_salary_count = 0
email_address_count = 0


for x in enron_data:
    print(x + " : " + str(len(enron_data[x])))
#     print(enron_data[x])
    if(enron_data[x]["poi"] == 1):
        poi_count +=1
    if(enron_data[x]['salary'] == 'NaN'):
        quantified_salary_count +=1
    if(enron_data[x]['email_address'] == 'NaN'):
        email_address_count +=1
        

quantified_salary_count = dictionary_length - quantified_salary_count
email_address_count = dictionary_length - email_address_count
print("\nPOIs in the Enron E+F dataset :" + str(poi_count))
print("\nPeople having a quantified salary :" + str(quantified_salary_count))
print("\nPeople having a known email address : " + str(email_address_count))

print("\nTotal Stock value of James Prentice : " + str(enron_data["PRENTICE JAMES"]['total_stock_value']))

print("Email messages from Wesley Colwell to POI : " + str(enron_data['COLWELL WESLEY']['from_this_person_to_poi']))

print("Value of stock options by Jeffrey K Skilling : " + str(enron_data['SKILLING JEFFREY K']['exercised_stock_options']))

print("\n")
#Adding pandas for no specific reason
data = {'name' : ['SKILLING JEFFREY K','LAY KENNETH L','FASTOW ANDREW S'],
        'total_payments' : [enron_data['SKILLING JEFFREY K']['total_payments'],enron_data['LAY KENNETH L']['total_payments'],enron_data['FASTOW ANDREW S']['total_payments']]}
pandasData = pd.DataFrame(data)
index = pandasData['total_payments'].idxmax()
print(pandasData.iloc[index])