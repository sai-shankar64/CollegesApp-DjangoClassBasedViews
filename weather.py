import click
import json

@click.command()
@click.argument('cityname')
def getweather(cityname):
    # response=requests.get('https://samples.openweathermap.org/data/2.5/group?id=524901,703448,2643743&units=metric&appid=b6907d289e10d714a6e88b30761fae22')
    # print(response.json)
    with open('weather.json') as json_data:
        data=json.load(json_data)
    for i in range(0,data['cnt']):
        if(data['list'][i]['name'].lower()==cityname.lower()):
            print(data['list'][0])

if __name__=="__main__":
    getweather()
