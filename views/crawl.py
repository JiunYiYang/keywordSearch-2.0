# -*- coding: utf-8 -*-
from selenium import webdriver
from pyvirtualdisplay import Display
# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import sys, json

# CHROME_PATH = '/usr/bin/google-chrome'
# CHROMEDRIVER_PATH = '/usr/local/bin/chromedriver'
# WINDOW_SIZE = "1920,1080"
# KEYWORDS = 'justin'
KEYWORDS = sys.stdin.read().splitlines()
ELE = []

display = Display(visible=0, size=(1366, 768))
display.start()

# chrome_options = Options()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
# chrome_options.binary_location = CHROME_PATH

# browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,
#                            chrome_options=chrome_options,
#                            service_args=['--ssl-protocol=any']
#                           )
browser = webdriver.Chrome()
# browser.implicitly_wait(10)
# browser.set_window_position(-50000, 0)
# browser.get('https://ubersuggest.io/')
browser.get('https://moz.com/explorer/keyword/suggestions?locale=en-US&q='+KEYWORDS[0])
browser.set_script_timeout(30)
browser.set_page_load_timeout(30)
# browser.find_element_by_id('keywordBox').clear()
# browser.find_element_by_css_selector('div.omnisearch-input input').clear()
# browser.find_element_by_id('keywordBox').send_keys(KEYWORDS[0])
# browser.find_element_by_css_selector('div.omnisearch-input input').send_keys(KEYWORDS[0])
# browser.find_element_by_id('suggest-button').click()
# browser.find_element_by_css_selector('form.omnisearch-form button').click()
# browser.find_elements_by_tag_name('td span')
browser.find_elements_by_css_selector('td.keyword')
soup = BeautifulSoup(browser.page_source, 'html.parser')
# for ele in soup.select('.dropdown-toggle span'):
for ele in soup.select('.keyword'):
    ELE.append(ele.text)
print(json.dumps(ELE, ensure_acsii=False))

# browser.get_screenshot_as_file("capture.png")
browser.close()
display.stop()


# import sys, json

# #Read data from stdin
# def read_in():
#     lines = sys.stdin.readlines()
#     # Since our input would only be having one line, parse our JSON data from that
#     return json.loads(lines[0])

# def main():
#     #get our data as an array from read_in()
#     lines = read_in()

#     # Sum  of all the items in the providen array
#     total_sum_inArray = 0
#     for item in lines:
#         total_sum_inArray += item

#     #return the sum to the output stream
#     print(total_sum_inArray)

# # Start process
# if __name__ == '__main__':
#     main()
    
