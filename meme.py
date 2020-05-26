Python
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

opts = Options()
opts.set_headless()
assert opts.headless  # без графического интерфейса.

browser = Firefox(options=opts)
browser.get('https://duckduckgo.com')
1
2
3
4
5
6
7
8
9
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
 
opts = Options()
opts.set_headless()
assert opts.headless  # без графического интерфейса.
 
browser = Firefox(options=opts)
browser.get('https://duckduckgo.com')
