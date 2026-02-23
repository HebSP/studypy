import json

def generate_html(data, topic):
    html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{topic}</title>
    <style>
        body {{ font-family: Arial; max-width: 800px; margin: auto; }}
        h1 {{ text-align: center; }}
        textarea {{ width: 100%; height: 80px; }}
        button {{ margin-top: 5px; }}
        .feedback {{ margin-top: 10px; font-weight: bold; }}
    </style>
</head>
<body>

<h1>{topic}</h1>

<h2>Explicação</h2>
<p>{data["explanation"]}</p>

<h2>Resumo</h2>
<p>{data["summary"]}</p>

<h2>Perguntas</h2>
<p>Responda às perguntas abaixo e depois clique em "Ver Resposta" para comparar com a resposta fornecida.</p>

<div id="questions"></div>

<script>
const data = {json.dumps(data, ensure_ascii=False)};

const container = document.getElementById("questions");

data.questions.forEach((q, index) => {{
    const div = document.createElement("div");

    div.innerHTML = `
        <h3>Pergunta ${{index + 1}}</h3>
        <p>${{q}}</p>
        <textarea id="answer-${{index}}"></textarea><br>
        <button onclick="showAnswer(${{index}})">Ver Resposta</button>
        <div class="feedback" id="feedback-${{index}}"></div>
        <hr>
    `;

    container.appendChild(div);
}});

function showAnswer(index) {{
    const feedback = document.getElementById(`feedback-${{index}}`);
    feedback.innerText = "Resposta: " + data.answers[index];
}}
</script>

</body>
</html>
"""

    with open("output.html", "w", encoding="utf-8") as f:
        f.write(html)