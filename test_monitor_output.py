
import json
import pandas as pd
from pathlib import Path
import random
#import modelop.utils as utils


#import modelop_sdk.restclient.moc_client as moc_client
def generate_random_rating():
    values=["L","M","H"]
    return random.choice(values)
def map(val):
     map={"L":1,"M":2,"H":3}
     return map[val]

def load_config(file):
     with open(file,"r") as f:
          return json.load(f)
     
def final_rating(config,field):
    scoring_table=config.get("scoring_table")
    inherent_risk_rating=config.get("inherent_risk_rating")
    random_combined_rating=scoring_table.get(field)
    category=None
    for lower,upper,level in inherent_risk_rating:
         if lower<=random_combined_rating<=upper:
              category=level
              return category     

# modelop.init
def init(init_param):
    #logger = utils.configure_logger()
    pass


# modelop.metrics
def metrics(data: pd.DataFrame):
    print("Running the metrics function") 
    config=load_config("./tables.json")
    field1=data['Risk Management'][0].get('What is the algorithmic complexity of the AI Product?').split()[0]
    field2=data['Risk Management'][0].get('What is the final state of the training data?').split()[0]
    field3=data['Risk Management'][0].get('Select the highest data classification used to build/use the AIP (e.g., training, validation, input data).').split()[0]
    field4=data['Risk Management'][0].get('What is the acceptable predictive accuracy of the AI Product relative to expected performance target(s)?').split()[0]
    field5=data['Risk Management'][0].get('Is the data used in the AI Product (e.g., training, validation, input, grounding) subject to data use restrictions?').split()[0]
    field6=data['Risk Management'][0].get('How controlled is the input data field?').split()[0]

    #other questions
    field7=data['Overview'][0].get('Select the intended use of the AI Product.')[:1]
    field8=data['Overview'][0].get('What is the opportunity cost of not having the AI Product?').split()[0]
    field9=data['Overview'][0].get('What is the impact to business operations if the AIP is not available for use?').split()[0]
    field10=data['Risk Management'][0].get("What is the potential impact to a data subject's (i.e., Employees, Customers, Consumers, Prospects, Applicants, etc.) legal rights (or similar) from an AIP decision?").split()[0]


    

    cat1=final_rating(config,field1)
    cat2=final_rating(config,field2)
    cat3=final_rating(config,field3)
    cat4=final_rating(config,field4)
    cat5=final_rating(config,field5)
    cat6=final_rating(config,field6)
    final_result={
    "cat1":cat1,"cat2":cat2,"cat3":cat3,"cat4":cat4,"cat5":cat5,"cat6":cat6,
    "risk":[{"cat1":cat1}]
    }
    yield final_result
    

def main():
    data = {"data1":993,"data2":36,"data3":3959,"label_value":0,"score":1}
    df = pd.DataFrame.from_dict([data])
    print(json.dumps(next(metrics(df)), indent=2))


if __name__ == '__main__':
	main()        
