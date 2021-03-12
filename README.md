# TechStart 2° Edição.

## Descrição
Este é um app back-end de serviço para criar, ler, atualizar e excluir:
 - **Products**
 - **Sellers**
 - **Categories**
 - **Marketplaces**

Através dos endpoints:
 - `/product`
 - `/seller`
 - `/category`
 - `/marketplace`

É possível listar produtos com filtros adicionais.

Veja mais sobre na camada visual.

A especificação completa do desafio está em [specification.md](./specification.md).

## Tecnologias utilizadas
Dependências utilizadas:
1. `Python`
2. `FastAPI`
3. `Pydantic`
4. `SQLAlchemy`
5. `Black`
6. `Uvicorn`

A camada visual gerada com `FastAPI` foi a `Swagger UI`, acessível na rota `/docs`.

## Como rodar
Para rodar o projeto, você precisará ter o [poetry](https://python-poetry.org/) instalado em
ambiente `unix`.

Passos (clonagem e instalação de dependências):
```sh
git clone https://github.com/marcospb19/TechStart_2Ed joao_marcos_desafio
cd joao_marcos_desafio
poetry install
```

E então, dentro da virtualenv do `poetry`, rode `python server/main.py`:
```sh
poetry shell
cd server
python main.py
```

Por padrão, o `Uvicorn` vai usar a porta _8000_, mas você pode customizar passando por linha de
comando.

Por exemplo, para rodar na porta _5050_:
```sh
python main.py 5050
```

Agora para acessar a camada visual e testar a API, entre em http://localhost:8000/docs, onde no
lugar de _8000_, você deve inserir a porta que está sendo utilizada (dica: aparece no terminal).

## Preview da interface do Swagger UI:
![Swagger UI Preview](https://i.imgur.com/x8Nu5mQ.png)

## O que ficou faltando?
 - Diminuir repetição de código dos controladores com `CRUD` genérico.
 - Permitir um produto ter várias categorias, e vice-versa.
 - Utilizar `Alembic` para fazer migrações do banco.
 - Testes automatizados.
 - Revisar documentação de cada módulo (`\_\_init\_\_.py`).
