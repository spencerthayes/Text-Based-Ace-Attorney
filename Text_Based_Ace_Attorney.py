from time import sleep
from nocasedict import NocaseDict
from random import randint
tGreen =  '\033[32m'
tBlue = '\u001b[38;5;75m'
tYellow = '\u001b[38;5;220m'
tRed = '\u001b[31m'
testimonyOp = '\u001b[38;5;21mWitness Testimony'
crossExaminationOp = '\033[32mCross Examination'
endTextColour = '\033[m'
evidence = NocaseDict({"Attorney's Badge": "No one would believe I was a defense attorney if I didn't carry this.", "Cindy's Autopsy Report": "Time of death: 7/31, 4PM-5PM. Cause of death: loss of blood due to blunt trauma."})
profiles = NocaseDict({"Mia Fey": "Age: 27, Gender: Female, Chief Attorney at Fey & Co.. My boss, and a very good defense attorney.", "Larry Butz": "Age: 23, Gender: Male, The defendant in this case. A likeable guy who was my friend in grade school.", "Cindy Stone": "Age: 22, Gender: Female, The victim in this case. A model, she lived in an apartment by herself."})
showProfiles = 0
canViewCourtRecord = 0
userChoice = ' '
health = 5
presentedItem = '''Put something in here that won't appear in your evidence or profile list'''

def dialogue(str):
	global userChoice
	while userChoice != '':
		userChoice = input(str)
		print(endTextColour + ' ')
	
		while userChoice.lower() == 'court record' and canViewCourtRecord == 1:
			sleep(.1)
			print(' ')
			print(list(evidence.keys()))
			print(' ')
			sleep(.5)
			courtRecordInput = input("Type the name of the evidence you would like more info on here (type profiles if you want to see the list of profiles or exit if you want to exit): ")
			capitalizedMessage = " ".join([
	   			word.capitalize()
	  			 for word in courtRecordInput.split(" ")
			])
			print(' ')
		
			if courtRecordInput.lower() == 'profiles':
				showProfiles = 1
			
				while showProfiles == 1:
					sleep(.1)
					print(' ')
					print(list(profiles.keys()))
					print(' ')
					sleep(.5)
					courtRecordInput = input("Type the name of the person you would like more info on here (type evidence if you want to see the list of evidence or exit if you want to exit): ")
				
					capitalizedMessage = " ".join([
	   					word.capitalize()
	  					 for word in courtRecordInput.split(" ")
					])
					print(' ')
		
					if capitalizedMessage in list(profiles.keys()):
						print(capitalizedMessage + ': ' + profiles[courtRecordInput])
						print(' ')
			
					elif courtRecordInput.lower() == 'exit':
						print(endTextColour + ' ')
						userChoice = ' '
						showProfiles = 0
						continue
			
					elif courtRecordInput.lower() == 'evidence':
						showProfiles = 0
						continue
				
					else:
						print('Invalid Profile')
				
			elif capitalizedMessage in list(evidence.keys()):
				print(capitalizedMessage + ': ' + evidence[courtRecordInput])
				print(' ')
			
			elif courtRecordInput.lower() == 'exit':
				print(endTextColour + ' ')
				userChoice = ' '
			
			else:
				print('Invalid Evidence')
	userChoice = ' '
	
def crossExaminationStatement(str):
	global userChoice
	userChoice = input(str)
	print(endTextColour + ' ')
	
	while userChoice.lower() == 'present' or userChoice.lower() == 'court record':
		sleep(.1)
		print(' ')
		print(list(evidence.keys()))
		print(' ')
		sleep(.5)
		courtRecordInput = input("Type the name of the evidence you would like more info on here (type profiles if you want to see the list of profiles or exit if you want to exit): ")
		capitalizedMessage = " ".join([
   			word.capitalize()
  			 for word in courtRecordInput.split(" ")
		])
		print(' ')
		
		if courtRecordInput.lower() == 'profiles':
			showProfiles = 1
			
			while showProfiles == 1:
				sleep(.1)
				print(' ')
				print(list(profiles.keys()))
				print(' ')
				sleep(.5)
				courtRecordInput = input("Type the name of the person you would like more info on here (type evidence if you want to see the list of evidence or exit if you want to exit): ")
				
				capitalizedMessage = " ".join([
   					word.capitalize()
  					 for word in courtRecordInput.split(" ")
				])
				print(' ')
		
				if capitalizedMessage in list(profiles.keys()):
					print(capitalizedMessage + ': ' + profiles[courtRecordInput])
					print(' ')
					presentQuestion = input("Would you like to present this evidence? (yes or no) ")
					if presentQuestion.lower() == 'y' or presentQuestion.lower() == 'yes':
						global presentedItem
						presentedItem = capitalizedMessage
						print(' ')
						userChoice = ' '
					else:
						pass
			
				elif courtRecordInput.lower() == 'exit':
					userChoice = ' '
					showProfiles = 0
					continue
			
				elif courtRecordInput.lower() == 'evidence':
					showProfiles = 0
					continue
				
				else:
					print('Invalid Profile')
				
		elif capitalizedMessage in list(evidence.keys()):
			print(capitalizedMessage + ': ' + evidence[courtRecordInput])
			print(' ')
			sleep(.2)
			presentQuestion = input("Would you like to present this evidence? (yes or no) ")
			if presentQuestion.lower() == 'y' or presentQuestion.lower() == 'yes':
				presentedItem = capitalizedMessage
				print(' ')
				userChoice = ' '
			else:
				pass
			
		elif courtRecordInput.lower() == 'exit':
			userChoice = ' '
			
		else:
			print('Invalid Evidence')
			
	global crossExaminationPosition
	if userChoice == '<<' or userChoice.lower() == 'back' and crossExaminationPosition > 1:
		crossExaminationPosition = crossExaminationPosition - 1
	else:
		crossExaminationPosition = crossExaminationPosition + 1

def penalty():
	global health
	health = health - 1
	if health < 1:
		print('*Gavel Slam*')
		sleep(.25)
		print(' ')
		print('Judge:')
		dialogue("That's enough! \u001b[38;5;220m >> ")
		dialogue("This court see no reason to further prolong the trial. \u001b[38;5;220m >> ")
		dialogue("The defense has failed to give the court sufficient reason to doubt the prosecution's claim. \u001b[38;5;220m >> ")
		dialogue("This court find the defendant, Mr. Larry Butz… \u001b[38;5;220m >> ")
		sleep(.5)
		print(' ')
		print('Guilty')
		print(' ')
		print(' ')
		sleep(.5)
		dialogue("The accused will surrender to the court immediately, to be held pending trial at a higher court within a month from today's date. \u001b[38;5;220m >> ")
		print("That is all. This court is adjourned!")
		sleep(.25)
		print('*Gavel Slam*')
		quit()
        
def wrongEvidence():
	wrongEvidenceRNG = randint(1, 4)
	if wrongEvidenceRNG == 1:
		print('Phoenix:')
		print("""Objection!""")
		print(' ')
		sleep(.5)
		dialogue("Your Honor! \u001b[38;5;220m >> ")
		dialogue("That statement contradicts this evidence! \u001b[38;5;220m >> ")
		
		print('Judge:')
		dialogue("…? \u001b[38;5;220m >> ")
		dialogue("It does? \u001b[38;5;220m >> ")
		dialogue("I don't see anything contradictory. \u001b[38;5;220m >> ")
		
		print('Phoenix:')
		dialogue("Huh? Really? \u001b[38;5;220m >> ")
		
		print('Judge:')
		dialogue("Objection overruled. \u001b[38;5;220m >> ")
		dialogue("Try to think before you make accusations, Mr. Wright! \u001b[38;5;220m >> ")
		
		print('Phoenix:')
		dialogue(tBlue + "(Whoops! That didn't go so well.) \u001b[38;5;220m >> ")
		
	elif wrongEvidenceRNG == 2:
		print('Phoenix:')
		print("""Objection!""")
		print(' ')
		sleep(.5)
		dialogue("Your Honor! \u001b[38;5;220m >> ")
		dialogue("What do you think about the witness's statement? \u001b[38;5;220m >> ")
		
		print('Judge:')
		dialogue("Uh… I'm not sure I follow? \u001b[38;5;220m >> ")
		
		print('Phoenix:')
		dialogue("It clearly, er, contradicts the… um… I thought… \u001b[38;5;220m >> ")
		
		print('Judge:')
		dialogue("You don't sound very convinced, Mr. Wright. Objection overruled. \u001b[38;5;220m >> ")
		
		print('Phoenix:')
		dialogue(tBlue + "(I don't think that won me any points with the judge…) \u001b[38;5;220m >> ")
		
	elif wrongEvidenceRNG == 3:
		print('Phoenix:')
		print("""Objection!""")
		print(' ')
		sleep(.5)
		dialogue("This evidence clearly reveals the contradiction in that statement, Your Honor! \u001b[38;5;220m >> ")
		
		print('Judge:')
		dialogue("How exactly are that evidence and the statement just now related…? \u001b[38;5;220m >> ")
		
		print('Phoenix:')
		dialogue("They aren't, are they… \u001b[38;5;220m >> ")
		
		print('Judge:')
		dialogue("Not at all. \u001b[38;5;220m >> ")
		dialogue("Mr. Wright, please think the facts over before making accusations. \u001b[38;5;220m >> ")
		
		print('Phoenix:')
		dialogue(tBlue + "(I don't think that won me any points with the judge…) \u001b[38;5;220m >> ")
		
	elif wrongEvidenceRNG == 4:
		print('Phoenix:')
		print("""Objection!""")
		print(' ')
		sleep(.5)
		dialogue("The witness's statement is clearly faulty, Your Honor! \u001b[38;5;220m >> ")
		
		print('Judge:')
		dialogue("… I'm sorry, but I can see nothing faulty. \u001b[38;5;220m >> ")
		dialogue("Unfortunately, I will have to penalize you, Mr. Wright. \u001b[38;5;220m >> ")
		
		print('Phoenix')
		dialogue(tBlue + "(Ugh. I must be on the wrong track?) \u001b[38;5;220m >> ")
	penalty()
	global presentedItem
	presentedItem = '''Put something in here that won't appear in your evidence or profile list'''
	
def presentEvidence():
	global userChoice
	userChoice = 'present'
	print(endTextColour + ' ')
	
	while userChoice.lower() == 'present' or userChoice.lower() == 'court record':
		sleep(.1)
		print(' ')
		print(list(evidence.keys()))
		print(' ')
		sleep(.5)
		courtRecordInput = input("Type the name of the evidence you would like more info on here (type profiles if you want to see the list of profiles): ")
		capitalizedMessage = " ".join([
   			word.capitalize()
  			 for word in courtRecordInput.split(" ")
		])
		print(' ')
		
		if courtRecordInput.lower() == 'profiles':
			showProfiles = 1
			
			while showProfiles == 1:
				sleep(.1)
				print(' ')
				print(list(profiles.keys()))
				print(' ')
				sleep(.5)
				courtRecordInput = input("Type the name of the person you would like more info on here (type evidence if you want to see the list of evidence): ")
				
				capitalizedMessage = " ".join([
   					word.capitalize()
  					 for word in courtRecordInput.split(" ")
				])
				print(' ')
		
				if capitalizedMessage in list(profiles.keys()):
					print(capitalizedMessage + ': ' + profiles[courtRecordInput])
					print(' ')
					presentQuestion = input("Would you like to present this evidence? (yes or no) ")
					if presentQuestion.lower() == 'y' or presentQuestion.lower() == 'yes':
						global presentedItem
						presentedItem = capitalizedMessage
						print(' ')
						userChoice = ' '
					else:
						pass
			
				elif courtRecordInput.lower() == 'evidence':
					showProfiles = 0
					continue
				
				else:
					print('Invalid Profile')
				
		elif capitalizedMessage in list(evidence.keys()):
			print(capitalizedMessage + ': ' + evidence[courtRecordInput])
			print(' ')
			sleep(.2)
			presentQuestion = input("Would you like to present this evidence? (yes or no) ")
			if presentQuestion.lower() == 'y' or presentQuestion.lower() == 'yes':
				presentedItem = capitalizedMessage
				print(' ')
				userChoice = ' '
			else:
				pass
			
		else:
			print('Invalid Evidence')
		
dialogue(tGreen + "Date: August 3, 9:47 AM, District Court, Defendant Lobby No.2 \u001b[38;5;220m >> ")
canViewCourtRecord = 1

print('Phoenix:')
dialogue(tBlue + "(Boy am I nervous!) \u001b[38;5;220m >> ")

print('Mia:')
dialogue("Wright! \u001b[38;5;220m >> ")

print('Pheonix:')
dialogue("Oh, h-hiya, Chief. \u001b[38;5;220m >> ")

print('Mia:')
dialogue("Whew, I'm glad I made it on time. \u001b[38;5;220m >> ")
dialogue("Well, I have to say Phoenix, I'm impressed! \u001b[38;5;220m >> ")
dialogue("Not everyone takes on a murder trial right off the bat like this. \u001b[38;5;220m >> ")
dialogue("It says a lot about you… and your client as well. \u001b[38;5;220m >> ")

print('Phoenix:')
dialogue("Um… thanks. \u001b[38;5;220m >> ")
dialogue("Actually, it's because I owe him a favor. \u001b[38;5;220m >> ")

print('Mia:')
dialogue("A favor? \u001b[38;5;220m >> ")
dialogue("You mean, you knew the defendant before this case? \u001b[38;5;220m >> ")

print('Phoenix:')
dialogue("Yes. \u001b[38;5;220m >> ")
dialogue("Actually, I kind of owe my current job to him. \u001b[38;5;220m >> ")
dialogue("He's one of the reasons I became an attorney. \u001b[38;5;220m >> ")

print('Mia:')
dialogue("Well, that's news to me! \u001b[38;5;220m >> ")

print('Phoenix:')
dialogue("I want to help him out any way I can! \u001b[38;5;220m >> ")
dialogue("I just… really want to help him, I owe him that much. \u001b[38;5;220m >> ")

print('???:')
dialogue(tGreen + "(It's over!) \u001b[38;5;220m >> ")
dialogue(tGreen + "(My life, everything, it's all over!) \u001b[38;5;220m >> ")

print('Mia:')
dialogue("… Isn't that your client screaming over there? \u001b[38;5;220m >> ")

print('Phoenix:')
dialogue("Yeah… that's him. \u001b[38;5;220m >> ")

print('???:')
dialogue(tGreen + "(Death! Despair! Ohhhh!) \u001b[38;5;220m >> ")
dialogue(tGreen + "(I'm gonna do it, I'm gonna die!!!) \u001b[38;5;220m >> ")

print('Mia:')
dialogue("It sounds like he wants to die… \u001b[38;5;220m >> ")

print('Phoenix:')
dialogue("Um, yeah. *sigh* \u001b[38;5;220m >> ")

print('Butz:')
dialogue("Nick!!! \u001b[38;5;220m >> ")

print('Phoenix:')
dialogue("Hey. \u001b[38;5;220m >> ")
dialogue("Hey there, Larry. \u001b[38;5;220m >> ")

