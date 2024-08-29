# Projeto REAL TIME

### Após a execução do script de backend:
* Toda vez que a API é chamada pelo frontend o script python se conecta ao mysql para buscar dados em tempo real.
### Após a execução do script de frontend:
* É agendado a cada 60 segundos a atualização da interface grafica com novos dados recebidos da API
* O arquivo HTML é salvo diretamente no repositório do nginx, a visualização fica disponivel para toda a rede interna atravez do IP do Servidor.


# BACKEND

### Bibliotecas usadas

- mysql-connector-python (conexão com MySQL)
- flask (criação da API)
- so (busca variaveis de ambiente)

### Script

- backend.py

### Start do backend

- flask --app backend run

# FRONTEND

### Bibliotecas usadas

- folium (disponibiliza dados em visão grafica)
- requests (requisição a API)
- schedule (atualização agendada do frontend e requisição da API)

### Script 

- frontend.py

### Start do frontend

- python frontend.py