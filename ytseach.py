from selenium import webdriver
import time
links=[]

# input data from user
query=input("Input your query : ")
number=1
number=int(input("Enter which query to be opened : "))

# opens firefox
driver=webdriver.Firefox(executable_path="D:\\Driver\\geckodriver.exe")
url=f"https://www.youtube.com/results?search_query={query}"
driver.get(url)

try:
    # opena the nth video requested by the user
    xxpath=(driver.find_elements_by_xpath('//*[@id="video-title"]'))
    time.sleep(3)
    xxpath[number-1].click()
    
except Exception as e:
    print("error : ")
    print(e)

