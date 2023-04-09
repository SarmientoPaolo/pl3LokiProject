# pl3LokiProject

Team Loki Project Proposal

Project Name: TransitMode

Programming Language: Python 

Description:
TransitMode is a transportation cost and time estimator, written in Python. It provides users with several transportation options and their associated fares, costs per kilometer, routes, and rush hour times. It then allows users to input their destination and distance, choose a transportation option, and enter their average speed. The program then calculates the estimated time of arrival (ETA) based on the distance, speed, and rush hour times of the chosen transportation option, and displays the cost and ETA information to the user. The program runs in a while loop that prompts the user to enter another destination if desired, and terminates if the user chooses not to continue. This program could be useful for individuals who are planning their transportation routes and would like to estimate the time and cost of their trip in advance. Additionally, it could be expanded to incorporate real-time traffic data to provide more accurate ETA estimations.

The main way this is achieved is similar to waze and grab, where the program has a dictionary on certain transportation modes and the prices often given for each individual mode of transportation. Like grab having certain fares per km or jeepneys and buses with certain fares of km. The other modes of transportation like trains will not necessarily be time efficient as the lines for the trains can often affect the time spent for transportation. Another restriction to this is that in first usage it may or may not know the paths as it requires more data on individual locations and such and we will be only be able to provide data based on own experiences as making a more complex dictionary would be more time consuming and the lack of resources and experience on multiple routes will hinder us in giving a good output.

Features:
 - User input and output
 - Calculation of costs based on distance and transportation option
 - Calculation of ETA based on distance, speed, and rush hour times
 - Handling of invalid user input
 - Looping until user chooses to exit the program.