print('Butz:')
dialogue("Dude, I'm so guilty!! Tell them I'm guilty!!! \u001b[38;5;220m >> ")
dialogue("Gimme the death sentence! I ain't afraid to die! \u001b[38;5;220m >> ")

print('Phoenix:')
dialogue("What!? What's wrong, Larry? \u001b[38;5;220m >> ")
  
print('Butz:')
dialogue("Oh, it's all over… I… I'm finished. Finished! \u001b[38;5;220m >> ")
dialogue("I can't live in a world without her! I can't! \u001b[38;5;220m >> ")
dialogue("Who… who took her away from me, Nick? Who did this!? \u001b[38;5;220m >> ")
dialogue("Aww, Nick, ya gotta tell me! Who took my baby away!? \u001b[38;5;220m >> ")

print('Phoenix:')
dialogue(tBlue + "(Hmm… The person responsible for your girlfriend's death?) \u001b[38;5;220m >> ")
dialogue(tBlue + "(The newspapers say it was \u001b[31myou\u001b[38;5;75m…) \u001b[38;5;220m >> ")

print('.')
sleep(1)
print('.')
sleep(1)
print('.')
sleep(0.5)

print('Phoenix:')
dialogue("My name is Phoenix Wright. \u001b[38;5;220m >> ")
dialogue("Here's the story: \u001b[38;5;220m >> ")
dialogue("My first case is a fairly simple one. \u001b[38;5;220m >> ")
dialogue("A young woman was killed in her apartment. \u001b[38;5;220m >> ")
dialogue("The guy they arrested was the unlucky sap dating her: \u001b[38;5;220m >> ")
dialogue("Larry Butz… my best friend since grade school. \u001b[38;5;220m >> ")
dialogue("""Our school had a saying: "\u001b[31mWhen something smells, it's usually the Butz.\033[m" \u001b[38;5;220m >> """)
dialogue("In the 23 years I've known him, it's usually been true. \u001b[38;5;220m >> ")
dialogue("He has a knack for getting himself in trouble. \u001b[38;5;220m >> ")
dialogue("One thing I can say though: it's usually not his fault. \u001b[38;5;220m >> ")
dialogue("He just has terrible luck. \u001b[38;5;220m >> ")
dialogue("But I know better than anyone, that he's a good guy at heart. \u001b[38;5;220m >> ")
dialogue("That and I owe him one. \u001b[38;5;220m >> ")
dialogue("Which is why I took the case… to clear his name. \u001b[38;5;220m >> ")
dialogue("And that's just what I'm going to do! \u001b[38;5;220m >> ")
sleep(2.5)

canViewCourtRecord = 0
dialogue(tGreen + "August 3, 10:00 AM, District Court, Courtroom No. 2 \u001b[38;5;220m >> ")
canViewCourtRecord = 1

print("*Gavel Slam*")
print(' ')
sleep(.225)

print('Judge:')
dialogue("The court is now in session for the trial of Mr. Larry Butz. \u001b[38;5;220m >> ")

print('Payne:')
profiles['Winston Payne'] = 'Age: 52, Gender: Male, The prosecutor for this case. Lacks presence. Generally bad at getting his points across.'
dialogue("The prosecution is ready, Your Honor. \u001b[38;5;220m >> ")

print('Phoenix:')
dialogue("The, um, defense is ready, Your Honor. \u001b[38;5;220m >> ")

print('Judge:')
dialogue("Ahem. Mr. Wright? This is your first trial, is it not? \u001b[38;5;220m >> ")

print('Phoenix:')
dialogue("Y-Yes, Your Honor. I'm, um, a little nervous. \u001b[38;5;220m >> ")

print('Judge:')
dialogue("Your conduct during this trial will decide the fate of your client. \u001b[38;5;220m >> ")
dialogue("Murder is a serious charge. For your client's sake, I hope you can control your nerves. \u001b[38;5;220m >> ")

print('Phoenix:')
dialogue("Thank… thank you, Your Honor. \u001b[38;5;220m >> ")

print('Judge:')
dialogue("… Mr. Wright, given the circumstances… \u001b[38;5;220m >> ")
dialogue("I think we should have a test to ascertain your readiness. \u001b[38;5;220m >> ")

print('Phoenix:')
dialogue("Yes, Your Honor. \u001b[38;5;220m >> ")
dialogue(tBlue + "(Gulp… Hands shaking… Eyesight… fading…) \u001b[38;5;220m >> ")

print('Judge:')
dialogue("This test will consist of a few simple questions. Answer them clearly and concisely. \u001b[38;5;220m >> ")

questionAnswer = ' '
while questionAnswer.lower() != 'larry butz':
	dialogue("Please state the name of \u001b[31mthe defendant\033[m in this case. \u001b[38;5;220m >> ")
	print('1: Phoenix Wright')
	sleep(.5)
	print(' ')
	print('2: Larry Butz')
	sleep(.5)
	print(' ')
	print('3: Mia Fey')
	sleep(.5)
	print(' ')
	questionAnswer = input('Type your answer here: ')
	print(' ')
	
	if questionAnswer.lower() == 'phoenix wright' or questionAnswer == '1':
		print('Phoenix:')
		dialogue("Um… the defendant… is me, right? \u001b[38;5;220m >> ")
		
		print('Mia:')
		dialogue("Wright! Have you completely lost your mind? Focus! \u001b[38;5;220m >> ")
		dialogue("The defendant is the person on trial! \u001b[38;5;220m >> ")
		dialogue("You're his lawyer! \u001b[38;5;220m >> ")
		
		print('Phoenix:')
		dialogue("Um, er, eh? Oh yeah, right! Eh heh heh. \u001b[38;5;220m >> ")
		
		print('Mia:')
		dialogue("This is no laughing matter! \u001b[38;5;220m >> ")
		dialogue("You did pass the bar, didn't you? \u001b[38;5;220m >> ")
		
		print('Judge:')
		dialogue("Sorry, I couldn't hear your answer. I'll ask once more: \u001b[38;5;220m >> ")
		
	elif questionAnswer.lower() == 'mia fey' or questionAnswer == '3':
		print('Phoenix:')
		dialogue("The, um, defendant? That's… er… Mia Fey? \u001b[38;5;220m >> ")
		
		print('Mia:')
		dialogue("Wrong, Wright. Look, I have to leave. \u001b[38;5;220m >> ")
		dialogue("I have to go home. I'm… I'm expecting a delivery. \u001b[38;5;220m >> ")
		
		print('Phoenix:')
		dialogue("Aw, c'mon Chief. There's no need to be going so soon, is there? \u001b[38;5;220m >> ")
		
		print('Mia:')
		dialogue("Listen! Wright! \u001b[38;5;220m >> ")
		dialogue("The defendant is the one on trial--your client! \u001b[38;5;220m >> ")
		dialogue("I mean, that's about as basic as you can get! \u001b[38;5;220m >> ")
		
		print('Phoenix:')
		dialogue(tBlue + "(I've put my foot in it this time! I've got to relax!) \u001b[38;5;220m >> ")
		
		print('Judge:')
		dialogue("Sorry, I couldn't hear your answer. I'll ask once more: \u001b[38;5;220m >> ")
		
	elif questionAnswer == '2':
		questionAnswer = 'larry butz'
		
	else:
		print('Judge:')
		dialogue("Sorry, I couldn't hear your answer. I'll ask once more: \u001b[38;5;220m >> ")
		
print('Phoenix:')
dialogue("The defendant? Well, that's Larry Butz, Your Honor. \u001b[38;5;220m >> ")

print('Judge:')
dialogue("Correct. \u001b[38;5;220m >> ")
dialogue("Just keep your wits about you and you'll do fine. \u001b[38;5;220m >> ")
dialogue("Next question: \u001b[38;5;220m >> ")
dialogue("This is a murder trial. Tell me, what's the \u001b[31mvictim's name\033[m? \u001b[38;5;220m >> ")

print('Phoenix:')
dialogue(tBlue + "(Whew, I know this one! Glad I read the case report cover to cover so many times.) \u001b[38;5;220m >> ")
dialogue(tBlue + "(It's… wait… Uh-oh!) \u001b[38;5;220m >> ")
dialogue(tBlue + "(No… no way! I forgot! I'm drawing a total blank here!) \u001b[38;5;220m >> ")

print('Mia:')
dialogue("Phoenix! Are you absolutely SURE you're up to this? \u001b[38;5;220m >> ")
dialogue("You don't even know the victim's name!? \u001b[38;5;220m >> ")

print('Phoenix:')
dialogue("Oh, the victim! O-Of course I know the victim's name! \u001b[38;5;220m >> ")
dialogue("I, um, just forgot. … Temporarily. \u001b[38;5;220m >> ")

print('Mia:')
dialogue("I think I feel a migraine coming on. \u001b[38;5;220m >> ")
dialogue("Look, the victim's name is listed in the \u001b[31mCourt Record\033[m. \u001b[38;5;220m >> ")
dialogue("Just type \u001b[31mCourt Record\033[m to check it at anytime, okay? \u001b[38;5;220m >> ")
dialogue("Remember to check it often. Do it for me, please. I'm begging you. \u001b[38;5;220m >> ")

print('Judge:')

questionAnswer = ' '
while questionAnswer.lower() != 'cindy stone':
	dialogue("Mr. Wright. Who is the \u001b[31mvictim \033[min this case? \u001b[38;5;220m >> ")
	print('1: Mia Fey')
	sleep(.5)
	print(' ')
	print('2: Cinder Block')
	sleep(.5)
	print(' ')
	print('3: Cindy Stone')
	sleep(.5)
	print(' ')
	questionAnswer = input('Type your answer here: ')
	print(' ')
	
	if questionAnswer.lower() == 'mia fey' or questionAnswer == '1':
		print('Phoenix:')
		dialogue("Um… Mia Fey? \u001b[38;5;220m >> ")
		
		print('Mia:')
		dialogue("W-W-What!? How can I be the victim!? \u001b[38;5;220m >> ")
		
		print('Phoenix:')
		dialogue("Oh! Right! Sorry! \u001b[38;5;220m >> ")
		dialogue("I, er, it was the first name that popped into my head, and-- \u001b[38;5;220m >> ")
		
		print('Mia:')
		dialogue("The Court Record command! \u001b[38;5;220m >> ")
		dialogue("Remember to use it when you are in a pinch. \u001b[38;5;220m >> ")
		
		print('Judge:')
		dialogue("Let me ask that one again: \u001b[38;5;220m >> ")
		
	elif questionAnswer.lower() == 'cinder block' or questionAnswer == '2':
		print('Phoenix:')
		dialogue("Oh, um, wasn't it Ms. Block? \u001b[38;5;220m >> ")
		dialogue("Ms. Cinder Block? \u001b[38;5;220m >> ")
		
		print('Judge:')
		dialogue("The person in question was a victim of murder, not ill-conceived naming, Mr. Wright. \u001b[38;5;220m >> ")
		
		print('Mia:')
		dialogue("Wright? If you forget something, just type Court Record to help you remember. \u001b[38;5;220m >> ")
		dialogue("A mistake in court could cost you the case. \u001b[38;5;220m >> ")
		
		print('Judge:')
		dialogue("I ask you again: \u001b[38;5;220m >> ")
		
	elif questionAnswer == '3':
		questionAnswer = 'cindy stone'
		
	else:
		print('Judge:')
		dialogue("Sorry, I couldn't hear your answer. I'll ask once more: \u001b[38;5;220m >> ")
		
print('Phoenix:')
dialogue("Um… the victim's name is \u001b[38;5;75mCindy Stone\033[m. \u001b[38;5;220m >> ")

print('Judge:')
dialogue("Correct. \u001b[38;5;220m >> ")
dialogue("Now, tell me, what was the cause of death? \u001b[38;5;220m >> ")

questionAnswer = ' '
while questionAnswer.lower() != 'hit with a blunt object':
	dialogue("She died because she was…? \u001b[38;5;220m >> ")
	print('1: Poisoned')
	sleep(.5)
	print(' ')
	print('2: Hit with a blunt object')
	sleep(.5)
	print(' ')
	print('3: Strangled')
	sleep(.5)
	print(' ')
	questionAnswer = input('Type your answer here: ')
	print(' ')
	
	if questionAnswer.lower() == 'poisoned' or questionAnswer == '1':
		print('Phoenix:')
		dialogue("Oh, right! \u001b[38;5;220m >> ")
		dialogue("Wasn't she, um, poisoned by er… poison? \u001b[38;5;220m >> ")
		
		print('Judge:')
		dialogue("You're asking me!? \u001b[38;5;220m >> ")
		
		print('Phoenix:')
		dialogue("Um… Chief! Help me out! \u001b[38;5;220m >> ")
		
		print('Mia:')
		dialogue("Check the court record. \u001b[38;5;220m >> ")
		dialogue("The \u001b[31mCourt Record \033[mcommand… remember? \u001b[38;5;220m >> ")
		
		print('Phoenix:')
		dialogue(tBlue + "(Geez. Give a guy a break!) \u001b[38;5;220m >> ")
		
		print('Judge:')
		dialogue("Let me ask again. \u001b[38;5;220m >> ")
		
	elif questionAnswer.lower() == 'strangled' or questionAnswer == '3':
		print('Phoenix:')
		dialogue("Right… she was strangled, wasn't she? \u001b[38;5;220m >> ")
		
		print('Mia:')
		dialogue("Please tell me that was you talking to yourself. \u001b[38;5;220m >> ")
		
		print('Judge:')
		dialogue("If you wish to hang yourself, Mr. Wright, you're welcome to, but not inside my courtroom. \u001b[38;5;220m >> ")
		dialogue("I suppose there's nothing to do but give you another try: \u001b[38;5;220m >> ")
		
	elif questionAnswer == '2':
		questionAnswer = 'hit with a blunt object'
		
	else:
		print('Judge:')
		dialogue("Sorry, I couldn't hear your answer. I'll ask once more: \u001b[38;5;220m >> ")
		
print('Phoenix:')
dialogue("She was struck once, by a blunt object. \u001b[38;5;220m >> ")

print('Judge:')
dialogue("Correct. \u001b[38;5;220m >> ")
dialogue("You've answered all my questions. \u001b[38;5;220m >> ")
dialogue("I see no reason why we shouldn't proceed. \u001b[38;5;220m >> ")
dialogue("You seem much more relaxed, Mr. Wright. Good for you. \u001b[38;5;220m >> ")

print('Phoenix:')
dialogue("Thank you, Your Honor. \u001b[38;5;220m >> ")
dialogue(tBlue + "(Because I don't FEEL relaxed, that's for sure.) \u001b[38;5;220m >> ")

print('Judge:')
dialogue("Well, then… First, a question for the prosecution. \u001b[38;5;220m >> ")
dialogue("Mr. Payne? \u001b[38;5;220m >> ")

print('Payne:')
dialogue("Yes, Your Honor? \u001b[38;5;220m >> ")

print('Judge:')
dialogue("As Mr. Wright just told us, the victim was struck with a blunt object. \u001b[38;5;220m >> ")
dialogue("""Would you explain to the court just what that "object" was? \u001b[38;5;220m >> """)

