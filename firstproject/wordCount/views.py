from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"home.html")

def result(request):
    sentence = request.GET['sentence']
    
    wordList = sentence.split()
# 공백을 기준으로 구분시켜줌
    wordDict={}

    for word in wordList:
        if word in wordDict:
            wordDict[word]+=1
        else:
            wordDict[word]=1
# for문을 이용해서 단어의 수 카운팅
    return render(request,"result.html",{'fulltext':sentence,'count':len(wordList),'wordDict':wordDict.items})
# 딕셔너리값을 담아서 문장,길이,단어를 return함
    