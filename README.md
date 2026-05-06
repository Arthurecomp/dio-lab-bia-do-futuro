# 🤖 Agente Financeiro Inteligente com IA Generativa

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![DIO Challenge](https://img.shields.io/badge/DIO-Lab-orange)](https://www.dio.me/)

> **Consultoria financeira personalizada, local e segura.** Um agente proativo que transforma dados brutos em decisões financeiras inteligentes sem depender de APIs externas.

## 📌 Contexto do Projeto

Este projeto foi desenvolvido como um desafio prático no laboratório da **DIO (Digital Innovation One)**. O objetivo é criar um protótipo de IA que atua como um consultor financeiro pessoal, analisando transações, perfil de investidor e histórico de atendimento para fornecer recomendações precisas e evitar o endividamento.



## 🚀 Funcionalidades Principais

- **Análise Proativa:** Entende o histórico de gastos e sugere economias antes mesmo do usuário perguntar.
- **Consultoria de Investimentos:** Recomenda produtos financeiros alinhados ao perfil de risco específico do cliente.
- **Anti-Alucinação (Grounding):** O agente utiliza estritamente os dados fornecidos na base de conhecimento para gerar respostas, garantindo confiabilidade.
- **Privacidade Total:** Execução local através de modelos de linguagem leves (SLMs), garantindo que dados sensíveis nunca saiam do dispositivo.

## 🏗️ Arquitetura do Sistema

O sistema utiliza uma abordagem de **RAG (Retrieval Augmented Generation)** para garantir que o contexto do cliente seja respeitado.



1.  **Ingestão de Dados:** Leitura de arquivos estruturados (CSV/JSON).
2.  **Processamento de Contexto:** O LLM recebe os dados filtrados como contexto do sistema.
3.  **Prompt Engineering:** Instruções de "Persona" definem o tom de voz consultivo, técnico e ético.
4.  **Interface de Resposta:** Geração de insights em linguagem natural para o usuário final.

## 📂 Base de Dados Utilizada

Para o funcionamento do protótipo, o agente consome os seguintes arquivos:

| Arquivo | Formato | Conteúdo |
| :--- | :--- | :--- |
| `transacoes.csv` | CSV | Histórico detalhado de entradas, saídas e categorias de gastos. |
| `perfil_investidor.json` | JSON | Nível de tolerância a risco, objetivos e prazos. |
| `historico_atendimento.csv` | CSV | Registro de interações passadas para manter a continuidade. |
| `produtos_financeiros.json` | JSON | Catálogo de investimentos disponíveis para sugestão. |

## 🛠️ Tecnologias

- **Linguagem:** Python
- **LLM Local:** Llama 3 (via Ollama) ou modelos similares quantizados para CPU.
- **Processamento de Dados:** Pandas / JSON.
- **Prompting:** Técnicas de *Zero-shot* e *Context-anchoring*.

## ⚙️ Como Executar

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/Arthurecomp/dio-lab-bia-do-futuro.git](https://github.com/Arthurecomp/dio-lab-bia-do-futuro.git)
   cd dio-lab-bia-do-futuro,


2. **Instale as dependências:**

   ```bash
  pip install -r requirements.txt ```


2. **Inicie o agente**

   ```bash
  streamlit run src/app.py```

### Diferenciais Técnicos

*    Modelo Leve: Projetado para rodar em hardware comum (ex: notebook padrão) sem custos de API externa.

*    Segurança Bancária: Foco na privacidade (Privacy by Design) — os dados não são usados para treinar modelos globais.

*    Foco em Educação: Além de recomendar, o agente explica o "porquê" de cada sugestão financeira.

  

    
