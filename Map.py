import geocoder
import folium

def main():
    g = geocoder.ip('me')
    latitude, longitude = g.latlng

    # Use the HTTP(S) URL for the Mapbox style
    mapbox_style_url = 'https://api.mapbox.com/styles/v1/abimeena/cllutqnf200d101pfgcxn620f/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoiYWJpbWVlbmEiLCJhIjoiY2xscWFnbGdnMGVpczNkdGhsZXQ3ZjloYyJ9.40_2kTW03fUcEilsHoNOMQ'

    # Specify the attribution for the Mapbox tiles
    attribution = 'Map data &copy; <a href="https://www.mapbox.com/">Mapbox</a>'

    # Load your existing Mapbox map with the style URL and attribution
    existing_map = folium.Map(location=[latitude, longitude], zoom_start=12, tiles=mapbox_style_url, attr=attribution)

    folium.Marker([latitude, longitude], popup="Your Live Location").add_to(existing_map)

    # Save the map with the added live location marker
    existing_map.save('map_with_live_location.html')

if __name__ == "__main__":
    main()


