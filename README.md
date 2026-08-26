Leandro Farias - RM566488

# 🧠 EthosFlow: Assistente de Produtividade com IA Ética (FIWARE)

## 📖 Sobre o Projeto
O EthosFlow é um "copiloto" de trabalho que não apenas gerencia tarefas, mas protege o usuário contra burnout. Ele utiliza a arquitetura **FIWARE** para processar contexto em tempo real e um motor de decisão em Python que explica o "porquê" de cada priorização.

## 🏗 Arquitetura
O sistema roda em uma Máquina Virtual Azure com a seguinte estrutura:
1.  **Orion Context Broker:** Recebe as demandas (simulando e-mails/tickets).
2.  **Ethos Worker (Python):** Consome as tarefas, aplica regras éticas (ex: detecção de prazos abusivos) e enriquece os dados.
3.  **Interface de Dados:** REST API (NGSIv2).

## 🚀 Como Rodar
1.  Certifique-se de ter o FIWARE Orion rodando (Docker).
2.  Instale dependências: `pip install requests`
3.  Execute o agente: `python3 app.py`

## 🧪 Evidências de Integração
<img width="464" height="289" alt="{6E68D545-4749-4002-BB5F-7AE6816B2485}" src="https://github.com/user-attachments/assets/19e84b7e-227c-4684-8c06-4f5775554f1e" />
<img width="709" height="308" alt="image" src="https://github.com/user-attachments/assets/9ca52393-c932-4410-9978-f1ca18e488ca" />



