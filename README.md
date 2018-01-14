Band News
---

Band News is the reference for heavy metal shows and news near you. 

Calendar
---

The calendar module is an interactive calendar that displays all bands
touring near you. The time and place of the events will be shown when the 
user clicks on the corresponding concert. Users can are also provided with
a link to buy a pair of tickets.

Tour dates are fetched from Facebook via Facebook's Graph API as most bands 
have an official Facebook page. Multiple other sources, such as a band's 
official website, is scraped for additional data and data validation from
Facebook.

The Calendar module is presently inactive as the database and the webscraper
are being built.

News
---

The News module displays the latest band news.

The module is currently inactive as all focus is on the calendar.

Design Methodology
---

Development of this software follows test-driven development practices with 
pytest (Python) and Jasmine (JavaScript).

A test is first written and failed every time a new function has to be created. 
Then, the function associated to the test is written and its test turns green. 
This cycle continues throughout the development process. Commits are only pushed 
if all tests pass.

Test files are stored under [/spec/][0].

To run the Python and JavaScript test suites, execute ```npm run testpy``` and 
```npm run testjs```, respectively.

---

Setup
---

1. Install the Python dependencies depending on your system.

    1. Under Linux    : ```npm run install```
    1. Under Windows  : to be determined
    1. Under WSL      : ```npm run install``` (to be confirmed)

1. Install the Node Modules: ```yarn install``` or ```npm install```

1. Set up the MariaDB (see **Database Setup**)

1. Generate the variables.env file with ```npm run make_variables_env```. 
This file contains sensitive information on your api keys and databse credentials. 
Therefore, it is crucial no one gets a hold of it.

1. Add a new app on [Facebook Developers website][1]

1. (NOT YET DONE) Replace the following the key:value pairs of the variable.env file.

    1. FB\_APP\_ID with **App ID** from the Facebook Developers app dashboard
    1. FB\_API\_SECRET with **App Secret** from the Facebook Developers app dashboard
    1. FB\_API\_ACCESS with **Access Token** from the [Graph Explorer][2]
    1. DB\_CONFIG: replace user and password. Database and host remain untouched
    1. GOOGLE\_API_KEY with your api key from [Google Developers][3]
    
 1. (NOT YET DONE) Populate the database by executing ```npm run populate_master_db```
 
 1. (NOT YET DONE) See **Usage** below

Usage
---

1. Start the development server: ```npm start
1. Fire a browser to ```http://localhost:3000```:

Database Setup
---

A database server running on your local machine is crucial if you want to test 
the web application.

[0]: https://github.com/reaper47/band-news/tree/master/spec
[1]: https://developers.facebook.com/apps/
[2]: https://developers.facebook.com/tools/explorer/
[3]: https://console.developers.google.com/apis/
