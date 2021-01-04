# Extract-the-data-from-github-user-details
Extract the data from github user details using python code.
questions:
Task 1:
Get the users and their followers in the CSV format
1. To get the list of users https://api.github.com/users
2. Get the list of user Ids divisible by 5
3. Iterate the result and get the user details https://api.github.com/users/{login}
4. Get the followers list for that user https://api.github.com/users/{login}/followers

From that data construct the CSV file as below

User Id	User Login	User Name	Follower ID	Follower Login
20	kevinclark	Kevin Clark	38	atmos
20	kevinclark	Kevin Clark	45	mojodna
30	fanvsfan		52926	zpmorgan

Task 2:
1. Upload the constructed CSV file into Google Drive.


Extract the data from URL using python code. In This project Extract the data from Github url to get user details.

How to run the code

download the below source code and save into your local machine. preferably use idle/pycharm/visual studio code editor

Run the code you get output like csv format

During run the program some other time you got this type of error

Traceback (most recent call last): File "C:\Users\adminpc\Documents\apton\github.py", line 14, in UserID=i['id'] TypeError: string indices must be integers

This error like Rate limit issue. Github allow only 60 API calls per hour so that issue occur.

the same time you check your url link 'https://api.github.com/users' you got the following message from your browser.

'''{"message":"API rate limit exceeded for 106.76.45.181. (But here's the good news: Authenticated requests get a higher rate limit. Check out the documentation for more details.)","documentation_url":"https://developer.github.com/v3/#rate-limiting"}'''

possible way to avoid this issue:

1.if you got rate limit error alternatively use your internet connection like use different wifi hotspots/ modem connection. or 2. download the data from url to save your local machine and run the program.

using python script to upload the csv file in google drive.
