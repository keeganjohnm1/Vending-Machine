# Vending-Machine
building a vending machine using TDD

This project can be ran from the terminal and the user will need to have python3 and poetry installed.

The project is built through a GitHub actions pipeline that installs python and poetry and runs unit tests associated with the project.

Poetry was used in this project as a modern way of handling dependencies. This dependency manager allows for this project to easily handle and track dependencies.

GitHub Actions was used as the CI/CD tool for this project. I personally like GHA for the centralized location of our projects build that will allow myself to triage any errors without having to go to jenkins or azure devops. There is also no need to set up any instances like there is in the case of using jenkins which is one less thing to maintain.

To run this project install the project locally and run the program with the following command from inside of the driectory where the project is located.
  python3 main.py
  
You will be asked to insert coins and prompted to select an item. If you have entered an invalid coin you will be prompted to enter a valid coin. Please note that the user will type in whether they are entering a penny, nickel, dime, or quarter by typing 'penny', 'nickel', etc. This was done so that the program can weigh the length of each input and then assign the corressponding value to the input.

There is a running total that is displayed for the customer and after the customer has inserted enough coins to purchase the product they are selecting the item will be dispensed and a message of THANK YOU is displayed. If there is any change left that will be shown in the coin return display.

If you have any questions feel free to reach out. Thanks!
