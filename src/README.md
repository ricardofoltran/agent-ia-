# Passo a Passo de Execução do Projeto

## Pré-requisitos

Antes de executar o projeto, certifique-se de que possui:

- Python 3.10 ou superior
- Ollama instalado e configurado (https://ollama.com)
- Pelo menos um modelo disponível no Ollama (ex: `llama3`)

Para verificar os modelos instalados, execute:

```bash
ollama list

```

## Código Completo

Todo código-fonte está no arquivo `app.py` 

## Como Executar o Projeto

```bash
# 1. Instalar as dependências
pip install streamlit pandas requests

# 2. Garantir que o Ollama está em execução
ollama serve

# 3. Rodar a aplicação
streamlit run src/app.py

```
