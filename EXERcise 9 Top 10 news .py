"""
IT is program which get the data from news api and tells the top trending news
on county  which we want

"""


def top10news():
    import requests

    #here we get the url from api news and there we have our api and get all top news
    url="https://newsapi.org/v2/top-headlines?country=in&apiKey=15b7bfe40ebe4deeaafe8c770b9802de"
                                              # country= which country you want top head lines here is in means india
    # here we made a request to gettin all the data
    get_infromation=requests.get(url)

    # when we get the data from server it is in the format of the json so we have to
    # convert it into the python so for this we use pythom.loads(get_information)
    # but here it will give error and to avoiding this error we use json() which
    # autmatically convert it
    get_infromation=get_infromation.json()

    # here we article list in one string
    article=get_infromation["articles"]

    # here it will get all the top titel ot top 10 lists of news
    top_trend_string=[]

    # here we appends all the title whci are present in thr articles in the string
    # of top_trend
    for ar in article:
        top_trend_string.append(ar["title"])

    # it will show top 10 stories
    for i in range(len(top_trend_string)): # here we also put values how much headlines we want eg--> range(0,10)
        print(i+1, top_trend_string[i])


    # it is used for speaking sound
    from win32com.client import Dispatch
    # setting voice
    sound=Dispatch("SAPI.Spvoice")
    # here what we put it will be speak
    sound.Speak("TOP Head Lines are...")
    sound.Speak(top_trend_string)

if __name__ == '__main__':
    top10news()

