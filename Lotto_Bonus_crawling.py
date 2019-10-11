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
        get_number_info = soup.find(name="div",attrs={"class":"num bonus"})
        
        try:
            get_number = get_number_info.select('span')[0]
            get_number = get_number.text
            temp.append(get_number.strip())
            
 
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
    data = pd.concat([data1])
    data = pd.DataFrame(data)
    data.to_csv('Lotto1.csv', mode='a', encoding='utf-8',header=None)  
print("저장성공")