print('Payne:')
dialogue("""The murder weapon was this statue of "The Thinker." \u001b[38;5;220m >> """)
dialogue("It was found lying on the floor, next to the victim. \u001b[38;5;220m >> ")

print('Judge:')
dialogue("I see… the court accepts it into evidence. \u001b[38;5;220m >> ")

evidence['Statue'] = '''A statue in the shape of "The Thinker". It's rather heavy.'''
dialogue(tBlue + "Statue added to the Court Record. \u001b[38;5;220m >> ")

print('Mia:')
dialogue("Wright… Be sure to pay attention to any evidence added during the trial. \u001b[38;5;220m >> ")
dialogue("That evidence is the only ammunition you have in court. \u001b[38;5;220m >> ")
dialogue("Type \u001b[31mCourt Record \033[mto check the Court Record frequently. \u001b[38;5;220m >> ")

print('Judge:')
dialogue("Mr. Payne, the prosecution may call its first witness. \u001b[38;5;220m >> ")

print('Payne:')
dialogue("The prosecution calls the defendant, Mr. Butz, to the stand. \u001b[38;5;220m >> ")

print('Phoenix:')
dialogue("Um, Chief, what do I do now? \u001b[38;5;220m >> ")

print('Mia:')
dialogue("Pay attention. \u001b[38;5;220m >> ")
dialogue("You don't want to miss any information that might help your client's case. \u001b[38;5;220m >> ")
dialogue("You'll get your chance to respond to the prosecution later, so be ready! \u001b[38;5;220m >> ")
dialogue("Let's just hope he doesn't say anything… unfortunate. \u001b[38;5;220m >> ")

print('Phoenix:')
dialogue(tBlue + "(Uh oh, Larry gets excited easily… this could be bad.) \u001b[38;5;220m >> ")

print('.')
sleep(1)
print('.')
sleep(1)
print('.')
sleep(0.5)

print('Payne:')
dialogue("Ahem. \u001b[38;5;220m >> ")
dialogue("Mr. Butz. \u001b[38;5;220m >> ")
dialogue("Is it not true that the victim had recently dumped you? \u001b[38;5;220m >> ")

print('Butz:')
dialogue("Hey, watch it buddy! \u001b[38;5;220m >> ")
dialogue("We were great together! \u001b[38;5;220m >> ")
dialogue("We were Romeo and Juliet, Cleopatra and Mark Anthony! \u001b[38;5;220m >> ")

print('Phoenix:')
dialogue(tBlue + "(Um… didn't they all die?) \u001b[38;5;220m >> ")

print('Butz:')
dialogue("I wasn't dumped! \u001b[38;5;220m >> ")
dialogue("She just wasn't taking my phone calls. \u001b[38;5;220m >> ")
dialogue("Or seeing me… Ever. WHAT'S IT TO YOU, ANYWAY!? \u001b[38;5;220m >> ")

print('Payne:')
dialogue("""Mr. Butz, what you describe is generally what we mean by "dumped." \u001b[38;5;220m >> """)
dialogue("In fact, she had completely abandoned you… and was seeing other men! \u001b[38;5;220m >> ")
dialogue("She had just returned from overseas with one of them the day before the murder! \u001b[38;5;220m >> ")

print('Butz:')
dialogue("""Whaddya mean, "one of them"!? \u001b[38;5;220m >> """)
dialogue("Lies! All of it, lies! I don't believe a word of it! \u001b[38;5;220m >> ")

print('Payne:')
dialogue("Your Honor, the victim's \u001b[38;5;75mpassport\033[m. \u001b[38;5;220m >> ")
dialogue("According to this, she was in Paris until the day before she died. \u001b[38;5;220m >> ")

evidence['Passport'] = 'The victim apparently arrived home from Paris on 7/30, the day before the murder.'
dialogue(tBlue + "Passport added to the Court Record. \u001b[38;5;220m >> ")

print('Judge:')
dialogue("Hmm… Indeed, she appears to have returned the day before the murder. \u001b[38;5;220m >> ")

print('Butz:')
dialogue("Dude… no way… \u001b[38;5;220m >> ")

print('Payne:')
dialogue("The victim was a model, but did not have a large income. \u001b[38;5;220m >> ")
dialogue("""It appears that she had several "Sugar Daddies." \u001b[38;5;220m >> """)

print('Butz:')
dialogue("Daddies? Sugar? \u001b[38;5;220m >> ")

print('Payne:')
dialogue("Yes. \u001b[38;5;220m >> ")
dialogue("Older men, who gave her money and gifts. \u001b[38;5;220m >> ")
dialogue("She took their money and used it to support her lifestyle. \u001b[38;5;220m >> ")

print('Butz:')
dialogue("Duuude! \u001b[38;5;220m >> ")

print('Payne:')
dialogue("We can clearly see what kind of woman this Ms. Stone was. \u001b[38;5;220m >> ")
dialogue("Tell me, Mr. Butz, \u001b[31mwhat do you think of her now? \u001b[38;5;220m >> ")

print('Mia:')
dialogue("Wright… I don't think you want him to answer that question. \u001b[38;5;220m >> ")

print('Phoenix:')
dialogue(tBlue + "(Yeah… Larry has a way of running his mouth in all the wrong directions.) \u001b[38;5;220m >> ")

questionAnswer = ' '
currentQuestion = 1
while currentQuestion != 0:
	dialogue(tBlue + "(Should I…?) \u001b[38;5;220m >> ")
	print('1: Wait and see what happens')
	sleep(.5)
	print(' ')
	print('2: Stop him from answering')
	sleep(.5)
	print(' ')
	questionAnswer = input('Type your answer here: ')
	print(' ')
	
	if questionAnswer.lower() == 'wait and see what happens' or questionAnswer == '1' or questionAnswer.lower() == 'wait and see':
		print('Phoenix:')
		dialogue(tBlue + "(Might be better not to get involved in this one…) \u001b[38;5;220m >> ")
		
		print('Payne:')
		dialogue("Well, Mr. Butz? \u001b[38;5;220m >> ")
		
		print('Butz:')
		dialogue("Dude, no way! That cheatin' she-dog! \u001b[38;5;220m >> ")
		currentQuestion = 0
		
	elif questionAnswer.lower() == 'stop him from answering' or questionAnswer == '2' or questionAnswer.lower() == 'stop him':
		print('Phoenix:')
		dialogue("My client had no idea the victim was seeing other men! \u001b[38;5;220m >> ")
		dialogue("That question is irrelevant to this case! \u001b[38;5;220m >> ")
		
		print('Payne:')
		dialogue("Oof! *wince* \u001b[38;5;220m >> ")
		
		print('Butz:')
		dialogue("""Dude! Nick! Whaddya mean, "irrelevant"!? That cheatin' she-dog! \u001b[38;5;220m >> """)
		currentQuestion = 0
		
	else:
		print('Phoenix:')
		dialogue(tBlue + "(Wait what was I thinking about? Oh right!) \u001b[38;5;220m >> ")
		
print('Butz:')
dialogue("I'm gonna die. I'm just gonna drop dead! \u001b[38;5;220m >> ")
dialogue("Yeah, and when I meet her in the afterlife… \u001b[38;5;220m >> ")
dialogue("I'm going to get to the bottom of this! \u001b[38;5;220m >> ")

print('Judge:')
dialogue("Let's continue with the trial, shall we? \u001b[38;5;220m >> ")

print('Payne:')
dialogue("I believe the accused's motive is clear to everyone. \u001b[38;5;220m >> ")

print('Judge:')
dialogue("Yes, quite. \u001b[38;5;220m >> ")

print("Phoenix:")
dialogue(tBlue + "(Oh boy. This is so not looking good.) \u001b[38;5;220m >> ")

print("Payne:")
dialogue("Next question! \u001b[38;5;220m >> ")
dialogue("You went to the victim's apartment on the day of the murder, did you not? \u001b[38;5;220m >> ")

print('Butz:')
dialogue("Gulp! \u001b[38;5;220m >> ")

print('Payne:')
dialogue("Well, did you, or did you not? \u001b[38;5;220m >> ")

print('Butz:')
dialogue("Heh? Heh heh. Well, maybe I did, and maybe I didn't! \u001b[38;5;220m >> ")

print('Phoenix:')
dialogue(tBlue + "(Uh oh. He went. What do I do?) \u001b[38;5;220m >> ")

questionAnswer = ' '
currentQuestion = 1
while currentQuestion != 0:
	dialogue(tBlue + "(I know! I'll send him a signal…) \u001b[38;5;220m >> ")
	print('1: Have him answer honestly')
	sleep(.5)
	print(' ')
	print('2: Stop him from answering')
	sleep(.5)
	print(' ')
	questionAnswer = input('Type your answer here: ')
	print(' ')
	
	if questionAnswer.lower() == 'Have him answer honestly' or questionAnswer == '1' or questionAnswer.lower() == 'answer honestly':
		print('Phoenix:')
		dialogue("*signals* \u001b[38;5;75m(TELL THE TRUTH) \u001b[38;5;220m >> ")
		
		print('Butz:')
		dialogue("Er… Yeah! Yeah! \u001b[38;5;220m >> ")
		dialogue("I was there! I went! \u001b[38;5;220m >> ")
		
		print('Payne:')
		print("""Objection!""")
		print(' ')
		sleep(.5)
		dialogue("Your Honor, the defendant is lying. \u001b[38;5;220m >> ")
		
		print('Judge:')
		dialogue("Lying? \u001b[38;5;220m >> ")
		
		print('Payne:')
		dialogue("The prosecution would like to call a \u001b[31mwitness\033[m who can prove Mr. Butz is lying. \u001b[38;5;220m >> ")
	
		currentQuestion = 0
		
	elif questionAnswer.lower() == 'stop him from answering' or questionAnswer == '2' or questionAnswer.lower() == 'stop him':
		print('Phoenix:')
		dialogue("*signals* \u001b[38;5;75m(LIE LIKE A DOG) \u001b[38;5;220m >> ")
		
		print('Butz:')
		dialogue("Um, well, see, it's like this: I don't remember. \u001b[38;5;220m >> ")
		
		print('Payne:')
		dialogue("""you "don't remember"? \u001b[38;5;220m >> """)
		dialogue("Well then, we'll just have to remind you! \u001b[38;5;220m >> ")
		
		print('Phoenix:')
		dialogue(tBlue + "(I got a bad feeling about this…) \u001b[38;5;220m >> ")
		
		print('Payne:')
		dialogue("We have a u001b[31mwitness\033[m that can prove he DID go to the victim's apartment that day! \u001b[38;5;220m >> ")
		currentQuestion = 0
		
	else:
		print('Phoenix:')
		dialogue(tBlue + "(Wait what was I thinking about? Oh right!) \u001b[38;5;220m >> ")
		
print('Judge:')
dialogue("Well, that simplifies matters. \u001b[38;5;220m >> ")
dialogue("Who is your witness? \u001b[38;5;220m >> ")

print('Payne:')
dialogue("The man who found the victim's body. \u001b[38;5;220m >> ")
dialogue("Just before making the gruesome discovery… \u001b[38;5;220m >> ")
dialogue("He saw the defendant fleeing the scene of the crime! \u001b[38;5;220m >> ")

print('Audience:')
print("*conversing*")
print(' ')
sleep(.5)

print('*Gavel Slam*')
print(' ')
sleep(.225)
print('*Gavel Slam*')
print(' ')
sleep(.255)

print('Judge:')
dialogue("Order! Order in the court! \u001b[38;5;220m >> ")
dialogue("Mr. Payne, the prosecution may call its witness. \u001b[38;5;220m >> ")

print('Payne:')
dialogue("Yes, Your Honor. \u001b[38;5;220m >> ")

print('Phoenix:')
dialogue(tBlue + "(This is bad…) \u001b[38;5;220m >> ")

print('Payne:')
dialogue("On the day of the murder, my witness was selling newspapers at the victim's building. \u001b[38;5;220m >> ")
dialogue("Please bring Mr. Frank Sahwit to the stand! \u001b[38;5;220m >> ")

print('.')
sleep(1)
print('.')
sleep(1)
print('.')
sleep(0.5)

print("Payne:")
dialogue("Mr. Sahwit, you sell newspaper subscriptions, is this correct? \u001b[38;5;220m >> ")

print('Sahwit:')
profiles['Frank Sahwit'] = "Discovered Ms. Stone's body. Newspaper salesman who saw Larry flee the scene."
dialogue("Oh, oh yes! Newspapers, yes! \u001b[38;5;220m >> ")

print('Judge:')
dialogue("Mr. Sahwit, you may proceed with your testimony. \u001b[38;5;220m >> ")
dialogue("Please tell the court what you saw on the day of the murder. \u001b[38;5;220m >> ")

print('.')
sleep(1)
print('.')
sleep(1)
print('.')
sleep(.5)

print(testimonyOp)
print(tRed + "--Witness's Account--" + endTextColour)
sleep(.75)

print('Sahwit:')
dialogue("I was going door-to-door, selling subscriptions when I saw a man fleeing an apartment. \u001b[38;5;220m >> ")
dialogue("I thought he must be in a hurry because he left the door half-open behind him. \u001b[38;5;220m >> ")
dialogue("Thinking it strange, I looked inside the apartment. \u001b[38;5;220m >> ")
dialogue("Then I saw her lying there… A woman… not moving… dead! \u001b[38;5;220m >> ")
dialogue("I quailed in fright and found myself unable to go inside. \u001b[38;5;220m >> ")
dialogue("I thought to call the police immediately! \u001b[38;5;220m >> ")
dialogue("However, the phone in her apartment wasn't working. \u001b[38;5;220m >> ")
dialogue("I went to a nearby park and found a public phone. \u001b[38;5;220m >> ")
dialogue("I remember the time exactly: It was 1:00 PM. \u001b[38;5;220m >> ")
dialogue("The man who ran was, without a doubt, the defendant sitting right over there. \u001b[38;5;220m >> ")

print('Judge:')
dialogue("Hmmm… \u001b[38;5;220m >> ")

print('Phoenix:')
dialogue(tBlue + "(Larry! Why didn't you tell the truth?) \u001b[38;5;220m >> ")
dialogue(tBlue + "(I can't defend you against a testimony like that!) \u001b[38;5;220m >> ")

print('Judge:')
dialogue("Incidentally, why wasn't the phone in the victim's apartment working? \u001b[38;5;220m >> ")

print('Payne:')
dialogue("Your Honor, at the time of the murder, there was a blackout in the building. \u001b[38;5;220m >> ")

print('Judge:')
dialogue("Aren't phones supposed to work during a blackout? \u001b[38;5;220m >> ")

print('Payne:')
dialogue("Yes, Your Honor… However, some cordless phones do not function normally. \u001b[38;5;220m >> ")
dialogue("The phone that Mr. Sahwit used was one of those. \u001b[38;5;220m >> ")
dialogue("Your Honor… I have a record of the blackout, for your perusual. \u001b[38;5;220m >> ")

