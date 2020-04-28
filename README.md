Author

By Dan Kariuki

Description

50BeansOut is a web appliction that displays news sources from around the world. Users are able to click on a news source and view a version of the particular news article. 

Application Name

50Beansout. To directly go to the application, click on this link https://fifthtime.herokuapp.com.

Developers Contact

For any issue, you can reach me at Dankariuki0101@gmail.com

Known bugs

A Feature called 'trending' is not working for now. It shall soon be soolved.


With the application, a user will be able to:

    See various news sources and select the ones they prefer.
    See all news sources from the source they selected.
    See Image description and time the news article was created.
    Click on an article, navigate further into its content
    
Specifications

        Behaviour 	   Input 	         Output

Display news sources | On page load  |List of various news sources is displayed per category

Display articles from a news source  |Click a news source  |Redirected to a page with a list of articles from the source

Display the preview of an article    |On page load | Each article displays an image, title, description and publication date

Read an entire article               |Click an article |Redirected to the news source's site to read the entire article

Prerequisites

You need the following to start working on the project on your local computer:

    A computer running on either Windows, MacOS or Ubuntu operating system installed with the following:

-Python version 3 and above
-Flask
-Pip or Pip3
-vA vietual environment
-A text Editor or an Integrated Development Environment

Getting Started

    Clone this repository
    Ensure you have python3.7 installed in your computer.
    From the terminal navigate to the cloned project folder.
    Create a virtual environment and access the folder via your virtual machine
    For an API_KEY Visit https://newsapi.org/
    Create start.sh file and in it write the following lines:

 Export NEWS_API_KEY='<Your-Api-Key>'
 python3.7 manage.py server

    Run chmod +x start.sh follwoed by ./start.sh while in the project folder to start the project.
    Once started, the project can be accessed on your localhost using the address: localhost:5000.
    Alternatively the application can be accessed by visiting 

Technologies Used

    Python v3.7
    
    Flask
