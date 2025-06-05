# 🎯 Sistema de Ouvidoria UNIFACISA

## 📋 Descrição
Este é um sistema de ouvidoria desenvolvido em Python para a UNIFACISA, que permite gerenciar manifestações através de um menu interativo de linha de comando.

## ⚡ Funcionalidades

O sistema oferece as seguintes opções através de um menu principal:

### 1. 📋 Listar manifestações
- Exibe todas as manifestações cadastradas no sistema

### 2. 🔍 Listar Manifestações por tipo
- Permite visualizar manifestações filtradas por tipo específico

### 3. ✏️ Criar uma nova manifestação
- Adiciona uma nova manifestação ao sistema

### 4. 📊 Exibir quantidade de manifestações
- Mostra o total de manifestações cadastradas

### 5. 🔎 Pesquisar manifestação por código
- Busca uma manifestação específica usando seu código identificador

### 6. 🗑️ Excluir uma manifestação por código
- Remove uma manifestação do sistema através do seu código

### 7. 🚪 Sair do sistema
- Encerra a aplicação

## 📦 Dependências

O sistema requer o módulo `operacoesbd` que deve conter a função `criarConexao` para estabelecer a conexão com o banco de dados.

## 🚀 Como usar

1. ✅ Certifique-se de que o banco de dados MySQL está rodando
2. ⚙️ Configure as credenciais de acesso no código (se necessário)
3. ▶️ Execute o arquivo `menu_sql.py`
4. 🖱️ Use o menu interativo digitando o número da opção desejada

## 📁 Estrutura do Projeto

```
sistema-ouvidoria/
├── 📄 menu_sql.py          # Arquivo principal com o menu interativo
├── 🔧 operacoesbd.py       # Módulo com operações de banco de dados
└── 📖 README.md           # Este arquivo
```
