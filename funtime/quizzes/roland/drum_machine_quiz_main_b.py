#drum_machine_main.py
#Runs the quiz

import drum_machine_quiz_build

class Quizzee:
	def __init__(self, choices):
		self.totals = []
		for c in range(0, choices):
			self.totals.append(0)

questions = [] #will contain a list of Question objects

def main():
	choices = 5 #the number of possible outcomes of the test, or the number of options to be provided to match each question
	drum_machine_quiz_build.main(questions)
	user = Quizzee(choices) #creates means of keeping score
	promptstr = "\n\nType 'help' and then press Enter to learn how to take this quiz, type 'history' to learn a little bit about drum machines, or just press Enter to skip the lessons."

	firstblood = input("\nWHICH CLASSIC ROLAND DRUM MACHINE ARE YOU?\n\nA scientifically rigorous personality test by Andrew Rose\n\nIf you've never taken this test before, type 'help' and then press Enter to learn about this quiz. If you'd like to learn a little about drum machines, say 'history' instead. Or, if you're ready to go, hit Enter to skip the lessons.\n")
	while(not (firstblood=="")):
		if (firstblood=="help"):
			print("\nOver the course of this quiz, you will be presented with a series of questions followed by a selection of answers. To choose an answer, enter its corresponding number, which will be displayed to the left of the answer.{}".format(promptstr))

		elif (firstblood=="history"):
			print("\nWelcome to the wonderful world of drum machines! These electronic musical instruments have been around since the 1960s, coming into their own over the 1970s before exploding into popular music over the 1980s. Their synthetic sounds have left an indelible mark upon our culture... and the almighty Roland Corporation created many of the most important ones! In particular, this test will match you with the one of these five Roland drum machines which best reflects your personality...\n\nFirst up, the CR-78 was released in 1978. Descended from boxes designed to be bolted to the undersides of organ keyboards, this machine has a distinctly delicate character that makes it poorly suited to dance music. Instead, the CR-78 was often put to work in tandem with a human drummer, as was done by the likes of Phil Collins and Blondie.\n\nNext, the lovely TR-606 \"Drumatix\" was released in 1981 alongside its sister, the TB-303 bass synthesizer. The two devices were originally intended for sale to musicians who wanted drum and bass accompaniment to practice along to, but the burdgeoning world of electronic music saw far greater potential in both. The 303 singlehandedly birthed the musical genre of acid house, while the 606, adorable both in appearance and in sonic character, has been heard in too many musical contexts to list.\n\nThe TR-707 is the only fully digital box on this list. Introduced in 1984, early sample-based machines such as these are responsible for the distinctively artificial feel of '80s pop percussion. Why? Because despite the fact that they work by replaying recordings of real drum hits, the technological limitations of these machines combine with their mechanical precision to prevent them from ever quite passing for human.\n\nThe TR-808, released in 1980, is hailed by some as the greatest drum machine ever built. Why? Aside from its enormous impact upon house, techno, and hip-hop, the 808 is commmonly heard in radio hits even today, and its long, booming kick drum is the reason that trap music exists. Brash yet versatile, the cultural impact of the 808 is hard to overstate. It is most strongly associated with hip-hop, however.\n\nFinally, the TR-909 was released in 1983 as a successor to the 808. At a time when the falling price of computer memory was making digital drum machines ever more capable and affordable, the 909 was an analog holdout... mostly. While the majority of its sounds are synthetic, its cymbals and hi-hats are digital samples. Its sound is inseparable from that of house music, and without the 909, it is doubtful whether the genre would ever have come into being.\n\nFinally, in case you were wondering, 'CR', 'TR', and 'TB' stand for 'CompuRhythm', 'Transistor Rhythm', and 'Transistor Bass', respectively.{}".format(promptstr))

		else:
			firstblood = input("\nInvalid input. {}".format(promptstr))

		firstblood = input()

	for q in questions:
		in_num = -1
		optnum = 0 #used to number the options for the reader's convenience
		bungled = False #tracks whether an invalid input has been given for this question
		print("\n{}".format(q.q_text))
		for a in q.a_list:
			optnum += 1
			print("{}) {}".format(optnum,a))
		while (in_num <= 0 or in_num > choices): #while the input number does not correspond to a legitimate answer
			try:
				if not bungled:
					in_num = int(input())
				else:
					in_num = int(input("Invalid input. Enter a number between 1 and {}.".format(choices)))
				if (in_num <= 0 or in_num > choices):
					bungled = True
			except:
				bungled = True
				in_num = -1
		user.totals[in_num-1] += 1 #increment the number of answers of the relevant category



	#for t in user.totals:
	#	print(t)

	


if __name__ == "__main__":
	main()
