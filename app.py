import requests
import time
import json
from datetime import datetime

ORION_URL = "http://localhost:1026"

HEADERS_GET = {
    "Accept": "application/json",
    "Fiware-Service": "openiot",
    "Fiware-ServicePath": "/"
}

HEADERS_POST = {
    "Content-Type": "application/json",
    "Fiware-Service": "openiot",
    "Fiware-ServicePath": "/"
}

def ai_engine_decision(description, deadline_hours):
    explanation = ""
    priority = "Normal"
    ethical_warning = "Nenhum"

    if deadline_hours <= 2:
        priority = "Urgente"
        ethical_warning = "⚠️ Risco de Burnout: Prazo muito curto."
        explanation = f"Priorizado como URGENTE, mas verifique a saúde da equipe."
    elif "relatório" in description.lower():
        priority = "Baixa"
        explanation = "Tarefa repetitiva detectada. Sugestão de automação."
    else:
        explanation = "Processado normalmente."

    return priority, explanation, ethical_warning

def process_tasks():
    print(f"[{datetime.now().strftime('%H:%M:%S')}] 🔍 Buscando tarefas...")
    
    try:
        url = f"{ORION_URL}/v2/entities?type=Task&options=keyValues"
        response = requests.get(url, headers=HEADERS_GET) 

        if response.status_code == 200:
            tasks = response.json()
            if not tasks:
                print("   ... Nenhuma tarefa 'Task' encontrada.")
            
            for task in tasks:
                if task.get("ai_status") == "processed":
                    continue

                print(f"   ⚡ Processando: {task['id']}")
                
                desc = task.get("description", "Sem descrição")
                try:
                    deadline = float(task.get("deadline_hours", 24))
                except:
                    deadline = 24

                prio, reason, warning = ai_engine_decision(desc, deadline)

                update_payload = {
                    "ai_priority": {"type": "Text", "value": prio},
                    "ai_reasoning": {"type": "Text", "value": reason},
                    "ai_ethical_alert": {"type": "Text", "value": warning},
                    "ai_status": {"type": "Text", "value": "processed"}
                }
                
                upd_response = requests.post(f"{ORION_URL}/v2/entities/{task['id']}/attrs", 
                              headers=HEADERS_POST, 
                              data=json.dumps(update_payload))
                
                if upd_response.status_code in [200, 204]:
                    print(f"   ✅ Tarefa {task['id']} atualizada!")
                else:
                    print(f"   ❌ Erro ao atualizar: {upd_response.text}")

        else:
            print(f"   ❌ Erro {response.status_code} no Orion.")
            print(f"   💬 O servidor disse: {response.text}") 
            
    except Exception as e:
        print(f"   ❌ Erro crítico de conexão: {e}")

if __name__ == "__main__":
    print("--- 🤖 EthosFlow V2: Debug Mode ---")
    while True:
        process_tasks()
        time.sleep(5)
