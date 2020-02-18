# Importing the necessary modules
from bs4 import BeautifulSoup
import urllib, os, urllib.request
from selenium import webdriver
from bs4 import BeautifulSoup
import csv
import time


# creating CSV file to be used - each title is separated by a comma

# Looping based on year (vYear), month (vMonth) and date vDate)
# - if you want 2014 to 2015, your year range should be range(2014,2016)
# - if you want January to March, your month range should be range(1,4) - if you want everything than do range(1,13)
# - if you want 1 to 12, your day range shoudl be range(1,13) - if you want everything than do range (1,32)

for year in range(2014, 2020):
    for month in range(1, 13):
        url = 'https://www.wunderground.com/history/monthly/kr/gangseo-gu/RKSS/date/{}-{}'.format(year, month)

        driver = webdriver.Chrome()
        driver.get(url)
        time.sleep(10)
        html = driver.execute_script("return document.documentElement.outerHTML")
        driver.close()
        soup = BeautifulSoup(html, 'html.parser')

        total_data = []
        for column in soup.find_all('table', {'class':'days ng-star-inserted'})[0].find_all('tr')[1].find_all('table'):
            column_data = []
            for row in column.find_all('tr'):
                if column.find_all('tr')[0].text.strip() in ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']:
                    column_data.append(row.text.strip())
                elif column.find_all('tr')[0].text.strip() == "Total":
                    column_data.append(row.text.strip())
                else:
                    column_data.append(row.find_all('td')[1].text.strip())
            total_data.append(column_data)

        rows = zip(total_data[0], total_data[1], total_data[2], total_data[3], total_data[4], total_data[5], total_data[6])

        with open('Data/Html-Data/weather_data_{}_{}.csv'.format(year, month), 'w') as csv_file:
            thewriter = csv.writer(csv_file)
            thewriter.writerow(["Time", "Average_Temperature_(F)", "Dew_Point_(F)", "Humidity_(%)", "Wind_Speed_(mph)",
                                "Pressure_(Hg)", "Precipitation_(in)"])
            for row in rows:
                thewriter.writerow(row)

            # for temp in soup.find_all('tr'):
            #     if temp.text.
            #
            #
            #     if temp.text.strip().replace('\n', '')[:6] == 'Actual' or temp.text.strip().replace('\n', '')[-6:] == "Record":
            #         pass
            #     elif temp.text.replace('\n', '')[-7:] == "RiseSet":
            #         break
            #     elif temp.find_all('td')[0].text == "Mean Temperature":
            #         if temp.find_all('td')[1].text.strip() == "-":
            #             Mean = "N/A"
            #         else:
            #             Mean = temp.find_all('td')[1].find(attrs={"class": "wx-value"}).text
            #     elif temp.find_all('td')[0].text == "Max Temperature":
            #         if temp.find_all('td')[1].text.strip() == "-":
            #             Max = "N/A"
            #         else:
            #             Max = temp.find_all('td')[1].find(attrs={"class": "wx-value"}).text
            #     elif temp.find_all('td')[0].text == "Min Temperature":
            #         if temp.find_all('td')[1].text.strip() == "-":
            #             Min = "N/A"
            #         else:
            #             Min = temp.find_all('td')[1].find(attrs={"class": "wx-value"}).text
            #     elif temp.find_all('td')[0].text == "Growing Degree Days":
            #         if temp.find_all('td')[1].text.strip() == "-":
            #             GrowingDegreeDays = "N/A"
            #         else:
            #             GrowingDegreeDays = temp.find_all('td')[1].text
            #     elif temp.find_all('td')[0].text == "Heating Degree Days":
            #         if temp.find_all('td')[1].text.strip() == "-":
            #             HeatingDegreeDays = "N/A"
            #         else:
            #             HeatingDegreeDays = temp.find_all('td')[1].text
            #     elif temp.find_all('td')[0].text == "Dew Point":
            #         if temp.find_all('td')[1].text.strip() == "-" or temp.find_all('td')[1].text.strip() == "":
            #             DewPoint = "N/A"
            #         else:
            #             DewPoint = temp.find_all('td')[1].find(attrs={"class": "wx-value"}).text
            #     elif temp.find_all('td')[0].text == "Average Humidity":
            #         if temp.find_all('td')[1].text.strip() == "-" or temp.find_all('td')[1].text.strip() == "":
            #             AvgHumidity = "N/A"
            #         else:
            #             AvgHumidity = temp.find_all('td')[1].text
            #     elif temp.find_all('td')[0].text == "Maximum Humidity":
            #         if temp.find_all('td')[1].text.strip() == "-" or temp.find_all('td')[1].text.strip() == "":
            #             MaxHumidity = "N/A"
            #         else:
            #             MaxHumidity = temp.find_all('td')[1].text
            #     elif temp.find_all('td')[0].text == "Minimum Humidity":
            #         if temp.find_all('td')[1].text.strip() == "-" or temp.find_all('td')[1].text.strip() == "":
            #             MinHumidity = "N/A"
            #         else:
            #             MinHumidity = temp.find_all('td')[1].text
            #     elif temp.find_all('td')[0].text == "Precipitation" and temp.find_all('td')[1].text.strip() != "":
            #         if temp.find_all('td')[1].text.strip() == "-" or temp.find_all('td')[1].text.strip() == "":
            #             Precipitation = "N/A"
            #         else:
            #             Precipitation = temp.find_all('td')[1].find(attrs={"class": "wx-value"}).text
            #     elif temp.find_all('td')[0].text == "Sea Level Pressure" and temp.find_all('td')[1].text.strip() != "":
            #         if temp.find_all('td')[1].text.strip() == "-":
            #             SeaLevelPressure = "N/A"
            #         else:
            #             SeaLevelPressure = temp.find_all('td')[1].find(attrs={"class": "wx-value"}).text
            #     elif temp.find_all('td')[0].text == "Wind Speed":
            #         if temp.find_all('td')[1].text.strip() == "-" or temp.find_all('td')[1].text.strip().replace('\n','') == "- ()" or temp.find_all('td')[1].text.strip() == "":
            #             AvgWindSpeed = "N/A"
            #         else:
            #             AvgWindSpeed = temp.find_all('td')[1].find(attrs={"class": "wx-value"}).text
            #     elif temp.find_all('td')[0].text == "Max Wind Speed":
            #         if temp.find_all('td')[1].text.strip() == "-" or temp.find_all('td')[1].text.strip() == "":
            #             MaxWindSpeed = "N/A"
            #         else:
            #             MaxWindSpeed = temp.find_all('td')[1].find(attrs={"class": "wx-value"}).text
            #     elif temp.find_all('td')[0].text == "Visibility":
            #         if temp.find_all('td')[1].text.strip() == "-":
            #             Visibility = "N/A"
            #         else:
            #             Visibility = temp.find_all('td')[1].find(attrs={"class": "wx-value"}).text
            #     elif temp.find_all('td')[0].text == "Events":
            #         if temp.find_all('td')[1].text.strip() == "-":
            #             Events = "N/A"
            #         else:
            #             Events = temp.find_all('td')[1].text.strip().replace(",", " ").replace('\n', '').replace('\t','')
            #             break
            #
            # # combining the values to be written to the CSV file
            # CombinedString = theDate + "," + Mean + "," + Max + "," + Min + "," + HeatingDegreeDays + "," + DewPoint + "," + AvgHumidity + "," + MaxHumidity + "," + MinHumidity + "," + Precipitation + "," + SeaLevelPressure + "," + AvgWindSpeed + "," + MaxWindSpeed + "," + Visibility + "," + Events + "\n"
            # file.write(bytes(CombinedString, encoding="ascii", errors='ignore'))
            #
            # # printing to help with any debugging and tracking progress
            # print(CombinedString)

file.close()
