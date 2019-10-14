# "import" allows you to ask the program to find a certain module of your preference and extracts it from the python library to be used in your program
# "as plt" gives this module a shorthand to be declared
import matplotlib.pyplot as plt 

i=5
num=0

x=[]
y=[]

for i in range (1,5):
	num = int(input("Input a number"))
	x.append(num)
	y.append(num+2)
	
	  
  
def kg_plot_graph(x,y):
	title = "y against x Graph" #gives the graph a title
	
	#gives the x and y axis a label
	xlab = "x"
	ylab = "y"
	model_title = title
	print("\ncreating plot ....\n") 
	output_line = plt.plot(x,y,'r-', label='Trend') #plots the graph using the x and y values in the list and displays the label for the line
	plt.axis('scaled') #scales the graph to an appropriate ratio
	plt.xlabel(xlab) 
	plt.ylabel(ylab)
	plt.legend()
	plt.title("%s\nLeong Kah Gene 2019" %(model_title)) 
	plt.ion() 
	plt.show()	#displays the created graph
	input("press enter to close plot ... ")
	plt.close('all') #closes the function upon user's input

kg_plot_graph(x,y) #calls the plotting graph function
