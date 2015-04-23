import urllib2
import json 
import ast
import numpy as np

# Note
# this code is taken from Azure Request Response API Documentation provided by Microsoft.
# To use this code, please ask API key from the author and replace it in line 31

class Prediction(object):
    
    def __init__(self, APayroll_mean = 0, APayroll_std = 0, Establishment_mean =0, Establishment_std=0, county_health_exp=0, income=0, municipal_health_exp=0, pov=0, revenue=0, state=0):
        inp = list(np.array([APayroll_mean, APayroll_std, Establishment_mean, Establishment_std, county_health_exp, income, municipal_health_exp,pov, revenue,state]).astype(int).astype(str))

        data =  {

                "Inputs": {

                        "input1":
                        {
                            "ColumnNames": ["APayroll_mean", "APayroll_std", "Establishment_mean", "Establishment_std", "county_health_exp", "income", "municipal_health_exp", "pov", "revenue", "state"],
                            "Values": [ inp]
                        },        },
                    "GlobalParameters": {
        }
            }

        self.body = str.encode(json.dumps(data))
    
    def result(self):
        
        url = 'https://ussouthcentral.services.azureml.net/workspaces/3b9d1865c2e8421faa3a516dd3f99318/services/8a3dded9d3e946fbb02a02f004884f9f/execute?api-version=2.0&details=true'
        api_key = '' 
        headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

        if not api_key:
            print(error.info())
            print('Please obtain API key') 
        req = urllib2.Request(url, self.body, headers) 
        
        try:
            response = urllib2.urlopen(req)
            result = response.read()
            result = ast.literal_eval (result)['Results']['output1']['value']['Values'][0][-4:]
            label = result[-1]
            probability = {'better':result[0], 'nominal': result[1], 'worse':result[2]}
            return (label, probability)
        
        except urllib2.HTTPError, error:
            print("The request failed with status code: " + str(error.code))
            # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
            print(error.info())
            print(json.loads(error.read()))                 