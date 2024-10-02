import json
import pandas as pd
import random
def generate_random_rating():
    values=["l","m","h"]
    return random.choice(values)


#modelop.init
def init(init_param):
      pass


#modelop.metrics
def metrics():
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
    "categories":["abc","cde","def"]
        }
    }
}
    return final_result

def main():
	data = '''
		{ "foo": 2.2,
		  "bar": 1.3,
		  "strvalue": "foo",
		  "objectvalue": {
		  	"val1": 0.8392,
		  	"val2": 0.987
		  }
		}
	'''
	data_dict = json.loads(data)
	df = pd.DataFrame.from_dict([data_dict])
	print(next(metrics(df)))


if __name__ == '__main__':
	main()