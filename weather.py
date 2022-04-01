import sys
import datetime
import requests
import json


with open("history_of_weather.json", "r") as f:
    saved_history = json.load(f)


def spr_danych_o_deszczu():
    if date_to_check in saved_history:
        print(f"Opady w dniu {date_to_check}: {saved_history[date_to_check]}")
    else:
        from datetime import datetime  # TODO: dlaczego nie zaciąga tu fromtimestamp z import datetime?
        url = "https://community-open-weather-map.p.rapidapi.com/forecast/daily"
        params = {"q": "san francisco,us", "lat": "35", "lon": "139", "cnt": "10", "units": "metric or imperial"}
        headers = {"X-RapidAPI-Host": "community-open-weather-map.p.rapidapi.com", "X-RapidAPI-Key": sys.argv[1]}
        response = requests.get(url, headers=headers, params=params)
        user_object = response.json()   # (response.json())
        for element in user_object["list"]:
            rain = element.get("pop", 0)
            date_info = element["dt"]
            day = datetime.fromtimestamp(date_info).date()
            saved_history[str(day)] = rain
        if date_to_check in saved_history:
            print(f"Opady w dniu {date_to_check}: {saved_history[date_to_check]}")
            with open("history_of_weather.json", "w") as f:  #TODO: nadpisuje wszystko, ZMIENIĆ na dopisywanie, chyba, że nie trzeba?
                json.dump(saved_history, f)
        else:
            print("Zapytanie o datę spoza naszej bazy")


if len(sys.argv) == 3:  # podano datę na wejściu
    API_key = sys.argv[1]
    date_to_check = sys.argv[2]    # TODO: sprawdzić popoprawność podania daty?
    spr_danych_o_deszczu()
elif len(sys.argv) == 2:  # nie podano daty na wejściu
    API_key = sys.argv[1]
    date_to_check = str(datetime.datetime.now().date() + datetime.timedelta(days=1))
    spr_danych_o_deszczu()
else:
    print("Błąd - wprowadzono niepoprawne dane wejściowe z std")

