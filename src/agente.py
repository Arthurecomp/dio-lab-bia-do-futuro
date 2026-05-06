import pandas as pd
import json
from gpt4all import GPT4All

# =========================
# MODELO LOCAL GPT4ALL
# =========================

MODEL_NAME = "Phi-3-mini-4k-instruct.Q4_0.gguf"
model = GPT4All(MODEL_NAME)


# =========================
# BASE DE DADOS
# =========================

def carregar_dados():
    transacoes = pd.read_csv("data/transacoes.csv")
    atendimento = pd.read_csv("data/historico_atendimento.csv")

    with open("data/perfil_investidor.json", "r", encoding="utf-8") as f:
        perfil = json.load(f)

    with open("data/produtos_financeiros.json", "r", encoding="utf-8") as f:
        produtos = json.load(f)

    return transacoes, atendimento, perfil, produtos


def resumir_transacoes(df):
    return df.groupby("categoria")["valor"].sum().to_dict()


# =========================
# CONTEXTO DO AGENTE
# =========================

def montar_contexto():
    transacoes, atendimento, perfil, produtos = carregar_dados()

    resumo_gastos = resumir_transacoes(transacoes)

    contexto = f"""
CLIENTE:
Nome: {perfil['nome']}
Idade: {perfil['idade']}
Renda: {perfil['renda_mensal']}
Perfil de investidor: {perfil['perfil_investidor']}
Objetivo: {perfil['objetivo_principal']}
Patrimônio: {perfil['patrimonio_total']}
Reserva de emergência: {perfil['reserva_emergencia_atual']}

RESUMO DE GASTOS:
{resumo_gastos}

PRODUTOS FINANCEIROS:
{produtos}

HISTÓRICO DE ATENDIMENTO:
{atendimento.to_dict(orient="records")}
"""
    return contexto


# =========================
# PROMPT DO AGENTE
# =========================

SYSTEM_PROMPT = """
Você é um agente financeiro inteligente e consultivo.

REGRAS OBRIGATÓRIAS:
- Use apenas o contexto fornecido
- Nunca invente informações financeiras
- Se não souber algo, diga que não há dados suficientes
- Baseie recomendações no perfil do cliente
- Seja claro, objetivo e explicativo
- Não forneça aconselhamento financeiro profissional direto
"""


# =========================
# FUNÇÃO PRINCIPAL
# =========================

def perguntar_agente(mensagem_usuario):
    contexto = montar_contexto()

    prompt_final = f"""
{SYSTEM_PROMPT}

CONTEXTO DO CLIENTE:
{contexto}

PERGUNTA DO USUÁRIO:
{mensagem_usuario}

RESPOSTA:
"""

    with model.chat_session():
        resposta = model.generate(prompt_final)

    return resposta