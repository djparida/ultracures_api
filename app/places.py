from app import app,Flask, api, ma, db, CORS, Resource, jsonify
from googleplaces import GooglePlaces, types, lang 
import requests
import json 


@app.route('/api/places')
def place():
    API_KEY = 'AIzaSyAgG3HIwJ6GMRgwDbrfaVSpp73cvPZ4Z50'
    google_places = GooglePlaces(API_KEY) 

    query_result = google_places.nearby_search( 
            # lat_lng ={'lat': 46.1667, 'lng': -1.15}, 
            lat_lng ={'lat': 20.354165, 'lng': 85.815463}, 
            radius = 5000, 
            # types =[types.TYPE_HOSPITAL] or 
            # [types.TYPE_CAFE] or [type.TYPE_BAR] 
            # or [type.TYPE_CASINO]) 
            types =[types.TYPE_HOSPITAL]) 

    if query_result.has_attributions: 
        print (query_result.html_attributions) 
        print('##############')

    # print(query_result.places)
    hospital_lists = []
    Latitude_list = []
    Longitude_list = []
    placess = json.dumps(str(query_result.places))
    for place in query_result.places: 
        Hospital = str(place.name)
        Latitude = str(place.geo_location['lat'])
        Longitude = str(place.geo_location['lng'])
        # plc = place_lists(Hospital,Latitude,Longitude)
        hospital_lists.append(Hospital)
        Latitude_list.append(Latitude)
        Longitude_list.append(Longitude)
        # return jsonify(nearHospital)
    # print(hospital_lists)
    # print(Latitude_list)
    # print(Longitude_list)
    return {"Hospitals":json.dumps(hospital_lists), "Latitude_list":json.dumps(Latitude_list),"Longitude_list":json.dumps(Longitude_list) }