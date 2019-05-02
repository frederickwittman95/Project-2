##### Frederick Wittman, Galen Damosso, Eli Oceanak, Trevor Evenson, Josh Malone
##### Dr. Hill
##### COSC 2030-01
##### 02 May 2019

# A simple node class.
class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.left = None
        self.right = None
        
        
def insert(root, node):
    """This function inserts a node with a key element consisting of a single character, either '-' or '.', and a value prescribed
    by the value in 'MorseTable' associated with the node's position in the binary search tree, into the binary search tree."""
    
    # This 'if' block inserts new nodes with key values that consist of a single "-" or "." element.
    if len(node.key) > 1:
        currSymbol = node.key.pop(0)
        if "-" == currSymbol: 
            if root.right is None:
                root.right = Node("-", None)
                insert(root.right, node)
            else:
                insert(root.right, node) 
        elif "." == currSymbol:
            if root.left is None:
                root.left = Node(".", None)
                insert(root.left, node)
            else: 
                insert(root.left, node)
        else: print("Error!  Improper symbol.")
            
    # Once the correct node has been found, this 'elif' block gives it the appropriate value.
    elif len(node.key) == 1:
        currSymbol = node.key[0]
        if "-" == currSymbol:
            if root.right is None:
                root.right = node
            else:
                root.right.val = node.val
        elif "." == currSymbol:
            if root.left is None:
                root.left = node
            else:
                root.left.val = node.val
                
        else: print("Error! Improper symbol!")


def createTree(infile, root):
    """createTree creates a binary search tree from the table of key-value pairs and a root element.  It returns the root of the binary search tree."""
    
    file = open(infile, "r")
    for line in file:
        line = line.rstrip("\n")
        key = list(line[2:])
        value = list(line[0])
        nodeToInsert = Node(key, value)
        insert(root, nodeToInsert)
    file.close()
    return root


def search(root, key):
    """search uses a binary search algorithm to return the value associated with the key argument from the binary search tree."""
    
    # Once the key has been decremented to 0 elements, either the correct value has been found or the Morse sequence does
    # not correspond with a value in the binary search tree.  In the latter case, return an appropriate flag.  In the former
    # case, just return the value.
    if len(key) == 0:
        if root == None:
            return list("(FLAG: INVALID MORSE SEQUENCE)")
        else:
            return root.val
        
    # This is the recursive part of the function.  It traces the value that corresponds with the key argument in the same
    # way that the binary search tree was created.
    curr = key.pop(0)
    if curr == "-":
        root = root.right
        return search(root, key)
    if curr == ".":
        root = root.left
        return search(root, key)
    
def buildDict(morseTable):
    """buildDict constructs a dictionary from the key-value pairs found in 'MorseTable' and returns the dictionary."""
    
    dict = {}
    mTable = open(morseTable, "r")
    for line in mTable:
        line = line.rstrip("\n")
        key = line[0]
        value = line[2:]
        dict[key] = value
    mTable.close()
    return dict
        
def morseToEnglish(infile, outfile, root):
    """morseToEnglish translates the Morse code content of a file to English and writes the English to an out-file."""
    
    ifile = open(infile, "r")
    ofile = open(outfile, "w")
    
    for line in ifile:
        line = line.rstrip("\n")
        letter = []
        i = 0
        
        # This 'while loop' processes each line of the Morse file.
        while i < len(line):
            
            # This 'if' prevents the index, i, from going out of range.  It deals with the last i.  Notice that the elif
            # block that follows does not suffer for missing the data contained in the last element of the line, because
            # a sequence of at least two spaces is always translated to a single English space.
            if i == (len(line) - 1):
                if letter:
                    ofile.write("".join(search(root, letter)))
                    letter.clear()
                if line[i] == " " and line[i - 1] == " ":
                    ofile.write(" ")
            
            # This 'if' block maps a single space to a new letter, and two or more spaces to a space.
            elif line[i] == " ":
                j = 0
                while line[i] == " " and i < len(line) - 1:
                    i = i + 1
                    j = j + 1
                if j == 1:
                    if letter:
                        ofile.write("".join(search(root, letter)))
                        letter.clear()
                    i = i - 1
                else:
                    if letter:
                        ofile.write("".join(search(root, letter)))
                        letter.clear()
                    ofile.write(" ")
                    i = i - 1
            
            # If an element of the line is a Morse character ('.' or ','), append it to a list. 
            elif line[i] == "-" or line[i] == ".":
                letter.append(line[i])
            
            # If line[i] is not a space or a "-" or ".", it is invalid.
            else:
                ofile.write("(FLAG: INVALID CHARACTER AT THIS POSITION)")
                
            i = i + 1 
            
    ifile.close()
    ofile.close()
    
