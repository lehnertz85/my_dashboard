from bs4 import BeautifulSoup
import json
import re

def analyze_errors(driveForm, serviceForm):

    html = ''

    for error in serviceForm.non_form_errors():
        #print('SERVICE FORM: NON ' + error.__unicode__)
        html += str(error.__unicode__)

    for error in serviceForm.errors:
        #print('SERVICE FORM ' + str(error))
        html += str(error)

    for error in driveForm.non_form_errors():
        #print('DRIVE FORM: NON ' + error.__unicode__)
        html += str(error.__unicode__)

    for error in driveForm.errors:
        #print('DRIVE FORM ' + str(error))
        html += str(error)

    html = re.sub("__all__", "", html)
    #html = re.sub("ul", 'ol', html)

    html = '<div class="browser-default">' + html + '</div>'

    soup = BeautifulSoup(html, "html.parser")
    #print('HTML SOUP: ' + str(soup))

    soup = parse_soup(soup)

   # print('JSON SOUP: ' + str(soup))

    return soup


# Parse the HTML in the soup to make the error's look better

def parse_soup(soup):
    json_errors = {}
    i = 0

    for li_tag in soup.ul:
        json_errors.update({ 'Error %s' % i: u' -> '.join(li_tag.findAll(text=True)) })
        #print('UL contains: ' + u': '.join(li_tag.findAll(text=True)))
        i += 1

    #print(json_errors.items())
    json_errors = json.dumps(json_errors)

    return json_errors
