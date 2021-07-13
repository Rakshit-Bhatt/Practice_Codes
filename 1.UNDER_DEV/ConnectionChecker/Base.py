import requests
from datetime import datetime
import time

"""
requests.exceptions.MissingSchema is one kind of Exception occcured when web address is not used correctly.

"""
def checker(site):
    count=10
    while count!=1:

        now=datetime.now()
        try:
            score=requests.get(url=site)
            if score.status_code==200:
                print(now, "Internet working fine...", score)
            else:
                print(now, "Speed is slow....", score)

        except Exception as e:
            print("got an error:", e)
            break

        count-=1
        time.sleep(1)    

def URL_Collector(site):
    try:
        score=requests.get(url=site).headers
        print(score)
    except  Exception as e:
        print("An Error occured here! ", e)


if __name__=="__main__":

    webAddress=input("Enter the address of the site: ")
    
    #function call to check connection
    checker(webAddress)         #link its result to the connection label

    #function call to get headers.
    URL_Collector(webAddress)   #link its result to the output label
