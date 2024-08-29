#bibliotecas
from mysql import connector as conector 
from flask import Flask
import os

host = os.getenv('SERVER_MYSQL')
user = os.getenv('USER_MYSQL')
password = os.getenv('PWD_MYSQL')
database = os.getenv('DB_MYSQL')


query = "SELECT concat(latitude,',', longitude) as geolocalizacao, nome, placa_veiculo, cast(tempo_atividade as char) as tempo_atividade FROM VIEW_RESUMIDA_LOCALIZACAO_REAL_TIME_TRANSLOVATO"

#conexão com MYSQL

def conectAndExecute():
    conexao = conector.connect(host=host, user=user, password=password, database=database)
    print('Conectado ao banco...')

    #criação do select
    cursor = conexao.cursor()

    def selectMysql():
        cursor.execute(query)
        resultDef = cursor.fetchall()
        print('Atualizando dados...')
        return resultDef

    result = selectMysql()
    conexao.commit()
    print('Comando executado...')

    #fecha conexões
    cursor.close()
    conexao.close()
    print('Conexão e cursor finalizados...')

    return result

#resultados disponibilizados via API
app = Flask(__name__)
@app.route("/dados")
def dados():
    result = conectAndExecute()
    return result
