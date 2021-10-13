# Project 1 Milestone 2- Ross Miller


# About

### Purpose:
    - Make a website that desplays top songs from your favorite artists for individual user accounts that allows you to save artists to your account as well as remove them

    includes:
        - new weekly music releases
        - Song search
        - Artist search
        - personal account
        - Artist image
        - Top songs
        - Album art for each song
        - Song preview
        - Genius lyrics link

### Tech Stack:
    - Python
        - flask for web framework
        - requests for api calls
        - Custom built encryption system
        - SQLALCHEMY for postgres db
        - regex for password validation
    - HTML & CSS
    - Heroku for deployment environment 

### What it does:
1. My project takes a list of artist ids from the PostgreSQL database on each user account from Spotify, makes 2 requests to the Spotify API:
    1. A call to the artist endpoint:
        - This gets the artist name as well as the artist picture
    2. A call to their top songs endpoint:
        - This gets the top song names, album art  and song preview

2. Then it makes a call to the genius api, passes the song name and the artist name and gets the link to the lyrics page.

3. Lastly, my app takes all this data and passes it to the HTML front end where it loops through all the artists, their songs, ect... and builds a collapsible dropdown to display this information.

Live demo located at `https://project1-rmiller87.herokuapp.com`

### Questions:

1. What are at least 3 technical issues you encountered with your project? How did you fix them?

    - The first technical issue I ran into was troubles with flask-login it was not storing the login sessions right and I had to use cookies to store the sessions to notify it as logged in, the final fix ended up being that I recoded all the login and changed locations of how it stored and stored the login user and everything started to work.
    - The second was I was having an issue displaying a message that says your discovery is empty if you dont have any artists stored. The solution was to make a separate variable to store if the dict was empty or not.
    - The third had to do with displaying the flashes, I had the wrong format and the fix was to change the code that displayed the flashes.

2. What would you do to improve your project in the future? 
    - To improve my project in the future, Id implement the rest of the functionalities I had planned, setting for accounts to change passwords and usernames, email auth for forgotten passwords to send a forgot password token, comments on peoples accounts as well as a chat wall and general profile information, an add artist button on each artist when searched to make it able to be added directly instead of typing in the artist id, a remove button on each artist in the discovery, and change the layout to look cleaner and more transitional coloring

3. How did your experience working on this milestone differ from what you pictured while working through the planning process? What was unexpectedly hard? Was anything unexpectedly easy?
    - This milestone for me was easier then the first one because I had most of the functionalities already built out it was just a matter of adding a few new ones and changing the redirects to pages rather then adding it all on to the same page
    - The flask login stuff for me was harder then expected I just had to rethink my work to make it work properly
    - Creating routing and sending parameters through requests was easier then expected

### Extra Credit:
    - Search funtionality works off of Song ID and name as well as Artist ID and name, however you can only add by artist id not name to the discovery page
    - Removing aritsts from your discovery by id
    - Built out my own encryption system for passwords to store based off of auto generated key that once deleted makes everything basically useless
    
# Imports

For api requesting:
```
requests - for api requests
os - for .env variables
dotenv - for env variables
regex - for password validation
```

For website:
```
flask - for web
flask-login - for login functionality
```

To import use `pip install <package>`

# How to run

1. clone down the project from github
    - `git clone https://www.github.com/csc4350-f21/project1-rmiller87`

2. switch to Branch milestone-2

3. install all packages in [Imports](#imports)

4. create a .env file where you will store your environment variables
    ```
    Needed environment Variables:

    FROM SPOTIFY:

    CLIENT_ID=''
    CLIENT_SECRET = ''

    FROM GENIUS:

    GENIUS_ACCESS_TOKEN=''

    DATABASE_URL=''

    SECRET_KEY=''

    ```
5. open and run app.py `python3 routes.py`
