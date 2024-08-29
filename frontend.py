#bibliotecas
import folium
import requests
import schedule

urlAPI = f'http://127.0.0.1:5000/dados'

#buscando dados da API backend

def main():
    print('Iniciando atualização...')
    request = requests.get(urlAPI)
    if request.status_code == 200:
        databaseAPI = request.json()
    else:
        print("Requisição ao back sem sucesso!")

    #criando mapa
    mapa = folium.Map(
                    location = [-15.816094272808728, -47.9281817833751], 
                    zoom_start= 4
                    )


    #setando localização dos caminhões com looping
    def markerMap(localizacao, nome, placa, tempo_status):
        folium.Marker(
                    location=localizacao.split(","), 
                    popup=f"<b>Motorista:</b> {nome}\n<b>Tempo:</b> {tempo_status}", 
                    tooltip=f"<b>Placa:</b> {placa}", 
                    icon=folium.Icon(color= 'red', icon_color= 'white', icon="truck", prefix="fa")
                    ).add_to(mapa)    

    for x in databaseAPI:
        #indices ( geolocalizacao, nome do motorista, placa, tempo no status)
        markerMap(x[0],x[1],x[2],x[3])    

    #exportando mapa
    mapa.save('C:/nginx/html/index.html')
    print('Atualização finalizada...')
#main()

schedule.every(60).seconds.do(main)

while True:
    schedule.run_pending()