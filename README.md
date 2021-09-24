### Table of contents:

[Purpose](#purpose)

[User Stories](#user-stories) 

[Design and UX](#design-and-ux) 
* [Story map and flow chart](#story-map-and-flow-chart)

[Features](#features)

[Technologies](#technologies)

[Testing ](#testing)
* [Code Validation](#code-validation)
* [Browser Compatibility](#browser-compatibility)
* [Performance Testing](#performance-testing)
* [Manual Testing](#manual-testing)
* [User Stories Testing](#user-stories-testing)

[Debugging and known bugs](#debugging-and-known-bugs)

[Deployment](#deployment)

[Credits](#credits)

### Purpose

The Rhubarb Witch is a text-based choose your own adventure game with mechanics taken from Dungeons and Dragons. At the beginning you choose a character class: Barbarian, Bard, Rogue or Sorcerer. At each fork in the path you will roll a ‘dice’ which will determine whether you succeed or fail in taking that action. The class you chose affects the outcome of the roll, which will be further explained in the Design section of the Readme.

### User Stories

A first time user looking to play the game:
* I want to be able to choose a character
* I want the instructions to be clear
* I want the game to be engaging

A returning user looking to play the game again:
* I want to be able to play the game multiple times without the same ending/path
* I want to be able to choose a different character

As the owner of the site:
* I want users to be able to use the game easily and intuitively
* I want the game to be engaging
* I want errors to be handled efficiently
* I want what is going on to be clear to the users at all times

### Design and UX

Inspiration for this game is taken from shows such as [Dimenson 20](https://www.youtube.com/watch?v=_zZxCVBi7-k) and [Polygon’s TTRPG videos](https://www.youtube.com/watch?v=oCp_2hqguUg&t=27s).

In D&D, almost every action is accompanied by a roll of a dice, usually one with twenty sides known as a D20. There are many variables as to the success or fail of your action, not just the roll but the stats of your character, special moves and so on. This is too intricate and complicated for this short, simple game so I have pre-determined the player’s stats for each action/path based on the character classes. That information can be found [here] and is in the form of a simple + or - for each divergent path. The stats are based on the characteristics of each character; for example a barbarian would be likely to make a bold move so that would be a positive number, but a subtle or stealthy move would be negative for a barbarian, but positive for a rogue.

At each path the program will roll a number between 1 and 20 and the stat will be added or taken away from the number. If it is 1-10 inclusive the move fails and the player will be sent down the opposite path, 11-20 inclusive then the move succeeds. This will hopefully make the game more dynamic than a standard choose your own adventure and allow the player to have multiple playthroughs without the same path each time.

It is possible, after the character stats have been taken into account, for the final roll to be below 1 or above 20. This is the same case in D&D so I have left it in. It makes the success more sweet, or makes the fail feel more harsh.

Text is kept relatively short so as to keep the user engaged. The game never goes more than a few sentences (usually 2 or 3) before introducing a choice.

### Story map and flow chart





### Features

Instructions - game explained clearly and efficiently.

Character choice - user given choice of 3 characters. Enough to make it interesting but not so many as to be overwhelming. Character choice is confirmed by printing same choice back to character.

Text width - text does not extend the width of the page; during initial testing I discovered that it was easier to parse and pay attention to the text if it took up less width of the page. If it takes up the whole width the whole field is filled and the user is overloaded before having read anything. In a text-heavy game, I am keen to avoid this if I can.

Rolling - line break between the player making a choice and the computer revealing the decision in order to build suspense and highlight that a ‘roll’ is being made. 

Final roll - final roll is shown to the player to indicate whether they have succeeded or failed.

Increased number of lines in terminal - The number of rows in the terminal has been increased from 24 to 30; this is to allow some of the longer files to display on the screen at the same time as the choices. Without these additional rolls, the user would have to manually scroll up the page in order to see what they had missed.

Type 'r' to return to the beginning - require user input to return to the beginning of the game, allowing the user to fully read the current path before triggering a reset and printing the beginning text. Handles user errors such as uppercase 'R' or any other character.

Background - The site background invokes a deep dark forest, as most of the action takes place outside. It is neutral so as not to detract from the game.

Penny - inventory function for penny 'path' to add an extra aspect to the game; you can only 'find' the penny and add it to your inventory if you successfully go down that exact path. Conditional statement later in game to check if user has penny or not. Inventory reset when game is reset.

User name - user is given a themed name at the beginning of the game. Names and code are adapted from my previous Javascript project [Wizard Name Generator](https://elyserh.github.io/wizard-name-generator/index.html).

### Technologies
Languages used:
Python 3
HTML5 ?
CSS ?
Javascript ?

Frameworks, Libraries and Programs Used:
GitHub - for hosting the site
Heroku - for the deployment of the site
Gitpod - for editing the files

### Testing 



### Debugging and known bugs
tbc
### Deployment
### Publishing
The project was deployed using Heroku
The live link is: 
### Forking and Cloning
To save a copy of the code and work on it yourself, here are the steps for forking and cloning using Github:
In the repository, click the 'Fork' button, which is on the top right hand side, next to 'Star'.
Github will automatically create a new repo, which is forked from the original. If you would like to clone it you have two options:
Within the repository, click the 'Code' dropdown, which is located next to 'Add File' on the right (underneath the Settings tab); there is an option to download all files and save a copy locally.
In the same 'Code' dropdown, you can opt to open the code with GitHub Desktop and work from there.

### Credits (content and media)
Research for information on Dungeons and Dragons character class information comes from:
 - [Dungeons and Dragons Fandom Wiki](https://dungeonsdragons.fandom.com/wiki/Dungeons_and_Dragons_Wiki)
 - [D&D Beyond](https://www.dndbeyond.com/)

All HTML and CSS (except the minimal amount of code where marked) is created by Code Institute for the purpose of creating a functioning terminal environment within a webpage. Many thanks to CI for this!

Background image comes from [Pexels](https://www.pexels.com/)

All text was written by myself.
