from pydrive.auth import GoogleAuth  #import pydrive module to upload files in google drive
from pydrive.drive import GoogleDrive

import requests  
import json
import csv    #this module used to write output in csv file 

def upload_to_google_drive():   #upload file to google drive
    gauth = GoogleAuth()        # calling the constructor      
    gauth.LocalWebserverAuth()   # calling the method
    drive = GoogleDrive(gauth)
    file = drive.CreateFile({"mimeType": "text/csv"})
    file.SetContentFile("output_file.csv")
    file.Upload()


html = requests.get('https://api.github.com/users') #request module used to get the data from url.

json_data = json.loads(html.text) #load the data in json format



csv_data_upload = []     # create empty list/array to append data
for user in json_data:   # for loop to iterate the data one by one.
    if user["id"]%5==0:  #condition for user id divisible by 5 
        #if condition is true process the following code.
        UserLogin=user['login']
        UserName=user['login']
        FollowUrl=user['followers_url']
        Follow_url = requests.get(FollowUrl) #request the follwer url to get the data
        followers_details = json.loads(Follow_url.text)#follower url to load the data in json format.
        followersID=[]
        followersLogin=[]
        

        for followers in followers_details:
            csv_data_upload.append([user["id"],user["login"],user["login"],followers["id"],followers['login']])

fields = ['UserId', 'UserLogin', 'UserName', 'FollowerId', 'FollowerLogin']

with open("output_file.csv", 'w') as file:  #open the csv file/ create a csv file
    csvwriter = csv.writer(file)            # write the data
    csvwriter.writerow(fields)              # write headers
    csvwriter.writerows(csv_data_upload)    #write the data's


upload_to_google_drive()   # file upoload google drive function call
             
             
