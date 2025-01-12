import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv
from numpy.f2py.crackfortran import kindselector
from setuptools.command.rotate import rotate
with open('test1.csv', 'r', encoding='UTF-8') as file:
     data = pd.read_csv(file, delimiter=';')
     dataId = data.IDLogin# один столбец
     dataId = dataId.drop_duplicates()# удаляем дубликаты
     data_val = dataId.values
cond = data[data['IDLogin'] == 20]
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
plt.legend([6, 20])
plt.xticks(rotation=90)
plt.show()