# Die Funktion input!

# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)

# # Output:
# # Tell me something, and I will repeat it back to you:Hello mister!
# # Hello mister!

########################################################################
# Programmbeending durch den Benutzer

prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != "quit":
    message = input(prompt)
    print(message)

# # Output:
# # Tell me something, and I will repeat it back to you:
# # Enter 'quit' to end the program. Hello everyone
# # Hello everyone

# # Tell me something, and I will repeat it back to you:
# # Enter 'quit' to end the program. Hello again
# # Hello again

# # Tell me something, and I will repeat it back to you:
# # Enter 'quit' to end the program. quit
# # quit

########################################################################
# Programmbeending durch den Benutzer

# prompt = "\nTell me something, and I will repeat it back to you: "
# prompt += "\nEnter 'quit' to end the program. "
# message = ""
# while message != "quit":
#     message = input(prompt)

#     if message != "quit":
#         print(message)

# # Outtput:
# # Tell me something, and I will repeat it back to you:
# # Enter 'quit' to end the program. Hello
# # Hello

# # Tell me something, and I will repeat it back to you:
# # Enter 'quit' to end the program. Hello again
# # Hello again

# # Tell me something, and I will repeat it back to you:
# # Enter 'quit' to end the program. quit
# # quit

# # Tell me something, and I will repeat it back to you:
# # Enter 'quit' to end the program.


########################################################################

# Flag

# prompt = "\nTell me something, and I will repeat it back to you: "
# prompt += "\nEnter 'quit' to end the program. "
# active = True

# while active:
#     message = input(prompt)

#     if message != "quit":
#         active = False
#     else:
#         print(message)

# # Output:
# # Tell me something, and I will repeat it back to you:
# # Enter 'quit' to end the program. Hello mister
# # Hello mister

# # Tell me something, and I will repeat it back to you:
# # Enter 'quit' to end the program. Hello mister agian
# # Hello mister agian

# # Tell me something, and I will repeat it back to you:
# # Enter 'quit' to end the program. quit
