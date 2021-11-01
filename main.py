url_form_google_spreadsheet = "https://docs.google.com/forms/d/e/1FAIpQLSfLZkZzjgSQJSlTluOR2B28kRC6Omdu4JgtuvT99FHPiCAlWQ/viewform"
for n in range(2001, 2021):
    link_1 = f"https://www.skysports.com/manchester-united-results/{n}-{n+1}"
    from bs4 import BeautifulSoup
    import requests
    import lxml

    #requesting the data
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
    accept_lang = "ru-UA,ru-RU;q=0.9,ru;q=0.8,en-GB;q=0.7,en;q=0.6,en-US;q=0.5,uk;q=0.4"
    headers = {
        "User-Agent": user_agent,
        "Accept-Language": accept_lang
    }
    response = requests.get(link_1, headers=headers)
    response.raise_for_status()
    web_response = response.text
    soup = BeautifulSoup(web_response, "lxml")
    #finding the dates:
    date_played = []
    dates = soup.findAll(class_='fixres__header2')
    for date in dates:
        date_played.append(date.text)
    print(date_played)
    print(len(date_played))

    #finding the championship:
    championship_type = []
    championships = soup.findAll(class_='fixres__header3')
    for championship in championships:
        championship_type.append(championship.text)

    print(championship_type)
    print(len(championship_type))
    #finding the score
    score_list = []
    scores = soup.findAll(class_='matches__teamscores')
    for score in scores:
        score_text = score.text
        score_list.append(score_text)

    print(score_list)
    print(len(score_list))
    #finding the teams that played
    team_list = []
    teams = soup.findAll(class_='swap-text__target')
    for team in teams:
        team_text = team.text
        team_list.append(team_text)
    team_list = team_list[1:]
    team_home = team_list[::2]

    team_away = team_list[1::2]

    print(team_home)
    print(len(team_home))
    print(team_away)
    print(len(team_away))
    #hour played
    hour_list = []
    hours = soup.findAll(class_='matches__date')
    for hour in hours:
        hour_text = hour.text
        hour_list.append(hour_text)

    print(hour_list)
    print(len(hour_list))


    from selenium import webdriver
    from time import sleep
    from selenium.webdriver.common.keys import Keys


    chrome_web_driver = "C:/development/chromedriver_win32/chromedriver.exe"
    driver = webdriver.Chrome(executable_path=chrome_web_driver)
    driver.get(url_form_google_spreadsheet)
    sleep(10)



    for n in range(1, len(date_played)):
        date_answer = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        date_answer.send_keys(date_played[n-1])
        sleep(3)
        competition_answer = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        competition_answer.send_keys(championship_type[n-1])
        sleep(3)
        team_home_answer = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        team_home_answer.send_keys(team_home[n-1])
        sleep(3)
        team_away_answer = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
        team_away_answer.send_keys(team_away[n-1])
        sleep(3)
        score_answer = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')
        score_answer.send_keys(score_list[n-1])
        sleep(3)
        time_played = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input')
        time_played.send_keys(hour_list[n-1])
        sleep(3)
        submit = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
        submit.click()
        sleep(5)
        submit_2 = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
        submit_2.click()
        sleep(10)

