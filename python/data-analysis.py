import pandas as pd

file_path = 'high_diamond_ranked_10min.csv'
data = pd.read_csv(file_path)
data_describe = data.describe()
lines, columns = data.shape
data_head = data.head(10)
cont_values = data['blueWins'].value_counts()

print(data) # Mostra a tabela completa do data frame
print(data_describe) # Mostra a table resumida, com informações como: contagem, média, desvio padrão, valor mínimo, quartis e valor máximo
print("Lines: ", lines, "Columns: ", columns) # Mostra o número de linhas e colunas do data frame
print(data_head) # Mostra o determinado número das primeiras linhas do data frame
print(cont_values)