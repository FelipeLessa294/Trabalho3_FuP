#Você precisa implementar as seguintes funções:
def carrega_arquivo(nome_arquivo: str): 
    na=nome_arquivo.splitlines()
    na[0]
    #Primeira linha do arquivo de treino: Nome e Sobrenome
    #Segunda linha: Data do treino formato será [dia] - [mês] - [ano]
    #linha opcional de peso, formato Peso: [peso]
    #Cada linha subsequente terá o formato:
    #[Nome do exercício]: [peso da primeira série], [repetições na primeira série];[peso da segunda série], [repetições na segunda série];assim até a ultima

    return#Esta função adiciona as informações do arquivo denominado nome_arquivo às suas estruturas de
          #dados para que as chamadas subsequentes às outras funções possam retornar
          #os valores corretos. Nao retorna nada
def pega_exercicios(nome: str, data: str): #-> lista de str

    return # uma lista de todos os nomes de exercícios realizados por nome na data. Pode retornar uma lista vazia.
def pega_conjunto_exercicios(nome: str, data: str, nome_exercicio: str) :
   return #-> lista de tuplas (float, int) uma lista representando os conjuntos de nome_exercicio realizados por nome na data.
             #Cada elemento da lista é uma tupla de dois elementos.
             # O primeiro elemento é um float que representa o peso do exercício em kg.
             # O segundo é um int que representa o número de repetições naquele peso.
             # Pode retornar uma lista vazia.
def pega_treino(nome: str, data: str) :
    return #-> lista de (str, lista de (float, int) tuplas))
           #Retorna uma representação do treino realizado por nome na data.
           # Pode retornar uma lista vazia.
           # Cada exercício do treino é representado por uma string que é o nome do exercício e uma lista.
           # Cada elemento da lista é uma tupla de dois elementos. 
           # O primeiro elemento é um float que representa o peso do exercício em kg. 
           # O segundo é um int que representa o número de repetições naquele peso.
def max_peso_exercicio(nome_exercicio: str) : 
    return #-> (str, str, float) o nome e adata da pessoa que teve o maior peso em nome_exercicio, junto com o peso.
def max_peso_total(nome_exercicio: str) :
   return #-> (str, str, float)Retorna o nome, data peso levatando por uma pessoa no nome_exercicio (contando todas as repetições em uma única série)
          #em todas as séries e repetições de um determinado exercício em um dia. 
          #Portanto, se para o supino, a pessoa A levantasse 100 kg 3 vezes e a pessoa B levantasse 75 kg 5 vezes,
          #essa função retornaria ('B', '11-11-2010 ', 375,0) (assumindo que B realizou este treino em 11 de novembro de 2010). 
          #Esta função pesquisa em todas as datas possíveis. 
def max_peso_data(data: str, peso: float): 
    return
    # -> lista de str 
    # Retorna uma lista de nomes cujo peso corporal era menor que o peso na data