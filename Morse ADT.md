##### Frederick Wittman, Galen Damosso, Eli Oceanak, Trevor Evenson, Josh Malone
##### Dr. Hill
##### COSC 2030-01
##### 02 May 2019

# Morse Code Abstract Data Type

## ADT Summary

This abstract data type allows for translation between Morse code and English, and vice-versa.

## Data Items and Operations

### Data Items

#### Node class

The node class has four member variables: key, value, right child, and left child.  It does not have any member functions.  Its constructor requires initialization of the key and value fields and assigns the left child and right child fields to "None".  This node class is inflexible; it was built for a specific purpose.

#### treeRoot
treeRoot is a global variable that serves as a pointer to the left and right subtrees of the binary search tree.  It does not contain a key or value.

#### table
table is a global variable that maps English characters to Morse code sequences through the use of the dictionary class.

### Operations

#### insert (root, node)
* Parameters: the root node of the binary tree search tree and the node to be inserted.
* Pseudocode: The binary search tree consists of nodes with key values that consist of single characters: either "-" or ".".  The paths along the nodes of the binary search tree sequentially describe the key values of its data items.  The final node of a sequence stores the appropriate value.  search prints an error message and rejects the insertion request if the key contains a symbol that is not a dot or dash.

#### createTree (infile, root)
* Parameters: a file containing the key-value pairs and the root of the binary search tree.
* Pseudocode: createTree reads the key-value (Morse-English) pairs from a source file and inserts them into the binary search tree.

#### search (root, key)
* Parameters: the root of the binary search tree and a Morse code key value.
* Pseudocode: search is a recursive function that returns the English character value associated with a Morse key.  If no English character corresponds with the key in the binary search tree, an appropriate error message is returned as a string.  This would then be written to an outfile.

#### morseToEnglish (infile, outfile, root)
* Parameters: a read-file containing the Morse code to be translated, a write file to write English characters to, and the root of the binary search tree.
* Pseudocode: morseToEnglish relies on the insert, createTree, and search functions.  This function reads the infile line by line.  It ignores newline characters.  If the function encounters a sequence of Morse characters followed by a space, it writes the appropriate English character, found by search, to the outfile.  If the function encounters multiple spaces in the same scenario, it writes the English character followed by a space.

#### buildDict (morseTable)
* Parameter: a file containing the key-value pairs.
* Pseudocode: buildDict constructs a dictionary with English characters as its keys and sequences of Morse code as its values.

#### englishToMorse (table, infile, outfile)
* Parameters: a dictionary with English character keys and Morse sequences for values, a read file, and a write file.
* englishToMorse reads lines from the the read file.  If it encounters a space, it writes a space to the out file.  If it encounters a character, it looks up the appropriate Morse sequence in the table and writes it to the out file, followed by a space.  It ignores newline characters.  We thought the decision to ignore newline characters in this function as well as morseToEnglish, and to even avoid replacing them with a space in the test files, was justified because the files can in principle be translated correctly using our scheme; this can be seen in the lone test file we created.

#### userInterface ()
* Pseudocode: userInterface prompts the user for the type of translation required, and for valid read and write files, until correct input is provided.  The user can continue translating files until a sentinal value is entered.

## Enhancement

We selected support for capital letters as our enhancement.  Unfortunately, there is no other way to do this other than to provide a unique signature for each captial letter.  The unique key-value pairs needed to support this operation could be loaded into the look-up table, MorseTable.txt.  Then, they would be stored in the binary search tree and the English-to-Morse-code dictionary.  From there, capital letters could be translated from Morse code to English, and vice-versa.

