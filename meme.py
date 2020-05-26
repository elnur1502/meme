import urllib.request
# открываем соединение к URL-адресу с помощью urllib2
webUrl  = urllib.request.urlopen('https://9gag.com/meme')
 
# получаем код результата и выводим его
print ("result code: " + str(webUrl.getcode()))
 
# читаем данные с URL-адреса и выводим их data = webUrl.read()
print (data)
