# Avaliação SUTHUB

projeto está no GitHub para Baixar
https://github.com/giovanniPanella/APIFast


Este projeto consiste em uma API para gerenciar **faixas etárias** e realizar **inscrições de usuários** com base em sua idade e CPF. O sistema oferece autenticação via **Basic Auth** e persistência dos dados em **MongoDB local**.

---

## Funcionalidades

### Para usuários administradores (com autenticação):

- Cadastrar nova faixa etária (`/age-groups/`)
- Listar todas as faixas etárias (`/age-groups/`)
- Deletar uma faixa etária (`/age-groups/{id}`)

### Para usuários finais:

- Solicitar inscrição (`/enrollments/`)
- Verificar status da inscrição por CPF (`/enrollments/status/{cpf}`)

---

## Autenticação
- A rota de inscrição e Cosnulta deixei Publica, pois entendi que o usuário final não precisa estar logado para fazer a inscrição

- O sistema utiliza **Basic Auth**.
- As credenciais padrão estão definidas em um arquivo estático ou variável de ambiente:

```bash
Usuário: admin
Senha: 1234
```
##  Testes usei PYtest
pytest -v

---

## Docker
para rodar o container precisa do Docker e Docker Compose
```bash
docker-compose up --build
```
terá a API e o db em Mongo
A API estará disponível em http://localhost:8000
http://localhost:8000/docs

