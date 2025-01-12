import pandas as pd
import matplotlib.pyplot as plt
arr, el, col = [], [], ['Дата']
with open('test.csv', 'r', encoding='UTF-8') as file:
     data = pd.read_csv(file, delimiter=';')
     dataId = data.IDLogin
     dataId = dataId.drop_duplicates()
     data_val = dataId.values
     for val in range(len(data_val)):
         el.append(0)
     dataDate = data.DATE
     dataDate = dataDate.drop_duplicates()
     dataDate = sorted(dataDate)
     for dat in range(len(dataDate)):
         arr.append([dataDate[dat]] + el)
     count = 0
for id in data_val:
     col.append(id)
     condition = data[data['IDLogin'] == id]
     group_date = condition.groupby(['DATE'])['DATE'].max()
     date_id = group_date.values
     group_cond = condition.groupby(['DATE'])['Sum'].sum()
     sum_id = group_cond.values
     count += 1
     for date in arr:
         for d in range(len(date_id)):
             if date_id[d] == date[0]:
                 date[count] = float(sum_id[d])
                 break
df = pd.DataFrame(arr, columns=col)
df.plot(x="Дата", y=data_val)
plt.xticks(rotation=30)
plt.title('billing')
plt.ylabel('Траффик')
plt.show()