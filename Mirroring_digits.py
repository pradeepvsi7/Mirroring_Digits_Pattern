def mirror(n):
	var1 = 2
	var2 = 1
	for i in range(n):
		for j in range(n-1,i,-1):
			print(" ",end="")
		for k in range(1,var1):
			print(abs(k - var2),end="")
		var1+=2
		var2+=1
		print()
n = int(input("Enter the interger ? "))
mirror(n)
