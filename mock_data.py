import json

def build_mock_response(prompt: str, API_KEY: str) -> dict:
    # Extract topic from prompt ()
    topic = prompt.split('"')[1] if '"' in prompt else "unknown topic"

    topic_lower = topic.lower()

    explanation = build_explanation(topic, topic_lower)
    questions, answers = build_questions_and_answers(topic)

    summary = build_summary(explanation)

    return {
    "choices": [
        {
            "message": {
                "content": json.dumps({
                    "explanation": explanation.strip(),
                    "summary": summary.strip(),
                    "questions": questions,
                    "answers": answers
                }, ensure_ascii=False)
            }
        }
    ]
}


def build_explanation(topic, topic_lower):

    if "inteligência artificial" in topic_lower or "ia" in topic_lower:
        return f"""
Inteligência Artificial é o campo que estuda sistemas capazes de simular
processos cognitivos humanos, como aprendizado, reconhecimento de padrões
e tomada de decisão.

Um exemplo prático é um modelo de classificação que analisa dados históricos
para prever resultados futuros com base em padrões identificados.
"""

    if "programação" in topic_lower:
        return f"""
Programação consiste na construção de algoritmos e instruções lógicas
que permitem que um computador execute tarefas específicas.

Por exemplo, um sistema pode receber dados do usuário,
processá-los e retornar uma resposta com base em regras previamente definidas.
"""

    # fallback genérico
    return f"""
O tema '{topic}' envolve fundamentos teóricos e aplicações práticas
que exigem compreensão conceitual e análise estruturada.

Ele pode ser aplicado em diferentes contextos para resolver problemas
de forma lógica e sistemática.
"""


def build_questions_and_answers(topic):
    questions = [
        f"Quais são os fundamentos principais de {topic}?",
        f"Como {topic} pode ser aplicado na prática?",
        f"Quais desafios estão associados a {topic}?"
    ]

    answers = [
        f"Os fundamentos de {topic} envolvem conceitos estruturais e princípios teóricos centrais.",
        f"{topic} pode ser aplicado na resolução de problemas reais por meio de análise e implementação prática.",
        f"Os desafios incluem complexidade conceitual, limitações técnicas e necessidade de adaptação ao contexto."
    ]

    return questions, answers


def build_summary(explanation):
    lines = explanation.strip().split("\n")
    clean_lines = [line.strip() for line in lines if line.strip()]
    return " ".join(clean_lines[:3])