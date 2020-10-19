import time

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#open browser
from selenium.webdriver.support.wait import WebDriverWait

opts = Options()
opts.set_headless()
assert opts.headless  # Operating in headless mode
browser = webdriver.Firefox(options=opts)
browser.get('https://duckduckgo.com')

#back to prev page
browser.back()
#go to next page
browser.forward()

#find input by id
search_form = browser.find_element_by_id('search_form_input_homepage')
search_form.send_keys('real python')
search_form.submit()

#multipl classes
results = browser.find_elements_by_class_name('result')
print(results[0].text)

#click button
browser.find_element_by_class_name('playbutton').click()

element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.link_text, "Courses"))
    )
# click the element
element.click()


#close browser
browser.close()


def tracks():
    '''
    Query the page to populate a list of available tracks.
    '''

    # Sleep to give the browser time to render and finish any animations
    time.sleep(1)

    # Get the container for the visible track list
    discover_section = browser.find_element_by_class_name('discover-results')
    left_x = discover_section.location['x']
    right_x = left_x + discover_section.size['width']

#more_track
def more_tracks( page='next'):
    '''
    Advances the catalogue and repopulates the track list. We can pass in a number
    to advance any of the available pages.
    '''

    next_btn = [e for e in browser.find_elements_by_class_name('item-page')
                if e.text.lower().strip() == str(page)]

    if next_btn:
        next_btn[0].click()
        tracks()



if __name__ == '__main__':

    pass
