import csv

climateList = list()  # list for values

headString = ["number", "temperature", "rainfall", "humidity", "apple_yield"]  # heads for columns of csv file


def count_weight_temperature(x):  # function to calculate weight of temperature
    return float(x) * 0.3


def count_weight_rainfall(x):  # function to calculate weight of rainfall
    return float(x) * 0.2


def count_weight_humidity(x):  # function to calculate weight of humidity
    return float(x) * 0.5


def calc_apple_yield(temp, rain, humid):  # function to calculate the apple_yield
    return count_weight_temperature(temp)+count_weight_rainfall(rain)+count_weight_humidity(humid)


with open('climate.txt', encoding='UTF-8') as f:
    infoFromFile = f.readlines()


for i in range(1, len(infoFromFile)):  # append to climateList values from climate.txt
    climateList.append(infoFromFile[i].rstrip().split(','))

for j in range(0, len(climateList)):
    climateList[j].insert(0, j+1)  # insert into climateList sequence number of the region
    climateList[j].append(calc_apple_yield(climateList[j][1], climateList[j][2], climateList[j][3]))  # insert into climateList the value of apple_yield of region

with open('resultPredict.csv', "w") as f:  # create file with all results
    writer = csv.writer(f)
    writer.writerow(headString)
    for j in range(0, len(climateList)):
       writer.writerow(climateList[j])

with open('bestRes.csv', "w") as f:  # create file with the best results
    writer = csv.writer(f)
    writer.writerow(headString)
    for j in range(0, len(climateList)):
        if float(climateList[j][4]) >= 95.00:
            writer.writerow(climateList[j])

with open('worstRes.csv', "w") as f:  # create file with the worst results
    writer = csv.writer(f)
    writer.writerow(headString)
    for j in range(0, len(climateList)):
        if float(climateList[j][4]) <= 25.00:
            writer.writerow(climateList[j])
