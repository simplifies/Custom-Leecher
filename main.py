# Imports
from googlesearch import search
import os
import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Custom Leecher | github.com/localsgithub")
# defining a function
def startLeecher():
    # Clears the screen
    os.system('cls')
    # Scrapes pastebin using google for the given word
    results = search("site:" + url + " " + input1, num_results=int(amountOfResults), lang="en")
    # Saving output to file
    print("Saving to file 'results.txt'")
    with open("results.txt", 'w+') as f:
        f.writelines("Search Term: " + input1 + "\n")
        f.writelines("% s\n" % data for data in results)
        f.close()
        print("Done!")
    os.system('PAUSE')
    start()

# defining a function
def defineVariables():
    # Allowing global use of variables
    global input1
    global amountOfResults
    global url

    # Clearing the screen
    os.system("cls")

    # First input
    url = input("! DOMAIN ONLY !\nURL: ")
    if url == "":
        print("The value you entered was null. Please try again.")
        os.system("PAUSE")
        defineVariables()
    elif url == " ":
        print("The value you entered was null. Please try again.")
        os.system("PAUSE")
        defineVariables()
    # Second input
    amountOfResults = input("\n\nNumber of results: ")
    # Checking second input
    if amountOfResults == "":
        print("The value you entered was null or not a string. Please try again.")
        os.system("PAUSE")
        defineVariables()
    # Checking second input
    elif amountOfResults == " ":
        print("The value you entered was null or not a string. Please try again.")
        os.system("PAUSE")
        defineVariables()
    # Checking if the second input contains a integer or not
    elif amountOfResults.isdigit() == False:
        print("The value you entered was null or not a string. Please try again.")
        os.system("PAUSE")
        defineVariables()

    # Third Input
    input1 = input("\n\nSearch Term: ")
    # Checking input
    if input1 == " ":
        print("The value you entered was null. Please try again.")
        os.system("PAUSE")
        defineVariables()
    # Checking input
    elif input1 == "":
        print("The value you entered was null. Please try again.")
        os.system("PAUSE")
        defineVariables()


# Main function
def start():
    defineVariables()
    startLeecher()

if __name__ == "__main__":
    start()
