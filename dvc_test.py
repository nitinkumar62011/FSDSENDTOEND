import pandas as pd 
data=[
    {"Name":"Nitin kumar","age":24,"city":"Patna"},
    {"Name":"arya kumar","age":23,"city":"kolkatta"},
    {"Name":"Amit kumar","age":21,"city":"Delhi"},
    {"Name":"Anup kumar","age":19,"city":"Noida"}
]

df=pd.DataFrame(data)
df.to_csv("data/data.csv",index=False)