# 📋 Gerenciador de Tarefas (CLI)

Aplicação de linha de comando para gerenciamento de tarefas, desenvolvida em Python com persistência de dados em SQLite. Projeto criado para praticar operações CRUD (Create, Read, Update, Delete) e integração entre Python e banco de dados relacional.

## ⚙️ Funcionalidades

- **Adicionar tarefa** — cria uma nova tarefa com título, status inicial ("pendente") e data de criação
- **Listar tarefas** — exibe todas as tarefas cadastradas, com ID, título, status e data
- **Concluir tarefa** — atualiza o status de uma tarefa para "concluída", buscando pelo ID
- **Deletar tarefa** — remove uma tarefa do banco de dados pelo ID
- **Tratamento de erros** — validação de opções inválidas no menu e de IDs inexistentes, sem quebrar a execução do programa

## 🛠️ Tecnologias utilizadas

- Python 3
- SQLite3 (módulo nativo `sqlite3`)
- Módulo `datetime` para registro da data de criação das tarefas

## 📂 Estrutura do projeto
gerenciador-tarefas/
├── main.py # Interface com o usuário (menu interativo)
├── database.py # Lógica de conexão e operações com o banco de dados
├── requirements.txt
└── README.md
O projeto foi estruturado separando a lógica de banco de dados (`database.py`) da interface com o usuário (`main.py`), facilitando manutenção e reaproveitamento de código.

## ▶️ Como executar

1. Clone este repositório:
```bash
git clone https://github.com/JulianaSantos943/gerenciador-tarefas.git
```

2. Acesse a pasta do projeto:
```bash
cd gerenciador-tarefas
```

3. Execute o programa:
```bash
python main.py
```

> Não é necessário instalar dependências externas — o projeto utiliza apenas bibliotecas nativas do Python.

## 🖥️ Exemplo de uso
1 - Adicionar tarefa
2 - Listar tarefa
3 - Concluir tarefa
4 - Deletar tarefa
0 - Sair
Escolha uma opção: 1
Digite o título da tarefa: Estudar SQL
Tarefa adicionada com sucesso!
## 🚀 Possíveis melhorias futuras

- Busca de tarefas por título, além do ID
- Interface gráfica (GUI) ou versão web
- Categorização de tarefas por prioridade ou prazo

## 👩‍💻 Autora

Desenvolvido por Juliana Santos como parte do portfólio de estudos em Python e desenvolvimento de sistemas.

[LinkedIn](https://linkedin.com/in/juliana-santos-340061417) | [GitHub](https://github.com/JulianaSantos943)