import requests
import sys
import tkinter as tk

def get_streaming_options(title):
    API_KEY = "a0cf2c95f38333f028ccf03f2e6510d4"

    movie_title = title 

    search_url= f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={movie_title}"

    #sending an http request to the search URL for the Movie Title and convert it from json to python readable dictionary list
    search_resp = requests.get(search_url).json()

    #getting the ID information from the results array at position 0
    try:
        movie_id = search_resp['results'][0]['id']
    except IndexError:
        sys.exit("That movie does not exist")
        

    #accessing the watch/providers endpoint to with the movie ID and key
    provider_url = f"https://api.themoviedb.org/3/movie/{movie_id}/watch/providers?api_key={API_KEY}"

    #make get request for provider information and provider_url
    provider_resp = requests.get(provider_url).json()

    #the database stores this information using country codes. 
    #use .get with US parameter to get the US data fron the results data
    us_providers = provider_resp['results'].get('US')

    #flatrate buy and rent are the 3 catergories
    #for the 3 types, if it exists with that type in the us providers array, print it to console
   
    if us_providers:
        results =[]
        print(f"{movie_title}")
        for type_ in ['flatrate','buy','rent']:
            if type_ in us_providers:
                results.append(f"Avaliable to {type_}:")
                for provider in us_providers[type_]:
                    results.append(f" - {provider['provider_name']}")
    else:
        print("No US Providers")
    return results


window = tk.Tk()
frame_a = tk.Frame()
frame_b = tk.Frame()
label_1 = tk.Label(master= frame_a, text="Im in frame a")
label_2 = tk.Label(master= frame_b, text="Im in frame b")
button_a = tk.Button(master=frame_a,text="a Button")
frame_a.pack()
frame_b.pack()
label_1.pack()
label_2.pack()
button_a.pack()



window.mainloop()



#options = get_streaming_options("Kikis Delivery Service")
#for line in options:
#    print(line)