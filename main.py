import os
import json
import webbrowser
from dotenv import load_dotenv
from prompts import build_prompt_ask, build_prompt_check
from html import generate_html
from call_api import call_api
# MODO MOCK (se você não tem acesso a API mas gostaria de testar o fluxo e ver um exemplo de resposta, descomente o código abaixo e comente a chamada real da API)
# as respostas nesse modo são apenas um exemplo e não reflete necessariamente o que a API real retornaria para um prompt específico, mas serve para testar o restante do código sem precisar da API.
# para usar o modo mock, basta descomentar a linha abaixo e comentar a linha acima que importa a função call_api real.
#from mock_data import build_mock_response as call_api



load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")


def main():
    topic = input("Digite um tema para estudar: ")
    prompt = build_prompt_ask(topic)

    response = call_api(prompt, API_KEY)

    content = response["choices"][0]["message"]["content"]

    parsed = json.loads(content)

    with open("output.json", "w", encoding="utf-8") as f:
        json.dump(parsed, f, indent=4, ensure_ascii=False)

    print("Conteúdo salvo em output.json")
    generate_html(parsed, topic)
    print("HTML gerado em output.html")
    print("abrir output.html para revisar o conteúdo e responder as perguntas.")
    webbrowser.open("output.html")
    

if __name__ == "__main__":
    main()