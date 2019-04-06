import requests
from nltk import SnowballStemmer

headers = {
    "user-key": "784ec322311e436a68a78070efb3d960"
}

def SummaryByName():
    print('Enter name please')
    r = requests.get("https://api-v3.igdb.com/games/?search="+str(input())+"&fields=name,summary", headers = headers)
    r = r.json()
    for i in r:
        print(i.get('name')+'\n')
        print(i.get('summary')+'\n\n')
    return

def NameBySummary():
    print('Enter genre')
    r = requests.get("https://api-v3.igdb.com/genres/", headers = headers).json()
    #TODO
    return

ch = str()  #input var
check = False  #check var, used in algoryphm cycling
print('Hello! How can I help you?\nChoose one of these: "find game" or "find summary.')
while check == False:
    ch = SnowballStemmer('english').stem(str(input()))
    if SnowballStemmer('english').stem('summary') in ch:
        SummaryByName()
        check = True
    elif SnowballStemmer('english').stem('game') in ch:
        NameBySummary()
        check = True
    else:
        print('Sorry, I cannot understand you. Repeat please')
