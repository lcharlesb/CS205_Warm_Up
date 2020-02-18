import csv, sqlite3, sys
from DB import LoadData
from ratings import ratingsMaster
from sales import salesMaster
from splitInput import splitInput

# If program invoked directly
if __name__ == "__main__":

    userInput = ""
    dataLoaded = False

    while (userInput != "quit"):

        # Get user input
        userInput = input("")

        if(dataLoaded == False):

            if(userInput.lower() == "load data"):
                LoadData()
                dataLoaded = True
                print("Data loaded.")
            else:
                print("Data has not yet been loaded. Please type 'load data' to continue.")

        else:

            # Handle user input
            inputArray = splitInput(userInput)
            firstWord = inputArray[0].lower()

            if(firstWord == "sales"):
                salesMaster(str(inputArray[1]))
            elif(firstWord == "ratings"):
                ratingsMaster(str(inputArray[1]))
            elif(firstWord == "help"):
                print("-------- HELP MENU --------")
                print(" - sales ")
                print(" - sales title [title]")
                print(" - sales year [year]")
                print(" - sales platform [platform]")
                print(" - sales rank [rank]")
                print("")
                print(" - ratings ")
                print(" - ratings title [title]")
                print(" - ratings userRating [rating]")
                print(" - ratings criticRating [rating]")
                print("---------------------------")
            else:
                print("Invalid input. Type 'help' for options.")


    # Exit b/c user input == "quit"
    sys.exit()
