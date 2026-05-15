# 🍔 Delivery System - Django

Sistema de delivery desenvolvido em Django com foco na aplicação de padrões de projeto (Design Patterns), arquitetura modular e boas práticas de desenvolvimento web.

---

# 📚 Sobre o Projeto

O projeto simula um sistema de delivery de lanches artesanais, permitindo:

* Cadastro e autenticação de usuários
* Realização de pedidos
* Escolha de adicionais
* Seleção de entrega
* Pagamento via PIX ou Cartão
* Controle de saldo do usuário
* Histórico de pedidos
* Cadastro de cartão
* Área do usuário
* Interface responsiva e moderna

---

# 🏗️ Arquitetura do Projeto

O sistema foi modularizado utilizando múltiplos apps Django, separando responsabilidades por domínio de negócio.

```txt
delivery_project/
│
├── accounts/
├── products/
├── orders/
├── core/
│
├── delivery_project/
│
├── db.sqlite3
├── manage.py
└── seed.py
```

---

# 📦 Responsabilidade de Cada App

## accounts

Responsável por:

* Login
* Logout
* Cadastro
* Perfil do usuário
* Saldo
* Cartão
* Endereço

---

## products

Responsável por:

* Catálogo de produtos
* Cardápio

---

## orders

Responsável por:

* Pedidos
* Histórico
* Regras de negócio
* Pagamentos
* Estratégias de entrega

---

## core

Responsável por:

* Templates globais
* Navbar
* Estilização
* Layout base

---

# 🎯 Padrões de Projeto Utilizados

O projeto utiliza diversos Design Patterns de forma integrada.

---

## 1. Decorator Pattern

Utilizado para adicionar adicionais aos lanches dinamicamente.

### Exemplo:

* Queijo
* Bacon
* Catupiry

Cada adicional altera:

* descrição
* preço do pedido

### Arquivo:

```txt
orders/services/decorators.py
```

---

## 2. Strategy Pattern

Utilizado para cálculo do tipo de entrega.

### Estratégias:

* Entrega Normal
* Entrega Expressa

### Arquivo:

```txt
orders/services/delivery_strategy.py
```

---

## 3. Factory Pattern

Utilizado para criação dinâmica dos pagamentos.

### Tipos:

* PIX
* Cartão

Cada forma possui regras específicas:

* PIX aplica desconto
* Cartão cobra valor integral

### Arquivo:

```txt
orders/services/payment_factory.py
```

---

## 4. Facade Pattern

Responsável por centralizar toda a lógica de finalização do pedido.

### Responsabilidades:

* calcular descontos
* calcular entrega
* aplicar pagamento
* descontar saldo
* criar pedido

### Arquivo:

```txt
orders/services/order_facade.py
```

---

# 🖥️ Tecnologias Utilizadas

* Python
* Django
* Bootstrap 5
* SQLite
* HTML
* CSS

---

# 🎨 Frontend

O frontend foi desenvolvido utilizando:

* Bootstrap 5
* CSS customizado
* Layout responsivo
* Navbar fixa
* Cards modernos
* Interface mobile friendly

---

# 🔐 Funcionalidades de Segurança

## Validação de senha

A senha deve possuir:

* mínimo de 8 caracteres
* uma letra maiúscula
* uma letra minúscula
* um caractere especial

---

# 👤 Área do Usuário

O usuário possui acesso a:

* saldo
* endereço
* cartão cadastrado
* histórico de pedidos

---

# 💳 Regras de Pagamento

## PIX

* aplica 10% de desconto
* desconta do saldo

## Cartão

* valor integral
* exige cartão cadastrado
* desconta do saldo

---

# 🚚 Tipos de Entrega

## Normal

Taxa:

```txt
R$ 5
```

## Expressa

Taxa:

```txt
R$ 15
```

---

# 🧪 Seed de Dados

O projeto possui um arquivo de seed para popular automaticamente:

* produtos
* usuários
* perfis

---

# ▶️ Como Executar o Projeto

## 1. Clonar o repositório

```bash
git clone <url-do-repositorio>
```

---

## 2. Entrar na pasta

```bash
cd delivery_project
```

---

## 3. Criar ambiente virtual

### Windows

```bash
py -m venv venv
```

---

## 4. Ativar ambiente virtual

### Windows

```bash
venv\Scripts\activate
```

---

## 5. Instalar dependências

```bash
pip install django
```

---

## 6. Executar migrations

```bash
py manage.py makemigrations
```

```bash
py manage.py migrate
```

---

## 7. Executar seed

```bash
py seed.py
```

---

## 8. Rodar servidor

```bash
py manage.py runserver
```

---

# 🌐 Acessar o Sistema

```txt
http://127.0.0.1:8000
```

---

# 👨‍💻 Usuários Mockados

Senha padrão:

```txt
123
```

Usuários:

```txt
Carlos
Marina
Fernanda
Lucas
```

---

# 📱 Funcionalidades Implementadas

* [x] Cadastro
* [x] Login
* [x] Logout
* [x] Histórico de pedidos
* [x] Controle de saldo
* [x] Cadastro de cartão
* [x] Adicionais no pedido
* [x] Estratégias de entrega
* [x] Pagamentos
* [x] Seed automática
* [x] Navbar responsiva
* [x] Layout moderno
* [x] Arquitetura modular
* [x] Class Based Views

---

# 📌 Melhorias Futuras

* Upload real de imagens
* Integração com gateway de pagamento
* Painel administrativo customizado
* Cupons de desconto
* Sistema de avaliações
* WebSockets para status do pedido
* Dockerização
* Deploy em cloud

---

# 👨‍🏫 Objetivo Acadêmico

Este projeto foi desenvolvido com foco no estudo de:

* Arquitetura de Software
* Padrões de Projeto
* Django
* Organização de código
* Escalabilidade
* Separação de responsabilidades

---
