How to upload files in google drive

1. first install the python module 

pip install pydrive

2. google search to search google developer console

 1.create a new project and give your project name

 2.In Dashboard add + ENABLE APIS AND SERVICES button to serach Google Drive API to enable the service.

 3.select Credentials button to choose oauth client Id
    1.select the application type like (Web application)
    2.Authorized JavaScript origins to add url to cpoy and paste the following link
      http://localhost:8080
    3.Authorized redirect URIs  to give this link
       http://localhost:8080


Finally select the create button

popup window shown it hold your project clientid.
select credentials to download the file in json format and move that file in your current directory
Rename the file to client_secrets.json file

afterthat run your python code it redirect to browser and select your Gmail account give authentication access to select blue color agree button.
finally upload your file to google drive.
