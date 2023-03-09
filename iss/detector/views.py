from django.shortcuts import render
import requests
from bs4 import BeautifulSoup


# Create your views here.
def home(request):
    if request.method == 'POST':
        loc = request.POST.get('loc')
        def convert(lst):
            return (lst[0].split())
        lst = [loc]
        lst = convert(lst)
        country = lst[0]
        city = lst[1]
        #city = request.POST.get('cit')
        find_iss(country, city)
        n_t = find_iss.n_t
        context = {
            'n_t': n_t
        }
    else:
        context = {}

        print("Not Requested")
    return render(request, 'index.html',context)


def find_iss(country,city):
    page = requests.get('https://spotthestation.nasa.gov/sightings/view.cfm?country={}&region=None&city={}'.format(country,city))
    soup = BeautifulSoup(page.content, 'html.parser')
    table = soup.find_all('table')[0]
    find_iss.n_t = []
    for row in table.find_all('tr'):
        new = []
        for col in row.find_all('td')[0:5]:
            new.append(col.get_text())
        find_iss.n_t.append(new)
    find_iss.n_t.pop(0)