evidence['Blackout Report'] = '''Electricity to Ms. Stone's building was out from noon to 6 PM on the day of the crime.'''
dialogue(tBlue + "Blackout Report added to the Court Record. \u001b[38;5;220m >> ")

print('Judge:')
dialogue("Now, Mr. Wright… \u001b[38;5;220m >> ")

print('Phoenix:')
dialogue("Yes! \u001b[38;5;220m >> ")
dialogue("Er… yes, Your Honor? \u001b[38;5;220m >> ")

print('Judge:')
dialogue("You may begin your \u001b[31mcross-examination\033[m. \u001b[38;5;220m >> ")

print('Phoenix:')
dialogue("\u001b[31mC-Cross-examination\033[m, Your Honor? \u001b[38;5;220m >> ")

print('Mia:')
dialogue("Alright, Wright, this is it. \u001b[38;5;220m >> ")
dialogue("The real deal! \u001b[38;5;220m >> ")

print('Phoenix:')
dialogue("Uh… what exactly am I supposed to do? \u001b[38;5;220m >> ")

print('Mia:')
dialogue("Why, you expose the \u001b[31mlies\033[m in the testimony the witness just gave! \u001b[38;5;220m >> ")

print('Phoenix:')
dialogue("Lies! What?! He was lying!? \u001b[38;5;220m >> ")

print('Mia:')
dialogue("Your client is innocent, right? \u001b[38;5;220m >> ")
dialogue("Then that witness must have lied in his testimony! \u001b[38;5;220m >> ")
dialogue("Or is your client really… guilty? \u001b[38;5;220m >> ")

print('Phoenix:')
dialogue("!!! \u001b[38;5;220m >> ")
dialogue("How do I prove he's not? \u001b[38;5;220m >> ")

print('Mia:')
dialogue("You hold the key! It's in the \u001b[31mevidence\033[m! \u001b[38;5;220m >> ")
dialogue("Compare the witness's testimony to the evidence at hand. \u001b[38;5;220m >> ")
dialogue("here's bound to be a \u001b[31mcontradiction\033[m in there! \u001b[38;5;220m >> ")
dialogue("First, find contradictions between the \u001b[31mCourt Record\033[m and the witness's testimony. \u001b[38;5;220m >> ")
dialogue("Then, once you've found the contradicting \u001b[31mevidence\033[m… \u001b[31mpresent\033[m it and rub it in the witness's face! \u001b[38;5;220m >> ")

print('Phoenix:')
dialogue("Um… okay. \u001b[38;5;220m >> ")

print('Mia:')
dialogue("Use the \u001b[31mCourt Record\033[m command and point out \u001b[31mcontradictions\033[m in the testimony! \u001b[38;5;220m >> ")

crossExaminationPosition = 1
crossExamination = 1
print(crossExaminationOp)
print(tRed + "--Witness's Account--" + endTextColour)
sleep(.75)

print('Sahwit:')
while crossExamination == 1:
	if crossExaminationPosition == 1:
		crossExaminationStatement(tGreen + "I was going door-to-door, selling subscriptions when I saw a man fleeing an apartment. \u001b[38;5;220m >> ")
		if userChoice.lower() == 'press':
			print('Phoenix:')
			print("""Hold it!""")
			print(' ')
			sleep(.5)
			dialogue("Isn't a man leaving an apartment a common sight? \u001b[38;5;220m >> ")
			dialogue("I find it odd you would take notice of him… \u001b[38;5;220m >> ")
			
			print('Sahwit:')
			dialogue("Er… heh. I don't know. \u001b[38;5;220m >> ")
			dialogue("He just seemed strange to me, that's all. \u001b[38;5;220m >> ")
			dialogue("Like he was mad, and yet frightened at the same time. \u001b[38;5;220m >> ")
			dialogue("Just like… a criminal fleeing the scene of a crime! \u001b[38;5;220m >> ")
			
			print('Phoenix:')
			dialogue("The defense requests that the witness refrain from conjecture! \u001b[38;5;220m >> ")
			
			print('Payne:')
			dialogue("Of course. \u001b[38;5;220m >> ")
			dialogue("What the witness means is that the man he saw looked suspicious. \u001b[38;5;220m >> ")
			dialogue("So, what happened next? \u001b[38;5;220m >> ")
			
			print('Sahwit:')
		elif presentedItem not in list(evidence.keys()) and presentedItem not in list(profiles.keys()):
			pass
		else:
			wrongEvidence()
			
	if crossExaminationPosition == 2:
		crossExaminationStatement("\u001b[38;5;220m<< \033[32m I thought he must be in a hurry because he left the door half-open behind him. \u001b[38;5;220m >> ")
		if userChoice.lower() == 'press':
			print('Phoenix:')
			print("""Hold it!""")
			print(' ')
			sleep(.5)
			dialogue("Half-open… you say? \u001b[38;5;220m >> ")
			
			print('Sahwit:')
			dialogue("Yes, yes, the door was open halfway. \u001b[38;5;220m >> ")
			dialogue("Yes. I watched for a moment, but no one came to close the door. ")
			dialogue(""""That's odd, in a big city like this," I thought… \u001b[38;5;220m >> """)
			
			print('Payne:')
			dialogue("I see. And what happened next? \u001b[38;5;220m >> ")
			
			print('Sahwit:')
		elif presentedItem not in list(evidence.keys()) and presentedItem not in list(profiles.keys()):
			pass
		else:
			wrongEvidence()
			
	if crossExaminationPosition == 3:
		crossExaminationStatement("\u001b[38;5;220m<< \033[32m Thinking it strange, I looked inside the apartment. \u001b[38;5;220m >> ")
		if userChoice.lower() == 'press':
			print('Phoenix:')
			print("""Hold it!""")
			print(' ')
			sleep(.5)
			dialogue("What gave you the idea to do that? \u001b[38;5;220m >> ")
			
			print('Sahwit:')
			dialogue("Well, the door was half-open, you see. \u001b[38;5;220m >> ")
			dialogue("Isn't it only human to want to… peek? \u001b[38;5;220m >> ")
			dialogue("We climb mountains because they are there! \u001b[38;5;220m >> ")
			dialogue("It's the same thing. \u001b[38;5;220m >> ")
			
			print('Payne:')
			dialogue("Truer words have never been spoken! \u001b[38;5;220m >> ")
			dialogue("Anyone would look inside! \u001b[38;5;220m >> ")
			
			print('Phoenix:')
			dialogue(tBlue + "(Hmm… why did Payne cut him off so quickly?) \u001b[38;5;220m >> ")
			
			print('Payne:')
			dialogue("So you looked into the apartment. \u001b[38;5;220m >> ")
			dialogue("What happened then? \u001b[38;5;220m >> ")
			
			print('Sahwit:')
		elif presentedItem not in list(evidence.keys()) and presentedItem not in list(profiles.keys()):
			pass
		else:
			wrongEvidence()
			
	if crossExaminationPosition == 4:
		crossExaminationStatement("\u001b[38;5;220m<< \033[32m Then I saw her lying there… A woman… not moving… dead! \u001b[38;5;220m >> ")
		if userChoice.lower() == 'press':
			print('Phoenix:')
			print("""Hold it!""")
			print(' ')
			sleep(.5)
			dialogue("Are you sure she was dead? \u001b[38;5;220m >> ")
			
			print('Sahwit:')
			dialogue("W-Well, no, I guess I wasn't. \u001b[38;5;220m >> ")
			dialogue("But, she wasn't moving at all, and there was blood everywhere. \u001b[38;5;220m >> ")
			
			print('Phoenix:')
			dialogue(tBlue + "(I guess that would look fatal to anyone…) \u001b[38;5;220m >> ")
			dialogue("Very well, what happened next? \u001b[38;5;220m >> ")
			
			print('Sahwit:')
		elif presentedItem not in list(evidence.keys()) and presentedItem not in list(profiles.keys()):
			pass
		else:
			wrongEvidence()
			
	if crossExaminationPosition == 5:
		crossExaminationStatement("\u001b[38;5;220m<< \033[32m I quailed in fright and found myself unable to go inside. \u001b[38;5;220m >> ")
		if userChoice.lower() == 'press':
			print('Phoenix:')
			print("""Hold it!""")
			print(' ')
			sleep(.5)
			dialogue("So, you didn't touch ANYTHING in the apartment? \u001b[38;5;220m >> ")
			
			print('Sahwit:')
			dialogue("Um, yes. I mean no! Nothing. \u001b[38;5;220m >> ")
			
			print('Phoenix:')
			dialogue("Okay. What happened next? \u001b[38;5;220m >> ")
			
			print('Sahwit:')
		elif presentedItem not in list(evidence.keys()) and presentedItem not in list(profiles.keys()):
			pass
		else:
			wrongEvidence()
			
	if crossExaminationPosition == 6:
		crossExaminationStatement("\u001b[38;5;220m<< \033[32m I thought to call the police immediately! \u001b[38;5;220m >> ")
		if userChoice.lower() == 'press':
			print('Phoenix:')
			print("""Hold it!""")
			print(' ')
			sleep(.5)
			dialogue("""You "thought" to call the police?  \u001b[38;5;220m >> """)
			dialogue("Does that mean you didn't actually call them!? \u001b[38;5;220m >> ")
			
			print('Payne:')
			dialogue("Please, please… \u001b[38;5;220m >> ")
			dialogue("Listen to the rest of the testimony. \u001b[38;5;220m >> ")
			dialogue("You thought to call the police… \u001b[38;5;220m >> ")
			dialogue("What happened next? \u001b[38;5;220m >> ")
			
			print('Sahwit')
		elif presentedItem not in list(evidence.keys()) and presentedItem not in list(profiles.keys()):
			pass
		else:
			wrongEvidence()
			
	if crossExaminationPosition == 7:
		crossExaminationStatement("\u001b[38;5;220m<< \033[32m However, the phone in her apartment wasn't working. \u001b[38;5;220m >> ")
		if userChoice.lower() == 'press':
			print('Phoenix:')
			print("""Hold it!""")
			print(' ')
			sleep(.5)
			dialogue("The phone in her apartment wasn't working? \u001b[38;5;220m >> ")
			
			print('Sahwit:')
			dialogue("Yes. I mean, no, no it wasn't. Right. \u001b[38;5;220m >> ")
			
			print('Phoenix:')
			dialogue("But you said you didn't go into the apartment… or did you!? \u001b[38;5;220m >> ")
			
			print('Sahwit:')
			dialogue("Oh, oh, that? \u001b[38;5;220m >> ")
			dialogue("I can explain that! \u001b[38;5;220m >> ")
			dialogue("There was a cordless phone on a shelf in the entranceway. \u001b[38;5;220m >> ")
			dialogue("I reached inside and tried using that to call… \u001b[38;5;220m >> ")
			
			print('Payne:')
			dialogue("And the phone wasn't working, correct? \u001b[38;5;220m >> ")
			dialogue("What happened next? \u001b[38;5;220m >> ")
			
			print('Sahwit:')
		elif presentedItem not in list(evidence.keys()) and presentedItem not in list(profiles.keys()):
			pass
		else:
			wrongEvidence()
			
	if crossExaminationPosition == 8:
		crossExaminationStatement("\u001b[38;5;220m<< \033[32m I went to a nearby park and found a public phone. \u001b[38;5;220m >> ")
		if userChoice.lower() == 'press':
			print('Phoenix:')
			print("""Hold it!""")
			print(' ')
			sleep(.5)
			dialogue("Why use a public phone? \u001b[38;5;220m >> ")
			
			print('Sahwit:')
			dialogue("Well, you see, I don't have a cell phone. \u001b[38;5;220m >> ")
			dialogue("And, being the middle of the afternoon, there was no answer at the nearby apartments. \u001b[38;5;220m >> ")
			
			print('Phoenix:')
			dialogue("Ah, right… what time did you call again? \u001b[38;5;220m >> ")
			
			print('Sahwit:')
		elif presentedItem not in list(evidence.keys()) and presentedItem not in list(profiles.keys()):
			pass
		else:
			wrongEvidence()
	if crossExaminationPosition == 9:
		crossExaminationStatement("\u001b[38;5;220m<< \033[32m I remember the time exactly: It was 1:00 PM. \u001b[38;5;220m >> ")
		if userChoice.lower() == 'press':
			print('Phoenix:')
			print("""Hold it!""")
			print(' ')
			sleep(.5)
			dialogue("1:00 PM! Are you certain? \u001b[38;5;220m >> ")
			
			print('Sahwit:')
			dialogue("Yes. Absolutely. \u001b[38;5;220m >> ")
			
			print('Phoenix:')
			dialogue(tBlue + "(Hmm… He seems really confident.) \u001b[38;5;220m >> ")
			
			print('Mia:')
			dialogue("\u001b[31m1:00 PM\033[m? \u001b[38;5;220m >> ")
			dialogue("Wright. Doesn't that seem strange to you? \u001b[38;5;220m >> ")
			dialogue("Present some \u001b[31mevidence\033[m to \u001b[31mcontradict\033[m him! \u001b[38;5;220m >> ")
			
			print('Sahwit:')
		elif presentedItem.lower() == "cindy's autopsy report":
			print('Phoenix:')
			print("""Objection!""")
			print(' ')
			sleep(.5)
			crossExamination = 0
			presentedItem = '''Put something in here that won't appear in your evidence or profile list'''
			continue
		elif presentedItem not in list(evidence.keys()) and presentedItem not in list(profiles.keys()):
			pass
		else:
			wrongEvidence()
		
	if crossExaminationPosition == 10:
		crossExaminationStatement("\u001b[38;5;220m<< \033[32m The man who ran was, without a doubt, the defendant sitting right over there. \u001b[38;5;220m >> ")
		if userChoice.lower() == 'press':
			print('Phoenix:')
			print("""Hold it!""")
			print(' ')
			sleep(.5)
			dialogue("Are you absolutely, 100% positive? \u001b[38;5;220m >> ")
			
			print('Sahwit:')
			dialogue("Yes, it was him. \u001b[38;5;220m >> ")
			dialogue("No mistake about it. \u001b[38;5;220m >> ")
			
			print('Payne:')
			dialogue("The witness says he's certain! \u001b[38;5;220m >> ")
			
		elif presentedItem not in list(evidence.keys()) and presentedItem not in list(profiles.keys()):
			pass
		else:
			wrongEvidence()
			
	if crossExaminationPosition > 10:
		print('Mia:')
		dialogue("That's all of it. \u001b[38;5;220m >> ")
		dialogue("There must be a contradiction in there somewhere. \u001b[38;5;220m >> ")
		dialogue("Examine the \u001b[31mCourt Record\033[m if something strikes you as being suspicious. \u001b[38;5;220m >> ")
		dialogue("Then, find the evidence that contradicts his testimony, and \u001b[31mpresent\033[m it to him! \u001b[38;5;220m >> ")
		
		print('Sahwit:')
		crossExaminationPosition = 1

# Phoenix:
dialogue("You found the body at 1:00 PM. You're sure? \u001b[38;5;220m >> ")

print('Sahwit:')
dialogue("Yes. It was 1:00 PM, for certain. \u001b[38;5;220m >> ")

