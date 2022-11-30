import pandas as pd
import math
import json

def calculate_mean(data):
    sum=0
    for val in data:
        sum+=val
    mean=sum/len(data)
    return mean

data = pd.read_csv("./datasets/salary.csv")
headers = data.columns.values
X=data[headers[0]]
Y=data[headers[1]]
X=X.truncate(0,4899)
Y=Y.truncate(0,4899)
X_mean=calculate_mean(X)
Y_mean=calculate_mean(Y)
upper=0
lower=0
for indx in range(len(X)):
    upper+=(X[indx]-X_mean)*(Y[indx]-Y_mean)
    lower+=math.pow(X[indx]-X_mean,2)
m=upper/lower
c=Y_mean-(m*X_mean)
trained_data={}
trained_data["m"]=m
trained_data["c"]=c
trained_data["Y_mean"]=Y_mean
with open("./trained/trained_data.txt",'w') as file:
    file.write(json.dumps(trained_data))