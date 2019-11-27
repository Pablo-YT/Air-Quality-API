from django.shortcuts import render
import json
import requests



def API(request):
    # url = "http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=100&API_KEY=89AE5CA9-63B7-48DB-AEEE-D88482F920DA"

    # url = "http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=75051&distance=1000&API_KEY=89AE5CA9-63B7-48DB-AEEE-D88482F920DA"

    if request.method == "POST":
        zipcode = request.POST['zipcode']

        api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=100&API_KEY=89AE5CA9-63B7-48DB-AEEE-D88482F920DA")

        try:
            api = json.loads(api_request.content)
        
        except Exception as e:
            api = "Error...!"
        

        if api[0]['AQI'] <= 50:
            category_description = 'Good (0 - 50):  Air quality is considered satisfactory, and air pollution poses little or no risk'
            
            category_color = "good"
            
        elif api[0]['AQI'] <= 100: 
            category_description = 'Moderate (51 - 100): Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution.'
            
            category_color = "moderate"    
            
        elif api[0]['AQI'] <= 150:
            category_description = 'Unhealthy for Sensitive Groups (101 - 150): Although general public is not likely to be affected at this AQI range, people with lung disease, older adults and children are at a greater risk from exposure to ozone, whereas persons with heart and lung disease, older adults and children are at greater risk from the presence of particles in the air.'
            
            category_color = "usg"

        elif api[0]['AQI'] <= 200:
            category_description = 'Unhealthy (151 - 200): Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects.'
            
            category_color = "unhealthy"

        elif api[0]['AQI'] <= 300:
            category_description = 'Very Unhealthy (201 - 300): Health alert: everyone may experience more serious health effects.'
            
            category_color = "veryunhealthy"


        elif api[0]['AQI'] <= 500:
            category_description = 'Hazardous (301 - 500): Health warnings of emergency conditions. The entire population is more likely to be affected.'
            
            category_color = "hazardous"


        context = {
            'api': api,
            'category_description': category_description,
            'category_color' : category_color,
            'zipcode':zipcode
        }

        return render(request, 'API.html',context)

    else:
        api_request = requests.get('http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=25&API_KEY=89AE5CA9-63B7-48DB-AEEE-D88482F920DA')
        
        try:
            api = json.loads(api_request.content)
        
        except Exception as e:
            api = "Error...!"
        

        if api[0]['AQI'] <= 50:
            category_description = 'Good (0 - 50):  Air quality is considered satisfactory, and air pollution poses little or no risk'
            
            category_color = "good"
            
        elif api[0]['AQI'] <= 100: 
            category_description = 'Moderate (51 - 100): Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution.'
            
            category_color = "moderate"    
            
        elif api[0]['AQI'] <= 150:
            category_description = 'Unhealthy for Sensitive Groups (101 - 150): Although general public is not likely to be affected at this AQI range, people with lung disease, older adults and children are at a greater risk from exposure to ozone, whereas persons with heart and lung disease, older adults and children are at greater risk from the presence of particles in the air.'
            
            category_color = "usg"

        elif api[0]['AQI'] <= 200:
            category_description = 'Unhealthy (151 - 200): Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects.'
            
            category_color = "unhealthy"

        elif api[0]['AQI'] <= 300:
            category_description = 'Very Unhealthy (201 - 300): Health alert: everyone may experience more serious health effects.'
            
            category_color = "veryunhealthy"


        elif api[0]['AQI'] <= 500:
            category_description = 'Hazardous (301 - 500): Health warnings of emergency conditions. The entire population is more likely to be affected.'
            
            category_color = "hazardous"


        context = {
            'api': api,
            'category_description': category_description,
            'category_color' : category_color
        }

        return render(request, 'API.html',context)

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


def world_api(request):
    if request.method == "POST":
        city = request.POST['city']

        api_request = requests.get('https://api.waqi.info/feed/'+ city +'/?token=3d800fb686310da4b921000b3326d2388f30e166')

        try:
            api = json.loads(api_request.content)
        
        except Exception as e:
            api = "Error...!"
        

        if api['data']['aqi'] <= 50:
            category_description = 'Good (0 - 50):  Air quality is considered satisfactory, and air pollution poses little or no risk'
            
            category_color = "good"
            
        elif api['data']['aqi'] <= 100: 
            category_description = 'Moderate (51 - 100): Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution.'
            
            category_color = "moderate"    
            
        elif api['data']['aqi'] <= 150:
            category_description = 'Unhealthy for Sensitive Groups (101 - 150): Although general public is not likely to be affected at this AQI range, people with lung disease, older adults and children are at a greater risk from exposure to ozone, whereas persons with heart and lung disease, older adults and children are at greater risk from the presence of particles in the air.'
            
            category_color = "usg"

        elif api['data']['aqi'] <= 200:
            category_description = 'Unhealthy (151 - 200): Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects.'
            
            category_color = "unhealthy"

        elif api['data']['aqi'] <= 300:
            category_description = 'Very Unhealthy (201 - 300): Health alert: everyone may experience more serious health effects.'
            
            category_color = "veryunhealthy"


        elif api['data']['aqi'] <= 500:
            category_description = 'Hazardous (301 - 500): Health warnings of emergency conditions. The entire population is more likely to be affected.'
            
            category_color = "hazardous"


        context = {
            'api': api,
            'category_description': category_description,
            'category_color' : category_color,
        }

        return render(request, 'world_api.html',context)

    else:
        api_request = requests.get('https://api.waqi.info/feed/beijing/?token=3d800fb686310da4b921000b3326d2388f30e166')
        
        try:
            api = json.loads(api_request.content)
        
        except Exception as e:
            api = "Error...!"
        

        if api['data']['aqi'] <= 50:
            category_description = 'Good (0 - 50):  Air quality is considered satisfactory, and air pollution poses little or no risk'
            
            category_color = "good"
            
        elif api['data']['aqi'] <= 100: 
            category_description = 'Moderate (51 - 100): Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution.'
            
            category_color = "moderate"    
            
        elif api['data']['aqi'] <= 150:
            category_description = 'Unhealthy for Sensitive Groups (101 - 150): Although general public is not likely to be affected at this AQI range, people with lung disease, older adults and children are at a greater risk from exposure to ozone, whereas persons with heart and lung disease, older adults and children are at greater risk from the presence of particles in the air.'
            
            category_color = "usg"

        elif api['data']['aqi'] <= 200:
            category_description = 'Unhealthy (151 - 200): Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects.'
            
            category_color = "unhealthy"

        elif api['data']['aqi'] <= 300:
            category_description = 'Very Unhealthy (201 - 300): Health alert: everyone may experience more serious health effects.'
            
            category_color = "veryunhealthy"


        elif api['data']['aqi'] <= 500:
            category_description = 'Hazardous (301 - 500): Health warnings of emergency conditions. The entire population is more likely to be affected.'
            
            category_color = "hazardous"


        context = {
            'api': api,
            'category_description': category_description,
            'category_color' : category_color
        }

        return render(request, 'world_api.html',context)


    return render(request, 'world_api.html')