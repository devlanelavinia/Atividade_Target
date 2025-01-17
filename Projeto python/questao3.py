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
