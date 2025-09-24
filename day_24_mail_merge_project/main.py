#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# Get the letter value
def original_letter():
    with open("./Input/Letters/starting_letter.txt", mode="r") as f:
        return f.read()

# Get all names from the file and store them
def get_names(names):
    f = open("./Input/Names/invited_names.txt", mode="r")
    for line in f:
        for word in line.split():
            names.append(word)
    f.close()

list_names = []
get_names(list_names)
letter = original_letter()

for name in list_names:
    new_letter = letter.replace("[name]",name)
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as f:
        f.write(new_letter)

