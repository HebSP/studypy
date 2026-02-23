def build_prompt_ask(topic):
    return f"""
Explique o tema "{topic}" de forma clara e didática para nível universitário.
Inclua um exemplo prático.

Depois gere:
- Um resumo de até 5 linhas.
- Exatamente 3 perguntas abertas para revisão.
- responda as perguntas usando o conteúdo explicado, na mesma ordem, sem repetir a explicação.
Responda SOMENTE em JSON válido no formato:

{{
  "explanation": "...",
  "summary": "...",
  "questions": ["...", "...", "..."],
  "answers": ["...", "...", "..."]
}}
Sem markdown e sem texto adicional.
"""


# Essa função é para construir um prompt que verifica se a resposta do usuário está correta, comparando com uma resposta de exemplo e usando a explicação fornecida. O feedback deve incluir uma pontuação de 0 a 100 e um comentário explicativo.
# poderia ser usada para avaliar as respostas do usuário às perguntas geradas, dando um feedback construtivo para ajudar no aprendizado.
# implementação futura quando o sistema estiver funcionando com um servidor backend para receber as respostas do usuário e processar o feedback.
def build_prompt_check(topic, answer, example_answer, question, explanation):
    return f"""
Você é um assistente educacional que verifica se a resposta está correta.

Verifique se a resposta sobre o tema "{topic}" está correta e completa com base na explicação fornecida e gera um feedback, podendo complementar ou corrigir a resposta, se necessário.

avalie a resposta com uma pontuação de 0 a 100, onde 100 é uma resposta completa que demonstra entendimento correto de todos os conceitos e 0 é completamente incorreta ou não relacionada ao tema, que não explica nada do que esteja na pergunta.

questão: "{question}"
resposta: "{answer}"
explicação: "{explanation}"

uma resposta de exemplo valida para a questão que pode ser usada para avaliar e comparar com a resposta obtida é: "{example_answer}"

Responda SOMENTE em JSON válido no formato:

{{
  "score": 0-100,
  "feedback": "..."

}}
Sem markdown e sem texto adicional.
"""