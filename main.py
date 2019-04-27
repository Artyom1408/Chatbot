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
    genre,company,description,check,SearchQuote,platform = str(),str(),str(),False,str(),str()
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
    print('Which parameters of game do you know?\n(Such as genre, platform or short description)')
    ch = SnowballStemmer('english').stem(str(input()))
    if SnowballStemmer('english').stem('genre') in ch:
        while check == False:
            print('Enter genre:')
            genre = str(input())
            for k in genres:
                if SnowballStemmer('english').stem(k) in SnowballStemmer('english').stem(genre):
                    SearchQuote = "https://api-v3.igdb.com/genres/"+k+"&fields=name,platform,summary" 
                    check = True
            if check == False:
                print('I do not know this genre. Repeat pls.')
    else:
        SearchQuote = "https://api-v3.igdb.com/games/&fields=name,platform,summary"
    if SnowballStemmer('english').stem('platform') in ch:
        print('Enter platform:')
        platform = str(input())
    if SnowballStemmer('english').stem('description') in ch:
        print('Enter description:')
        description = str(input())
    r = requests.get(SearchQuote,headers=headers).json()
    print("I found this:") 
    for block in r:
        if description!=str() and platform==str():
            if description in block:
                print(block.get(name)+\n)
                print(block.get(summary)+\n\n)
        elif description==str() and platform!=str():
            if platform in block:
                print(block.get(name)+\n)
                print(block.get(summary)+\n\n)
        elif description!=str() add platform!=str():
            if description in block and platform in block:
                print(block.get(name)+\n)
                print(block.get(summary)+\n\n)
        else:
            print("I can't help you if you know nothing") 

ch = str()  #input var
check = False  #check var, used in algoryphm cycling
print('Hello!\nI can recommend you a game or show you summary of any game.\nChoose please.')
while check == False:
    ch = SnowballStemmer('english').stem(str(input())).split()
    if SnowballStemmer('english').stem('summary') in ch:
        SummaryByName()
        check = True
    elif SnowballStemmer('english').stem('game') in ch:
        NameBySummary()
        check = True
    else:
        print('Sorry, I cannot understand you. Repeat please')

