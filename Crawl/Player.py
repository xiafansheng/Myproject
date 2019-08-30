
from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
import requests
import re
import time

#generate the player summary page to playerSummary.csv
def generatePlayerList():
    #create csv file named "playerSummary" using append mode
    player = open('playerSummary.csv','a')
    #read player summary page from A to Z
    for i in range(ord('a'),ord('z')+1):
        time.sleep(1)
        # no palyer's last name start with X
        if chr(i)=='x':
            continue
        else:
            url_player=('https://www.basketball-reference.com/players/'+chr(i)+'/')
            webpage_PlayerList = str(urlopen(url_player,).read())
            #remove <strong>
            webpage_PlayerList = re.sub(r'<strong>',"", webpage_PlayerList)
            webpage_PlayerList = re.sub(r'</strong>',"", webpage_PlayerList)

            soup = BeautifulSoup(webpage_PlayerList,"html.parser")
            table = soup.find("table",attrs={"id":"players"}).findAll("tr")
            header = soup.find("table",{"id":"players"}).find("thead")
            if chr(i)=="a":
                for j in header.find_all("th"):
                    player.write(j.get_text()+",")
                player.write("URL"+",")
                player.write("\n")

            for i in table:
                d=i.find("th")
                if d.get_text()=="Player":
                    continue
                else:
                    #year_max means the last season is season year_max-1 to year_max
                    for n in i.find_all('td',attrs={'data-stat':"year_max"}):
                        if float(n.get_text())<2008:
                            continue
                        else:
                            #year_min means the first season is season year_min-1 to year_mim
                            for m in i.find_all('td',attrs={'data-stat':"year_min"}):
                                if float(m.get_text())>2017:
                                    continue
                                else:                        
                                    player.write(d.get_text()+",")
                                    for j in i.find_all("td"):
                                        k=j.get_text().replace(","," ").replace("-",".")
                                        player.write(k+",")
                                    for m in d.find_all('a'):
                                        player.write(m.get('href')+',')
                                    player.write("\n")
    player.close()
    print('playerSummary.csv created')

#generate url for all palyers using regular expression
def getPlayerUrlListRE():
    for i in range(ord('a'),ord('z')+1):
            time.sleep(1)
            # no palyer's last name start  with X
            if chr(i)=='x':
                continue
            else:
                webpage_PlayerList = str(urlopen('https://www.basketball-reference.com/players/'+chr(i)+'/').read())
                tables = re.findall(r'<table class="sortable stats_table"[\s\S]*<\/table>', webpage_PlayerList, re.S)

                subUrl = re.findall(r'<a href=\"\/players\/([^"]*)\"',tables[0])
                playerUrlList=[]
                for i in range(len(subUrl)):
                    playerUrlList.append("/players/"+subUrl[i])
                    time.sleep(1)
    return playerUrlList



#generate url for all palyers using BeautifulSoup, in this function, only active players between season 0708 to season 1617 are included for convenience 
def getPlayerUrlListBS():
    playerUrlList=[]
    for i in range(ord('a'),ord('z')+1):
        time.sleep(1)
        if chr(i)=='x':
            continue
        else:
            url_player=('https://www.basketball-reference.com/players/'+chr(i)+'/')
            webpage_PlayerList = str(urlopen(url_player,).read())
            #remove <strong>
            webpage_PlayerList = re.sub(r'<strong>',"", webpage_PlayerList)
            webpage_PlayerList = re.sub(r'</strong>',"", webpage_PlayerList)

            soup = BeautifulSoup(webpage_PlayerList,"html.parser")
            table = soup.find("table",attrs={"id":"players"}).findAll("tr")
            header = soup.find("table",{"id":"players"}).find("thead")
            for i in table:
                d=i.find("th")
                if d.get_text()=="Player":
                    continue
                else:
                    #year_max means the last season is season year_max-1 to year_max
                    for n in i.find_all('td',attrs={'data-stat':"year_max"}):
                        if float(n.get_text())<2008:
                            continue
                        else:
                            #year_min means the first season is season year_min-1 to year_mim
                            for m in i.find_all('td',attrs={'data-stat':"year_min"}):
                                if float(m.get_text())>2017:
                                    continue
                                else:                        
                                    for m in d.find_all('a'):
                                        playerUrlList.append(m.get('href'))  
    return playerUrlList 


#get player basic info using BecautifulSoup
def getPlayerBasicInfoBS():
    for url in getPlayerUrlListBS():
        time.sleep(1)
        url_player_details=('https://www.basketball-reference.com'+url)
        
        webpage_PlayerList = str(urlopen(url_player_details,).read())
        webpage_PlayerList = re.sub(r'<strong>',"", webpage_PlayerList)
        webpage_PlayerList = re.sub(r'</strong>',"", webpage_PlayerList)
        

        soup = BeautifulSoup(webpage_PlayerList,"html.parser")
        playerBasicInfo = open('playerBasicInfo.csv','a')
        #if condition in case of no such a table for certain palyer
        if  soup.find("div",attrs={"itemtype":"https://schema.org/Person"}) is not None:
            table = soup.find("div",attrs={"itemtype":"https://schema.org/Person"}).findAll("p")
            for i in table:
                n=i.get_text().replace("-",".").replace(u'\u25aa','').replace('\n',' ').replace(',','.').replace(u'\xa0','').encode('utf-8')
                #playerBasicInfo.write(n+",")
                playerBasicInfo.write("\n")
            
        playerBasicInfo.close()
    print('Table details generated.')