print('Phoenix:')
dialogue("Frankly, I find that hard to believe! \u001b[38;5;220m >> ")
dialogue("Your statement directly contradicts the autopsy report. \u001b[38;5;220m >> ")
dialogue("The autopsy notes the time of death at sometime after \u001b[31m4PM\033[m. \u001b[38;5;220m >> ")
dialogue("""There was nobody to… er… no "body" to find at 1:00 PM! \u001b[38;5;220m >> """)
dialogue("How do you explain this three-hour gap? \u001b[38;5;220m >> ")

print('Sahwit:')
dialogue("!!! \u001b[38;5;220m >> ")
dialogue(" Oh, that! Oh, er…")

print('Payne:')
print("""Objection!""")
print(' ')
sleep(.5)
dialogue("This is trivial! \u001b[38;5;220m >> ")
dialogue("The witness merely forgot the time! \u001b[38;5;220m >> ")

print('Judge:')
dialogue("After his testimony, I find that hard to believe. \u001b[38;5;220m >> ")
dialogue("Mr. Sahwit… \u001b[38;5;220m >> ")
dialogue("Why were you so certain that you found the body at 1:00 PM? \u001b[38;5;220m >> ")

print('Sahwit:')
dialogue(".. er… well, I… \u001b[38;5;220m >> ")
dialogue("Gee, that's a really good question! \u001b[38;5;220m >> ")

print('Mia:')
dialogue("Great job, Wright! \u001b[38;5;220m >> ")
dialogue("Way to put him on the spot! \u001b[38;5;220m >> ")
dialogue("That's all you have to do: point out contradictions! \u001b[38;5;220m >> ")
dialogue("Lies always beget more lies! \u001b[38;5;220m >> ")
dialogue("See through one, and their whole story falls apart! \u001b[38;5;220m >> ")

print('Sahwit:')
dialogue("Wait! I remember now! \u001b[38;5;220m >> ")

print('Judge:')
dialogue("Would you care to give your testimony again? \u001b[38;5;220m >> ")

print(testimonyOp)
print(tRed + "--The Time of Discovery--" + endTextColour)
sleep(.75)

print('Sahwit:')
dialogue("You see, when I found the body, I heard the time. \u001b[38;5;220m >> ")
dialogue("There was a voice saying the time… It was probably coming from the television. \u001b[38;5;220m >> ")
dialogue("Oh, but it was three hours off, wasn't it? \u001b[38;5;220m >> ")
dialogue("I guess the victim must have been watching a video of a taped program! \u001b[38;5;220m >> ")
dialogue("That's why I thought it was 1:00 PM! \u001b[38;5;220m >> ")
dialogue("Terribly sorry about the misunderstanding… \u001b[38;5;220m >> ")

print('Judge:')
dialogue("Hmm… I see. \u001b[38;5;220m >> ")
dialogue("You heard a voice saying the time on a taped program. \u001b[38;5;220m >> ")
dialogue("Mr. Wright, you may cross-examine the witness. \u001b[38;5;220m >> ")

print('Mia:')
dialogue("Wright! You know what to do! \u001b[38;5;220m >> ")

print('Phoenix:')
dialogue("I've got this one. \u001b[38;5;220m >> ")

crossExaminationPosition = 1
crossExamination = 1
print(crossExaminationOp)
print(tRed + "--The Time of Discovery--" + endTextColour)
sleep(.75)

print('Sahwit:')
while crossExamination == 1:
	if crossExaminationPosition == 1:
		crossExaminationStatement("\u001b[38;5;220m<< \033[32m You see, when I found the body, I heard the time. \u001b[38;5;220m >> ")
		if userChoice.lower() == 'press':
			print('Phoenix:')
			print("""Hold it!""")
			print(' ')
			sleep(.5)
			dialogue("""You said "heard"… \u001b[38;5;220m >> """)
			dialogue("""Not "saw"? \u001b[38;5;220m >> """)
			
			print('Sahwit:')
			dialogue("Yes, heard. \u001b[38;5;220m >> ")
			dialogue("All I saw was the body lying there… \u001b[38;5;220m >> ")
			dialogue("I didn't think to look at anything else, least of all my watch. \u001b[38;5;220m >> ")
			
			print('Phoenix:')
			dialogue("Hmm… \u001b[38;5;220m >> ")
			dialogue("Isn't that a little strange? \u001b[38;5;220m >> ")
			dialogue("""So you're saying you "heard" something. \u001b[38;5;220m >> """)
			dialogue("But if you were so shocked by the body, you wouldn't hear anything at all! \u001b[38;5;220m >> ")
			
			print('Payne:')
			print("""Objection!""")
			print(' ')
			sleep(.5)
			dialogue("The witness did say he actually heard the time. \u001b[38;5;220m >> ")
			dialogue("""It's ludicrous to suggest he "wouldn't hear anything"! \u001b[38;5;220m >> """)
			
			print('Judge:')
			dialogue("Hmm… \u001b[38;5;220m >> ")
			dialogue("I have to agree with the prosecution. \u001b[38;5;220m >> ")
			dialogue("Witness, continue your testimony. \u001b[38;5;220m >> ")
			
			print('Sahwit:')
		if presentedItem.lower() == 'blackout report':
			print('Phoenix:')
			print("""Objection!""")
			print(' ')
			sleep(.5)
			crossExamination = 0
			presentedItem = '''Put something in here that won't appear in your evidence or profile list'''
			continue
		elif presentedItem not in list(evidence.keys()) and presentedItem not in list(profiles.keys()):
			pass
		else:
			wrongEvidence()
			
	if crossExaminationPosition == 2:
		crossExaminationStatement("\u001b[38;5;220m<< \033[32m There was a voice saying the time… It was probably coming from the television. \u001b[38;5;220m >> ")
		if userChoice.lower() == 'press':
			print('Phoenix:')
			print("""Hold it!""")
			print(' ')
			sleep(.5)
			dialogue("Are you sure it was a television and not… a radio? \u001b[38;5;220m >> ")
			
			print('Sahwit:')
			dialogue("Well, no, I guess it might have been a radio. \u001b[38;5;220m >> ")
			
			print('Payne:')
			dialogue("Incidentally, there was no radio on the premises. \u001b[38;5;220m >> ")
			dialogue("There was only one large television. \u001b[38;5;220m >> ")
			
			print('Mia:')
			dialogue("Wright! I can't put my finger on it, but something about this seems fishy. \u001b[38;5;220m >> ")
			dialogue("""Something about "hearing" the television… \u001b[38;5;220m >> """)
			
			print('Payne:')
			dialogue("The witness has testified. \u001b[38;5;220m >> ")
			dialogue("He heard the time. \u001b[38;5;220m >> ")
			
			print('Sahwit:')
		if presentedItem.lower() == 'blackout report':
			print('Phoenix:')
			print("""Objection!""")
			print(' ')
			sleep(.5)
			crossExamination = 0
			presentedItem = '''Put something in here that won't appear in your evidence or profile list'''
			continue
		elif presentedItem not in list(evidence.keys()) and presentedItem not in list(profiles.keys()):
			pass
		else:
			wrongEvidence()
			
	if crossExaminationPosition == 3:
		crossExaminationStatement("\u001b[38;5;220m<< \033[32m Oh, but it was three hours off, wasn't it? \u001b[38;5;220m >> ")
		if userChoice.lower() == 'press':
			print('Phoenix:')
			print("""Hold it!""")
			print(' ')
			sleep(.5)
			dialogue("How do you explain the gap! \u001b[38;5;220m >> ")
			
			print('Judge:')
			dialogue("Well, witness? \u001b[38;5;220m >> ")
			dialogue("Can you explain this? \u001b[38;5;220m >> ")
			
			print('Sahwit:')
		if presentedItem.lower() == 'blackout report':
			print('Phoenix:')
			print("""Objection!""")
			print(' ')
			sleep(.5)
			crossExamination = 0
			continue
		elif presentedItem not in list(evidence.keys()) and presentedItem not in list(profiles.keys()):
			pass
		else:
			wrongEvidence()
			
	if crossExaminationPosition == 4:
		crossExaminationStatement("\u001b[38;5;220m<< \033[32m I guess the victim must have been watching a video of a taped program! \u001b[38;5;220m >> ")
		if userChoice.lower() == 'press':
			print('Phoenix:')
			print("""Hold it!""")
			print(' ')
			sleep(.5)
			dialogue("A.. video? \u001b[38;5;220m >> ")
			
			print('Sahwit:')
			dialogue("Yes, that would explain why the time was wrong! \u001b[38;5;220m >> ")
			
			print('Phoenix:')
			dialogue("True, true… \u001b[38;5;220m >> ")
			
			print('Mia:')
			dialogue("Wright! \u001b[38;5;220m >> ")
			dialogue("I think the problem lies someplace else… \u001b[38;5;220m >> ")
			
			print('Judge:')
			dialogue("We're agreed that you heard the time at the scene, then. \u001b[38;5;220m >> ")
			
			print('Sahwit:')
		if presentedItem.lower() == 'blackout report':
			print('Phoenix:')
			print("""Objection!""")
			print(' ')
			sleep(.5)
			crossExamination = 0
			presentedItem = '''Put something in here that won't appear in your evidence or profile list'''
			continue
		elif presentedItem not in list(evidence.keys()) and presentedItem not in list(profiles.keys()):
			pass
		else:
			wrongEvidence()
			
	if crossExaminationPosition == 5:
		crossExaminationStatement("\u001b[38;5;220m<< \033[32m That's why I thought it was 1:00 PM! \u001b[38;5;220m >> ")
		if userChoice.lower() == 'press':
			print('Phoenix:')
			print("""Hold it!""")
			print(' ')
			sleep(.5)
			dialogue("Are you sure the voice you heard said it was 1:00 PM? \u001b[38;5;220m >> ")
			
			print('Sahwit:')
			dialogue("Yes, I can practically hear it now. \u001b[38;5;220m >> ")
			dialogue("It was quite clear. \u001b[38;5;220m >> ")
			
			print('Judge:')
			dialogue("Mr. Payne, has the prosecution verified this testimony? \u001b[38;5;220m >> ")
			
			print('Payne:')
			dialogue("My apologies, Your Honor. \u001b[38;5;220m >> ")
			dialogue("""I, too, have only just learned that the witness "heard" the time. \u001b[38;5;220m >> """)
			
			print('Sahwit:')
			dialogue("Oh, I'm really sorry. \u001b[38;5;220m >> ")
			dialogue("I only remembered it just now. \u001b[38;5;220m >> ")
		if presentedItem.lower() == 'blackout report':
			print('Phoenix:')
			print("""Objection!""")
			print(' ')
			sleep(.5)
			crossExamination = 0
			presentedItem = '''Put something in here that won't appear in your evidence or profile list'''
			continue
		elif presentedItem not in list(evidence.keys()) and presentedItem not in list(profiles.keys()):
			pass
		else:
			wrongEvidence()
	
	if crossExaminationPosition == 6:
		crossExaminationStatement("\u001b[38;5;220m<< \033[32m Terribly sorry about the misunderstanding… \u001b[38;5;220m >> ")
		if userChoice.lower() == 'press':
			print('Phoenix:')
			print("""Hold it!""")
			print(' ')
			sleep(.5)
			dialogue("Well, you just watch it! \u001b[38;5;220m >> ")
			dialogue(tBlue + "(Hmm…) \u001b[38;5;220m >> ")
			dialogue(tBlue + "(Not much point pressing him on that one, was there?) \u001b[38;5;220m >> ")
		
		elif presentedItem not in list(evidence.keys()) and presentedItem not in list(profiles.keys()):
			pass
		else:
			wrongEvidence()
			
	if crossExaminationPosition > 6:
		print('Mia:')
		dialogue("Notice anything suspicious? \u001b[38;5;220m >> ")
		
		print('Sahwit:')
		crossExaminationPosition = 1
		
# Phoenix:
dialogue("Hold it right there! \u001b[38;5;220m >> ")
dialogue("The prosecution has said there was a blackout at the time of the discovery! \u001b[38;5;220m >> ")
dialogue("And this record proves it! \u001b[38;5;220m >> ")

print('Sahwit:')
dialogue("…! \u001b[38;5;220m >> ")

print('Phoenix:')
dialogue("You couldn't have heard a television… or a video! \u001b[38;5;220m >> ")

print('Sahwit:')
dialogue("Gah!!! \u001b[38;5;220m >> ")
dialogue("I… well… urk! \u001b[38;5;220m >> ")

print('Judge:')
dialogue("The defense has a point. \u001b[38;5;220m >> ")
dialogue("Do you have an explanation for this, Mr. Sahwit? \u001b[38;5;220m >> ")

print('Sahwit:')
dialogue("No, I… I find it quite puzzling myself! Quite! \u001b[38;5;220m >> ")
dialogue("… \u001b[38;5;220m >> ")
dialogue("Aah! W-wait! I remember now! \u001b[38;5;220m >> ")

print('Judge:')
dialogue("Mr. Sahwit? \u001b[38;5;220m >> ")
dialogue("The court would prefer to hear an accurate testimony from the very beginning. \u001b[38;5;220m >> ")
dialogue("These constant corrections are harming your credibility. \u001b[38;5;220m >> ")
dialogue("That, and you seem rather… distraught. \u001b[38;5;220m >> ")

print('Sahwit:')
dialogue("…! \u001b[38;5;220m >> ")
dialogue("M-my apologies, Your Honor! \u001b[38;5;220m >> ")
dialogue("It… er, it must have been the shock of finding the body! \u001b[38;5;220m >> ")

print('Judge:')
dialogue("Very well, Mr. Sahwit. \u001b[38;5;220m >> ")
dialogue("Let's hear your testimony once more please. \u001b[38;5;220m >> ")

print(testimonyOp)
print(tRed + "--Hearing the Time--" + endTextColour)
sleep(.75)

print('Sahwit:')
dialogue("""Actually, I didn't "hear" the time… I "saw" it! \u001b[38;5;220m >> """)
dialogue("There was a table clock in the apartment, wasn't there! \u001b[38;5;220m >> ")
dialogue("Yeah, the murder weapon! The killer used it to hit the victim! \u001b[38;5;220m >> ")
dialogue("That must have been what I saw. \u001b[38;5;220m >> ")

print('Judge:')
dialogue("You saw a clock? \u001b[38;5;220m >> ")
dialogue("I guess that would explain it. \u001b[38;5;220m >> ")
dialogue("The defense may cross-examine the witness. \u001b[38;5;220m >> ")

print('Phoenix:')
dialogue("Gladly. \u001b[38;5;220m >> ")

crossExaminationPosition = 1
crossExamination = 1
print(crossExaminationOp)
print(tRed + "--Hearing the Time--" + endTextColour)
sleep(.75)

