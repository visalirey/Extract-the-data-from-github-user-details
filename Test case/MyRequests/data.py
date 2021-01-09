import  requests
import json
import csv 

class Data_Extraction(object):
    def __init__(self):
        self.headers = {
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'en-US,en;q=0.8',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            #'Referer': 'http://www.wikipedia.org/',
            'Connection': 'keep-alive'}
        self.url = "https://api.github.com/users"

    @property
    def get(self):
        try:
            result = requests.get(url=self.url, headers= self.headers, timeout=1)
            if result.ok:
                return result
            else:
                return None
        except requests.exceptions.Timeout:
            return 'Bad Response'

obj1=Data_Extraction()
print(obj1.get)
#print(obj1.get_data.text)
#print(obj1.get_data.json())

json_data = json.loads(obj1.get.text) #load the data in json format

print(json_data)

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

with open("testcase_output.csv", 'w') as file:  #open the csv file/ create a csv file
    csvwriter = csv.writer(file)            # write the data
    csvwriter.writerow(fields)              # write headers
    csvwriter.writerows(csv_data_upload)    #write the data's




