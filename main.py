import requests

from nltk import SnowballStemmer

headers = {
    "user-key": "784ec322311e436a68a78070efb3d960"
}

def SummaryByName():
    print('Enter name please')
    r = requests.get("https://api-v3.igdb.com/games/?search="+str(input())+"&fields=name,summary", headers = headers).json()
    for i in r:
        print(i.get('name')+'\n')
        print(i.get('summary')+'\n\n')
    return

def NameBySummary():
    genre,company,description,SearchQuoteIn,check,SearchQuote,platform = str(),str(),str(),str(),False,str(),str()
    genres = [
        'point-and-click',
        'fighting',
        'shooter',
        'music',
        'platform',
        'puzzle',
        'racing',
        'real-time-strategy-rts',
        'role-playing-rpg',
        'simulator',
        'sport',
        'strategy',
        'turn-based-strategy-tbs',
        'tactical',
        'hack-and-slash-beat-em-up',
        'quiz-trivia',
        'pinball',
        'adventure',
        'indie',
        'arcade'
    ]
    print('Which parameters of game do you know?\n(Such as genre, company (developer or publisher),platform or short description)')
    ch = SnowballStemmer('english').stem(str(input()))
    if SnowballStemmer('english').stem('genre') in ch:
        while check == False:
            print('Enter genre:')
            genre = str(input())
            for k in genres:
                if SnowballStemmer('english').stem(k) in SnowballStemmer('english').stem(genre):
                    SearchQuoteIn = "https://api-v3.igdb.com/genres/"+k
                    check = True
            if SearchQuote == None:
                print('I do not know this genre. Repeat pls.')
    else:
        SearchQuoteIn = "https://api-v3.igdb.com/"
    if SnowballStemmer('english').stem('company') in ch:
        print('Enter company:')
        company = str(input())                                  #TODO
        if  SearchQuoteIn == "https://api-v3.igdb.com/"
        SearchQuote += ',company'
    if SnowballStemmer('english').stem('platform') in ch:
        print('Enter platform:')
        platform = str(input())
        SearchQuote += ',platform'
    if SnowballStemmer('english').stem('description') in ch:
        print('Enter description:')
        description = str(input())
        SearchQuote += ',description'
    
    return

ch = str()  #input var
check = False  #check var, used in algoryphm cycling
print('Hello!\nI can search for specific game or show you summary of any game.\nChoose please.')
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
