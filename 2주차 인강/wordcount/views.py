from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html') 
    # render은 3개의 인자까지 받을 수 있다. 첫 번째는 고정적으로 requrest받고 두번째는 template인자를 받고 세 번째는 사전형 객체를 받는다. dictionary 자료형

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext']
    words = text.split()
    word_dictionary = {}
    
    for word in words:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            #add to dictionary
            word_dictionary[word] = 1
    

    return render(request, 'result.html', {'full': text, 'total':len(words), 'dictionary':word_dictionary.items()})   #파이썬의 사전형 객체 