import pandas
import data_loader as dl
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
sns.set(style="white")

def hist(data, field, filename):
	#sns.distplot(x)

	# Draw a count plot to show the number of planets discovered each year
	g = sns.factorplot(x=field, data=data, kind="count",
                   palette="BuPu", size=6, aspect=1.5)
	plt.savefig(filename)




if __name__ == '__main__':
	dl.init()
	hist(dl.training_data, 'Stance', 'label_distribution.pdf')
	hist(dl.training_data, 'Target', 'topic_distribution.pdf')