#get player basic info using regular expression
def getPlayerBasicInfoRE():
    for url in getPlayerUrlListBS():
        time.sleep(1)

        url_player_details=('https://www.basketball-reference.com'+url)
        
        webpage_PlayerList = str(urlopen(url_player_details,).read())
        webpage_PlayerList = re.sub(r'<strong>',"", webpage_PlayerList.decode('utf-8'))
        webpage_PlayerList = re.sub(r'</strong>',"", webpage_PlayerList)
        #get the player info section
        table=re.compile(r'<div itemscope itemtype="https://schema.org/Person" >(.*?)</div>',re.DOTALL).search(webpage_PlayerList)
        #find the title, in this case it is player's name
        playername = re.findall(r'<h1 itemprop="name">([^"]*)<\/h1>',table.group(1))
        #findall row in this section
        tableP=re.findall(r'<p>(.*?)</p>',table.group(1),re.MULTILINE|re.DOTALL)

        playerBasicInfo = open('playerBasicInfo.csv','a')
        #add title(player's name into csv)
        playerBasicInfo.write(playername[0])
        #add each row into csv  
        for i in tableP:
            i=re.sub(r'<(.*?)>','',i)
            n=i.replace('\n','').replace('&#9642;','').replace(',','.').replace('-','')
            #playerBasicInfo.write(n+",")
            playerBasicInfo.write("\n")
        playerBasicInfo.write("\n")
        playerBasicInfo.close()
        playername = re.findall(r'<h1 itemprop="name">([^"]*)<\/h1>',table.group(1))
    print('Table details generated.')

#get player table details
def getTable(tablename):
    count =1
    for url in getPlayerUrlListBS():
        time.sleep(1)
        url_player_details=('https://www.basketball-reference.com'+url)
        
        webpage_PlayerList=requests.get(url_player_details)
        webpage_PlayerList = re.sub(r'(?m)^\<!--.*\n?', '', webpage_PlayerList.content)
        webpage_PlayerList = re.sub(r'(?m)^\-->.*\n?', '', webpage_PlayerList)
        
        #webpage_PlayerList = urlopen(url_player_details).read()
        #webpage_PlayerList = re.sub(r'(?m)^\<!--.*\n?', '', webpage_PlayerList)
        #webpage_PlayerList = re.sub(r'(?m)^\-->.*\n?', '', webpage_PlayerList)

        soup = BeautifulSoup(webpage_PlayerList,"html.parser")
        #if condition in case of no such a table for certain palyer
        if  soup.find("table",attrs={"id":tablename}) is not None:
            table = soup.find("table",attrs={"id":tablename}).findAll("tr",{"class":["full_table","light_text partial_table"]})
            header = soup.find("table",{"id":tablename}).find("thead")

            #output to csv file
            tableDetails = open(tablename+'.csv','a')

            # only one header is required
            if count <2:
                for j in header.find_all("th"):
                    tableDetails.write(j.get_text()+",")
                tableDetails.write("URL"+",")
                tableDetails.write("\n")

            for i in table:  
                d=i.find("th")
                tableDetails.write(d.get_text()+",")
                for j in i.find_all("td"):
                        tableDetails.write(j.get_text()+",")
                tableDetails.write(url)
                tableDetails.write("\n")
            count+=1
        else:
            count+=1
            
    tableDetails.close()
    print('Table details generated.')




#get player salaries details
def getSalaries(tablename):
    count =1
    for url in getPlayerUrlListBS():
        time.sleep(1)
        url_player_details=('https://www.basketball-reference.com'+url)
        webpage_PlayerList=requests.get(url_player_details)
        webpage_PlayerList = re.sub(r'(?m)^\<!--.*\n?', '', webpage_PlayerList.content)
        webpage_PlayerList = re.sub(r'(?m)^\-->.*\n?', '', webpage_PlayerList)
        
        
        #webpage_PlayerList = urlopen(url_player_details).read()
        #webpage_PlayerList = re.sub(r'(?m)^\<!--.*\n?', '', webpage_PlayerList)
        #webpage_PlayerList = re.sub(r'(?m)^\-->.*\n?', '', webpage_PlayerList)

        soup = BeautifulSoup(webpage_PlayerList,"html.parser")
         #if condition in case of no such a table for certain palyer
        if soup.find("table",attrs={"id":tablename}) is None:
            count+=1
        else:
            table = soup.find("table",attrs={"id":tablename}).findAll("tr")
            header = soup.find("table",{"id":tablename}).find("thead")

                #output to csv file
            tableDetails = open(tablename+'.csv','a')
                #print table

                # only one header is required
            if count <2:
                for j in header.find_all("th"):
                    tableDetails.write(j.get_text()+",")
                tableDetails.write("URL"+",")
                tableDetails.write("\n")

            for i in table:  
                d=i.find("th")
                if d.get_text()=="Career" or d.get_text()=="Season": 
                    continue
                else:
                    tableDetails.write(d.get_text()+",")
                    for j in i.find_all("td"):           
                        tableDetails.write(j.get_text().replace(",","").replace("-",".")+",")
                    tableDetails.write(url)
                    tableDetails.write("\n")
            count+=1
    tableDetails.close()
    print('Table details generated.')

generatePlayerList()
#please only execute one of the following 2 functions to get the player profile information
getPlayerBasicInfoBS()
getPlayerBasicInfoRE()
# getTable('per_game')
# getTable('advanced')
# getTable('playoffs_per_game')
# getTable('playoffs_advanced')
# getSalaries('all_salaries')

