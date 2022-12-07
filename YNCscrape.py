from bs4 import BeautifulSoup
from selenium import webdriver
driver = webdriver.Chrome()
import csv
username_list = []
title_list = []
stat_list = []
up_vote_list = []
csv_final_list = []
header = ['title','user name','date','comments','views','up votes']
i = 0
j = 0
driver.get("https://theync.com/most-recent/")
searchsoup = BeautifulSoup()
content = driver.page_source.encode('utf-8').strip()
soup = BeautifulSoup(content,'html.parser')
titles = soup.find_all('span',class_='title')
stats_of_video = soup.find_all('span',class_='count')
up_votes = soup.find_all('span',class_='label total-value')
user_names = soup.find_all('span',class_='user')
user_name_minus_last_null = user_names[:75]
titles_minus_last_null = titles[:75]
stats_of_video_minus_last_null = stats_of_video[:225]
up_votes_minus_last_null = up_votes[:75]
for name in user_name_minus_last_null:
    actual_usernames = str(name.find('a'))
    mini_soup = BeautifulSoup(actual_usernames,'html.parser')
    a_tag = mini_soup.a.extract()
    username_final_string = a_tag.string.extract()
    username_list.append(username_final_string)
for title in titles_minus_last_null:
    mini_soup = BeautifulSoup(str(title),'html.parser')
    span_tag = mini_soup.span.extract()
    title_final_string = span_tag.string.extract()
    title_list.append(title_final_string)
for stat in stats_of_video_minus_last_null:
    mini_soup = BeautifulSoup(str(stat),'html.parser')
    span_tag = mini_soup.span.extract()
    stat_final_string = span_tag.string.extract()
    stat_list.append(stat_final_string)
for upvote in up_votes_minus_last_null:
    mini_soup = BeautifulSoup(str(upvote),'html.parser')
    span_tag = mini_soup.span.extract()
    up_vote_final_string = span_tag.string.extract()
    up_vote_list.append(up_vote_final_string)
page_number = 2
while page_number < 101:
        driver.get(f"https://theync.com/most-recent/page{page_number}.html")
        print(page_number,'=======page number')
        content = driver.page_source.encode('utf-8').strip()
        soup = BeautifulSoup(content,'html.parser')
        titles = soup.find_all('span',class_='title')
        stats_of_video = soup.find_all('span',class_='count')
        up_votes = soup.find_all('span',class_='label total-value')
        user_names = soup.find_all('span',class_='user')
        user_name_minus_last_null = user_names[:75]
        titles_minus_last_null = titles[:75]
        stats_of_video_minus_last_null = stats_of_video[:225]
        up_votes_minus_last_null = up_votes[:75]
        for name in user_name_minus_last_null:
            actual_usernames = str(name.find('a'))
            mini_soup = BeautifulSoup(actual_usernames,'html.parser')
            try:
                a_tag = mini_soup.a.extract()
                username_final_string = a_tag.string.extract()
                username_list.append(username_final_string)
            except:username_list.append('null')
        for title in titles_minus_last_null:
            mini_soup = BeautifulSoup(str(title),'html.parser')
            try:
                span_tag = mini_soup.span.extract()
                title_final_string = span_tag.string.extract()
                title_list.append(title_final_string)
            except:title_list.append('null')
        for stat in stats_of_video_minus_last_null:
            mini_soup = BeautifulSoup(str(stat),'html.parser')
            try:
                span_tag = mini_soup.span.extract()
                stat_final_string = span_tag.string.extract()
                stat_list.append(stat_final_string)
            except:
                stat_list.append('null')
        for upvote in up_votes_minus_last_null:
            mini_soup = BeautifulSoup(str(upvote),'html.parser')
            try:
                span_tag = mini_soup.span.extract()
                up_vote_final_string = span_tag.string.extract()
                up_vote_list.append(up_vote_final_string)
            except:
                up_vote_list.append('null')
        page_number+=1
with open('onehundredpages2.csv', 'w', encoding='UTF8',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    while i < 7500:
        csv_final_list.append(title_list[i])
        csv_final_list.append(username_list[i])
        csv_final_list.append(stat_list[j])
        csv_final_list.append(stat_list[j + 1])
        csv_final_list.append(stat_list[j + 2])
        csv_final_list.append(up_vote_list[i])
        writer.writerow(list(csv_final_list))
        j+=3
        i+=1
        csv_final_list = [] 