Readme
Purpose
User Stories
Design and UX
Wireframes
Colour schemes and typography
Accessibility
Features
Technologies
Testing
Code Validation
Browser Compatibility
Performance Testing
Manual Testing
User Stories Testing
Debugging and known bugs
Deployment
Credits
Acknowledgements

Purpose

The Rhubarb Witch is a text-based choose your own adventure game with mechanics taken from Dungeons and Dragons. At the beginning you choose a character class: Barbarian, Bard, Rogue or Sorcerer. At each fork in the path you will roll a ‘dice’ which will determine whether you succeed or fail in taking that action. The class you chose affects the outcome of the roll, which will be further explained in the Design section of the Readme.


User Stories

A first time user looking to play the game:
I want to be able to choose a character
I want the game to be engaging
I don’t want to wait too long between choices/paths

A returning user looking to play the game again:
I want to be able to play the game multiple times without the same ending/path
I want to be able to choose a different character

A disabled user who is new or returning to the site:
need to know more

As the owner of the site:
I want users to be able to use the game easily and intuitively
I want the game to be engaging
I want what is going on to be clear to the users at all times
I want to provide the same experience for all users - need to know more

Design and UX

Inspiration from shows such as Dimenson 20 (link) and Polygon’s TTRPG videos (link to cyperpunk red?)

In D&D, almost every action is accompanied by a roll of a dice, usually one with twenty sides known as a D20. There are many variables as to the success or fail of your action, not just the roll but the stats of your character, special moves and so on. This is too complicated for this short, simple game so I have pre-determined the player’s stats for each action/path based on the character classes. That information can be found [here] and is in the form of a simple + or - for each divergent path. At each path the program will roll a number between 1 and 20 and the stat will be added or taken away from the number. If it is 1-10 inclusive the move fails and the player will be sent down the opposite path, 11-20 inclusive then the move succeeds. This will hopefully make the game more dynamic than a standard choose your own adventure and allow the player to have multiple playthroughs without the same path each time.

Text is kept relatively short so as to keep the user engaged. The game never goes more than a few sentences (usually 2 or 3) before introducing a choice; I have noticed from my own play throughs of choose your own adventure games that there is a tendency to skip to the end if I see a block of text, which I wanted to avoid here.

Wireframes
Colour schemes and typography


The site background invokes a deep dark forest, as most of the action takes place outside. It is neutral so as not to detract from the game.

Accessibility
Semantic HTML and aria labels were implemented across the site (only keep this section if you have more to say, otherwise this is covered in testing section)(does this apply to heroku app??)

Features - all pages, per page


Rolling - a countdown/number of lines between the player making a choice and the computer revealing the decision in order to build suspense and highlight that a ‘roll’ is being made. 

Technologies
Languages used:
HTML5 ?
CSS ?
Javascript ?
Python 3
Frameworks, Libraries and Programs Used:
Google Fonts - for the typography ?
Balsamiq - for creating the wireframes in the design stage ?
Firefox Developer Tools - for inspecting and testing the site
GitHub - for hosting the site
GitPages - for the deployment of the site
Gitpod - for editing the files
Heroku?

Testing 



Debugging and known bugs
tbc
Deployment
Publishing
The project was deployed using GitHub pages. The steps to deploy using GitHub pages are:
In the repository, click the 'Settings' tab, which is the furthest to the right
Scroll down until you see the 'Pages' tab, which will be in the menu on the left hand side
Underneath the 'Source' heading, open the drop down and choose the 'master' branch to build from
Click 'Save' and the site link will appear in a blue box. After a few moments the box will turn green and then the site will be live.
The live link is: 
Forking and Cloning
To save a copy of the code and work on it yourself, here are the steps for forking and cloning using Github:
In the repository, click the 'Fork' button, which is on the top right hand side, next to 'Star'.
Github will automatically create a new repo, which is forked from the original. If you would like to clone it you have two options:
Within the repository, click the 'Code' dropdown, which is located next to 'Add File' on the right (underneath the Settings tab); there is an option to download all files and save a copy locally.
In the same 'Code' dropdown, you can opt to open the code with GitHub Desktop and work from there.

Credits (content and media)
Character class information - research done on dungeons and dragons fandom .com (link) and d&d beyond (link)
