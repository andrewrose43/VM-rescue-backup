#drum_machine_build.py
#Generates the list of questions that the quizzee is asked

class Question:
	"""A class containing one quiz question, consisting of a question and a set of answers sorted by category."""
	
	def __init__(self, q_txt, a_li):
		self.q_text = q_txt
		self.a_list = a_li

	def get_ans(self, n):
		return self.a_list[n-1] #so feed this answers numbered beginning at 1, not zero

	def get_num_ans():
		return len(self.a_list)

def main(questions):
	
	#questions = [] #the big ol list of all the questions & answers supplied to the quizzee

	tmpli = ["Critic", "Restauranteur", "Programmer", "Celebrity", "Firefighter"]
	addquestion(questions, "What job would you like to have?", tmpli)

	tmpli = ["Class", "Smiles", "Brainpower", "Booty", "Honesty"]
	addquestion(questions, "What do you find most attractive?", tmpli)

	tmpli = ["Skating", "Ice Cream", "Gaming", "Clubbing", "Concerts"]
	addquestion(questions, "What is your favourite thing to do with a significant other?", tmpli)

def addquestion(q_list, q_text, a_list): #makes a Question object and appends it to questions
	q_list.append(Question(q_text, a_list))
