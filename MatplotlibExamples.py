import matplotlib.pyplot as plt

year = [1950, 1970, 1990, 2010]
pop = [2.519, 3.692, 5.263, 6.972]

#Only tells what to plot.  doesnt actually show it with this function call.  Note that plot() function rerturns
#a line plot
plt.plot(year, pop)
#show th plot
plt.show()

#Scatter plot example.  Note that you have to first close the plot above before this code is executed.
#Note that when you're trying to assess if there's a correlation between two variables,
# for example, the scatter plot is the better choice
plt.scatter(year, pop)
plt.show()

#Histogram helps explore your data.  Shows the distrubution of your variables
histoexamplelist = [0,1,1,5,20,1,10, 15]
bin = 10
plt.hist(histoexamplelist, bins=bin)
plt.show()