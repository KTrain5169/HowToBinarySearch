var1 = 0

print("What is binary searching?\nBinary search is a type of search that can be much quicker than searching one by one.\n")

print("Suppose you are trying to find an issue caused by Minecraft mods.\nIn this case, the process is as follows:")
print("1. Try running without any mods. If this does not fix, it's likely an issue with the game itself.")
print("2. If the game works, add back as close to half of the mods you had, and test for the issue.\n-> If the game works as intended, swap to the other half and test for the issue.\n|-> If the issue still exists, halve your mod count and test again.\n-> If the game still exhibits the error, halve your mod count again.")
print("3. Keep repeating step 2 until you find the mods causing the issue.\n")

needhelp = input(str("Do you still need help performing a binary search? "))
if needhelp.lower() == "yes":
    print("OK! Let's start. Tell me what your issue is and I'll repeat that to you every step.")
    issue = input("What's your issue? ")
    print('Ok, set your issue to ', issue, '".')
    print("So let's start!")
    
    
elif needhelp.lower() == "no":
    print("Alright, I'll leave you to it.")
    print("Once you're done, type EXIT to close this window.")
    abort = input(str("Type EXIT to abort. "))
    if abort.upper() == "EXIT":
        exit()
else:
    print("Uh... can't understand you.")
    abort = input(str("Type EXIT to abort. "))
    if abort.upper() == "EXIT":
        exit()
