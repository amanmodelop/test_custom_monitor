import json
import pandas as pd
from pathlib import Path
import random
#import modelop.utils as utils


#import modelop_sdk.restclient.moc_client as moc_client
def generate_random_rating():
    values=["l","m","h"]
    return random.choice(values)
def map(val):
     map={"l":1,"m":2,"h":3}
     return map[val]
     

# modelop.init
def init(init_param):
    #logger = utils.configure_logger()
    pass


# modelop.metrics
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
    "data":{
        "risk_data":[map(cat1),map(cat2),map(cat3),map(cat4),map(cat5),map(cat6)]
        },
    "categories": ["cat1","cat2","cat3","cat4","cat5","cat6"]
    }
    }
    yield final_result
