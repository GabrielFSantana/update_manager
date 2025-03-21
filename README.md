Gerenciador de Atualizações
Este projeto é um sistema web simples desenvolvido com Python (Flask) e SQLite, com o objetivo de gerenciar atualizações de sistemas, atribuindo tarefas a analistas e controlando o status das atualizações.

🛠 Funcionalidades
Adicionar clientes e analistas.
Atribuir atualizações a clientes e analistas.
Alterar o status da atualização (Pendente, Em andamento, Pausado, Concluído).
Registro automático da data e hora de conclusão.
Filtrar visualização das atualizações por status.
💻 Tecnologias Utilizadas
Python 3
Flask
Flask-SQLAlchemy
SQLite
HTML/CSS (Jinja2 para templates)
📦 Instalação
Clone o repositório:
bash
Copiar
Editar
git clone https://github.com/SEU_USUARIO/gerenciador-atualizacoes.git
cd gerenciador-atualizacoes
Crie um ambiente virtual e ative:
bash
Copiar
Editar
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate
Instale as dependências:
bash
Copiar
Editar
pip install flask flask_sqlalchemy
Execute a aplicação:
bash
Copiar
Editar
python app.py
O sistema estará disponível em: http://localhost:5000

🗂 Estrutura do Projeto
csharp
Copiar
Editar
gerenciador-atualizacoes/
│
├── app.py                 # Código principal da aplicação Flask
├── update_manager.db      # Banco de dados SQLite (gerado automaticamente)
├── templates/
│   └── index.html         # Página principal
├── static/
│   └── styles.css         # Estilos da interface
└── README.md              # Documentação do projeto
✅ Status do Projeto
🚧 Em desenvolvimento – novas funcionalidades podem ser adicionadas.
