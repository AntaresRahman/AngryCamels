Execute the file AngryCamels(executable).

Angry Camels
Momin Javed & Antares Rahman
Final Project
COM 110, Fall 2013
Instructor: Christine Chung


Statement of the project:
Angry Camels is a project inspired by the video game Angry Birds developed by Rovio Entertainment. The goal of the project is to make a video game similar to Angry Birds and to maximize user-friendliness and user-computer interaction.

The video game starts with a title screen which is not only graphic, but also somewhat interactive. It also displays a story of the game through which it very briefly describes to the user how the game is played and how the scoring system works (using buckets of water). We made sure there was no “rocket science” involved in our description, because users are likely to be of a relatively young age group. The game allows the user to choose between two difficulty levels: Easy and Hard. The rewards are doubled in the Hard level.

The aim of the game is to correctly launch a Connecticut College Camel at a Bowdoin Polar Bear (no offense meant towards Bowdoin College) using a slingshot and the knowledge of projectiles. The user is given three tries in each level. On either success or failure, the user is given the option to either play the same level again or go back to the main menu in order to select the difficulty level.


Major components of the design:
The design of the program uses mostly the “AngryCamels(executable).py” file, which runs the main program. It contains the Projectile class and the functions file_read(filename), title(gwin), intro(gwin), menuFunc(gwin) and main().

Projectile class:
We referred to the book “Python Programming: An Introduction to Computer Science” by John M. Zelle, Ph.D. in order to make this class. The class takes the parameters angle, velocity, x-coordinate and y-coordinate of the Projectile object. These parameters determine the initial conditions and position for the projectile of the object (in the game, this depends on where the user clicks). The class uses four methods:
I)	.update(time): This method takes the time parameter, which determines the interval of time taken between each position of the Projectile object as the motion of the object progresses. In our Angry Camels program, we defined time as 0.001. So the method calcuates the x- and y- coordinates of the object in every 0.001s interval.
II)	.getYpos(): This method returns the instance variable self.ypos, which is the y-coordinate of the Projectile object.
III)	.getXpos(): This method returns the instance variable self.xpos, which is the x-coordinate of the Projectile object.
IV)	.getMoveY(): This method returns the change in y-coordinate compared to the previous position of the Projectile object.
V)	.getMoveY(): This method returns the change in x-coordinate compared to the previous position of the Projectile object.



file_read(filename) function: This function opens a .txt file given a filename (excluding the file extension), reads the whole file into a string and returns this string. This makes displaying .txt files as string outputs much simpler.

title(gwin) function: This function simply creates the title screen for the Angry Birds game. It calls the intro(gwin) function (see below) that displays an introduction to the game from the “intro.txt” file should the user opt to read it. We have kept it optional using a button, because the user may not want to see it every time the game is run. This function returns a .getMouse() call, which is made use of later in the main() function. We have intentionally not given the user the option to exit the program from the title screen, just as the Angry Birds game does.

intro(gwin) funtion: It makes use of the file_read(filename) function to read the “intro.txt” file which gives an introduction to the game.

menuFunc(gwin): This function creates the main menu screen where the user is allowed to choose between the difficulty levels: Easy and Hard. This is done by clicking on the screen-shots of the levels, which are simply drawn on top of buttons. The user may also exit the program from the Main Menu. Depending on where the user clicks, this function returns values. If the user clicks on the level “Easy”, it returns 1. If the user clicks on the level “Hard”, it returns 2. If the user clicks on the Exit button, it returns an empty string (“”), which is just used as a case for breaking a loop to exit the program in the main() function, where menuFunc(gwin) is called.

main(): The main() function directly calls the title(gwin) and menuFunc(gwin) functions, and makes extensive use of the Projectile class and the Button class. The Camel is described as a Projectile object in this program.

The program also makes use of the Zelle Graphics (graphics.py), math, time and random modules, and a slightly modified version of the Button module (buttonClass.py) made earlier in class.

Modifications to the Button module:
The parameter color has been added to the Button class, and it has also been stored as an instance variable self.color in the class definition. It allows us to define the color of the button which is important in a graphic-heavy game.

	The .draw(gwin) and the .undraw() methods have also been added to this class to allow easier control over drawing (and activating) and undrawing (and deactivating) the “buttons” whenever required.


A glimpse at the obstacles and the future of Angry Camels:
Angry Camels was a fun, yet rather challenging project we encountered. We have done all sorts of testing for the robustness of the program and tried maximizing the user satisfaction while minimizing the run-time as much as possible. While the program is quite robust and enjoyable, it is not the most efficient in term of run-time. There are lags in the projectile of the Camel, and between changes in the screens. We believe we can improve this using more efficient coding. We would like to add more levels to the game and challenge the user to a further extent, which will definitely increase user-computer interactions. This is evidently seen in Angry Birds. We have much room to improve in terms of graphical work and building the overall game-play. One thing we definitely want to look into is incorporating audio with the game and learning how to carry out simultaneous calls using code. There are many parts where the user has to wait till a function call ends before the user can do something else (for instance, exit the game).
