# **fastAPI-studies**

![HTML](https://img.shields.io/badge/html-51.6%25-blue)
![Python](https://img.shields.io/badge/python-48.4%25-blue)
![Languages](https://img.shields.io/badge/languages-2-blue)

---

## Construído com as tecnologias:

![pip](https://img.shields.io/badge/pip-red) &nbsp;
![HTML](https://img.shields.io/badge/HTML-yellow) &nbsp;
![Python](https://img.shields.io/badge/py-fastAPI-blue) &nbsp;
![CSS](https://img.shields.io/badge/css-Tailwind.css-blue) &nbsp;

---

# Visão Geral

**fastAPI-studies** é uma API em **Python** e **FastAPI**, com uma interface em **HTML** e **Tailwind.css**, desenvolvidada como estudo sobre a aplicação de Inteligência Artificial e dos serviços da **OpenRouter**, direcionado para o meu Projeto Integrador da *Fatec São Caetano do Sul*.
A partir de uma inserção de arquivos *.txt* ou *.json*, a API recebe uma requisição *Post* e converte o conteúdo do arquivo em uma string, passando pelos devidos filtros decorrente do formato do arquivo, e enviando esta string para um modelo de IA do DeepSeek, onde esta processa a informação e retorna ao console da API

A escolha de depositar o conteúdo dos arquivos e enviar como uma string para o modelo de IA vem da maneira pela qual os serviços da OpenRouter são estruturados, permitindo a leitura de arquivos apenas mediante *tokens* de utilização pagos, sendo assim, uma primeira alternativa para solucionar esta problemática, visto o objetivo de custo zero com tecnologia do meu projeto, é a conversão do conteúdo à maneira gratuita de se enviar informações para os modelos disponíveis: Strings; e com uma pré-configuração do *prompt* à ser enviado ao modelo, podemos receber informações com um nível de similariedade adequada para os fins do projeto.

Este estudo também serviu como uma introdução pessoal ao Tailwind.css, tecnologia que nunca tive muito contato, porém se provou muito eficiente para este estudo.

---

## Primeiros Passos

### Pré-requisitos

Este projeto requer as seguintes dependências:

- **Linguagem de Programação:** Python
- **Gerenciador de Pacotes:** Pip

---

### Instalação

Construa a API a partir do código-fonte e instale as dependências:

1. **Clone o repositório:**

    ```bash
    git clone https://github.com/zanettIno/fastAPI-studies.git
    ```

2. **Navegue até o diretório do projeto:**

    ```bash
    cd fastAPI-studies
    ```

3. **Crie e ative um ambiente virtual Python:**

    Windows
    ```bash 
    python -m venv venv_name
    .\venv\Scripts\activate
    ```

     Linux
     ```bash 
     python3 -m venv venv_name
     source venv/bin/activate
    ```

4. **Instale as dependências Python:**

    ```bash
    pip install -r requirements.txt
    ```

---

### Uso

Para executar o servidor localmente em modo de desenvolvimento:

```bash
uvicorn main:app --reload
