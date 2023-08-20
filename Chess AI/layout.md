This is a complicated program, so we will keep it organized:

DATA PROCESSING:
    We might get the movements, but we need to turn that into a list of boards.
    extractData - This will take the files that we need to use, read the neccicary data from them, and then if given, will also sort out the highest rating of data (meaning the score also needs to be calulated there).
    
    getMoves - This will take the data in the long list of boards and can convert two boards into movetext, and can also get the previous 5 moves, along with the movetext for the key. This will be used for deployment of the AI as well
    
    verifyData - This will go through the data and make sure that there arn't any mistakes.

MODEL BUILDING:
    There isn't much here, but there will be a lot of tweaking of the neural network

POST PROCESSING:
    Not sure what will go here, but will likely be necciary

DEPLOYMENT:
    To begin, you can play the chess AI on the command line, but eventually, I want to make a website that you can play the AI on.
    
