# Pandas Plotting Syntax:

# Line Plot
DataFrame.plot.line()  # Shows trends and changes over time
df.plot(x='year', y='sales', kind='line')

# Area Plot
DataFrame.plot.area()  # Displays data series as filled areas, showing the relationship between them
df.plot(kind='area')

# Histogram
Series.plot.hist()  # Displays bars representing the data count in each interval/bin
s.plot(kind='hist', bins=10)

# Bar Chart
DataFrame.plot.bar()  # Displays data using rectangular bars
df.plot(kind='bar')

# Pie Chart
Series.plot.pie() or DataFrame.plot.pie()  # Displays data as a circular plot divided into slices, representing proportions or percentages of a whole
s.plot(kind='pie', autopct='%1.1f%%')

# Box Plot
DataFrame.plot.box()  # Displays the distribution of a dataset along with key statistical measures
df_can.plot(kind='box')

# Scatter Plot
DataFrame.plot.scatter()  # Uses Cartesian coordinates to display values for two variables
df.plot(x='Height', y='Weight', kind='scatter')


# Matplotlib Plotting Syntax:

# Line Plot
plt.plot()  # Shows trends and changes over time
plt.plot(x, y, color='red', linewidth=2)

# Area Plot
plt.fill_between()  # Display data series as filled areas
plt.fill_between(x, y1, y2, color='blue', alpha=0.5)

# Histogram
plt.hist()  # Displays bars representing the data count in each interval/bin
plt.hist(data, bins=10, color='orange', edgecolor='black')

# Bar Chart
plt.bar()  # Displays data using rectangular bars
plt.bar(x, height, color='green', width=0.5)

# Pie Chart
plt.pie()  # Displays data as a circular plot divided into slices, representing proportions or percentages of a whole
plt.pie(sizes, labels=labels, colors=colors, explode=explode)

# Box Plot
plt.boxplot()  # Displays the distribution of a dataset along with key statistical measures
plt.boxplot(data, notch=True)

# Scatter Plot
plt.scatter()  # Uses Cartesian coordinates to display values for two variables
plt.scatter(x, y, color='purple', marker='o', s=50)

# Subplotting
plt.subplots()  # Creating multiple plots on one figure
fig, axes = plt.subplots(nrows=2, ncols=2)

# Customization
# Various customization options such as title, labels, legend, and grid
plt.title('Title')
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.legend()
plt.grid(True)
