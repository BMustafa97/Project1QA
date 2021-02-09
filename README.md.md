---


---

<p>**</p>
<h2 id="family-todo-app">Family ToDo App</h2>
<p>**</p>
<p><strong>Brief</strong><br>
The contents of this document shall explain the necessary steps I completed to achieve a functional ToDo App. The Project Brief was to create a web application which had the functionality to Create, Read, Update and Delete data. In order to successfully achieve this various tools and frameworks were concomitantly applied.</p>
<p>Aside from the crux of <strong>CRUD</strong> Functionality I also needed to meet a subset of requirements:</p>
<ul>
<li>Documentation of the development and design of the app</li>
<li>Usage of a <strong>Kanban</strong> board showing planning and subsequently progression of app planning/evolution</li>
<li>A <strong>relational database</strong> comprising of two tables</li>
<li>Testing of the app via <strong>Unit tests</strong></li>
<li>Functional Front-end interface</li>
<li>The use of a version control system</li>
<li><strong>CI pipeline</strong> with <strong>automation</strong> via <strong>Jenkins</strong></li>
</ul>
<p>**Initiation of Project **<br>
In light of the Project specification I decided to create an app which would allow for user input to be a simple ‘Todo’ with update and delete functionality.</p>
<p>For example a user could input Todo: <em>Visit Grandmother at 7pm</em><br>
This would immediately appear on the app homepage and would be set to <em>Not Completed</em> initially. This Todo could then be updated and be seen as <em>Completed</em>. A user could then disregard the Todo and delete it from sight.</p>
<p>An additional feature was the assignment of a task to a <strong>person</strong>. This would allow for a group of people to access the same homepage and see what tasks they were due to do on the day. Particularly handy for a parent who needs a task to be assigned to a family member.</p>
<p>**</p>
<p><strong>Project Tracking</strong></p>
<p>I used a Trello Board to plan my project and track any progress by simply moving tasks from a state of Todo &gt;&gt; Doing &gt;&gt; Done. This allowed me to apply a <em>Ranking</em> method to the importance of my tasks from very important to not so important.</p>
<p><img src="https://photos.app.goo.gl/3sAmzRTzCnohjkVo8" alt="Trello Board (Mid-Project)"></p>
<p><strong>Relational Database</strong><br>
<img src="https://photos.app.goo.gl/gWY56zfQJ2exqWS97" alt="Tables"><br>
The above ERD  diagram displays the tables in my database and their respective connections. This entity relationship diagram allowed for the smooth creation of tables and their links before development of code.</p>
<p><strong>Continuous Integration Pipeline</strong></p>
<p>A continuous integration pipeline was used for this project to automate the testing and deployment of the app. This was conducted via the <strong>Jenkins</strong> platform.<br>
<img src="https://photos.app.goo.gl/f2x7A6ZmZ7SThav27" alt="CI Pipeline"></p>
<p><strong>Unit Testing</strong><br>
Testing primarily was conducted using <em>Pytests</em>. This automated feature allowed my app to achieve successful functionality of the app with an overall 80% coverage.</p>
<p><strong>Improvements</strong><br>
No app can be perfect and my first project was far from it. For a humble first attempt I believe there are more than 5 areas where I would like to improve in:</p>
<ul>
<li>Implementation of a User Login where up to a specified amount of users can easily access the app</li>
<li>Increase in testing features</li>
<li>Apply aesthetic features to the app</li>
</ul>
<p>Creator<br>
Bilal Mustafa</p>
<p>Acknowledgements<br>
QA Academy team in particular Peter Rhodes, Luke Benson and Raji Kolluru</p>
<blockquote>
<p>Written with <a href="https://stackedit.io/">StackEdit</a>.</p>
</blockquote>