print('Sahwit:')
while crossExamination == 1:
	if crossExaminationPosition == 1:
		crossExaminationStatement(tGreen + """Actually, I didn't "hear" the time… I "saw" it! \u001b[38;5;220m >> """)
		if userChoice.lower() == 'press':
			print('Phoenix:')
			print("""Hold it!""")
			print(' ')
			sleep(.5)
			dialogue("That strikes me as a very suspicious mistake. \u001b[38;5;220m >> ")
			
			print('Sahwit:')
			dialogue("Yes, I can see how you'd be a little doubtful… \u001b[38;5;220m >> ")
			dialogue("I'm really sorry. I only just remembered that table clock! \u001b[38;5;220m >> ")
			
			print('Judge:')
			dialogue("""A "table clock"? \u001b[38;5;220m >> """)
			
			print('Sahwit:')
		elif presentedItem not in list(evidence.keys()) and presentedItem not in list(profiles.keys()):
			pass
		else:
			wrongEvidence()
		
	if crossExaminationPosition == 2:	
		crossExaminationStatement("\u001b[38;5;220m<< \033[32m There was a table clock in the apartment, wasn't there! \u001b[38;5;220m >> ")
		if userChoice.lower() == 'press':
			print('Phoenix:')
			print("""Hold it!""")
			print(' ')
			sleep(.5)
			dialogue("""A "table clock"? \u001b[38;5;220m >> """)
			dialogue("Was there a clock at the scene? \u001b[38;5;220m >> ")
			
			print('Judge:')
			dialogue("This is the first I've heard of it! \u001b[38;5;220m >> ")
			
			print('Sahwit:')
		if presentedItem.lower() == 'statue/the thinker':
			print('Phoenix:')
			print("""Objection!""")
			print(' ')
			sleep(.5)
			crossExamination = 0
			presentedItem = '''Put something in here that won't appear in your evidence or profile list'''
			continue
		elif presentedItem not in list(evidence.keys()) and presentedItem not in list(profiles.keys()):
			pass
		else:
			wrongEvidence()
		
	if crossExaminationPosition == 3:
		crossExaminationStatement("\u001b[38;5;220m<< \033[32m Yeah, the murder weapon! The killer used it to hit the victim! \u001b[38;5;220m >> ")
		if userChoice.lower() == 'press':
			print('Phoenix:')
			print("""Hold it!""")
			print(' ')
			sleep(.5)
			dialogue("The… murder weapon? \u001b[38;5;220m >> ")
			
			print('Sahwit:')
			dialogue("Yes, the table clock that was used as a weapon! \u001b[38;5;220m >> ")
			dialogue("That's what I just said. \u001b[38;5;220m >> ")
			dialogue("Did you doze off in the middle of my testimony or something? \u001b[38;5;220m >> ")
			
			print('Phoenix:')
			dialogue(tBlue + "(Something's fishy here…) \u001b[38;5;220m >> ")
			
			print('Sahwit:')
		if presentedItem.lower() == 'statue/the thinker':
			print('Phoenix:')
			print("""Objection!""")
			print(' ')
			sleep(.5)
			crossExamination = 0
			presentedItem = '''Put something in here that won't appear in your evidence or profile list'''
			continue
		elif presentedItem not in list(evidence.keys()) and presentedItem not in list(profiles.keys()):
			pass
		else:
			wrongEvidence()
		
	if crossExaminationPosition == 4:
		crossExaminationStatement("\u001b[38;5;220m<< \033[32m That must have been what I saw. \u001b[38;5;220m >> ")
		if userChoice.lower() == 'press':
			print('Phoenix:')
			print("""Hold it!""")
			print(' ')
			sleep(.5)
			dialogue("Why didn't you tell us that in the first place? \u001b[38;5;220m >> ")
			
			print('Sahwit:')
			dialogue("I guess it just slipped my mind! \u001b[38;5;220m >> ")
			dialogue("I'm not really sure how it happened myself… \u001b[38;5;220m >> ")
			
			print('Payne:')
			dialogue("The witness says he saw the table clock. \u001b[38;5;220m >> ")
			dialogue("End of story. \u001b[38;5;220m >> ")
			
		if presentedItem.lower() == 'statue/the thinker':
			print('Phoenix:')
			print("""Objection!""")
			print(' ')
			sleep(.5)
			crossExamination = 0
			presentedItem = '''Put something in here that won't appear in your evidence or profile list'''
			continue
		elif presentedItem not in list(evidence.keys()) and presentedItem not in list(profiles.keys()):
			pass
		else:
			wrongEvidence()
	
	if crossExaminationPosition > 4:
		print('Mia:')
		dialogue("Now, find the contradiction! \u001b[38;5;220m >> ")
		
		print('Sahwit:')
		crossExaminationPosition = 1
		
# Phoenix:
dialogue("Wait just a moment! \u001b[38;5;220m >> ")
dialogue("The murder weapon wasn't a clock. \u001b[38;5;220m >> ")
dialogue("It was this statue! \u001b[38;5;220m >> ")
dialogue("Now how is this supposed to be a clock? \u001b[38;5;220m >> ")

print('Sahwit:')
dialogue("Whaa!? \u001b[38;5;220m >> ")
dialogue("""Y-you with your "objections," and your "evidence"… \u001b[38;5;220m >> """)
dialogue("Just who do you think you are!? \u001b[38;5;220m >> ")

print('Phoenix:')
dialogue("Just answer the question, Mr. Sahwit. \u001b[38;5;220m >> ")

print('Sahwit:')
dialogue("Hey, I… \u001b[38;5;220m >> ")
dialogue("I saw it there, okay! \u001b[38;5;220m >> ")
dialogue("That's a clock! \u001b[38;5;220m >> ")

print('Payne:')
dialogue("Your Honor! \u001b[38;5;220m >> ")
dialogue("If I may… \u001b[38;5;220m >> ")

print('Judge:')
dialogue("Yes, Mr. Payne? \u001b[38;5;220m >> ")

print('Payne:')
dialogue("As the witness stated, this statue is indeed a clock. \u001b[38;5;220m >> ")
dialogue("The neck is a switch. \u001b[38;5;220m >> ")
dialogue("You just tilt it, and it says the time out loud. \u001b[38;5;220m >> ")
dialogue("As it doesn't look like a clock, I submitted it as a statue. \u001b[38;5;220m >> ")
dialogue("My apologies. \u001b[38;5;220m >> ")

print('Judge:')
dialogue("I see. \u001b[38;5;220m >> ")
dialogue("So the murder weapon was a table clock after all. \u001b[38;5;220m >> ")
dialogue("Well, Mr. Wright? \u001b[38;5;220m >> ")
dialogue("It appears that the witness's testimony was correct. \u001b[38;5;220m >> ")
dialogue("This is a clock. \u001b[38;5;220m >> ")

questionAnswer = ' '
currentQuestion = 1
while currentQuestion != 0:
	dialogue("Do you have any problems with his testimony now? \u001b[38;5;220m >> ")
	print('1: Yes')
	sleep(.5)
	print(' ')
	print('2: No')
	sleep(.5)
	print(' ')
	questionAnswer = input('Type your answer here: ')
	print(' ')
	
	if questionAnswer.lower() == 'yes' or questionAnswer == '1' or questionAnswer.lower() == '1: yes':
		print('Phoenix:')
		dialogue("Your Honor, there is a gaping hole in the witness's testimony! \u001b[38;5;220m >> ")
		currentQuestion = 0
		
	elif questionAnswer.lower() == 'no' or questionAnswer == '2' or questionAnswer.lower() == '2: no':
		print('Phoenix:')
		dialogue("I guess not. \u001b[38;5;220m >> ")
		dialogue("There was a clock on the scene, so, no problem. \u001b[38;5;220m >> ")
		
		print('Mia:')
		dialogue("Wright! \u001b[38;5;220m >> ")
		dialogue("Are you out of your mind!? \u001b[38;5;220m >> ")
		dialogue("That clock doesn't look like a clock at all! \u001b[38;5;220m >> ")
		dialogue("The witness couldn't have possibly known it was a clock just by seeing it! \u001b[38;5;220m >> ")
		dialogue("He said himself, he never entered the apartment! \u001b[38;5;220m >> ")
		dialogue("It was in his testimony! \u001b[38;5;220m >> ")
		
		print('Phoeniz:')
		dialogue("Hey! You're right! \u001b[38;5;220m >> ")
		
		print('Judge:')
		dialogue("Is something the matter? \u001b[38;5;220m >> ")
		dialogue("Does the defense have anything to add? \u001b[38;5;220m >> ")
		
		print('Phoenix:')
		dialogue("Yes… \u001b[38;5;220m >> ")
		dialogue("Yes I do! \u001b[38;5;220m >> ")
		currentQuestion = 0
		
	else:
		print('Phoenix:')
		dialogue(tBlue + "(Wait what was I thinking about? Oh right!) \u001b[38;5;220m >> ")
		
		print('Judge:')
		
#Phoenix:
dialogue("The only way he could have known the weapon was a clock is to hold it in his hand. \u001b[38;5;220m >> ")
dialogue("Yet the witness testified that he never entered the apartment! \u001b[38;5;220m >> ")
dialogue("Clearly, a contradiction! \u001b[38;5;220m >> ")

print('Judge:')
dialogue("Hmm… indeed! \u001b[38;5;220m >> ")

print('Phoenix:')
questionAnswer = ' '
currentQuestion = 1
while currentQuestion != 0:
	dialogue("The witness knew it was a clock, because he… \u001b[38;5;220m >> ")
	print('1: Went into the apartment')
	sleep(.5)
	print(' ')
	print('2: Knew the victim')
	sleep(.5)
	print(' ')
	questionAnswer = input('Type your answer here: ')
	print(' ')
	
	if questionAnswer.lower() == 'went into the apartment' or questionAnswer == '1' or questionAnswer.lower() == '1: went into the apartment':
		print('Phoenix')
		currentQuestion = 0
		
	elif questionAnswer.lower() == 'knew the victim' or questionAnswer == '2' or questionAnswer.lower() == '2: knew the victim':
		print('Phoenix:')
		dialogue("Tell me, isn't it true that you knew the victim? \u001b[38;5;220m >> ")
		dialogue("""In fact, you were one of her "sugar daddies"! \u001b[38;5;220m >> """)
		dialogue("Be frank with us, Mr. Sahwit! \u001b[38;5;220m >> ")
		
		print('Sahwit:')
		dialogue("""Hmph. "Frank"? \u001b[38;5;220m >> """)
		dialogue("""I'm always "Frank"! \u001b[38;5;220m >> """)
		
		print('Payne:')
		dialogue("Your Honor. \u001b[38;5;220m >> ")
		dialogue("We have complete records of the victim's relationships. \u001b[38;5;220m >> ")
		dialogue("Mr. Frank Sahwit does not appear anywhere. \u001b[38;5;220m >> ")
		
		print("Phoenix:")
		dialogue("Huh? \u001b[38;5;220m >> ")
		dialogue("Oh, really? \u001b[38;5;220m >> ")
		
		print('Judge:')
		dialogue("""Please, Mr. Wright… Is "Huh" the best response you can muster up? \u001b[38;5;220m >> """)
		dialogue("Try to refrain from making off-the-cuff accusations in the future. \u001b[38;5;220m >> ")
		
		print('Phoenix:')
		dialogue("Y-yes, Your Honor. \u001b[38;5;220m >> ")
		dialogue("Let me think this over. \u001b[38;5;220m >> ")
		
	else:
		print('Phoenix:')
		dialogue(tBlue + "(Wait what was I thinking about? Oh right!) \u001b[38;5;220m >> ")
		
# Phoenix:
dialogue("You're lying! \u001b[38;5;220m >> ")
dialogue("You were inside the apartment on the day of the murder! \u001b[38;5;220m >> ")

print('Sahwit:')
dialogue("Oh yeah? \u001b[38;5;220m >> ")
dialogue("Prove it! Prove I went in there! \u001b[38;5;220m >> ")

print('Phoenix:')
dialogue("I'll do better than that! \u001b[38;5;220m >> ")
dialogue("I can prove you were the one who killed her! \u001b[38;5;220m >> ")
dialogue("You struck her with the clock, and the shock of the blow triggered the clock's voice! \u001b[38;5;220m >> ")
dialogue("That was the sound you heard! \u001b[38;5;220m >> ")

print('Audience:')
print("*conversing*")
print(' ')
sleep(.5)

print('*Gavel Slam*')
print(' ')
sleep(.225)
print('*Gavel Slam')
print(' ')
sleep(.255)

print('Judge:')
dialogue("Order in the court! \u001b[38;5;220m >> ")
dialogue("Intriguing. \u001b[38;5;220m >> ")
dialogue("Please continue, Mr. Wright. \u001b[38;5;220m >> ")

print('Phoenix:')
dialogue("Yes, Your Honor. \u001b[38;5;220m >> ")
dialogue("Mr. Sahwit. \u001b[38;5;220m >> ")
dialogue("The sound must have left quite an impression on you. \u001b[38;5;220m >> ")
dialogue("Understandable, since the murder weapon spoke just as you hit the victim! \u001b[38;5;220m >> ")
dialogue("That voice was burned into your mind. \u001b[38;5;220m >> ")
dialogue("That's why you were so certain about the time! \u001b[38;5;220m >> ")

print('Payne:')
print("""Objection!""")
print(' ')
sleep(.5)
dialogue("W-w-what's the meaning of this? \u001b[38;5;220m >> ")
dialogue("This is all baseless conjecture! \u001b[38;5;220m >> ")

print('Phoenix:')
dialogue("Baseless…? \u001b[38;5;220m >> ")
dialogue("Just look at the witness's face! \u001b[38;5;220m >> ")

print('Sahwit:')
dialogue("Ngh… grrrah!")

print('Judge:')
dialogue("Would the witness care to elaborate? \u001b[38;5;220m >> ")
dialogue("Did you strike the victim with the clock? \u001b[38;5;220m >> ")

print('Sahwit:')
dialogue("I… I…! \u001b[38;5;220m >> ")
dialogue("That… that day… \u001b[38;5;220m >> ")
dialogue("I… I never! \u001b[38;5;220m >> ")
dialogue("Look… I… the clock… \u001b[38;5;220m >> ")
dialogue("I heard, no! \u001b[38;5;220m >> ")
dialogue("I mean, I saw…Saw… nggg! \u001b[38;5;220m >> ")
dialogue("Gwaaaaaaaaaaaaah! \u001b[38;5;220m >> ")
dialogue("Shutupshutupshutup! \u001b[38;5;220m >> ")
dialogue("I hate you! \u001b[38;5;220m >> ")
dialogue("I-it was him, I tell you! \u001b[38;5;220m >> ")
dialogue("I saw him! \u001b[38;5;220m >> ")
dialogue("H-he killed her and he should burn! Burn! \u001b[38;5;220m >> ")
dialogue("Give him death! \u001b[38;5;220m >> ")

print('Judge:')
dialogue("Order! \u001b[38;5;220m >> ")
dialogue("Order in the court I say! \u001b[38;5;220m >> ")

print('Payne:')
dialogue("Your Honor, a-a moment please! \u001b[38;5;220m >> ")
dialogue("There isn't a shred of evidence supporting the defense's claims! \u001b[38;5;220m >> ")

print('Judge:')
dialogue("Mr. Wright! \u001b[38;5;220m >> ")

print('Phoenix:')
dialogue("Your Honor?")

