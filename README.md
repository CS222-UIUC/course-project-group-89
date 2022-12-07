# course-project-group-89
This Project is for CS 222, a University of Illinois at Urbana-Champaign course. 

Our project goal was to build a scheduler based on our experience with Self Service, the current class scheduler at the University. We also wanted to expand on a traditional scheduler by adding a feature in which two users could identify classes that they could take together. 

(a) Summary of presentation introduction 
When choosing classes, trying to coordinate with friends to take the same classes can become an arduous process. Different majors can have different requirements, and classes have many options to choose from. Our goal was to simplify the process by narrowing down a list of classes that two friends can take together when provided with their major, the classes they have already taken, as well as the time frame in which they prefer their classes to be. 

(b) Describes the technical architecture
The front end utilizes HTML/CSS to design user interfaces and Javascript to add functionality for user inputs such as a user’s major, classes already taken by a user, and ideal start/end time for both users. The user input is then sent to the backend via Flask POST Requests and stored in a text file to save the data as users go from screen to screen.

Once the information is collected, functions from parsing.py use Pandas and NumPy libraries to identify the final set of classes both users can take.


(c) Provides reproducible installation instructions 

Open your terminal. We will be checking for two libraries to be installed: Flask and Pandas

Use the command to check if Flask is already installed:
flask --version
If you receive a message like this, you are good to go:
Python 3.9.12
Flask 2.1.2
Werkzeug 2.1.2
Otherwise, you need to install flask to use in our web application. Run the following command:
	pip install flask

Use the command to check if pandas is already installed:
		pip show pandas
If you receive a message like this, you are good to go:
Name: pandas
Version: 1.3.2
…
Otherwise, you need to install pandas to use in our web application. Run the following command:
	pip install pandas

To run our application, make sure you are in the main directory. Run the following command:
	flask run

Click on the link shown (i.e. http://127.0.0.1:5000) or type it into your web browser to see the web application.



		

(d) Group members and their roles
Sammy: worked on frontend, created webpages for User 1, contributed to the final display, and created the Flask infrastructure for GET and POST requests. I also implemented the procedure to store the User imputed information as they went between pages. The code base was created with scalability in mind to allow for more users for future uses.
Jessica: worked on frontend, worked on templates for pages using HTML, added CSS in order to add formatting to templates, worked on getting checkboxes set up for classes already taken and passing that information to backend
Esther: worked on backend and frontend; created last page on frontend which automatically populates table with list of common classes. Redesigned CSS/HTML for all Submission Pages using flexbox to create a more intuitive layout. Wrote backend functions including the following: filter for a user’s remaining classes, check for time conflicts amongst classes, remove courses which meet the same requirement from a user’s set of classes. Helped set up github actions and test cases. Helped connect the frontend and backend, working out any bugs in the process.
Emily: worked on backend; created functions intended to return correct data as a Pandas dataframe to frontend given user inputs; functions included returning required classes based on a given major, retrieving all courses and course explorer information for given courses, and filtering a dataframe given user-selected start and end times and a dataframe of courses and their information

