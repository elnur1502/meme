import urllib2
 
def main():
   webUrl = urllib2.urlopen("https://9gag.com/meme")
  
#получаем код результата и выводим его
   print "result code: " + str(webUrl.getcode()) 
  
# читаем данные с URL-адреса и выводим их   data
 = webUrl.read()
   print data
 
if __name__ == "__main__":
  main()
