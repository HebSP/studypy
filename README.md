# 📚 Study Assistant - Gerador de Conteúdo Educacional (DEMO)

Sistema simples para geração automática de explicações, resumos e
perguntas para estudo, com interface HTML interativa para responder
questões e receber feedback.

------------------------------------------------------------------------

## 🚀 Funcionalidades

-   Geração automática de:
    -   Explicação didática
    -   Resumo
    -   3 perguntas abertas
    -   Respostas modelo
-   Interface HTML interativa
-   Campo para resposta do usuário
-   Botão para visualizar resposta correta
-   Estrutura preparada para avaliação automática
-   Sistema mock para demonstração de funcionamento sem dependência de API externa

------------------------------------------------------------------------

## 🏗️ Estrutura do Projeto
```
project/ 
│
├── main.py      # Arquivo principal
├── mock_data.py # Gerador de conteúdo simulando resposta da API
├── call_api.py  # função para chamar a API
├── html.py      # Gerador da interface HTML
├── prompts.py   # Estrutura preparada para uso com API real
├── output.json  # Conteúdo gerado
├── output.html  # Interface interativa
└── README.md
```
------------------------------------------------------------------------

## ⚙️ Como Executar

1.  Clone o repositório

2.  instale os requerimentos

```
    pip install -r requirements.txt
```

3. Configure o ambiente:

    - Adicione sua chave de API em um arquivo .env, ou

    - Ative o modo mock em main.py

Exemplo .env:

```
    OPENAI_API_KEY=sua_chave_aqui
```


4.  Execute:

    python main.py

5.  Digite um tema

6.  Arquivo `output.html` gerado será aberto no navegador

------------------------------------------------------------------------

## 🧠 Como Funciona

### 1️⃣ Geração de Conteúdo

O sistema pode operar em dois modos:

#### 🔹 Modo Mock (desenvolvimento)

Utiliza mock_data.py, que simula uma resposta estruturada de API:

- Analisa o tema informado
- Gera explicação contextual
- Cria perguntas abertas
- Fornece respostas modelo
- Produz resumo automático

🔹 Modo API Real (produção)

Utiliza call_api.py, que envia o prompt estruturado para um modelo de linguagem e retorna resposta em formato JSON.

A alternância entre os modos é feita por configuração no main.py.

------------------------------------------------------------------------

### 2️⃣ Persistência

O conteúdo gerado é salvo em `output.json`

Isso permite: - Reutilização do conteúdo - Separação entre backend e
interface - Possibilidade de futuras análises

------------------------------------------------------------------------

### 3️⃣ Interface HTML

O `html.py` gera automaticamente uma página contendo:

-   Título do tema
-   Explicação
-   Resumo
-   Perguntas numeradas
-   Campo para resposta
-   Espaço para feedback
-   Botão para visualizar resposta gerada

------------------------------------------------------------------------

## 🔮 Melhorias Futuras

### 🤖 Avaliação Semântica com IA

-   Similaridade semântica usando embeddings
-   Correção automática baseada em contexto
-   Geração de feedback personalizado
-   Classificação automática de nota (0-100)

Possível implementação futura: - Integração com API de IA - Cálculo de
similaridade textual - Análise de coerência e completude

------------------------------------------------------------------------

### 📊 Sistema de Notas

-   Cálculo automático de pontuação
-   Histórico de desempenho
-   Métricas por tema

------------------------------------------------------------------------

### 🌐 Versão Web

-   Implementação com Flask ou FastAPI
-   Banco de dados
-   Autenticação de usuários
-   Interface dinâmica

------------------------------------------------------------------------

## 🧩 Objetivos Técnicos do Projeto

Este projeto demonstra:

-   Organização modular em Python
-   Separação de responsabilidades
-   Manipulação de JSON
-   Geração automática de HTML
-   Arquitetura preparada para integração com IA
-   Estrutura escalável para evolução futura

------------------------------------------------------------------------
