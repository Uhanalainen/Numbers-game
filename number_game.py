# # # # # # # # # # # # # # # # # #
#         The number game         #
#                                 #
# Rules: Enter a positive integer #
#                                 #
# Add the reversed version of the #
# same integer to the initial one #
#                                 #
#   If the number reads the same  #
# when reading from front to back #
#   and back to front, you lose   #
#                                 #
# Otherwise, repeat the addition  #
#                                 #
#   The longer you get to keep    #
#        going, the better        #
#                                 #
# # # # # # # # # # # # # # # # # #

def calculate(num):
	if not isinstance(num, int):
		raise ValueError

	if num < 10:
		return "The number should have at least two digits"