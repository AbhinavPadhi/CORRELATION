import csv
import plotly.express as pe
import numpy as np

with open("coffee_sleep.csv") as data:
    df = csv.DictReader(data)
    fig = pe.scatter(df, x = "Coffee in ml" , y = "sleep in hours")
    fig.show()

def getDataSource(data_path):
    marks_in_percentage = []
    days_present = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            marks_in_percentage.append(float(row["Coffee in ml"]))
            days_present.append(float(row["sleep in hours"]))

    return {"x" : marks_in_percentage, "y": days_present}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between coffee and sleep :-  \n--->",correlation[0,1])

def setup():
    data_path  = "coffee_sleep.csv"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()