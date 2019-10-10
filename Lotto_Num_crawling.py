#네이버 뮤직에서 데이터를 수집합니다.
#수집할 데이터가 들어있는 주소를 수집
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
from pandas import DataFrame


num = 870

while (1):
    temp = []
    
    myurl = "https://www.nlotto.co.kr/gameResult.do?method=byWin&drwNo="+str(num)
    print(myurl)
    url = urlopen(myurl)

    soup = BeautifulSoup(url,"lxml")

    try:
        get_number_info = soup.find(name="div",attrs={"class":"nums"})
        
        try:
            get_number1 = get_number_info.select('span')[0]
            get_number1 = get_number1.text
            temp.append(get_number1.strip())
            
 
        except:
            print("번호없음")
        try:
            get_number2 = get_number_info.select('span')[1]
            get_number2 = get_number2.text
            temp.append(get_number2.strip())
            
 
        except:
            print("번호없음")
        try:
            get_number3 = get_number_info.select('span')[2]
            get_number3 = get_number3.text
            temp.append(get_number3.strip())
            
 
        except:
            print("번호없음")
        try:
            get_number4 = get_number_info.select('span')[3]
            get_number4 = get_number4.text
            temp.append(get_number4.strip())
            
 
        except:
            print("번호없음")
        try:
            get_number5 = get_number_info.select('span')[4]
            get_number5 = get_number5.text
            temp.append(get_number5.strip())
            
 
        except:
            print("번호없음")
        try:
            get_number6 = get_number_info.select('span')[5]
            get_number6 = get_number6.text
            temp.append(get_number6.strip())
            
 
        except:
            print("번호없음") 
            
    except:
        print("번호없음")
        pass
    
    print(temp)
    num = num +1
    if num == 880:
        break
    
    
    data1 = DataFrame(temp)
    data = pd.concat([data1], axis = 1)
    data = pd.DataFrame(data)
    data.to_csv('Lotto.csv', mode='a', encoding='utf-8',header=None)  
print("저장성공")
