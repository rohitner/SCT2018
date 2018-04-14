import matplotlib as mpl;
import matplotlib.pyplot as plt;
import numpy as np;
from pandas import read_csv;
import gzip;
import StringIO;
import sys;

def parse_header_of_csv(csv_str):
	# Isolate the headline columns:
	headline = csv_str[:csv_str.index('\n')];
	columns = headline.split(',');

	# The first column should be timestamp:
	assert columns[0] == 'timestamp';
	# The last column should be label_source:
	assert columns[-1] == 'label_source';
	
	# Search for the column of the first label:
	for (ci,col) in enumerate(columns):
		if col.startswith('label:'):
			first_label_ind = ci;
			break;
		pass;

	# Feature columns come after timestamp and before the labels:
	feature_names = columns[1:first_label_ind];
	# Then come the labels, till the one-before-last column:
	label_names = columns[first_label_ind:-1];
	for (li,label) in enumerate(label_names):
		# In the CSV the label names appear with prefix 'label:', but we don't need it after reading the data:
		assert label.startswith('label:');
		label_names[li] = label.replace('label:','');
		pass;
	
	return (feature_names,label_names);

def parse_body_of_csv(csv_str,n_features):
	# Read the entire CSV body into a single numeric matrix:
	full_table = np.loadtxt(StringIO.StringIO(csv_str),delimiter=',',skiprows=1);
	
	# Timestamp is the primary key for the records (examples):
	timestamps = full_table[:,0].astype(int);
	
	# Read the sensor features:
	X = full_table[:,1:(n_features+1)];
	
	# Read the binary label values, and the 'missing label' indicators:
	trinary_labels_mat = full_table[:,(n_features+1):-1]; # This should have values of either 0., 1. or NaN
	#print trinary_labels_mat, "labels"
	M = np.isnan(trinary_labels_mat); # M is the missing label matrix
	#print M, 'm'
	Y = np.where(M,0,trinary_labels_mat) ; # Y is the label matrix
	#print Y, 'Y'
	
	return (X,Y,M,timestamps);

'''
Read the data (precomputed sensor-features and labels) for a user.
This function assumes the user's data file is present.
'''
def read_user_data(uuid):
	user_data_file = 'data/%s.features_labels.csv.gz' % uuid;

	# Read the entire csv file of the user:
	with gzip.open(user_data_file,'rb') as fid:
		csv_str = fid.read();
		pass;

	(feature_names,label_names) = parse_header_of_csv(csv_str);
	n_features = len(feature_names);
	(X,Y,M,timestamps) = parse_body_of_csv(csv_str,n_features);

	return (X,Y,M,timestamps,feature_names,label_names);

def figure__pie_chart(Y,label_names,labels_to_display,title_str,ax):
	portion_of_time = np.mean(Y,axis=0);
	portions_to_display = [portion_of_time[label_names.index(label)] for label in labels_to_display];
	pretty_labels_to_display = [get_label_pretty_name(label) for label in labels_to_display];
	
	ax.pie(portions_to_display,labels=pretty_labels_to_display,autopct='%.2f%%');
	ax.axis('equal');
	plt.title(title_str);
	return;

def get_label_pretty_name(label):
	if label == 'FIX_walking':
		return 'Walking';
	if label == 'FIX_running':
		return 'Running';
	if label == 'LOC_main_workplace':
		return 'At main workplace';
	if label == 'OR_indoors':
		return 'Indoors';
	if label == 'OR_outside':
		return 'Outside';
	if label == 'LOC_home':
		return 'At home';
	if label == 'FIX_restaurant':
		return 'At a restaurant';
	if label == 'OR_exercise':
		return 'OR_exerciseise';
	if label == 'LOC_beach':
		return 'At the beach';
	if label == 'OR_standing':
		return 'Standing';
	if label == 'WATCHING_TV':
		return 'Watching TV'
	
	if label.endswith('_'):
		label = label[:-1] + ')';
		pass;
	
	label = label.replace('__',' (').replace('_',' ');
	label = label[0] + label[1:].lower();
	label = label.replace('i m','I\'m');
	return label;

def plotpie(uuid):

	(X,Y,M,timestamps,feature_names,label_names) = read_user_data(uuid)

	fig = plt.figure(figsize=(15,5),facecolor='white');

	ax1 = plt.subplot(1,2,1);
	labels_to_display = ['LYING_DOWN','SITTING','OR_standing','FIX_walking','FIX_running'];
	figure__pie_chart(Y,label_names,labels_to_display,'Body state',ax1);

	ax2 = plt.subplot(1,2,2);
	labels_to_display = ['PHONE_IN_HAND','PHONE_IN_BAG','PHONE_IN_POCKET','PHONE_ON_TABLE'];
	figure__pie_chart(Y,label_names,labels_to_display,'Phone position',ax2);