import requests, json, time, os, sys

with open('yt_api_key.txt', 'r') as f: API_KEY = f.read().strip() # Reads The API key from the file
BASE_URL = "https://www.googleapis.com/youtube/v3/search"

def main():
    def banner():
        BANNER = f"""
██    ██ ████████ ███████ ███████  █████  ██████   ██████ ██   ██ ██████  ██    ██ 
 ██  ██     ██    ██      ██      ██   ██ ██   ██ ██      ██   ██ ██   ██  ██  ██  
  ████      ██    ███████ █████   ███████ ██████  ██      ███████ ██████    ████   
   ██       ██         ██ ██      ██   ██ ██   ██ ██      ██   ██ ██         ██    
   ██       ██    ███████ ███████ ██   ██ ██   ██  ██████ ██   ██ ██         ██    
                                                        YTSEARCHPY - @bootlegfish  
                """
        print(BANNER)



    def again():
        time.sleep(0.75)
        choice = input("\n Do You Wish To Run The Program Again (y/n): ")
        if choice == 'y':
            if os.name == 'posix':
                os.system("clear")
                main()
            elif os.name == 'nt':
                os.system("cls")
                main()
        elif choice == 'n':
            if os.name == 'posix':
                os.system("clear")
                sys.exit(0)
            elif os.name == 'nt':
                os.system("cls")
                sys.exit(0)
        elif choice != 'y' or 'n':
            choice2 = input("ERROR: Invalid Answer")
            again()



    def yt_search():
        # Prompt Input Questions
        query = input("\nEnter Search Prompt: ")
        content_type = input("\nEnter Content Type (video, channel, playlist): ")
        max_results = input("\nWhat Is The Maximum Amount Of Results You Would Like?: ")

        params = {
            'part': 'snippet',
            'q': query,
            'type': content_type,
            'maxResults': max_results,
            'key': API_KEY 
        }

        try:
            response = requests.get(BASE_URL, params=params)
            response.raise_for_status()
            data = response.json()
            print(f"Total results found: {data.get('pageInfo', {}).get('totalResults')}\n")
            for item in data.get('items', []):
                video_id = item['id']['videoId']
                title = item['snippet']['title']
                channel_title = item['snippet']['channelTitle']
                writedata = f"Title: {title} \n Channel: {channel_title} \n Video Url: https://www.youtube.com/watch?v={video_id} \n -------------------------------------\n"
                # Write The Data To The Text File
                if os.path.exists("ytsearchpy_results.txt"): 
                    with open('ytsearchpy_results.txt', 'a') as file: file.write(writedata)
                else:
                    if os.name == 'nt':
                        os.system("echo. > ytsearchpy_results.txt")
                        with open('ytsearchpy_results.txt', 'a') as file: file.write(writedata)
                    elif os.name == 'posix':
                        os.system("touch ytsearchpy_results.txt")
                        with open('ytsearchpy_results.txt', 'a') as file: file.write(writedata)
                print(writedata) # Output The Data To The Terminal
                
                
            again()

        except requests.exceptions.HTTPError as err:
            print(f"HTTP error occurred: {err}")
            print(f"Response Body: {response.text}")
        except requests.exceptions.RequestException as e:
            print(f"An error occurred during the request: {e}")



    banner()
    time.sleep(2)
    yt_search()

if __name__ == "__main__":
    main()
