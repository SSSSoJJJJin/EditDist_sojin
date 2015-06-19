###########################
### Sequence Allignment ###
### 201422455 Sojin Ahn ###
###########################



class Initial_matrix:
	def __init__(self, seq_x, seq_y):
		self.seq_x = seq_x
		self.seq_y = seq_y
		self.matrix = []

		for i in range(len(self.seq_x)+1):
			self.matrix.append([int(i)])
		for j in range(len(self.seq_y)+1):
			self.matrix[0].append(int(j))
		

class edit_dist(Initial_matrix):
	
	def scoring_matrix(self):
		
		for i in range(1,len(self.seq_x)+1):
			for j in range(1,len(self.seq_y)+1):
				temp_list = []
				temp_list.append(self.matrix[i][j-1]+1)
				temp_list.append(self.matrix[i-1][j]+1)
				if self.seq_x[i-1] == self.seq_y[j-1]:
					temp_list.append(self.matrix[i-1][j-1])
				if self.seq_x[i-1] != self.seq_y[j-1]:
					temp_list.append(self.matrix[i-1][j-1] + 1)
				self.matrix[i].append(min(temp_list))
		print 'Edit Distance : ', self.matrix[len(self.seq_x)][len(self.seq_y)]


Test1 = edit_dist("AAATTTAA","AAATTTA")
Test1.scoring_matrix()