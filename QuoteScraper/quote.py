import requests
import re   # Regular Expression for string matching
from requests.exceptions import RequestException, ConnectionError


def main():

     # Print Menu
    print("-------Program to display Quote of the Day-------")
    print("""\
0:  Exit Program
1:  Brainy Quote
2:  Art Quote
3:  Love Quote
4:  Nature Quote
5:  Funny Quote
    """)

    # Prompt User Input
    while(True):
        choice = input('Please Enter your Choice: ')
        
        # Exit Program 
        if not re.search('[0-5]',choice):
            print('Not Match! ')
        elif choice == '0':
            break
        else:
            # Set URL 
            URL = ""
            print("") 
            if choice == '1':
                URL = "https://www.brainyquote.com/link/quotebr.js"
                print("----Brainy Quotes----")
            elif choice == '2':
                URL = "https://www.brainyquote.com/link/quotear.js"
                print("----Art Quotes----")
            elif choice == '3':
                URL ="https://www.brainyquote.com/link/quotelo.js"
                print("----Love Quotes----")
            elif choice == '4':
                URL = "https://www.brainyquote.com/link/quotena.js"
                print("----Nature Quotes----")
            elif choice == '5':
                URL = "https://www.brainyquote.com/link/quotefu.js"
                print("----Funny Quotes----")
            
            # Send Request
            try : 
                # User-Agent
                headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
                
                response = requests.get(URL, headers=headers)
                # only parse if status code is 200
                if (response.status_code == 200):
                    # Split response
                    text = response.text
                    text = text.split(';\n')
                    quote = text[2]
                    author = text[3]    
                    # Regex to scrape output
                    author = re.findall("(?<=[>]).*(?=[<])", author)[0]
                    quote = re.findall("(?<=[\"]).*\.",quote)[0]
                    print(quote)
                    print(f'by {author}\n')
                else:
                    print("Something went wrong !")
            
            except ConnectionError as e: 
                print (f'It seems like network is down....')
            except RequestException as e:
                print(f'Error Occured: {e}')


    print('Bye !')

    
if __name__ == '__main__':
    main()
