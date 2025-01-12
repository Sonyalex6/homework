import random
array_size = 10
random_array = [random.randint(1, 100) for _ in range(array_size)]
print(f"Массив случайных чисел: {random_array}")
array_size = 10
random_array = [random.randint(1, 100) for _ in range(array_size)]
def list_sum(*args):
    s = sum(*args)
    return s
print(list_sum(random_array))
import numpy as np
def get_random_average(min, max, count):
    l = np.random.randint(min, max, count)
    avg = np.mean(l)
    return f'{l=}, {avg=}'
print(get_random_average(1, 100, 20))
import pandas as pd
"""
Пример программы на Python с использованием библиотеки Pandas
для чтения CSV-файла и печати первых пяти строк:
"""
csv_file_path = "/content/drive/MyDrive/Colab Notebooks/example_5kb.csv"
data = pd.read_csv(csv_file_path)
print(data.head(5))
import pandas as pd
import matplotlib.pyplot as plt

"""
 На первом этапе подготовим данные для графика matplotlib.
 Для этого загрузим с локального компьютера подготовленный
 csv файл биллинга по датам каждого мерчанта с суммами транзакций.
 Наша первоочередная задача сгруппировать в pandas данные по мерчанту
 и дате с функцией аггрегации сумм за каждый день по каждому мерчанту.
 Это файл excelweek2017_2018.csv. Сразу еще одно замечание: суммы в файле
 указаны в формате денежном (100,00) через запятую, нам нужна будет точка
 (100.00). Так как функцией DataFrame.replace(',', '.') заменить не получается
 (в файле данные не в списке или словаре), то проще будет обычными средствами
python заменить запятые на точки, убрать двойные кавычки и уже далее обработать pandas
"""
csv_file_path = "/content/drive/MyDrive/Colab Notebooks/excelweek2017_2018.csv"
with open(csv_file_path, 'r', encoding='UTF-8') as csv_file:
    f_str = csv_file.read().replace(',', '.')
    f_str = f_str.replace('\"', '')
with open('test.csv', 'w', encoding='UTF-8') as fl:
    fl.write(f_str)
    import pandas as pd
    import matplotlib.pyplot as plt

    """
    из нового файла читаем данные в DataFrame и вычисляем сумму их по мерчанту и дате
    """
    with open('test.csv', 'r', encoding='UTF-8') as file:
        data = pd.read_csv(file, delimiter=';')
        grouped_data = data.groupby(['IDLogin', 'DATE'])['Sum'].sum()
        print(grouped_data)
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
                arr.append([dataDate[
                                dat]] + el)
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
                        date[count] = float(sum_id[
                                                d])
                        break

        df = pd.DataFrame(arr,
                          columns=col)
        df.plot(x="Дата", y=data_val)
        plt.xticks(rotation=30)
        plt.title('billing')
        plt.xlabel('Дата')
        plt.ylabel('Траффик')
        plt.show()
import random
POPULATION_SIZE = 100
GENES = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP
QRSTUVWXYZ 1234567890, .-;:_!"#%&/()=?@${[]}'''
TARGET1 = "In principio erat Verbum"
TARGET = TARGET1[::-1]
class Individual(object):
	'''
	Класс, представляющий отдельную особь (индивида) в популяции
	'''
	def __init__(self, chromosome):
		self.chromosome = chromosome
		self.fitness = self.cal_fitness()
	@classmethod
	def mutated_genes(self):
		'''
		Создаем случайные гены для мутации
		'''
		global GENES
		gene = random.choice(GENES)
		return gene
	@classmethod
	def create_gnome(self):
		'''
		Создаем хромосому или набор генов
		'''
		global TARGET
		gnome_len = len(TARGET)
		return [self.mutated_genes() for _ in range(gnome_len)]
	def gene_transfer(self, par2):
		'''
		Передаем гены новому поколению индивидов
		'''

		child_chromosome = []
		for gp1, gp2 in zip(self.chromosome, par2.chromosome):
			prob = random.random()
			if prob < 0.45:
				child_chromosome.append(gp1)
			elif prob < 0.90:
				child_chromosome.append(gp2)
			else:
				child_chromosome.append(self.mutated_genes())
		return Individual(child_chromosome)
	def cal_fitness(self):
		'''
		Рассчитываем показатель соответствия, это количество
		символов в строке, которые отличаются от целевой
		строки.
		'''
		global TARGET
		fitness = 0
		for gs, gt in zip(self.chromosome, TARGET):
			if gs != gt: fitness+= 1
		return fitness
def main():
	global POPULATION_SIZE
	generation = 1

	found = False
	population = []
	for _ in range(POPULATION_SIZE):
				gnome = Individual.create_gnome()
				population.append(Individual(gnome))

	while not found:
		population = sorted(population, key = lambda x:x.fitness)
		if population[0].fitness <= 0:
			found = True
			break
		new_generation = []
		s = int((10*POPULATION_SIZE)/100)
		new_generation.extend(population[:s])
		s = int((90*POPULATION_SIZE)/100)
		for _ in range(s):
			parent1 = random.choice(population[:50])
			parent2 = random.choice(population[:50])
			child = parent1.gene_transfer(parent2)
			new_generation.append(child)
		population = new_generation
		print("Generation: {}\tString: {}\tFitness: {}".
			format(generation,
			"".join(population[0].chromosome),
			population[0].fitness))
		generation += 1
	print("Generation: {}\tString: {}\tFitness: {}".
		format(generation,
		"".join(population[0].chromosome),
		population[0].fitness))
if __name__ == '__main__':
	main()
