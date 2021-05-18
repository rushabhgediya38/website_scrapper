from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.parsers import JSONParser

from .models import freq
from bs4 import BeautifulSoup

import requests
from collections import Counter

from .serializers import FreqSerializers

import nltk

nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def Home(request):
    return render(request, 'home.html')


def FreqUrlGet(request):
    if request.method == 'POST':
        data1 = request.POST['freq_url']
        saveSerializedData = FreqSerializers(data=request.POST)
        if saveSerializedData.is_valid():

            t1 = freq.objects.filter(freq_url=data1).first()
            if t1:
                context = {
                    'ab': t1,
                }
                return render(request, 'ResultFreq.html', context)
            else:
                global data_url
                data_url = data1

                page = requests.get(data_url)
                soups = BeautifulSoup(page.content, 'html.parser')
                hello = soups.text
                lower_word = hello.lower()
                # print(type(lower_word))  # string

                stop_words = ("'all', 'just', 'being', 'over', 'both', 'through', 'yourselves', 'its', "
                              "'before', 'herself', 'had', 'should', 'to', 'only', 'under', 'ours', "
                              "'has', 'do', 'them', 'his', 'very', 'they', 'not', 'during', 'now', "
                              "'him', 'nor', 'did', 'this', 'she', 'each', 'further', 'where', 'few', "
                              "'because', 'doing', 'some', 'are', 'our', 'ourselves', 'out', 'what', "
                              "'for', 'while', 'does', 'above', 'between', 't', 'be', 'we', 'who', "
                              "'were', 'here', 'hers', 'by', 'on', 'about', 'of', 'against', 's', "
                              "'or', 'own', 'into', 'yourself', 'down', 'your', 'from', 'her', "
                              "'their', 'there', 'been', 'whom', 'too', 'themselves', 'was', 'until', "
                              "'more', 'himself', 'that', 'but', 'don', 'with', 'than', 'those', 'he', "
                              "'me', 'myself', 'these', 'up', 'will', 'below', 'can', 'theirs', 'my', "
                              "'and', 'then', 'is', 'am', 'it', 'an', 'as', 'itself', 'at', 'have', "
                              "'in', 'any', 'if', 'again', 'no', 'when', 'same', 'how', 'other', "
                              "'which', 'you', 'after', 'most', 'such', 'why', 'a', 'off', 'i','’', '>', "
                              "'yours', 'so', 'the', 'having', 'once',''['', '']'' '.', '``','''',"
                              " '(', ')', '{', '}', '=', ',""', ':', '^', ';', '?'")
                word_tokens = word_tokenize(lower_word)
                # already in list
                filtered_sentences = [w for w in word_tokens if not w in stop_words]
                # filtered_sentence = " ".join(filtered_sentences)

                # print(type(filtered_sentence))

                Counters = Counter(filtered_sentences)

                common_data = Counters.most_common(10)

                saveSerializedData.save(content=common_data)

            return redirect('ResultFreq')

    else:
        return render(request, 'freUrl.html')


def ResultFreq(request):
    abc = data_url
    question = get_object_or_404(freq, freq_url__iexact=abc)

    context = {
        'single_data': question
    }

    return render(request, 'ResultFreq.html', context)


