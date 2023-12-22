import requests
import folium

def get_user_location():
    try:
        # Fetching public IP address using a free service
        ip_response = requests.get('https://api.ipify.org?format=json')
        ip = ip_response.json()['ip']

        # Fetching location based on IP address using ip-api.com
        location_response = requests.get(f'http://ip-api.com/json/{ip}')
        location_data = location_response.json()

        return location_data
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def display_location_on_map(location_data):
    if location_data:
        lat = location_data['lat']
        lon = location_data['lon']
        location = f"{location_data['city']}, {location_data['regionName']}, {location_data['country']}"

        # Create a map centered around the user's location
        user_map = folium.Map(location=[lat, lon], zoom_start=10)
        folium.Marker([lat, lon], popup=location).add_to(user_map)

        # Save the map as an HTML file
        user_map.save("user_location_map.html")
        print(f"Map generated and saved as 'user_location_map.html'.")
    else:
        print("No location data available.")

# Get user's location data
user_location = get_user_location()

# Display location on a map
display_location_on_map(user_location)
