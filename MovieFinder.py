import requests
import sys
import tkinter as tk


def get_options(title):
        
    try:
        # Validate input
        if not title or not isinstance(title, (str, int, float)):
            return ["Error: Invalid title provided. Title must be a non-empty string or number."]

        category_labels = {
            'flatrate': "Streaming",
            'rent': "Rental",
            'buy': "Purchase"
        }
       ################################################ 
        API_KEY = "a0cf2c95f38333f028ccf03f2e6510d4"
        movie_title = str(title) 
       ###################################################    
        
        
        # Step 1: Search for the movie
        search_url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={movie_title}"
        
        try:
            search_resp = requests.get(search_url)
            search_resp.raise_for_status()  # Raises exception for 4XX/5XX errors
            search_data = search_resp.json()
        except requests.exceptions.RequestException as e:
            return [f"Error: Failed to fetch movie data - {str(e)}"]
        except ValueError:
            return ["Error: Invalid JSON response from movie search API"]

        # Check if results exist
        if not search_data.get('results'):
            return [f"Error: No movie found with title '{movie_title}'"]

        # Step 2: Get movie ID
        try:
            movie_id = search_data['results'][0]['id']
        except (KeyError, IndexError):
            return ["Error: Could not extract movie ID from API response"]

        # Step 3: Get provider information
        provider_url = f"https://api.themoviedb.org/3/movie/{movie_id}/watch/providers?api_key={API_KEY}"
        
        try:
            provider_resp = requests.get(provider_url)
            provider_resp.raise_for_status()
            provider_data = provider_resp.json()
        except requests.exceptions.RequestException as e:
            return [f"Error: Failed to fetch provider data - {str(e)}"]
        except ValueError:
            return ["Error: Invalid JSON response from provider API"]

        # Step 4: Process provider data
        results = [f"{title}"]
        
        try:
            us_providers = provider_data.get('results', {}).get('US', {})
            
            for category in ['flatrate', 'rent', 'buy']:
                if category in us_providers:
                    results.append(category_labels[category])
                    for provider in us_providers[category]:
                        results.append(f"--{provider['provider_name']}")
                        
            # If no providers found at all
            if len(results) == 1:  # Only title was added
                results.append("No streaming, rental, or purchase options found for US region.")
                
        except Exception as e:
            return [f"Error: Failed to process provider data - {str(e)}"]

        return results

    except Exception as e:
        return [f"Unexpected error: {str(e)}"]
   




#options = get_options("Bfdasf")
    
#print('\n'.join(options))


