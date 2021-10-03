# pokemon-finder README

How to run pokemon-finder through windows 10

1 - Use the following link and install the latest version of python https://www.python.org/downloads/.

2 - After you have downloaded the python.exe file, find it in the folder you have downloaded it to and double click it to run.

3 - Tick the box 'Add Python 3.9 to PATH', click next, disable the 'path length limit'. Then follow the steps on the python installer to install it.

4 - Open the link https://github.com/JL-PD/pokemon-finder, press the green button 'Code', it will open a menu and click 'Download ZIP'.

5 - Navigate to the downloaded ZIP, select the file by left clicking it once and in the toolbar menu, click 'Compressed Folder Tools', then press 'Extract all' and choose where you would like to extract the file. 

6 - Navigate to the folder you created from unzipping in step 5, it should be called 'pokemon-finder-main', open it then open 'scripts'.

7 - Once you are in the 'scripts' folder, hold the shift key and right click just below the files in the folder, a menu should appear, click on 'Open PowerShell window here', this will open powershell in the correct directory needed to run pokemon-finder!

8 - In Powershell, copy and paste 'python --version' and press enter to show if you have python installed on your computer, it will return the word python with numbers stating the version, for example 'Python 3.9.2' 

** This line can be skipped. ** At this point you may want to set up a virtual environment (advanced users) look at the 'Virtual Environment' section for more details. 

9 - In Powershell, copy and paste the following and press enter 'pip install -r requirements.txt', this will install required packages. 

10 - After the installation is complete, you are now ready to run the pokemon finder! copy and paste the following and hit enter 'python pokemon_finder.py'

11 - Type the pokemon you wish to search for and hit enter, if you would like to terminate the program type 'exit' or close the terminal.


** Virtual Environment **
- In Powershell, copy and paste the following line to create a virtual environment 'python -m venv venv'.
- Then to activate your virtual environment, copy and paste the following line '.\venv\Scripts\Activate.ps1'. (you may run into an error 'execution of scripts is disabled on this system' run Powershell as administrator and copy and paste 'Set-ExecutionPolicy RemoteSigned' and type 'Y' this should allow you to activate the virtual environment afterwards.)



Dockerfile installation for pokemon-finder

1 - Use the following link and install docker on your computer https://docs.docker.com/desktop/windows/install/

2 - Then download the pokemon-finder zip from https://github.com/JL-PD/pokemon-finder

3 - Open the pokemon-finder directory and shift + right click inside the directory and click 'Open PowerShell window here'.

4 - In the powershell window copy and paste 'docker build -t pokemon-finder .'

5 - Then to run the pokemon-finder, copy and paste 'docker run -t -i pokemon-finder', if you would like to exit the program type 'exit' to stop the pokemon-finder.



Anything you would do differently for a production API:

As there is a limit for the translation calls that can be done of up to 5 per hour, I would suggest either paying for the premium services to stop this limitation, or paying for the service temporarily and performing api calls for all of the pokemon and caching the translations, storing them in a local database assuming that this is within the legal requirements of the api.

I would have used pytest instead of unittest, as it is built over unittest and it has additional features/controls over the tests.

If I were working in a group with other engineers on this project, I would use separate branches instead of only the main branch.

End to end testing would be a good idea to implement.

I would also loop through all of the pokemon in the api list and check that the code holds up for all happy paths when testing.

Through my research preparing for this task, I discovered logging in python, if this became a production API, using a logger in replacement of using print statements for debugging would be a better and more efficient approach. This would be more advantageous when the size of the project scales and reduces the difficulty when monitoring and detecting issues.

Develop the ascii 3rd party function interaction further, some of the ascii images are not presented due to differences in pokemon api/ascii naming. A potential approach would be through the use of parsing or to run a comparison with the ID's presented in the ascii with the ID's in the pokemon api.