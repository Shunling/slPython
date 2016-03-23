
import numpy as np

def isMatch(a,b):

	x = len(a) + 1
	y = len(b) + 1
	dp = np.zeros((x,y))
	dp[0][0] = 1
	for j in range(1,y/2):
		if b[2*j - 1] == '*':
			dp[0][2*j] =  1	

	for i in range(1,x):
		for j in range(i,y):		
			if b[j - 1] == a[i - 1] or b[j - 1] == '.':
				dp[i][j] = dp[i - 1][j - 1]			
					
			elif b[j - 1] == '*':
				if dp[i][j - 1] or (j > 2 and dp[i - 1][j - 2]): 
					dp[i][j] = 1
	print dp
	
	if dp[x - 1][y - 1]:
		return True
	else: return False

print isMatch("aaaa","c*a*a*b*a")



