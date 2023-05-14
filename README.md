# Banco_DIM0517
Projeto para matéria DIM0517 - GERÊNCIA DE CONFIGURAÇÃO E MUDANÇAS (2023.1). 

## Requisitos

* Python Python 3.10 ou mais recente.

> Você pode ignorar os requisitos caso execute com docker.

## Executar

1. Execute o seguinte comando na raiz do projeto:
    ```
    PYTHONPATH=$PWD python src/client/main.py
    ```

## Docker

1. Faça build da imagem:

    ```
    docker build -t banco .
    ```
2. Execute o container em modo iterativo:

    ```
    docker run -it --rm banco
    ```