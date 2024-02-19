###############################################################

# Aufgabe 8-9


# def send_messages(unsorted_messages, sorted_messages):
#     while unsorted_messages:
#         current_message = unsorted_messages.pop()
#         print(f"\nHier ist die message: {current_message}!")
#         sorted_messages.append(current_message)


# unsorted_messages = ["hello!", "Buy", "Nice day!"]
# sorted_messages = []
# send_messages(unsorted_messages, sorted_messages)

# Output:
# Hier ist die message: Nice day!!

# Hier ist die message: Buy!

# Hier ist die message: hello!!

################################################################

# Aufgabe 8-10


# def send_messages(unsorted_messages, sorted_messages):
#     while unsorted_messages:
#         current_message = unsorted_messages.pop()
#         print(f"\nHier ist die message: {current_message}!")
#         sorted_messages.append(current_message)


# def sent_messages(sorted_messages):
#     for message in sorted_messages:
#         print(f"\nHier wurde die message: {message}! - gesendet!")


# unsorted_messages = ["hello!", "Buy", "Nice day"]
# sorted_messages = []
# send_messages(unsorted_messages, sorted_messages)
# sent_messages(sorted_messages)

# # Output:
# # Hier ist die message: Nice day!!

# # Hier ist die message: Buy!

# # Hier ist die message: hello!!

# # Hier wurde die message: Nice day!! - gesendet!

# # Hier wurde die message: Buy! - gesendet!


################################################################
# Aufgabe 8-11


# def send_messages(unsorted_messages, sorted_messages):
#     while unsorted_messages:
#         current_message = unsorted_messages.pop()
#         print(f"\nHier ist die message: {current_message}!")
#         sorted_messages.append(current_message)


# def sent_messages(sorted_messages):
#     for message in sorted_messages:
#         print(f"\nHier wurde die message: {message}! - gesendet!")


# unsorted_messages = ["hello", "Buy", "Nice day"]
# sorted_messages = []
# send_messages(unsorted_messages[:], sorted_messages)
# sent_messages(sorted_messages)
# print(f"\nOriginal list: {unsorted_messages}")

# # `output:
# # Hier ist die message: Nice day!

# # Hier ist die message: Buy!

# # Hier ist die message: hello!

# # Hier wurde die message: Nice day! - gesendet!

# # Hier wurde die message: Buy! - gesendet!

# # Hier wurde die message: hello! - gesendet!

# # Original list: ['hello', 'Buy', 'Nice day']`
