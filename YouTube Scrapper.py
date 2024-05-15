from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd # type: ignore

# get webdriver
driver=webdriver.Edge();
driver.set_page_load_timeout(500);

# get the desired website
driver.get('https://www.youtube.com/');
driver.maximize_window();
sleep(5);

# get the search bar from the website
search_bar=driver.find_element(By.NAME,"search_query");
search_bar.clear();

# search the desired content using title or keywords
search_bar.send_keys("Why does a Muslim’s Passion for Worship Go down after Ramadhaan? - Dr Zakir Naik");
search_bar.send_keys(Keys.ENTER);
sleep(5);

# get the desired element you want to access
video=driver.find_element(By.XPATH,"""//*[@id="video-title"]/yt-formatted-string""");
video.click();
sleep(10);

# scroll the window to load enough comments
for i in range(10):
    driver.execute_script("window.scrollBy(0,700)","");
    sleep(2);
sleep(10);

comments=[];

# get the comments section
comment_section=driver.find_elements(By.XPATH,"""//*[@id="content-text"]/span""");

# convert the comments in text and store in comments array
for comment in comment_section:
    comments.append(comment.text);

# store the comments in a dataframe
df=pd.DataFrame({"comments":comments});
df.to_csv('comments.csv',index=False);
print(df);
assert "No Results Found." not in driver.page_source;
driver.close();