def englishToMorse (table, infile, outfile):
    """englishToMorse converts the English language contents of an in-file to Morse code, via a table look-up, and writes the Morse code to an outfile"""
    
    ifile = open(infile, "r")
    ofile = open(outfile, "w")
    
    for line in ifile:
        line = line.lower().rstrip("\n")
        
        # If an element of the English language file is a space, write a space to the Morse file.  Otherwise, write
        # the sequence of Morse characters associated with the English language character, followed by a space.
        for i in range(len(line)):
            if line[i] == " ":
                ofile.write(" ")
            elif (line[i] in table):
                    ofile.write(table[line[i]] + " ")
    
    ifile.close()
    ofile.close()
    
# Create the binary search tree, along with a pointer to the binary search tree, and build the key-value table for English
# to Morse translation.
treeRoot = Node(None, None)
treeRoot = createTree("MorseTable.txt", treeRoot)
table = buildDict("MorseTable.txt")

# This user interface allows the user to exit at any time by typing "exit".  It will repeatedly prompt the user until
# an acceptable translation scheme ("E2M" or "M2E") and valid input-output file names have been entered.
def userInterface ():
    """userInterface allows a user to easily use the other functions to translate between Morse code and English."""
    
    print("Welcome to the Morse/English translator!  Type 'exit' at any time to stop translating.")
    
    while(True):
        user_request = input("If you would like to translate from English to Morse code, type 'E2M'.  If you would like to translate from Morse code to English, type 'M2E'.")
        while(str(user_request).lower() != "E2M".lower() and str(user_request).lower() != "M2E".lower()):
            if user_request == "exit":
                return
            user_request = input("If you would like to translate from English to Morse code, type 'E2M'.  If you would like to translate from Morse code to English, type 'M2E'.")
        
        infile = input("Please provide the name of the input file with a .txt extension.")
        while True:
            if infile == "exit":
                return
            try: ifile = open(infile)
            except IOError as errno:
                infile = input("Sorry, that's not a valid file name.  Enter a new file name or type 'exit' to quit.")
                continue
            else:
                break
            
        outfile = input("Please provide the name of the output file with a .txt extension.")
        while True:
            if outfile == "exit":
                return
            try: ofile = open(outfile)
            except IOError as errno:
                outfile = input("Sorry, that's not a valid file name.  Enter a new file name or type 'exit' to quit.")
                continue
            else:
                break
                
        table = buildDict("MorseTable.txt")
            
        if(user_request == "E2M".lower()):
            englishToMorse(table, infile, outfile)
        
        if(user_request == "M2E".lower()):
            morseToEnglish(infile, outfile, treeRoot)

# 1. Testing framework
#   a) These tests verify perform the appropriate translations on the selected files.
englishToMorse(table, "E2MTest1.txt", "E2MTest1_Output.txt")
englishToMorse(table, "E2MTest2.txt", "E2MTest2_Output.txt")
morseToEnglish("M2ETest1.txt", "M2ETest1_Output.txt", treeRoot)
morseToEnglish("M2ETest2.txt", "M2ETest2_Output.txt", treeRoot)
#   b) These tests translate the output files back to the originals.
englishToMorse(table, "M2ETest1_Output.txt", "M2E2MTest1_Output.txt")
englishToMorse(table, "M2ETest2_Output.txt", "M2E2MTest2_Output.txt")
morseToEnglish("E2MTest1_Output.txt", "E2M2ETest1_Output.txt", treeRoot)
morseToEnglish("E2MTest2_Output.txt", "E2M2ETest2_Output.txt", treeRoot)
#   c) Finally, these two tests translate the Steganography message and symbols added to MorseTable.txt to Morse code
#      and then translate them back to English.
englishToMorse(table, "newCharacter+StegTest_E2M.txt", "newCharacter+StegTest_E2M_Output.txt")
morseToEnglish("newCharacter+StegTest_E2M_Output.txt", "newCharacter+StegTest_E2M2E_Output.txt", treeRoot)
# Call "userInterface()" for additional testing
userInterface()
