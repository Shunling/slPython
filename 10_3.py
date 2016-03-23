
import numpy as np

def isMatch(a,b):

	dp = np.zeros((len(a) + 1,len(b) + 1))
	dp[0][0] = 1
	for j in range(1,len(b)/2 + 1):
		if b[2*j - 1] == '*':
			dp[0][2*j] =  dp[0][2*(j - 1)]

	for i in range(1,len(a) + 1):
		for j in range(1,len(b) + 1):		
			if b[j - 1] == a[i - 1] or b[j - 1] == '.':
				dp[i][j] = dp[i - 1][j - 1]			
					
			elif b[j - 1] == '*' and j > 1:
				if dp[i][j - 2] or dp[i][j - 1]:#*=0 or *=1
					dp[i][j] = 1
				elif p[j - 2] == '.' or (i > 1 and s[i - 1] == s[i - 2] and p[j - 2] == s[i - 1]): #*>1 and 
					dp[i][j] = dp[i - 1][j]


	print dp
	
	if dp[len(a)][len(b)]:
		return True
	else: return False





