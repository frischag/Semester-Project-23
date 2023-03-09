import requests
import utils
import news_utils
import pprint

class HEADLINES:
    def __init__(self):
        print(utils.title("Today's Headlines"))

    def get_headline(self):
        self.headline_key = input("Enter keyword search: ")
        self.headline = f"{self.headline_key}"

    def parameters(self):
        try:
            query_string = {
                "q": self.headline,
                "apiKey": news_utils.API_KEY,
                "language": "en"
            }

            response = requests.get(
                news_utils.TOP_HEADLINES,
                params=query_string
            )
            
            if(response.status_code == 200):
                self.headline_return = response.json()
                pprint.pprint(self.headline_return)
                for i in self.headline_return['articles']:
                    print("")
                    print(i['title'])
                    print(i['description'])
                    print(i['url'])
                # print(response.text)
                # print(self.headline_return)
                
                
            else:
                print("Try again.")
                self.get_headline()

           
            

            
        except:
            print("Sorry. Nope.")

            

headlines = HEADLINES()
headlines.get_headline()
headlines.parameters()
