# Avaliação e Métricas

## Como Avaliar seu Agente

A avaliação foi feita por meio de testes estruturados baseados em dados reais simulados do cliente e validação de comportamento do agente em diferentes cenários financeiros.

Além disso, foram considerados:

* consistência com o perfil do investidor
* uso correto da base de dados
* capacidade de reconhecer limitações
---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade** | O agente respondeu o que foi perguntado? | Perguntar o saldo e receber o valor correto |
| **Segurança** | O agente evitou inventar informações? | Perguntar algo fora do contexto e ele admitir que não sabe |
| **Coerência** | A resposta faz sentido para o perfil do cliente? | Sugerir investimento conservador para cliente conservador |

> [!TIP]
> Peça para 3-5 pessoas (amigos, família, colegas) testarem seu agente e avaliarem cada métrica com notas de 1 a 5. Isso torna suas métricas mais confiáveis! Caso use os arquivos da pasta `data`, lembre-se de contextualizar os participantes sobre o **cliente fictício** representado nesses dados.

---

## Exemplos de Cenários de Teste

Crie testes simples para validar seu agente:

### Teste 1: Consulta de gastos
- **Pergunta:** "Quanto gastei com alimentação?"
- **Resposta esperada:** Valor baseado no `transacoes.csv`
- **Resultado:** [ x] Correto  [ ] Incorreto

### Teste 2: Recomendação de produto
- **Pergunta:** "Qual investimento você recomenda para mim?"
- **Resposta esperada:** Produto compatível com o perfil do cliente
- **Resultado:** [x ] Correto  [ ] Incorreto

### Teste 3: Pergunta fora do escopo
- **Pergunta:** "Qual a previsão do tempo?"
- **Resposta esperada:** Agente informa que só trata de finanças
- **Resultado:** [x ] Correto  [ ] Incorreto

### Teste 4: Informação inexistente
- **Pergunta:** "Quanto rende o produto XYZ?"
- **Resposta esperada:** Agente admite não ter essa informação
- **Resultado:** [ x] Correto  [ ] Incorreto

---

## Resultados

Após os testes, registre suas conclusões:

**O que funcionou bem:**

*  Respostas consistentes com o perfil do cliente
*  Uso correto da base de dados (transações e produtos)
*  Não inventa informações inexistentes
*    Recomendações coerentes com perfil moderado

**O que pode melhorar:**

*  Velocidade de resposta (depende do modelo local)
*  Melhor sumarização de grandes históricos
*  Otimização do contexto para reduzir consumo de memória
*  Melhor precisão em perguntas muito específicas

---

## Métricas Avançadas (Opcional)

Para quem quer explorar mais, algumas métricas técnicas de observabilidade também podem fazer parte da sua solução, como:

- Consumo de memória: alto com modelos 7B+
- Taxa de erro: baixa (principalmente em perguntas fora do contexto)
- Uso de logs: não implementado (pode ser melhoria futura)
