# Base de Conhecimento

## Dados Utilizados

Os dados utilizados foram os arquivos fornecidos na pasta data/, estruturados para permitir análise financeira completa do usuário, personalização de recomendações e contextualização de respostas.

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

Os dados utilizados foram os arquivos mockados fornecidos na pasta data/, sem alterações estruturais significativas.

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Os arquivos CSV e JSON são carregados no início da execução da aplicação utilizando bibliotecas como pandas e json. Esses dados ficam disponíveis em memória durante toda a sessão do agente.

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

Os dados não são colocados integralmente no prompt, mas sim processados e filtrados antes de serem enviados ao LLM.

Estratégia aplicada:

* O CSV de transações é resumido (ex: total por categoria)
* O perfil do investidor é convertido em texto estruturado
* Produtos financeiros são filtrados com base no perfil do usuário
* Apenas informações relevantes são injetadas no contexto do prompt

Isso reduz custo de tokens e melhora precisão das respostas.

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
Dados do Cliente:
- Nome: João Silva
- Idade: 32 anos
- Profissão: Analista de Sistemas
- Renda mensal: R$ 5.000
- Perfil de investidor: Moderado
- Objetivo principal: Construir reserva de emergência
- Patrimônio total: R$ 15.000
- Reserva de emergência atual: R$ 10.000
- Aceita risco: Não

Metas financeiras:
1. Completar reserva de emergência (R$ 15.000 até 2026-06)
2. Entrada do apartamento (R$ 50.000 até 2027-12)

Resumo de gastos recentes:
- Moradia: R$ 1.380
- Alimentação: R$ 570
- Transporte: R$ 295
- Lazer: R$ 55,90
- Saúde: R$ 188

Histórico de atendimento:
- Cliente buscou informações sobre CDB e Tesouro Selic
- Já acompanha progresso da reserva de emergência
- Já teve dúvidas sobre funcionamento do Tesouro Direto

Produtos recomendados:
- Tesouro Selic
- CDB Liquidez Diária
- LCI/LCA
```
