from random import randint

class QLearning():
	def __init__ (self):
		# constant
		self.y = 0.8
		# declation of actions posssible , actions positions 
		self.Actions = self.ActionPositions = self.Actions2 = self.ActionPositions2 = []
		# rooms available in the building (environment)
		self.rooms = ["a" , "b", "c", "d", "e", "f"]
		# the two arrays = q which is initialized to zeros and r the has some values assigned in it.
		self.R = [["-" for x in range (6)] for i in range (6)]
		self.Q = [[0 for x in range(6)] for i in range(6)]
      # value assignment in the array R
		self.R[0][4] = 0
		self.R[4][0] = 0
		self.R[1][3] = 0
		self.R[3][1] = 0
		self.R[1][5] = 100
		self.R[2][3] = 0
		self.R[3][2] = 0
		self.R[3][4] = 0
		self.R[4][3] = 0
		self.R[4][5] = 100
		self.R[5][5] = 100
		self.R[5][1] = 0
		self.R[5][4] = 0		
     # printing of the Q nd R array.
		print ("\nThe Current R Matrix with some values")
		for i in self.R:
			for j in i:
				print (j, end = "\t")
			print ()
      # function printQ declaration
		self.printQ()

	def printQ(self):
		print ("\nThe Current Q Matrix, first initialized to ZEROs")
		for i in self.Q:
			for j in i:
				print (j, end = "\t")
			print ()
			# computational starts here.
	def episode (self, currentState):

		while True:
			print ("\nCurrent State is (where you are now!!) ", self.rooms[currentState])
			# get the possible actions from where you are. the rooms one can access while at the current room
			self.Actions = [action for action in self.R[currentState] if action != "-"]
			# get the positions where the value is any other value other than "-".
			self.ActionPositions = [i for i in range(6) if self.R[currentState][i] != "-"]	
			# print the room one is able to access while at the current room
			print ("The possible (Rooms from current room) Action States from ", self.rooms[currentState], " are: ", [self.rooms[i] for i in self.ActionPositions])
			#Randomly select an action (which is the room)
			selectedAction = self.ActionPositions [randint (0, len(self.Actions) - 1)]
			# print the room selected randomly from which was your current room
			print ("The selected Room (Action state) is: ", self.rooms[selectedAction])

			print ("\nTNow take the current room (Action) as the current state")
			# get the possible actions from where you are. the rooms, one can access while at the current room.
			self.Actions2 = [action for action in self.R[selectedAction] if action != "-"]
			 # get the positions, where the value is any other value other than "-".
			self.ActionPositions2 = [i for i in range(6) if self.R[selectedAction][i] != "-"]
			# print the room one is able to access while at the current room
			print ("The possible (Rooms from current room) Action States from ", self.rooms[selectedAction], " are: ", [self.rooms[i] for i in self.ActionPositions2], end = " ")
			# calculate the reward (0-100) value in Q array (popullate the Q array with values since it was intialized to zeros at the start).
			rewards = [ self.Q[selectedAction][x] for x in self.ActionPositions2]
			print ("with Q values : ", rewards)
			self.Q[currentState][selectedAction] = round (self.R[currentState][selectedAction] + (0.8 * max (rewards)), 0)
			self.printQ()
			# if the selected room if 	F the goal is reached.
			if selectedAction == 5 : 
				print ("\nEnd of Episode\n")
				break
			else : 
				# the process continues.
				currentState = selectedAction

	# the funtion to show the path
	def testPath (self):
		print ()
		
		while True:
			room = input ("Enter Room You need the path For: ")
			if len (room) == 1 and room in self.rooms : break
		path = room + "-"
		# the room position
		roomPosition = self.rooms.index(room)
		while True:
			Actions = [action for action in self.Q[roomPosition] if action != "-"]
			bestRoom = Actions.index (max(Actions))
			path += self.rooms[bestRoom]
		# when you get to room f which is the goal room
			if bestRoom == 5:
				break
			else:
				roomPosition = bestRoom
				path += "-"
 # print the path from the room you need to the goal
		print ("The best Path is  :: ", path)


ql = QLearning();

i = 0
# the number of times the episode to loop
while i < 60:
	state = randint(0,5)
	ql.episode(state)
	i += 1
ql.testPath()