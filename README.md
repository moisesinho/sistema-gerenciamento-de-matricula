# Sistema de Gerenciamento de Matrículas

Sistema CRUD completo para gerenciamento de matrículas de alunos usando Python e PostgreSQL.

## Funcionalidades

- ✅ Cadastrar aluno
- ✅ Listar todos os alunos
- ✅ Atualizar dados do aluno
- ✅ Excluir aluno
- ✅ Validação de dados
- ✅ Interface interativa via menu

## Pré-requisitos

1. **PostgreSQL** instalado e rodando
2. **Python 3.7+**
3. Biblioteca **psycopg2**

## Configuração

### 1. Instalar dependências
\`\`\`bash
pip install -r requirements.txt
\`\`\`

### 2. Configurar PostgreSQL
Ajuste as credenciais de conexão no arquivo `gerenciador.py`:
\`\`\`python
self.connection = psycopg2.connect(
    host="localhost",
    database="student_db",
    user="postgres",        # Seu usuário
    password="password",    # Sua senha
    port="5432"
)
\`\`\`

### 3. Criar banco de dados (opcional)
\`\`\`bash
python scripts/banco_de_dados.py
\`\`\`

## Como usar

Execute o sistema principal:
\`\`\`bash
python scripts/gerenciador.py
\`\`\`

### Menu do Sistema
\`\`\`
--- Sistema de Matrículas ---
1 - Cadastrar aluno
2 - Listar alunos
3 - Atualizar aluno
4 - Excluir aluno
0 - Sair
\`\`\`

## Estrutura do Banco

**Tabela: alunos**
- `id` - SERIAL PRIMARY KEY (auto-incremento)
- `nome` - VARCHAR(255) NOT NULL
- `curso` - VARCHAR(255) NOT NULL
- `matriculado` - VARCHAR(3) CHECK ('Sim' ou 'Não')
- `semestre` - INTEGER NOT NULL

## Validações

- Nome e curso não podem estar vazios
- Status de matrícula aceita apenas "Sim" ou "Não"
- Semestre deve ser um número positivo
- Confirmação antes de excluir registros
# Sistema de Gerenciamento de Matrículas

Sistema CRUD completo para gerenciamento de matrículas de alunos usando Python e PostgreSQL.

## Funcionalidades

- ✅ Cadastrar aluno
- ✅ Listar todos os alunos
- ✅ Atualizar dados do aluno
- ✅ Excluir aluno
- ✅ Validação de dados
- ✅ Interface interativa via menu

## Pré-requisitos

1. **PostgreSQL** instalado e rodando
2. **Python 3.7+**
3. Biblioteca **psycopg2**

## Configuração

### 1. Instalar dependências
\`\`\`bash
pip install -r requirements.txt
\`\`\`

### 2. Configurar PostgreSQL
Ajuste as credenciais de conexão no arquivo `gerenciador.py`:
\`\`\`python
self.connection = psycopg2.connect(
    host="localhost",
    database="student_db",
    user="postgres",        # Seu usuário
    password="password",    # Sua senha
    port="5432"
)
\`\`\`

### 3. Criar banco de dados (opcional)
\`\`\`bash
python scripts/banco_de_dados.py
\`\`\`

## Como usar

Execute o sistema principal:
\`\`\`bash
python scripts/gerenciador.py
\`\`\`

### Menu do Sistema
\`\`\`
--- Sistema de Matrículas ---
1 - Cadastrar aluno
2 - Listar alunos
3 - Atualizar aluno
4 - Excluir aluno
0 - Sair
\`\`\`

## Estrutura do Banco

**Tabela: alunos**
- `id` - SERIAL PRIMARY KEY (auto-incremento)
- `nome` - VARCHAR(255) NOT NULL
- `curso` - VARCHAR(255) NOT NULL
- `matriculado` - VARCHAR(3) CHECK ('Sim' ou 'Não')
- `semestre` - INTEGER NOT NULL

## Validações

- Nome e curso não podem estar vazios
- Status de matrícula aceita apenas "Sim" ou "Não"
- Semestre deve ser um número positivo
- Confirmação antes de excluir registros
