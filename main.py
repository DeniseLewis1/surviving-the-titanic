import csv
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Open and convert titanic1.csv
with open("titanic1.csv", "r") as file:
  data = csv.reader(file, delimiter=",")
  headers = next(data)
  data_list = list(data)
  titanic_data1 = np.array(data_list)

# Open and convert titanic2.csv
with open("titanic2.csv", "r") as file:
  data = csv.reader(file, delimiter=",")
  headers = next(data)
  data_list = list(data)
  titanic_data2 = np.array(data_list)

# Merge two datasets
combined_data = np.concatenate((titanic_data1, titanic_data2), axis=0)

listify = combined_data.tolist()
titanic_lists_to_string = []
for titanic_lists in listify:
  titanic_string = (",").join(titanic_lists)
  titanic_lists_to_string.append(titanic_string)

complete_titanic = ("\n").join(titanic_lists_to_string)

with open("titanic.csv", "w") as file:
  file.write('Survived,Pclass,Name,Sex,Age,Siblings/Spouses Aboard,Parents/Children Aboard,Fare\n')
  file.write(complete_titanic)

dataframe = pd.read_csv("titanic.csv", delimiter=",")
dataframe = dataframe.replace({"Survived": {0: "Did Not Survive", 1: "Survived"}})

sns.scatterplot(x="Age", y="Fare", hue="Survived", data=dataframe)
plt.xlabel("Passenger Age")
plt.ylabel("Passenger Fare")
plt.title("Sinking of the Titanic Survivors")
plt.savefig("titanic.png")