print('Judge:')
dialogue("You claim the sound the witness heard came from the clock… \u001b[38;5;220m >> ")
dialogue("Do you have any evidence? \u001b[38;5;220m >> ")

print('Phoenix:')
dialogue(tBlue + "(The whole case is riding on this!) \u001b[38;5;220m >> ")
dialogue(tBlue + "(I'd better think it through carefully!) \u001b[38;5;220m >> ")
dialogue("Yes, Your Honor. \u001b[38;5;220m >> ")

while currentQuestion != 0:
	dialogue("The sound Mr. Sahwit heard was definitely this clock. A fact which is clear if you simply…  \u001b[38;5;220m >> ")
	print("1: Examine the clock's batteries")
	sleep(.5)
	print(' ')
	print('2: Ask the neighbors')
	sleep(.5)
	print(' ')
	print('3: Try sounding the clock')
	sleep(.5)
	print(' ')
	questionAnswer = input('Type your answer here: ')
	print(' ')
	
	if questionAnswer.lower() == "examine the clock's batteries" or questionAnswer == '1' or questionAnswer.lower() == "1: examine the clock's batteries":
		print('Phoenix:')
		dialogue("All you have to do is examine the batteries! \u001b[38;5;220m >> ")
        
		print('Judge:')
		dialogue("Indeed? The batteries are… \u001b[38;5;220m >> ")
		dialogue("…in the right way. \u001b[38;5;220m >> ")
		dialogue("The clock seems to be working fine. \u001b[38;5;220m >> ")
		dialogue("What exactly did you mean, Mr. Wright? \u001b[38;5;220m >> ")
        
		print('Phoenix:')
		dialogue("Yes, the clock was working fine! \u001b[38;5;220m >> ")
        
		print('Payne:')
		dialogue("Yes, and…? \u001b[38;5;220m >> ")
        
		print('Phoenix:')
		dialogue("… Umm, I'm sorry, I think I got confused back there with all those testimonies. \u001b[38;5;220m >> ")
        
		print('Judge:')
		dialogue("Mr. Wright! \u001b[38;5;220m >> ")
		dialogue("I expect more from a lawyer in this court. \u001b[38;5;220m >> ")
		dialogue("Even if it is your first day. \u001b[38;5;220m >> ")
		dialogue("I'm afraid I have to penalize you! \u001b[38;5;220m >> ")
		penalty()
		dialogue("Try to think things through more carefully. \u001b[38;5;220m >> ")
        
		print('Phoenix:')
		dialogue("Y-yes, Your Honor. \u001b[38;5;220m >> ")
		dialogue("As I was saying… \u001b[38;5;220m >> ")
        
	elif questionAnswer.lower() == 'ask the neighbors' or questionAnswer == '2' or questionAnswer.lower() == '2: ask the neighbors':
		print('Phoenix:')
		dialogue("All you have to do is talk to the victim's neighbors! \u001b[38;5;220m >> ")
		
		print('Judge:')
		dialogue("Talk to the neighbors…? \u001b[38;5;220m >> ")
		
		print('Phoenix:')
		dialogue("I'm sure one of them heard the clock tell the time when the incident occurred! \u001b[38;5;220m >> ")
		
		print('Judge:')
		dialogue("I see… \u001b[38;5;220m >> ")
		dialogue("Does the prosecution have anything to say, Mr. Payne? \u001b[38;5;220m >> ")
		
		print('Payne:')
		dialogue("We have already made all the necessary inquiries. \u001b[38;5;220m >> ")
		dialogue("Everyone living near the victim's apartment was out at the time of the murder. \u001b[38;5;220m >> ")
		dialogue("Furthermore, even if a neighbor had heard the clock, that would not prove that Mr. Sahwit had heard anything. \u001b[38;5;220m >> ")
		
		print('Judge:')
		dialogue("Hmm… That is true. \u001b[38;5;220m >> ")
		dialogue("I believe you may be wrong, Mr. Wright. \u001b[38;5;220m >> ")
		dialogue("You'll receive a penalty for that, unfortunately. \u001b[38;5;220m >> ")
		penalty()
		
		print('Phoenix:')
		dialogue("I-I'm sorry, Your Honor! \u001b[38;5;220m >> ")
		dialogue("Let me think about it again! \u001b[38;5;220m >> ")
	
	elif questionAnswer.lower() == 'try sounding the clock' or questionAnswer == '3' or questionAnswer.lower() == '3: try sounding the clock':
		print('Phoenix:')
		currentQuestion = 0
	
	else:
		print('Phoenix:')
		dialogue(tBlue + "(Wait what was I thinking about? Oh right!) \u001b[38;5;220m >> ")
		
#Phoenix:
dialogue("Let's sound the clock now, here in this court. \u001b[38;5;220m >> ")
dialogue("Your Honor, may I have the clock? \u001b[38;5;220m >> ")
dialogue("I ask the court to listen very carefully… \u001b[38;5;220m >> ")

print('Alarm clock:')
print(tRed + "…*beep*…")
sleep(.25)
dialogue(tGreen + "[I think it's 8:25.] \u001b[38;5;220m >> ")

print('Judge:')
dialogue("That certainly is a strange way to announce the time. \u001b[38;5;220m >> ")

print('Phoenix:')
dialogue("""Well, he is "The Thinker," after all. \u001b[38;5;220m >> """)

print('Judge:')
dialogue("So, we've heard the clock. \u001b[38;5;220m >> ")
dialogue("What are your conclusions, Mr. Wright? \u001b[38;5;220m >> ")

print('Phoenix:')
dialogue("Mr. Payne… can you tell me what time it is now? \u001b[38;5;220m >> ")

print('Payne:')
dialogue("It's 11:25… \u001b[38;5;220m >> ")
dialogue("Ack! \u001b[38;5;220m >> ")

print('Phoenix:')
dialogue("As you can see, this clock is exactly three hours slow! \u001b[38;5;220m >> ")
dialogue("Precisely the discrepancy between what Mr. Sahwit heard and the actual time of death! \u001b[38;5;220m >> ")
dialogue("So, Mr. Sahwit… \u001b[38;5;220m >> ")
dialogue("Try to talk your way out of this one! \u001b[38;5;220m >> ")

print('Sahwit:')
dialogue("…")
dialogue("…Hah! \u001b[38;5;220m >> ")
dialogue("Hah hah! \u001b[38;5;220m >> ")
dialogue("You forgot one thing! \u001b[38;5;220m >> ")

print('Phoenix:')
dialogue(tBlue + "(Uh oh… what's he talking about…?) \u001b[38;5;220m >> ")

print('Sahwit:')
dialogue("While it may seem like that clock IS running three hours slow… \u001b[38;5;220m >> ")
dialogue("It proves nothing! \u001b[38;5;220m >> ")
dialogue("How do you know it was running three days slow on \u001b[31mthe day of the murder\033[m!? \u001b[38;5;220m >> ")
dialogue("If you can't prove that, you don't have a case! \u001b[38;5;220m >> ")

print('Phoenix:')
dialogue("…! \u001b[38;5;220m >> ")
dialogue(tBlue + "(He's right!) \u001b[38;5;220m >> ")
dialogue(tBlue + "(How am I going to prove that!?) \u001b[38;5;220m >> ")
dialogue(tBlue + "(Dammit! I was so close!) \u001b[38;5;220m >> ")

print('Judge:')
dialogue("Mr. Wright? \u001b[38;5;220m >> ")
dialogue("It seems you lack the critical evidence to support your claim. \u001b[38;5;220m >> ")

print('Phoenix:')
dialogue("…! \u001b[38;5;220m >> ")
dialogue("Yes, Your Honor. \u001b[38;5;220m >> ")

print('Judge:')
dialogue("This means I cannot let you indict the witness. \u001b[38;5;220m >> ")
dialogue("Unfortunately… \u001b[38;5;220m >> ")
dialogue("This ends the cross-examination of Mr. Frank Sahwit. \u001b[38;5;220m >> ")

print('Sahwit:')
dialogue("I come all the way down here to testify, and look what happens! \u001b[38;5;220m >> ")
dialogue("You treat me like a criminal! \u001b[38;5;220m >> ")
dialogue("A criminal! \u001b[38;5;220m >> ")
dialogue("You lawyers are all slime! \u001b[38;5;220m >> ")

print('Phoenix:')
dialogue(tBlue + "(Grr! I almost had him!) \u001b[38;5;220m >> ")
dialogue(tBlue + "(Sorry, Larry… I failed you.) \u001b[38;5;220m >> ")
dialogue(tBlue + "(There's nothing I can do about it now…) \u001b[38;5;220m >> ")

print('.')
sleep(1)
print('.')
sleep(1)
print('.')
sleep(0.5)

print('Mia:')
dialogue("Not so fast, Mr. Sahwit! \u001b[38;5;220m >> ")

print('Phoenix:')
dialogue("Mia! I mean, Chief! \u001b[38;5;220m >> ")

print('Mia:')
dialogue("Listen up, Wright! \u001b[38;5;220m >> ")
dialogue("Don't throw this one away, not like this! Think! \u001b[38;5;220m >> ")

print('Phoenix:')
dialogue("But, Chief, it's over. \u001b[38;5;220m >> ")
dialogue("I can't prove the clock was slow the day of the murder! \u001b[38;5;220m >> ")
dialogue("Nobody can prove that! \u001b[38;5;220m >> ")

print('Mia:')
dialogue("Um… well, yes. \u001b[38;5;220m >> ")
dialogue("But that doesn't mean you can't still win! \u001b[38;5;220m >> ")
dialogue("Try thinking out of the box! \u001b[38;5;220m >> ")
dialogue("Don't waste time doubting the facts. \u001b[38;5;220m >> ")
dialogue("Assume the clock was three hours slow and… \u001b[38;5;220m >> ")
dialogue("Think through it! \u001b[38;5;220m >> ")
dialogue("""Ask yourself, \u001b[31m"Why was the clock three hours slow"\033[m? \u001b[38;5;220m >> """)
dialogue("Figure out the reason, and you'll have your proof! \u001b[38;5;220m >> ")
dialogue("Right, Wright? \u001b[38;5;220m >> ")
currentQuestion = 1
while currentQuestion != 0:
	dialogue("Can you think of a reason as to why the clock would be three hours slow? \u001b[38;5;220m >> ")
	print('1: Yes')
	sleep(.5)
	print(' ')
	print('2: No')
	sleep(.5)
	print(' ')
	questionAnswer = input('Type your answer here: ')
	print(' ')
	
	if questionAnswer.lower() == 'yes' or questionAnswer == '1' or questionAnswer.lower() == '1: yes' or questionAnswer.lower() == 'y':
		print('Phoenix:')
		dialogue("… Wait! \u001b[38;5;220m >> ")
		dialogue("Maybe I can prove it! \u001b[38;5;220m >> ")
		
		print('Mia:')
		dialogue("You must have evidence somewhere that can prove it, Wright! \u001b[38;5;220m >> ")
		dialogue("Find it and let them have it! \u001b[38;5;220m >> ")
		
		print('Judge:')
		dialogue("Well, Mr. Wright? \u001b[38;5;220m >> ")
		dialogue("You say the clock was already running slow on the day of the murder… \u001b[38;5;220m >> ")
		dialogue("Have you found evidence to support this claim? \u001b[38;5;220m >> ")
		
		print('Phoenix:')
		dialogue("Of course. \u001b[38;5;220m >> ")
		dialogue("There is a piece of evidence in the Court Record that can prove my claim beyond a doubt! \u001b[38;5;220m >> ")
		
		print('Sahwit:')
		dialogue("Hah! \u001b[38;5;220m >> ")
		dialogue("Tough words! \u001b[38;5;220m >> ")
		dialogue("Let's see you pull this one off! \u001b[38;5;220m >> ")
		currentQuestion = 0
		
	elif questionAnswer.lower() == 'no' or questionAnswer == '2' or questionAnswer.lower() == '2: no' or questionAnswer.lower() == 'n':
		print('Phoenix:')
		dialogue("H-how am I supposed to know that!? \u001b[38;5;220m >> ")
		
		print('Mia:')
		dialogue("I know you can figure it out! \u001b[38;5;220m >> ")
		dialogue("There must be some evidence in the Court Record… \u001b[38;5;220m >> ")
		dialogue("Something that can show why that clock was three hours slow! \u001b[38;5;220m >> ")
		dialogue("Find it, and he won't have a foot to stand on! \u001b[38;5;220m >> ")
		
		print('Judge:')
		dialogue("Mr. Wright? \u001b[38;5;220m >> ")
		
		print('Phoenix:')
		dialogue("Y-y-yes, Your Honor! \u001b[38;5;220m >> ")
		
		print('Judge:')
		dialogue("You say the clock was already running slow on the day of the murder… \u001b[38;5;220m >> ")
		dialogue("Do you have evidence to prove this? \u001b[38;5;220m >> ")
		
		print('Phoenix:')
		dialogue(tBlue + "(This is it… all or nothing!) \u001b[38;5;220m >> ")
		dialogue("Yes, Your Honor. \u001b[38;5;220m >> ")
		dialogue("I believe I have the evidence that can prove my claim! \u001b[38;5;220m >> ")
		
		print('Sahwit:')
		dialogue("Hah hah! \u001b[38;5;220m >> ")
		dialogue("I'd like to see THAT! \u001b[38;5;220m >> ")
		currentQuestion = 0
		
	else:
		print('Phoenix:')
		dialogue(tBlue + "(Wait what was I thinking about? Oh right!) \u001b[38;5;220m >> ")
		
		print('Mia:')
		
print('Judge:')
crossExamination = 1
while crossExamination == 1:
	dialogue("Let's see this evidence that proves why the clock was running slow! \u001b[38;5;220m >> ")
	presentEvidence()
	if presentedItem.lower() == 'passport':
		print('Phoenix:')
		print("""Take that!""")
		print(' ')
		sleep(.5)
		crossExamination = 0
		presentedItem = '''Put something in here that won't appear in your evidence or profile list'''
		continue
	else:
		print('Phoenix:')
		print("""Take that!""")
		print(' ')
		sleep(.5)
		
		print('Judge:')
		dialogue("Um, excuse me. \u001b[38;5;220m >> ")
		dialogue("This proves your claim… how? \u001b[38;5;220m >> ")
		dialogue("I can't see what that evidence has to do with the clock. \u001b[38;5;220m >> ")
		
		print('Phoenix:')
		dialogue(tBlue + "(D'oh! That wasn't it!) \u001b[38;5;220m >> ")
		dialogue("One more chance… \u001b[38;5;220m >> ")
		dialogue("Give me just one more chance! \u001b[38;5;220m >> ")
		
		print('Judge:')
		dialogue("Alright, Mr. Wright, but time is not on your side. \u001b[38;5;220m >> ")
		dialogue("Be quick about it. \u001b[38;5;220m >> ")

