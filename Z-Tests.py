import pandas as pd
import csv
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go
import random

read_csv = pd.read_csv("medium_data.csv")

data = read_csv["reading_time"].tolist()

mean_list = []

def randomMeans():
    setOfMeans = []
    for i in range(0 , 30):
        index = random.randint(0 , len(data))
        value = data[index]
        setOfMeans.append(value)
    samplingMean = statistics.mean(setOfMeans)
    return samplingMean

def setup():
    for j in range(0 , 100):
        randMeans = randomMeans()
        mean_list.append(randMeans)

setup()

sampling_mean = statistics.mean(mean_list)
population_mean = statistics.mean(data)

sampling_stdev = statistics.stdev(mean_list)
population_stdev = statistics.stdev(data)

first_standard_deviation_start , first_standard_deviation_end = population_mean - population_stdev , population_mean + population_stdev
second_standard_deviation_start , second_standard_deviation_end = population_mean - (2 * population_stdev) , population_mean + (2 * population_stdev)
third_standard_deviation_start , third_standard_deviation_end = population_mean - (3 * population_stdev) , population_mean + (3 * population_stdev)

graph = ff.create_distplot([mean_list] , ["Reading Time"] , show_hist = False)
graph.add_trace(go.Scatter(x = [first_standard_deviation_start,first_standard_deviation_start] , y = [0,0.17] , mode = "lines" , name = "Standard Deviation 1 Start"))
graph.add_trace(go.Scatter(x = [second_standard_deviation_start,second_standard_deviation_start] , y = [0,0.17] , mode = "lines" , name = "Standard Deviation 2 Start"))
graph.add_trace(go.Scatter(x = [third_standard_deviation_start,third_standard_deviation_start] , y = [0,0.17] , mode = "lines" , name = "Standard Deviation 3 Start"))
graph.add_trace(go.Scatter(x = [first_standard_deviation_end,first_standard_deviation_end] , y = [0,0.17] , mode = "lines" , name = "Standard Deviation 1 End"))
graph.add_trace(go.Scatter(x = [second_standard_deviation_end,second_standard_deviation_end] , y = [0,0.17] , mode = "lines" , name = "Standard Deviation 2 End"))
graph.add_trace(go.Scatter(x = [third_standard_deviation_end,third_standard_deviation_end] , y = [0,0.17] , mode = "lines" , name = "Standard Deviation 3 End"))
graph.add_trace(go.Scatter(x = [population_mean,population_mean] , y = [0,0.17] , mode = "lines" , name = "mean"))

graph.show()

z_score = (sampling_mean - population_mean)/population_stdev
print(f"Z Score is {z_score}")