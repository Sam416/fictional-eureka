# Hudl Code Test

To run this code, you must have the selenium package installed in your Python environment.
Also, ensure that the executable chromedriver is on the system path.

Running this code requires that you have a file on your project path
named "blobs.txt" in the following format:
    
    username
    password
    incorrect password
 
 This tests 4 basic parts of logging in:
 both pressing enter and clicking the log in button for both a correct
 input and an incorrect input. To do this, it merely checks the page
 title after the action is performed. If there is no output, the tests 
 completed successfully.
 
 To run, simply run the .py script on a python console.