#Phoenix:
dialogue("The victim had just returned home from abroad the day before the murder. \u001b[38;5;220m >> ")
dialogue("As we all know, the time difference between here and Paris is nine hours! \u001b[38;5;220m >> ")
dialogue("When it's 4:00 PM here, it's 1:00 AM the next day there. \u001b[38;5;220m >> ")
dialogue("The clock wasn't three hours slow, it was nine hours fast! \u001b[38;5;220m >> ")
dialogue("The victim hadn't reset her clock since returning home! \u001b[38;5;220m >> ")
dialogue("That's why the time you heard when you struck her dead in her apartment was wrong! \u001b[38;5;220m >> ")
dialogue("Proof enough for you, Mr. Sahwit? \u001b[38;5;220m >> ")
dialogue("Or should I say… Mr. Did It! \u001b[38;5;220m >> ")

print('Sahwit:')
dialogue("Ngh! \u001b[38;5;220m >> ")
dialogue("…! *faints* \u001b[38;5;220m >> ")

print('Judge:')
dialogue("O-order! Order, I say! \u001b[38;5;220m >> ")

print('.')
sleep(1)
print('.')
sleep(1)
print('.')
sleep(0.5)

print('Judge:')
dialogue("Well… \u001b[38;5;220m >> ")
dialogue("This case has certainly turned out differently than we all expected. \u001b[38;5;220m >> ")
dialogue("Mr. Payne… your witness? \u001b[38;5;220m >> ")

print('Payne:')
dialogue("He… er… he was arrested and has been taken away, Your Honor. \u001b[38;5;220m >> ")

print('Judge:')
dialogue("Very well. \u001b[38;5;220m >> ")
dialogue("Mr. Wright? \u001b[38;5;220m >> ")

print('Phoenix:')
dialogue("Yes, Your Honor. \u001b[38;5;220m >> ")

print('Judge:')
dialogue("I have to say, I'm impressed. \u001b[38;5;220m >> ")
dialogue("I don't think I've ever seen someone complete a defense so quickly… \u001b[38;5;220m >> ")
dialogue("and find the true culprit at the same time! \u001b[38;5;220m >> ")

print('Phoenix:')
dialogue("Thank you, Your Honor. \u001b[38;5;220m >> ")

print('Judge:')
dialogue("At this point, this is only a formality, but… \u001b[38;5;220m >> ")
dialogue("This court finds the defendant, Mr. Larry Butz… \u001b[38;5;220m >> ")
sleep(.5)
print(' ')
print('Not Guilty')
print(' ')
print(' ')
sleep(.5)

print('Judge:')
dialogue("And with that… \u001b[38;5;220m >> ")
dialogue("The court is adjourned. \u001b[38;5;220m >> ")

print('.')
sleep(1)
print('.')
sleep(1)
print('.')
sleep(0.5)

print('Phoenix:')
dialogue("It turns out that Frank Sahwit was a common burglar! \u001b[38;5;220m >> ")
dialogue("He posed as a newspaper sales-man to check and see when people were out of the house! \u001b[38;5;220m >> ")
dialogue("That day… \u001b[38;5;220m >> ")
dialogue("When Larry went to her apartment, the victim wasn't home. \u001b[38;5;220m >> ")
dialogue("After he left, Mr. Sahwit let himself in to do his dirty work! \u001b[38;5;220m >> ")
dialogue("While he was searching her place, the victim returned! \u001b[38;5;220m >> ")
dialogue("Flustered, Mr. Sahwit grabbed the nearest blunt object he could find… \u001b[38;5;220m >> ")
sleep(2.5)

canViewCourtRecord = 0
dialogue(tGreen + "Date: August 3, 2:32 PM, District Court, Defendant Lobby No.2 \u001b[38;5;220m >> ")
canViewCourtRecord = 1

print('Phoenix:')
dialogue(tBlue + "(Whew… I still can't believe we won!) \u001b[38;5;220m >> ")

print('Mia:')
dialogue("Wright! \u001b[38;5;220m >> ")
dialogue("Good job in there! Congratulations! \u001b[38;5;220m >> ")

print('Phoenix:')
dialogue("Th-thanks, Chief. \u001b[38;5;220m >> ")
dialogue("I owe it all to you. \u001b[38;5;220m >> ")

print('Mia')
dialogue("Not at all, not at all! \u001b[38;5;220m >> ")
dialogue("You fought your own battles in there. \u001b[38;5;220m >> ")
dialogue("It's been a while since I've seen a trial end on such a satisfying note! \u001b[38;5;220m >> ")

print('Phoenix:')
dialogue("(I've never seen the chief looking this happy…) \u001b[38;5;220m >> ")
dialogue("(If she's this glad, imagine how Larry must feel!) \u001b[38;5;220m >> ")

print('Butz:')
dialogue("My life is over… \u001b[38;5;220m >> ")

print('Phoenix:')
dialogue("Larry! \u001b[38;5;220m >> ")
dialogue("You're supposed to be happy! \u001b[38;5;220m >> ")
dialogue("What's wrong now!? \u001b[38;5;220m >> ")

print('Butz:')
dialogue("Aww, Nick… \u001b[38;5;220m >> ")
dialogue("Don't worry 'bout me! \u001b[38;5;220m >> ")
dialogue("I'll be dead and gone soon! \u001b[38;5;220m >> ")

print('Phoenix:')
dialogue("Good! Wait, no! I mean… \u001b[38;5;220m >> ")
dialogue("Bad! \u001b[38;5;220m >> ")
dialogue("Bad bad bad! \u001b[38;5;220m >> ")
dialogue("Larry, you're innocent! \u001b[38;5;220m >> ")
dialogue("The case is closed. \u001b[38;5;220m >> ")

print('Butz:')
dialogue("… \u001b[38;5;220m >> ")
dialogue("But… but my Cindy-windy's gone, man! \u001b[38;5;220m >> ")
dialogue("Gone forever! \u001b[38;5;220m >> ")

print('Phoenix:')
dialogue(tBlue + "(Larry, she was a…) \u001b[38;5;220m >> ")
dialogue(tBlue + "(Nah… Never mind.) \u001b[38;5;220m >> ")

print('Mia:')
dialogue("Congratulations, Harry! \u001b[38;5;220m >> ")

print('Butz:')
dialogue("H-Harry…? \u001b[38;5;220m >> ")

print('Mia:')
dialogue("Yes, you! \u001b[38;5;220m >> ")
dialogue("I can practically see the headlines now: \u001b[38;5;220m >> ")
dialogue(""""Harry Butz, Innocent!" \u001b[38;5;220m >> """)

print('Butz:')
dialogue("Heh… um… thanks! \u001b[38;5;220m >> ")
dialogue("I really owe you one. \u001b[38;5;220m >> ")
dialogue("I won't forget this, ever! \u001b[38;5;220m >> ")
dialogue("Let's celebrate! Dinner? Movie? My treat! \u001b[38;5;220m >> ")

print('Mia:')
dialogue("Oh, no, I couldn't. \u001b[38;5;220m >> ")

print('Phoenix:')
dialogue("(Hey, I was the one who got you off the hook!) \u001b[38;5;220m >> ")

print('Butz:')
dialogue("Oh, hey! \u001b[38;5;220m >> ")
dialogue("H-here, take this! It's a present! \u001b[38;5;220m >> ")

print('Mia:')
dialogue("A present? For me? Wait… \u001b[38;5;220m >> ")
dialogue("Wasn't this the evidence that… \u001b[38;5;220m >> ")

print('Butz:')
dialogue("Actually, I made this clock for her! \u001b[38;5;220m >> ")
dialogue("I made one for her and one for me. \u001b[38;5;220m >> ")

print('Mia:')
dialogue("R-really? You? \u001b[38;5;220m >> ")
dialogue("You made this? \u001b[38;5;220m >> ")
dialogue("… \u001b[38;5;220m >> ")
dialogue("Well, thank you. \u001b[38;5;220m >> ")
dialogue("I'll keep it as a memento. \u001b[38;5;220m >> ")

print('Butz:')
dialogue("Yo, Nick… \u001b[38;5;220m >> ")
dialogue("Can you believe it? \u001b[38;5;220m >> ")
dialogue("I was so into that chick… \u001b[38;5;220m >> ")
dialogue("And… and she was just playing me for a fool! \u001b[38;5;220m >> ")
dialogue("Don't that make you wanna just cry? \u001b[38;5;220m >> ")
dialogue("*sob* \u001b[38;5;220m >> ")

print('Phoenix:')
dialogue("Larry…")

print('Mia:')
dialogue("… \u001b[38;5;220m >> ")
dialogue("Are you so sure? \u001b[38;5;220m >> ")

print('Butz:')
dialogue("Ex-squeeze me? \u001b[38;5;220m >> ")

print('Mia:')
dialogue("I think she thought quite a lot of you, in her own way. \u001b[38;5;220m >> ")

print('Butz:')
dialogue("Nah, you don't gotta sympathize with me, 'sokay. \u001b[38;5;220m >> ")

print('Mia:')
dialogue("Oh, I'm not just sympathizing, really. \u001b[38;5;220m >> ")
dialogue("Isn't that right, Wright? \u001b[38;5;220m >> ")
dialogue("Don't you have something to show your friend? \u001b[38;5;220m >> ")
dialogue("Something that proves how she felt about him? \u001b[38;5;220m >> ")

print('Phoenix:')
dialogue("H-huh? \u001b[38;5;220m >> ")
dialogue("Oh, yeah, right! \u001b[38;5;220m >> ")
crossExamination = 1
while crossExamination == 1:
	dialogue(tBlue + "(What the heck is she talking about?) \u001b[38;5;220m >> ")
	presentEvidence()
	if presentedItem.lower() == 'statue/the thinker':
		print('Phoenix:')
		print("""Take that!""")
		print(' ')
		sleep(.5)
		dialogue("Check this out, Larry. \u001b[38;5;220m >> ")
		dialogue("Proof Positive you weren't just some chump to her. \u001b[38;5;220m >> ")
		
		print('Butz:')
		dialogue("Huh…? \u001b[38;5;220m >> ")
		dialogue("What about that clock? \u001b[38;5;220m >> ")
		
		print('Phoenix:')
		dialogue("This is the clock YOU made for her, Larry! \u001b[38;5;220m >> ")
		dialogue("And she took it with her when she traveled. \u001b[38;5;220m >> ")
		
		print('Butz:')
		dialogue("Whatever. \u001b[38;5;220m >> ")
		dialogue("She probably just needed a clock, that's all. \u001b[38;5;220m >> ")

		print('Phoenix:')
		dialogue("You think so? \u001b[38;5;220m >> ")
		dialogue("It's a pretty heavy clock to take traveling. \u001b[38;5;220m >> ")
		
		print('Butz:')
		dialogue("… \u001b[38;5;220m >> ")
		
		print('Phoenix:')
		dialogue("Well, make of it what you will. \u001b[38;5;220m >> ")
		
		print('Butz:')
		dialogue("… Hey, Nick. \u001b[38;5;220m >> ")
		dialogue("I'm glad I asked you to be my lawyer. \u001b[38;5;220m >> ")
		dialogue("Really, I am. \u001b[38;5;220m >> ")
		dialogue("Thanks. \u001b[38;5;220m >> ")
		
		print('Phoenix:')
		dialogue(tBlue + "(Hope that made him feel a little better…) \u001b[38;5;220m >> ")		
		crossExamination = 0
		presentedItem = '''Put something in here that won't appear in your evidence or profile list'''
		continue
	else:
		print('Phoenix:')
		print("""Take that!""")
		print(' ')
		sleep(.5)
		dialogue("Here you go, Larry. Proof. \u001b[38;5;220m >> ")
		
		print('Butz:')
		dialogue("… \u001b[38;5;220m >> ")
		dialogue("Eh… heh heh? \u001b[38;5;220m >> ")
		dialogue("It's okay, Nick. \u001b[38;5;220m >> ")
		dialogue("Don't worry about me. \u001b[38;5;220m >> ")
		dialogue("I'll forget about her soon enough. \u001b[38;5;220m >> ")
		dialogue("Look, I'm gonna head home. \u001b[38;5;220m >> ")
		dialogue("Thanks a ton, eh? \u001b[38;5;220m >> ")
		
		print('Phoenix:')
		dialogue(tBlue + "(Guess that wasn't the right thing to show him…) \u001b[38;5;220m >> ")
		crossExamination = 0
		continue

print('Mia:')
dialogue("Wright? \u001b[38;5;220m >> ")
dialogue("I hope you see the importance of evidence now. \u001b[38;5;220m >> ")
dialogue("Also, hopefully you realize, things change depending on how you look at them. \u001b[38;5;220m >> ")
dialogue("People, too. \u001b[38;5;220m >> ")
dialogue("We never really know if our clients are guilty or innocent. \u001b[38;5;220m >> ")
dialogue("All we can do is believe in them. \u001b[38;5;220m >> ")
dialogue("And in order to believe in them, you have to believe in yourself. \u001b[38;5;220m >> ")
dialogue("Wright… \u001b[38;5;220m >> ")
dialogue("Listen. Learn. Grow strong. \u001b[38;5;220m >> ")
dialogue("Never let go of what you believe in. Never. \u001b[38;5;220m >> ")

print('.')
sleep(1)
print('.')
sleep(1)
print('.')
sleep(0.5)

print('Mia:')
dialogue("Well, I think our work here is done! \u001b[38;5;220m >> ")
dialogue("Shall we be off? \u001b[38;5;220m >> ")

print('Phoenix:')
dialogue("Yeah, I guess so! \u001b[38;5;220m >> ")

print('Mia:')
dialogue("Say, how about dinner. On me? \u001b[38;5;220m >> ")
dialogue("We'll drink a toast to innocent Butz! \u001b[38;5;220m >> ")

print('Phoenix:')
dialogue("Yeah! \u001b[38;5;220m >> ")

print('Mia:')
dialogue("Oh, speaking of Harry… \u001b[38;5;220m >> ")
dialogue("You were saying part of why you became a lawyer was because of him. \u001b[38;5;220m >> ")

print('Phoenix:')
dialogue("Er, yeah. \u001b[38;5;220m >> ")
dialogue("Part, at least. \u001b[38;5;220m >> ")

print('Mia:')
dialogue("You'll have to tell me more about it sometime! \u001b[38;5;220m >> ")
dialogue("Maybe… over drinks? \u001b[38;5;220m >> ")

print('.')
sleep(1)
print('.')
sleep(1)
print('.')
sleep(0.5)

print('Phoenix:')
dialogue("And so, my first trial came to a close. \u001b[38;5;220m >> ")
dialogue("""Larry slapped me on the back and said, "Gee, Nick, it's good to have friends!" \u001b[38;5;220m >> """)
dialogue("But I'm pretty sure he's not going to pay us. \u001b[38;5;220m >> ")
dialogue("Unless you count the clock he gave Mia. \u001b[38;5;220m >> ")
dialogue("… \u001b[38;5;220m >> ")
dialogue("I didn't know it then… \u001b[38;5;220m >> ")
dialogue("but that clock was soon going to be at the center of another incident. \u001b[38;5;220m >> ")
dialogue("And my promise to tell the chief about me and Larry… \u001b[38;5;220m >> ")
dialogue("would be one promise that I wouldn't be able to keep. \u001b[38;5;220m >> ")
