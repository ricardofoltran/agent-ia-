# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores |
| `perfil_investidor.json` | JSON | Personalizar recomendações |
| `produtos_financeiros.json` | JSON | Sugerir produtos adequados ao perfil |
| `transacoes.csv` | CSV | Analisar padrão de gastos do cliente |

> [!TIP]
> **Quer um dataset mais robusto?** Você pode utilizar datasets públicos do [Hugging Face](https://huggingface.co/datasets) relacionados a finanças, desde que sejam adequados ao contexto do desafio.

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Os dados mockados foram expandidos com a adição de dois novos produtos financeiros simulados: Fundo Imobiliário e ETF de Mercado Amplo. A estrutura original dos dados foi mantida, com o objetivo de ampliar os cenários de planejamento financeiro sem utilizar dados reais ou recomendações diretas.


---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Os dados do agente são carregados a partir de arquivos CSV e JSON locais, utilizados como base de conhecimento simulada e incorporados de forma contextual durante a execução, sem uso de informações reais ou sensíveis.

```python
import json
import pandas as pd

# ======== CARREGAR DADOS ========
perfil = json.load(open('./data/perfil_investidor.json'))
transacoes = pd.read_csv('./data/transacoes.cvs')
historico = pd.read_csv('./datahistorico.cvs')
produtos = json.load(open('./data/produtos_financeiro.json'))

````
    
### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

Os dados não são inseridos diretamente no system prompt. Eles são consultados de forma dinâmica e utilizados apenas quando relevantes para a solicitação do usuário, sendo incorporados de maneira contextual na construção do prompt para apoiar simulações e evitar respostas fora do escopo.

```text
DADOS DO CLIENTE E PERFIL (data/perfil_investidor.json): 
{
  "nome": "João Silva",
  "idade": 32,
  "profissao": "Analista de Sistemas",
  "renda_mensal": 5000.00,
  "perfil_investidor": "moderado",
  "objetivo_principal": "Construir reserva de emergência",
  "patrimonio_total": 15000.00,
  "reserva_emergencia_atual": 10000.00,
  "aceita_risco": false,
  "metas": [
    {
      "meta": "Completar reserva de emergência",
      "valor_necessario": 15000.00,
      "prazo": "2026-06"
    },
    {
      "meta": "Entrada do apartamento",
      "valor_necessario": 50000.00,
      "prazo": "2027-12"
    }
  ]
}

TRANSACOES DO CLIENTE (data/transacoes.csv):
data,descricao,categoria,valor,tipo
2025-10-01,Salário,receita,5000.00,entrada
2025-10-02,Aluguel,moradia,1200.00,saida
2025-10-03,Supermercado,alimentacao,450.00,saida
2025-10-05,Netflix,lazer,55.90,saida
2025-10-07,Farmácia,saude,89.00,saida
2025-10-10,Restaurante,alimentacao,120.00,saida
2025-10-12,Uber,transporte,45.00,saida
2025-10-15,Conta de Luz,moradia,180.00,saida
2025-10-20,Academia,saude,99.00,saida
2025-10-25,Combustível,transporte,250.00,saida

HISTORICO DE ATENDIMENTO DO CLIENTE (data/historico_atendimento.csv): 
data,canal,tema,resumo,resolvido
2025-09-15,chat,CDB,Cliente perguntou sobre rentabilidade e prazos,sim
2025-09-22,telefone,Problema no app,Erro ao visualizar extrato foi corrigido,sim
2025-10-01,chat,Tesouro Selic,Cliente pediu explicação sobre o funcionamento do Tesouro Direto,sim
2025-10-12,chat,Metas financeiras,Cliente acompanhou o progresso da reserva de emergência,sim
2025-10-25,email,Atualização cadastral,Cliente atualizou e-mail e telefone,sim

PRODUTOS FINANCEIROS DISPONIVEIS (data/produtos_financeiros.json): 
[
  {
    "nome": "Tesouro Selic",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "100% da Selic",
    "aporte_minimo": 30.00,
    "indicado_para": "Reserva de emergência e iniciantes"
  },
  {
    "nome": "CDB Liquidez Diária",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "102% do CDI",
    "aporte_minimo": 100.00,
    "indicado_para": "Quem busca segurança com rendimento diário"
  },
  {
    "nome": "LCI/LCA",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "95% do CDI",
    "aporte_minimo": 1000.00,
    "indicado_para": "Quem pode esperar 90 dias (isento de IR)"
  },
  {
    "nome": "Fundo Multimercado",
    "categoria": "fundo",
    "risco": "medio",
    "rentabilidade": "CDI + 2%",
    "aporte_minimo": 500.00,
    "indicado_para": "Perfil moderado que busca diversificação"
  },
  {
    "nome": "Fundo de Ações",
    "categoria": "fundo",
    "risco": "alto",
    "rentabilidade": "Variável",
    "aporte_minimo": 100.00,
    "indicado_para": "Perfil arrojado com foco no longo prazo"
  },
  {
  "nome": "ETF de Mercado Amplo",
  "categoria": "renda_variavel",
  "risco": "medio",
  "rentabilidade": "Variável",
  "aporte_minimo": 100.00,
  "indicado_para": "Quem busca diversificação com simplicidade"
},
{
  "nome": "Fundo Imobiliário",
  "categoria": "renda_variavel",
  "risco": "medio",
  "rentabilidade": "Variável",
  "aporte_minimo": 100.00,
  "indicado_para": "Quem busca renda periódica e diversificação"
}
]
```

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

O contexto apresentado abaixo é construído a partir da base original de conhecimento do agente, utilizando apenas as informações mais relevantes para o planejamento financeiro. Os dados são previamente resumidos e organizados com o objetivo de otimizar o consumo de tokens, mantendo todas as informações essenciais necessárias para que o agente SAM ofereça suporte eficaz e contextualizado ao usuário.

```

PERFIL DO CLIENTE:
- Nome: João Silva
- Idade: 32 anos
- Profissão: Analista de Sistemas
- Perfil de risco: Moderado
- Aceita risco elevado: Não
- Renda mensal: R$ 5.000,00

Objetivo Financeiro Principal:
- Construir reserva de emergência

Situação Atual:
- Patrimônio total: R$ 15.000,00
- Reserva de emergência atual: R$ 10.000,00
- Reserva desejada: R$ 15.000,00

RESUMO DE GASTOS MENSAIS:
- Moradia: R$ 1.500,00  
- Alimentação: R$ 900,00  
- Transporte: R$ 600,00  
- Lazer: R$ 400,00  
- Saúde: R$ 300,00  
- Outros: R$ 200,00  
Total de gastos mensais: R$ 3.900,00

PRODUTOS FINANCEIROS DISPONÍVEIS:
- Tesouro Selic — Risco: Baixo  
  > Apoia simulações de reserva de emergência e curto prazo.

- CDB com Liquidez Diária — Risco: Baixo  
  > Utilizado em cenários de liquidez e planejamento conservador.

- LCI / LCA — Risco: Baixo  
  > Simulações de médio prazo com menor liquidez.

- Fundo Multimercado — Risco: Médio  
  > Apoia cenários de diversificação moderada.

- Fundo Imobiliário — Risco: Médio  
  > Simulações de renda complementar de longo prazo.

- ETF de Mercado Amplo — Risco: Médio  
  > Simulações de diversificação e crescimento no longo prazo.
...
```
