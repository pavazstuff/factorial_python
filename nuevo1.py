
class Mate:
	def calcularFactorial(self, n):
		if n == 0:
			return 1
		else:
			return n * self.calcularFactorial(n-1)
		

def something():
	x = Mate()
	print x.calcularFactorial(5)
	
if __name__ == "__main__":
	something()