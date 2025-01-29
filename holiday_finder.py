import requests
def get_public_holidays(api_key, country, year):
    url = "https://calendarific.com/api/v2/holidays"
    params = {
        'api_key': api_key,
        'country': country,
        'year': year
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        if data['meta']['code'] == 200:
            return data['response']['holidays']
        else:
            print(f"Error: {data['meta']['error_detail']}")
            return None
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return None
    
def display_holidays(holidays):
    if holidays:
        for holiday in holidays:
            print(f"{holiday['date']['iso']}: {holiday['name']}")
    else:
        print("No holidays found or there was an error fetching the data.")

def main():
    api_key = 'your_api_key_here'  # Replace with your actual API key
    country = input("Enter the country code (e.g., US, GB): ").upper()
    year = input("Enter the year (e.g., 2023): ")
    
    holidays = get_public_holidays(api_key, country, year)
    display_holidays(holidays)

if __name__ == "__main__":
    main()            