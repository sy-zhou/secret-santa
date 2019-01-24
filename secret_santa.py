## ======================================
##  Secret Santa Name Generator
##  Sally Zhou 01.19
## ======================================

import os.path
import random

# constants
INTRO_PROGRAM_MESSAGE = \
"-----------------------------------\n\
>>> Secret Santa Name Generator <<<\n\
-----------------------------------\n\
Welcome! Choose one of the following options to get started:\n\
 1: Import a list of names from a text file.\n\
 2: Enter names directly."
INVALID_CHOICE_MESSAGE = "Invalid choice. Please enter again."
INVALID_FILE_MESSAGE = "Invalid file name. Please enter again."
CHOICE_FILE_MESSAGE = \
"\nYou have chosen to enter names from a text file.\n\
Note that your file must be formatted with one name on each line and\n\
that the file must be stored in the same folder as this program.\n\
If someone is to be excluded from being a recipient to a certain person,\n\
please ensure the excluded recipient's name is written after a space on\n\
the same line after the name of the person.\n\
(e.g. > Amy Bob ; means Amy is guaranteed to not be Bob's Secret Santa))"
CHOICE_DIRECT_MESSAGE = \
"\nYou have chosen to enter names directly.\n\
Proceed to enter the names of the people in your Secret Santa group.\n\
If someone is to be excluded from being a recipient to a certain person,\n\
please enter the excluded recipient's name after a space on the same\n\
line after you have entered the name of the person.\n\
(e.g. > Amy Bob ; means Amy is guaranteed to not be Bob's Secret Santa)\n\
Enter 'x' to indicate that all participants have been entered."
MATCHED_MESSAGE = \
"\nEach person has been matched! Choose one of the following:\n\
 1: Save matches to a text file.\n\
 2: Display matches here directly."
CHOICE_FILE_WRITE_MESSAGE = "\nYou have chosen to save the matches in a text file."
CHOICE_DIRECT_WRITE_MESSAGE = "\nYou have chosen to display matches directly."
CHOICE_FILE = "1"
CHOICE_DIRECT = "2"
FLAG_ALL_PARTICIPANTS_ENTERED = "x"


def main():
    print(INTRO_PROGRAM_MESSAGE)
    choice = get_choice()
    participants, possible_pairs = input_names(choice)
    if len(participants) > 1:
        final_pairing = match_all(participants, possible_pairs, [])
        # after match
        print(MATCHED_MESSAGE)
        choice = get_choice()
        output_match(choice, participants, final_pairing)
    else:
        print("\nA match cannot be made with one person.")
    print("\nThanks for using the Secret Santa name generator!")


def get_choice():
    """
    Get the choice of the user from input and ensure the choice is valid.

    Returns:
        a String indicating the preference of the user
    """
    valid_response = False
    choice = ""
    while not valid_response:
        choice = input(">>> ")
        if choice == CHOICE_FILE or choice == CHOICE_DIRECT:
            valid_response = True
        else: print(INVALID_CHOICE_MESSAGE)
    return choice


def get_file_name(prompt):
    '''
    Get a file name as input from user and ensure the file exists.

    Args:
        prompt (Str): a short message indicating what kind of file the program
            wants from the user

    Returns:
        a String representing the file name
    '''
    print(prompt)
    file_name = ""
    while True:
        file_name = input(">>> ")
        if file_name.lower().endswith('.txt') and os.path.isfile(file_name):
            break
        else:
            print(INVALID_FILE_MESSAGE)
    return file_name


def input_names(choice):
    '''
    Input participants' names into program and initialize them for matching.

    Args:
        choice (Str): an indicator of how the user wants to input names

    Returns:
        a list of participants' names and a list of the possible pairings
            corresponding to each participant
    '''
    participants = []
    excluded_names = []
    possible_pairs = []

    # names are entered into program and stored
    if choice == CHOICE_FILE:
        print(CHOICE_FILE_MESSAGE)
        file_name = get_file_name("Enter the name of your text file (e.g. names.txt)")
        file = open(file_name, "r")
        for line in file:
            names = line.strip().split()
            participants.append(names[0])
            excluded_names.append(names[1:])
        file.close()
    elif choice == CHOICE_DIRECT:
        print(CHOICE_DIRECT_MESSAGE)
        response = ""
        while True:
            response = input("> ")
            if response == FLAG_ALL_PARTICIPANTS_ENTERED:
                break
            else:
                names = response.split()
                participants.append(names[0])
                excluded_names.append(names[1:])

    # randomizing names and creating lists of possible pairings for each name
    random.shuffle(participants)

    for index in range(len(participants)):
        a = [x for x in participants if x != participants[index] and \
             x not in excluded_names[index]]
        random.shuffle(a)
        possible_pairs.append(a)

    return participants, possible_pairs


def match_all(participants, possible_pairs, matches):
    """
    Match each person in participants with another participant, where
    possible matches are stored in possible_pairs.
    
    Args:
        participants (listof Str): a list of names of those participating
        possible_pairs (listof (listof Str)): a list of lists of names which could
            be matched with the corresponding name in participants (i.e. the element
            in the same index), excluding indicated exceptions of names
        matches (listof Str): a list of matches made so far
        
    Returns:
        a list of str where each element is the name for whom each 
            element in participants must bring a gift for
    """
    if participants == []: return matches
    else:
        for name in possible_pairs[0]:
            result = []
            if name not in matches:
                result = match_all(participants[1:], possible_pairs[1:],\
                                   matches + [name])
            if result != []: return result
        return []


def output_match(choice, participants, final_pairing):
    """
    Output the match result to the user through console or into a text file.
    
    Args:
        choice (Str): an indicator of how to output the match results
        participants (listof Str): a list of names of those participating
        final_pairing (listof Str): a list of names of matches corresponding
            to each element in participants
    """
    if choice == CHOICE_FILE:
        print(CHOICE_FILE_WRITE_MESSAGE)
        file_name = get_file_name("Enter the name of the new file (e.g. names.txt)")
        file = open(file_name, "w")
        for i in range(len(participants)):
            file.write(participants[i] + " -> " + final_pairing[i] + "\n")
        print("The matches have been saved to", file_name)
        file.close()
    elif choice == CHOICE_DIRECT:
        print(CHOICE_DIRECT_WRITE_MESSAGE)
        for i in range(len(participants)):
            print(participants[i] + " -> " + final_pairing[i])


# ------------------------------------------
if __name__ == "__main__":
    main()
