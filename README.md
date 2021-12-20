# instawork
A web interface for instawork using Django, HTML, CSS and JavaScript

The project is developed in python **3.8**

All the work is done in Django framework.

I have tried to demonstrate the use of custom forms and REST API with this project.

The database of choice was in memory database **sqlite**.

All the required packages for the working of the app is mentioned in **[requirements.txt]** file.

The app is made to work as a localhost app. 
The default port for the app is given as 8000. 
If there is any change for the port number, change the port numbers with respect to the new port number in the html page located at "instawork/instawork/instaworkapp/templates/index.html" as well.

To start the working of the app, go to the folder "instawork/instawork/" and type the command "python manage.py runserver"

To migrate the sqlite db tables you need to execute the command "python manage.py migrate"

The base page of the app is http://localhost:8000/index

List Page

![image](https://user-images.githubusercontent.com/77734908/146844805-f489a4b1-a686-47c4-a1a8-ec75a19e4ef0.png)

Add Page

![image](https://user-images.githubusercontent.com/77734908/146844890-a7889566-0781-4b89-9d16-58e8308379f5.png)

Edit Page

![image](https://user-images.githubusercontent.com/77734908/146844935-b05bf531-ca57-44ac-a431-0f0c641fc017.png)
