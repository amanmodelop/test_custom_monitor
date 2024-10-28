
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
    print(data.head(),data.columns)
    field1=data['Risk Management']

    config=load_config("./tables.json")


    cat1=final_rating(config,field1)
    
    final_result={
    "cat1":cat1
    }
    yield final_result
    

def main():
    data = {"data1":993,"data2":36,"data3":3959,"label_value":0,"score":1}
    df = pd.DataFrame.from_dict([data])
    print(json.dumps(next(metrics(df)), indent=2))


if __name__ == '__main__':
	main()        
