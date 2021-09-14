import requests_cache
import requests
from bs4 import BeautifulSoup
from datetime import datetime


# source: https://www.moh.gov.cy/moh/moh.nsf/All/0EFA027144C9E54AC22586BE0032B2F5

# wrapping the whole script in a function to call from plan.R
def cyprus():

    source_url = 'https://www.moh.gov.cy/moh/moh.nsf/All/0EFA027144C9E54AC22586BE0032B2F5'

    #scrape the html into python
    page = requests.get(source_url)
    soup = BeautifulSoup(page.text, "html.parser")

    #find all the paragraph (<p>) tags in the html and put them in a list
    p_tags = soup.findAll('p')

    #extact the date text from the list and convert to datetime object
    str_date = p_tags[2].text[-10:]
    date = datetime.strptime(str_date, '%d/%m/%Y').date()

    # extract text from the list items (i.e. vaccination figures); remove commas, change dtype to integer, and assign to relevant variable names
    vaccinations = int(p_tags[1].text.replace(',', ''))
    people_vaccinated = int(p_tags[4].text.replace(',', ''))
    people_fully_vaccinated = int(p_tags[7].text.replace(',', ''))

    #create a dictionary object of all the required variables to pass into R
    cyprus_vax_dict = {'code': 'CYP',
    'date': date,
    'vaccinations' : vaccinations,
    'people_vaccinated': people_vaccinated,
    'people_fully_vaccinated': people_fully_vaccinated}

    return cyprus_vax_dict
