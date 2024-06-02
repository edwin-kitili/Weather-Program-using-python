import requests

# try:

#     # response = requests.get("https://api.openweathermap.org/data/2.5/weather? units = metrics$lat=50.8&lon=4.35&appid=eb95c29aad633a965f83a931cb027490")
#     response = requests.get("https://api.openweathermap.org/data/2.5/weather?units=metric&lat=50.8&lon=4.35&appid=eb95c29aad633a965f83a931cb027490")


#     print (response.json())
    
# except:
#     print("No internet connection")
    
# # print (response_json = response.json ["main"])
# # print (response_json = response.json ["main"])

# response_json = response.json()
# temp = (response_json["main"],["temp"])
# temp_min = (response_json["main"],["temp_min"])
# temp_max = (response_json["main"],["temp_max"])

# print (f" In Brussels it is {temp}° C")
# print (f"Today High: {temp_min}° C")
# print (f"Today Low: {temp_max}° C")

class City:
    def __init__(self,name,lat,lon, units = "metrics"):
        self.name= name
        self.lat = lat
        self.lon = lon
        self.units = units
        self.get_data()
    
    def get_data(self):
        try:
            response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?units={self.units}&lat={self.lat}&lon={self.lon}&appid=eb95c29aad633a965f83a931cb027490")
            print (response.json())
    
        except:
          print("No internet connection")
    



        self.response_json = response.json()
        self.temp = self.response_json["main"],["temp"]
        self.temp_min = self.response_json["main"],["temp_min"]
        self.temp_max = self.response_json["main"],["temp_max"]
    def temp_print(self):
        unit_symbol = "C"
        if self.units == "imperial":
                    unit_symbol = "F"

        print (f" In Brussels it is {self.temp}° {unit_symbol}")
        print (f"Today High: {self.temp_min}° {unit_symbol}")
        print (f"Today Low: {self.temp_max}° {unit_symbol}")
        
        
        
my_city = City("Brussels", 50.8,4.35)
my_city.temp_print()
vacation_city = City("Miami",25.7617,-80.1918, units="imperial")
my_city.temp_print ()
print (vacation_city.response_json)
        


