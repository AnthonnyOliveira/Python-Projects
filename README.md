# 💪 Sistema de Controle de Academia – Python + SQLite

Este projeto tem como objetivo registrar entradas e saídas de alunos da academia, associar dias de frequência e horários previstos, além de gerar relatórios de tempo de permanência e médias. Ideal para quem está começando com Python e quer aplicar lógica real com banco de dados.

---
## 📋 Desenvolvimento

### 🏗️ Arquitetura do Projeto

```bash
academia/
├── src/
│   ├── db/                    # Conexão e estrutura do banco
│   │   └── connection.py
│   ├── models/                # Representação dos dados (Aluno, Registro)
│   │   ├── aluno.py
│   │   └── registro.py
│   ├── services/              # Lógica de negócio (cadastro, registro, etc)
│   │   ├── aluno_service.py
│   │   └── registro_service.py
│   ├── reports/               # Relatórios e estatísticas
│   │   └── relatorio.py
│   └── cli/                   # Interface de linha de comando
│       └── menu.py
├── academia.db                # Banco de dados SQLite
└── main.py                    # Ponto de entrada do sistema
```

### 🔹 1. Planejamento
- [x] Definir funcionalidades principais
- [x] Escolher banco de dados: SQLite
- [x] Definir entidades: Aluno, Registro

### 🔹 2. Estrutura Inicial
- [x] Criar estrutura de pastas conforme arquitetura acima
- [x] Implementar script de criação do banco (`connection.py`)

### 🔹 3. Modelos (Camada de Dados)
- [x] Criar modelo `Aluno` com: `id`, `nome`, `dias_frequencia`, `horario_previsto`
- [x] Criar modelo `Registro` com: `id`, `aluno_id`, `entrada`, `saida`

### 🔹 4. Serviços (Regras de Negócio)
- [x] Função para cadastrar aluno
- [x] Função para registrar entrada
- [x] Função para registrar saída
- [x] Buscar aluno por nome ou ID
- [x] Validar se o aluno já possui entrada sem saída

### 🔹 5. Relatórios
- [ ] Calcular tempo total de permanência por aluno
- [ ] Calcular média de tempo por aluno
- [ ] Calcular média geral de permanência
- [ ] Exibir discrepância entre horário previsto e real

### 🔹 6. Interface CLI (Terminal)
- [ ] Criar menu principal (`menu.py`)
- [ ] Opções:
  - [ ] Cadastrar aluno
  - [ ] Registrar entrada
  - [ ] Registrar saída
  - [ ] Gerar relatórios
  - [ ] Sair

### 🔹 7. Extras (Para o futuro)
- [ ] Exportar relatórios para CSV
- [ ] Interface gráfica com Tkinter
- [ ] Adicionar autenticação para funcionários
- [ ] Interface web (API com Flask ou FastAPI)
