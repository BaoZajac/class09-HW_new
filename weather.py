import sys
import datetime
import requests
import pprint


# if len(sys.argv) == 3:  # podano datę na wejściu
#     API_key = sys.argv[1]
#     date_to_check = sys.argv[2]    # TODO: sprawdzić popoprawność podania daty?
#     print(date_to_check)
# elif len(sys.argv) == 2:  # nie podano daty na wejściu
#     API_key = sys.argv[1]
#     date_to_check = datetime.datetime.now().date() + datetime.timedelta(days=1)
#     print(date_to_check)
# else:
#     print("Błąd - wprowadzono niepoprawne dane wejściowe z std")


# url = "https://community-open-weather-map.p.rapidapi.com/forecast/daily"
# params = {"q": "san francisco,us", "lat": "35", "lon": "139", "cnt": "10", "units": "metric or imperial"}
# headers = {"X-RapidAPI-Host": "community-open-weather-map.p.rapidapi.com", "X-RapidAPI-Key": sys.argv[1]}

# response = requests.get(url, headers=headers, params=params)
#
# from datetime import datetime    #TODO: dlaczego nie zaciąga tu fromtimestamp z import datetime?
# pprint.pprint(response.json())
#
# user_object = (response.json())
# with open("output.txt", "w") as f:
#     f.write(user_object)

user_object2 = {'city': {'coord': {'lat': 37.7749, 'lon': -122.4194},
          'country': 'US',
          'id': 5391959,
          'name': 'San Francisco',
          'population': 805235,
          'timezone': -25200},
 'cnt': 10,
 'cod': '200',
 'list': [{'clouds': 96,
           'deg': 272,
           'dt': 1648756800,
           'feels_like': {'day': 285.53,
                          'eve': 284.79,
                          'morn': 282.37,
                          'night': 283.06},
           'gust': 5.88,
           'humidity': 69,
           'pop': 0,
           'pressure': 1014,
           'speed': 4.5,
           'sunrise': 1648734969,
           'sunset': 1648780267,
           'temp': {'day': 286.35,
                    'eve': 285.61,
                    'max': 286.77,
                    'min': 282.3,
                    'morn': 282.37,
                    'night': 283.8},
           'weather': [{'description': 'overcast clouds',
                        'icon': '04d',
                        'id': 804,
                        'main': 'Clouds'}]},
          {'clouds': 0,
           'deg': 267,
           'dt': 1648843200,
           'feels_like': {'day': 287.12,
                          'eve': 284.41,
                          'morn': 283.04,
                          'night': 283.48},
           'gust': 5.47,
           'humidity': 64,
           'pop': 0,
           'pressure': 1014,
           'speed': 5.1,
           'sunrise': 1648821278,
           'sunset': 1648866721,
           'temp': {'day': 287.92,
                    'eve': 285.12,
                    'max': 288.09,
                    'min': 283.04,
                    'morn': 283.04,
                    'night': 284.16},
           'weather': [{'description': 'sky is clear',
                        'icon': '01d',
                        'id': 800,
                        'main': 'Clear'}]}]}

historia_opadow = {}

# print(user_object2["list"])
# print(user_object2["list"][0:len(user_object2["list"])]["pop"])

for idx in user_object2["list"][0:len("list")]:
    # if "pop" in idx:
    #     print(["pop"])
    pprint.pprint(idx)

# if ["pop"] in user_object2["list"]:
#     print(["pop"])

# for date in user_object["list"]:
#     if datetime.fromtimestamp(date["dt"]).date() == date_to_check:
#         print("yes!")
        # print(user_object["list"][]["pop"])
# date = (user_object["list"][0]["dt"])
# print(datetime.fromtimestamp(date).date())




# NIEDZIAŁAJĄCE API ---v----------------------------------------------------------------------

# response = requests.get(url)
# # r = requests.post(url, data={"key":"value"})
# # print(r.text)
# user_object = response.json()
# # pprint.pprint(user_object["results"][0])
# # look = user_object.get("results")     #("results")
# # print(look)
#
#
# response = requests.get(url)
# user_object = response.json()
# print(len(user_object))
#
# pprint.pprint(user_object)
# # pprint.pprint(user_object["repository"][0])
# # pprint.pprint(user_object[0])
# # pprint.pprint(user_object[0].keys())

# NIEDZIAŁAJĄCE API ---^-----------------------------------------------------------------------
