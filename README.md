# pl3LokiProject

Team Loki Project Proposal

Project Name: TransitMode

Programming Language: Python 

Description:

A python program called TransitMode estimates the price and duration of transit. It offers consumers a variety of transportation choices, together with information about the prices, cost per kilometer, routes, and peak hours. The user can then enter their average speed, choose mode of transportation, then input their destination and distance. The application then calculates the estimated time of arrival (ETA) using the distance, speed, and rush hour times of the selected mode of transportation, and displays the cost and ETA information to the user. The software executes in a while loop that prompts the user to input a different destination if requested and ends if the user decides not to proceed. This tool might be helpful for people who are organizing their travel routes and want to calculate the length and expense of their journey in advance. To generate more precise ETA estimates, it might also be enhanced to include real-time traffic information.

The main way this is achieved is similar to waze and grab, where the program has a dictionary on certain transportation modes and the prices often given for each individual mode of transportation. Like grab having certain fares per km or jeepneys and buses with certain fares of km. The other modes of transportation like trains will not necessarily be time efficient as the lines for the trains can often affect the time spent for transportation. Another restriction to this is that in first usage it may or may not know the paths as it requires more data on individual locations and such and we will be only be able to provide data based on own experiences as making a more complex dictionary would be more time consuming and the lack of resources and experience on multiple routes will hinder us in giving a good output.

Features:
 - User input and output
 - Calculation of costs based on distance and transportation option
 - Calculation of ETA based on distance, speed, and rush hour times
 - Handling of invalid user input
 - Looping until user chooses to exit the program.
