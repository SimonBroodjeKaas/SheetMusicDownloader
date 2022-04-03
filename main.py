from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

images = []

def get_element_by_xpath(xpath):
  element = None
  while not element:
    try:
      element = driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
      pass
  
  return element

def get_images():
  global images
  container = driver.find_element_by_id('jmuse-scroller-component')
  divs = container.find_elements_by_xpath(".//*")
  for div in divs:
    childs = div.find_elements_by_xpath(".//img")
    if len(childs) > 0:
      src = childs[0].get_attribute("src")
      if not src in images:
        images.append(src)
  print(images)

driver.get('https://musescore.com/user/96606/scores/152043')

get_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/button[2]').click()

# target = driver.find_element_by_id('jmuse-scroller-component')

while True:
  driver.execute_script("document.getElementById('jmuse-scroller-component').scrollBy(100, 100)")
  get_images()
  # target.send_keys(Keys.PAGE_DOWN)
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()