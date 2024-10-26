#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open('./Input/Names/invited_names.txt','r') as fi:
    arr=fi.readlines()
with open('./Input/Letters/starting_letter.txt','r') as fi:
    con=fi.read()
print(con)
for i in arr:
    ai=i.strip()
    con1=con.replace('[name]',ai)
    with open(f"invitation_for_{ai}",mode='w') as wi:
        wi.write(con1)
