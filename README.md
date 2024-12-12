# Star Wars API

## Requisitos

- Python 3.9 ou superior
- Pipenv, pip ou virtualenv (opcional, mas recomendado)

---

## Instalação

### Configurar Ambiente Virtual (Opcional)

Recomendamos o uso de um ambiente virtual para isolar as dependências do projeto:

```bash
python -m venv venv  
source venv/bin/activate  # Linux/Mac  
venv\Scripts\activate     # Windows
```
### Instalar Dependências

Para instalar as dependências principais (produção):

```bash
pip install -r requirements.txt
```
Para instalar as dependências de desenvolvimento (inclui testes):

```bash
pip install -r requirements-dev.txt
```
---

## Configuração do Banco de Dados

A aplicação está configurada para utilizar **MongoDb** como banco de dados padrão.
Para preencher o banco de dados, rode o arquivo **seeds.py**
```bash
python seeds.py
```
---

## Executando a API

Para rodar o servidor de desenvolvimento:

```bash
python run.py
```
A API estará disponível em: [http://127.0.0.1:5000](http://127.0.0.1:8000)

---

## Testando a Aplicação

```bash
pytest
```
---

## Licença
Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para mais informações.