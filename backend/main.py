# function to detect continuous ones in data to get interval
# the function to fuzzify the crisp value of the label

from abcd import *
import skfuzzy as fuzz

mem = {"SLEEPING":[[310,570,870,1130],[0,0,460,720],[720,980,1440,1440]]}

def getcum(Y, lindex):
	print np.shape(Y)
	day = Y[1440*1:1440*2,lindex]
	plt.plot(day)
	sleep = np.sum(Y[1440*1:1440*2,lindex])
	print sleep

def getmem(label):
	x = np.arange(0,1440)
	mfx = mem[label]
	for i in mfx:
		mfxi = fuzz.trapmf(x,i)
		plt.plot(x,mfxi)

def main():
	bfile = np.array(read_csv('id.csv',sep='\n',header=None)).flatten()

	# print bfile[1]

	# y=np.array([])

	# print len(bfile)

	for i in range(1,2):
		uuid = bfile[i];
		print uuid
		(X,Y,M,timestamps,feature_names,label_names) = read_user_data(uuid);
		print label_names[5]
		# sleep = getcum(Y,5)
		getmem(label_names[5])


		# print "User %s has %d examples (~%d minutes of behavior)" % (uuid,len(timestamps),len(timestamps));
		# timestamps.shape

		# y = np.append(y,Y.shape[0])
		# plt.text(i,y[i],str(y[i]))
		# sys.stdout.write('.')
		# sys.stdout.flush()
		# print X.shape
		# print M.shape
		# print timestamps.shape
		# print len(feature_names)
		# print len(label_names)


		# n_examples_per_label = np.sum(Y,axis=0);
		# labels_and_counts = zip(label_names,n_examples_per_label);
		# sorted_labels_and_counts = sorted(labels_and_counts,reverse=True,key=lambda pair:pair[1]);
		# print "How many examples does this user have for each contex-label:";
		# print "-"*20;
		# for (label,count) in sorted_labels_and_counts:
		# 	print "label %s - %d minutes" % (label,count);
		# 	pass;


		# print("Since the collection of labels relied on self-reporting in-the-wild, the labeling may be incomplete.");
		# print("For instance, the users did not always report the position of the phone.");
		# fig = plt.figure(figsize=(15,5),facecolor='white');

		# ax1 = plt.subplot(1,1,1);
		# labels_to_display = ['LYING_DOWN','SITTING','OR_standing','FIX_walking','FIX_running'];
		# figure__pie_chart(Y,label_names,labels_to_display,'Body state',ax1);
		# plt.plot(y)
	plt.show()

if __name__ == '__main__':
	main()