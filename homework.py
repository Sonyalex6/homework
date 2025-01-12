import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv


with open('test1.csv', 'r', encoding='UTF-8') as file:
     data = pd.read_csv(file, delimiter=';')
     dataId = data.IDLogin# один столбец
     dataId = dataId.drop_duplicates()# удаляем дубликаты
     data_val = dataId.values
for id in data_val:# фильтруем по мерчанту
     cond = data[data['IDLogin'] == id]
     group_date = cond.groupby(['DATE'])['DATE'].max()
     group_cond = cond.groupby(['DATE'])['Sum'].sum()
     X, Y = [], []
     for date in group_date:
            X.append(date)
     for rows in group_cond:
            Y.append(rows)
     plt.plot(X, Y)
     group_cond.plot.bar()
plt.title('billing')
plt.xlabel('Дата')
plt.ylabel('Траффик')
plt.legend(data_val)
plt.xticks(rotation=30)
plt.show()