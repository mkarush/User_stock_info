# User_stock_info
Basic Application Information 
This App will help user to get real-time alue of stocks (which ever they want) and store in data.( using https://www.alphavantage.co/) 

Create_API_Key : This will create password like key to get values [each user have own key] 

Add-Stock : This will add stock in list

Symbol-Search : This will give top 10 matching stock name and symbol

Price : This will give latest prices of all the stock

Delete-Stock : This will delete stock from the list

<img src= "Flask_AlphaVantage_API/images/Screen%20Shot%202020-02-16%20at%209.48.04%20AM.png" width="700px">

Limitations:
1. Alphavantage only allow to make 5 api calls per minute 

Solutions:
In order to avoid Alphavantage-API issue i am using yfinance

Advantages: No need to create API Key

<img src= "yfinance_api/images/Screen%20Shot%202020-02-16%20at%205.17.51%20PM.png" width="700px">

Limitations: 
It little slow and it speed to get value depends upon user internet speed. 
