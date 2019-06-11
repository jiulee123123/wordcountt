from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def counter(request):
    full_text = request.GET['fulltext']

    word_list = full_text.split()

    word_dictionary = {}
    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1

    return render(request, 'counter.html', {'fulltext' : full_text,
    'total' : len(word_list), 'dictionary' : word_dictionary.items()})