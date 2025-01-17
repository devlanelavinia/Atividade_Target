# Atividades Práticas de Lógica e Análise em Python  

Este repositório contém soluções para cinco desafios práticos de lógica de programação e análise de dados, desenvolvidos em Python. As atividades exploram conceitos como cálculos iterativos, análise de dados em JSON e manipulação de strings.  

## 📋 Atividades  

### 1. Cálculo de somatório  
Um programa que calcula o valor acumulado de uma variável \(SOMA\) com base em um loop que incrementa um contador \(K\).  
  
```python
# Questão 1: Valor da variável SOMA
INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
    K += 1
    SOMA += K

print(f"O valor final de SOMA é: {SOMA}")

### 2. Verificação na sequência de Fibonacci  
Uma solução que verifica se um número informado pertence à sequência de Fibonacci.

# Questão 2: Fibonacci e verificação
def is_fibonacci(num):
    a, b = 0, 1
    while b < num:
        a, b = b, a + b
    return num == b or num == 0

# Entrada do número
number = int(input("Informe um número: "))

if is_fibonacci(number):
    print(f"O número {number} pertence à sequência de Fibonacci.")
else:
    print(f"O número {number} NÃO pertence à sequência de Fibonacci.")


### 3. Análise de faturamento diário  
Análise de dados de faturamento, incluindo:  
- Identificação do menor e maior faturamento diário.  
- Cálculo do número de dias com faturamento acima da média mensal.

# Questão 3: Análise de faturamento diário
import json

# Dados fictícios de faturamento
data = '''
{
    "faturamento": [0, 1000, 1500, 0, 2000, 3000, 0, 0, 4000, 0, 500, 0, 0, 6000]
}
'''

faturamento = json.loads(data)["faturamento"]
faturamento_validos = [valor for valor in faturamento if valor > 0]

menor_valor = min(faturamento_validos)
maior_valor = max(faturamento_validos)
media_mensal = sum(faturamento_validos) / len(faturamento_validos)

dias_acima_media = len([valor for valor in faturamento_validos if valor > media_mensal])

print(f"Menor faturamento: R${menor_valor:.2f}")
print(f"Maior faturamento: R${maior_valor:.2f}")
print(f"Dias acima da média: {dias_acima_media}")
  

### 4. Cálculo percentual por estado  
Calcula a participação percentual de cada estado no faturamento mensal de uma distribuidora, utilizando valores fornecidos.

# Questão 4: Percentual de faturamento por estado
faturamento_estados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

total = sum(faturamento_estados.values())

for estado, valor in faturamento_estados.items():
    percentual = (valor / total) * 100
    print(f"{estado}: {percentual:.2f}%")


### 5. Inversão de string  
Um programa que inverte os caracteres de uma string sem o uso de funções prontas como `reverse()`.

# Questão 5: Inversão de string
def inverter_string(s):
    invertida = ""
    for char in s:
        invertida = char + invertida
    return invertida

string = input("Digite uma string: ")
print(f"String invertida: {inverter_string(string)}")


---

## 🚀 Tecnologias utilizadas  
- **Python 3.10** ou superior  
- Estruturas de controle de fluxo (loops, condicionais)  
- Manipulação de listas e dicionários  
- Processamento de dados em formato JSON  

---

## 🛠️ Como executar  

1. **Clone este repositório**:  
   ```bash
   git clone https://github.com/seu-usuario/atividade_python.git
2. Acesse a pasta do projeto
3. Execute os arquivos individualmente

