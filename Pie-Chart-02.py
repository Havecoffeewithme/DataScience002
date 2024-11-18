from matplotlib import pyplot as plt


# dont use a pie chart if you have more than 5 elements , the example below I ust did it for demostration
plt.style.use("fivethirtyeight")

slices = [592, 554, 475, 364, 359, 319, 270, 203,
         205, 185, 180, 79, 733, 300, 40]

labels = ["JavaScript", "HTML/CSS", "SQL",
          "Python", "Java", "Shell/Bash","c#", "PHP", "C++", "Typescript", "C", "Other(s)", "Ruby", "Go","Assembly"]

plt.pie(slices, labels=labels, wedgeprops={"edgecolor": "black"})

plt.title("Developer survey")
plt.tight_layout()
plt.show()
