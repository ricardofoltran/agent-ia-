import json
import streamlit as st 
import pandas as pd
import requests 



# ======== CONFIGURAÇÃO ======== 
OLLAMA_URL ="http://localhost:11434/api/generate"
MODELO = "llama3"

# ======== CARREGAR DADOS ========
perfil = json.load(open('./data/perfil_investidor.json'))
transacoes = pd.read_csv('./data/transacoes.csv')
historico = pd.read_csv('./data/historico_atendimento.csv')
produtos = json.load(open('./data/produtos_financeiros.json'))

# ======== MONTAR CONTEXTO ========
contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']} anos, perfil {perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMÔNIO: R$ {perfil['patrimonio_total']} | RESERV: R$ {perfil['reserva_emergencia_atual']}

TRANSAÇÕES RECENTES: 
{transacoes.to_string(index=False)}

ATENDIMENTO ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""

# ======== SYSTEM PROMPT ======== 
SYSTEM_PROMPT = """Você é o SAM, um assistente de planejamento financeiro cuidadoso e responsável.

OBEJTIVO: 
Seu objetivo é auxiliar o usuário na organização de suas finanças, simulação de cenários e definição de metas financeiras, utilizando exclusivamente as informações fornecidas pelo próprio usuário e os dados disponíveis na base de conhecimento simulada.

REGRAS:
- O SAM responde apenas a temas de planejamento financeiro. Perguntas fora desse contexto devem ser recusadas e redirecionadas.
- Baseie todas as respostas apenas nos dados fornecidos no contexto e na base de conhecimento disponível.
- Não invente informações financeiras, valores, produtos ou cenários não apresentados.
- Não forneça recomendações financeiras personalizadas ou garantias de retorno.
- Utilize linguagem clara, objetiva e acessível, com tom profissional e respeitoso.
- Apresente sugestões sempre de forma condicional, baseadas em simulações.
- Quando não houver informações suficientes, solicite dados adicionais ou indique limitações.
- Não solicite, armazene ou utilize dados pessoais sensíveis.
- Não utilize fontes externas ou conhecimento fora do contexto fornecido.
"""
# ======== CHAMAR OLLAMA ======= 
def perguntar(msg):
    prompt = f"""
    {SYSTEM_PROMPT}

    CONTEXTO DO CLIENTE: 
    {contexto}

    Pergunta: {msg}"""

    r = requests.post(OLLAMA_URL, json={"model": MODELO, "prompt": prompt, "stream": False})
    return r.json()['response']

# ======== INTERFACE ======= 
st.title("🎓 SAM, Seu Planejador Financeiro")

if pergunta := st.chat_input("Sua dúvida sobre finanças..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("..."):
        st.chat_message("assistant").write(perguntar(pergunta))

