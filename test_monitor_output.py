
import json
import pandas as pd
from pathlib import Path
import random
#import modelop.utils as utils


#import modelop_sdk.restclient.moc_client as moc_client
def generate_random_rating():
    values=["l","m","h"]
    return random.choice(values)


# modelop.init
def init(init_param):
    #logger = utils.configure_logger()
    pass


#modelop.metrics
def metrics(data: pd.DataFrame):
    print("Running the metrics function") 

    cat1=generate_random_rating()
    cat2=generate_random_rating()
    cat3=generate_random_rating()
    cat4=generate_random_rating()
    cat5=generate_random_rating()
    cat6=generate_random_rating()

    final_result={
    "cat1":cat1,"cat2":cat3,"cat3":cat3,"cat4":cat4,"cat5":cat5,"cat6":cat6,
    "risk":[{"cat1":cat1}],"score":[{"cat2":cat2,"cat3":cat3,"cat4":cat4,"cat5":cat5,"cat6":cat6}],
    "horizontal_bar_graph":{
    "title":"title",
    "x_axis_label":"X-axis",
    "y_axis_label":"y-axis",
    "rotated":True, 
    "data":{"data":[1,2,1],
    "categories":["abc","cde","def"]}
    }}
    yield final_result
    

def main():
    data = {"data1":993,"data2":36,"data3":3959,"label_value":0,"score":1}
    df = pd.DataFrame.from_dict([data])
    print(json.dumps(next(metrics(df)), indent=2))


if __name__ == '__main__':
	main()        
     




