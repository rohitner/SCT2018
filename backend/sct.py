from abcd import *
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import pandas as pd
import statsmodels.api as sm 

def get_total_interval(data):
	# print data.shape
	total_interval = 0
	i = 0
	cnt = 0
	maxx = np.max(data)
	M = data<0.3*maxx
	data2 = np.where(M, 0, data)
	M = data2>0
	data = np.where(M, 1, data2)

	# plt.plot(data)
	# plt.show()
	while i < len(data):
		if data[i] == 1:
			total_interval += 1
			cnt = 0
			for j in range(i, len(data)):
				if data[j] == 0:
					break
				cnt += 1
			i += cnt
		i += 1	

	return total_interval
	
def get_total_sum(data):

	maxx = np.max(data)
	#print "max" + str(maxx)
	M = data<0.3*maxx
	data2 = np.where(M, 0, data)
	M = data2>0
	data = np.where(M, 1, data2)
	total_hours = np.sum(data)
	# print "total hours " + str(total_hours/60)
	return total_hours

def calculate_health(Y):

	sleep    = ctrl.Antecedent(np.arange(0, 1440, 1),    'sleep')
	eat 	 = ctrl.Antecedent(np.arange(0,  10, 1),      'eat')
	exercise = ctrl.Antecedent(np.arange(0, 1440, 1), 'exercise')
	health   = ctrl.Consequent(np.arange(0,  100, 1),   'health')

	sleep['L']    = fuzz.trapmf(   sleep.universe, [  0,  0, 180, 240])
	sleep['M']    = fuzz.trapmf(   sleep.universe, [180,300, 480, 540])
	sleep['H']    = fuzz.trapmf(   sleep.universe, [480,540, 720, 720])
	eat['L']      = fuzz.trapmf(  	 eat.universe, [  0,  0,   1,   2])
	eat['M']      = fuzz.trapmf(     eat.universe, [  1,  2,   4,   6])
	eat['H']      = fuzz.trapmf(     eat.universe, [  4,  6,  10,  10])	
	exercise['L'] = fuzz.trapmf(exercise.universe, [  0,  0,  30,  45])
	exercise['M'] = fuzz.trapmf(exercise.universe, [ 30, 45,  75,  90])
	exercise['H'] = fuzz.trapmf(exercise.universe, [ 80,100, 400, 400])
	health['L']   = fuzz.trapmf(  health.universe, [  0,  0,  30,  50])
	health['M']   = fuzz.trapmf(  health.universe, [  5, 35,  65,  90])
	health['H']   = fuzz.trapmf(  health.universe, [ 60, 70, 100, 100])

	rule = []

	rule = np.append(rule, ctrl.Rule(exercise['L'] & sleep['L'] & eat['L'], health['L']))
	rule = np.append(rule, ctrl.Rule(exercise['M'] & sleep['L'] & eat['L'], health['L']))
	rule = np.append(rule, ctrl.Rule(exercise['H'] & sleep['L'] & eat['L'], health['L']))
	rule = np.append(rule, ctrl.Rule(exercise['L'] & sleep['M'] & eat['L'], health['L']))
	rule = np.append(rule, ctrl.Rule(exercise['M'] & sleep['M'] & eat['L'], health['M']))
	rule = np.append(rule, ctrl.Rule(exercise['H'] & sleep['M'] & eat['L'], health['M']))
	rule = np.append(rule, ctrl.Rule(exercise['L'] & sleep['H'] & eat['L'], health['L']))
	rule = np.append(rule, ctrl.Rule(exercise['M'] & sleep['H'] & eat['L'], health['M']))
	rule = np.append(rule, ctrl.Rule(exercise['H'] & sleep['H'] & eat['L'], health['M']))
	rule = np.append(rule, ctrl.Rule(exercise['L'] & sleep['L'] & eat['M'], health['L']))
	rule = np.append(rule, ctrl.Rule(exercise['M'] & sleep['L'] & eat['M'], health['M']))
	rule = np.append(rule, ctrl.Rule(exercise['H'] & sleep['L'] & eat['M'], health['M']))
	rule = np.append(rule, ctrl.Rule(exercise['L'] & sleep['M'] & eat['M'], health['M']))
	rule = np.append(rule, ctrl.Rule(exercise['M'] & sleep['M'] & eat['M'], health['H']))
	rule = np.append(rule, ctrl.Rule(exercise['H'] & sleep['M'] & eat['M'], health['H']))
	rule = np.append(rule, ctrl.Rule(exercise['L'] & sleep['H'] & eat['M'], health['M']))
	rule = np.append(rule, ctrl.Rule(exercise['M'] & sleep['H'] & eat['M'], health['H']))
	rule = np.append(rule, ctrl.Rule(exercise['H'] & sleep['H'] & eat['M'], health['H']))
	rule = np.append(rule, ctrl.Rule(exercise['L'] & sleep['L'] & eat['H'], health['L']))
	rule = np.append(rule, ctrl.Rule(exercise['M'] & sleep['L'] & eat['H'], health['M']))
	rule = np.append(rule, ctrl.Rule(exercise['H'] & sleep['L'] & eat['H'], health['M']))
	rule = np.append(rule, ctrl.Rule(exercise['L'] & sleep['M'] & eat['H'], health['M']))
	rule = np.append(rule, ctrl.Rule(exercise['M'] & sleep['M'] & eat['H'], health['H']))
	rule = np.append(rule, ctrl.Rule(exercise['H'] & sleep['M'] & eat['H'], health['H']))
	rule = np.append(rule, ctrl.Rule(exercise['L'] & sleep['H'] & eat['H'], health['M']))
	rule = np.append(rule, ctrl.Rule(exercise['M'] & sleep['H'] & eat['H'], health['H']))
	rule = np.append(rule, ctrl.Rule(exercise['H'] & sleep['H'] & eat['H'], health['H']))

	health_calc = ctrl.ControlSystem(rule)

	percentage = ctrl.ControlSystemSimulation(health_calc)

	ans = get_total_sum(Y[0])
	if ans>720:
		percentage.input['sleep'] = 720
	else:
		percentage.input['sleep'] = ans
	ans = get_total_interval(Y[1])
	if ans>10:
		percentage.input['eat'] = 9
	else:
		percentage.input['eat'] = ans	
	ans = get_total_sum(Y[2])
	if ans>400:
		percentage.input['exercise'] = 400
	else:
		percentage.input['exercise'] = ans
	percentage.compute()
	z = percentage.output['health']

	return z

def calculate_work(Y):

	tech    = ctrl.Antecedent(np.arange(0, 1440, 1),    'tech')
	leisure = ctrl.Antecedent(np.arange(0, 1440, 1), 'leisure')
	work 	= ctrl.Consequent(np.arange(0,  100, 1),    'work')

	tech['L']    = fuzz.trapmf(   tech.universe, [  0,  0, 180, 240])
	tech['M']    = fuzz.trapmf(   tech.universe, [180,300, 480, 540])
	tech['H']    = fuzz.trapmf(   tech.universe, [480,540, 720, 720])
	leisure['L'] = fuzz.trapmf(leisure.universe, [  0,  0, 180, 240])                     #change the values
	leisure['M'] = fuzz.trapmf(leisure.universe, [480,540, 720, 720])
	leisure['H'] = fuzz.trapmf(leisure.universe, [480,540, 720, 720])	
	work['L']    = fuzz.trapmf(   work.universe, [  0,  0,  30,  50])
	work['M']    = fuzz.trapmf(   work.universe, [  5, 35,  65,  90])
	work['H']    = fuzz.trapmf(   work.universe, [ 60, 70, 100, 100])

	rule = []

	rule = np.append(rule,ctrl.Rule(tech['L'] & leisure['L'], work['L']))
	rule = np.append(rule,ctrl.Rule(tech['M'] & leisure['L'], work['M']))
	rule = np.append(rule,ctrl.Rule(tech['H'] & leisure['L'], work['M']))
	rule = np.append(rule,ctrl.Rule(tech['L'] & leisure['M'], work['M']))
	rule = np.append(rule,ctrl.Rule(tech['M'] & leisure['M'], work['H']))
	rule = np.append(rule,ctrl.Rule(tech['H'] & leisure['M'], work['H']))
	rule = np.append(rule,ctrl.Rule(tech['L'] & leisure['H'], work['M']))
	rule = np.append(rule,ctrl.Rule(tech['M'] & leisure['H'], work['H']))
	rule = np.append(rule,ctrl.Rule(tech['H'] & leisure['H'], work['H']))

	work_calc = ctrl.ControlSystem(rule)

	percentage = ctrl.ControlSystemSimulation(work_calc)
	
	ans = get_total_interval(Y[0])
	if ans>720:
		percentage.input['tech'] = 720
	else:
		percentage.input['tech'] = ans
	ans = get_total_interval(Y[1])
	if ans>720:
		percentage.input['leisure'] = 720
	else:
		percentage.input['leisure'] = ans

	percentage.compute()
	z = percentage.output['work']

	return z

def calculate_social(Y):

	interaction = ctrl.Antecedent(np.arange(0, 1440, 1), 'interaction')
	online      = ctrl.Antecedent(np.arange(0, 1440, 1),      'online')
	social      = ctrl.Consequent(np.arange(0,  100, 1),      'social')

	interaction['L'] = fuzz.trapmf(interaction.universe, [  0,  0, 460, 720])             #change the vlaues
	interaction['M'] = fuzz.trapmf(interaction.universe, [310,570, 870,1130])
	interaction['H'] = fuzz.trapmf(interaction.universe, [720,980,1440,1440])
	online['L']      = fuzz.trapmf(		online.universe, [  0,  0,  30,  45])             #change the values
	online['M']      = fuzz.trapmf(		online.universe, [ 30, 45,  75,  90])
	online['H']      = fuzz.trapmf(		online.universe, [ 80,100,1440,1440])	
	social['L']      = fuzz.trapmf(		social.universe, [  0,  0,  30,  50])
	social['M'] 	 = fuzz.trapmf(		social.universe, [  5, 35,  65,  90])
	social['H'] 	 = fuzz.trapmf(		social.universe, [ 60, 70, 100, 100])

	rule = []

	rule = np.append(rule,ctrl.Rule(interaction['L'] & online['L'], social['L']))
	rule = np.append(rule,ctrl.Rule(interaction['M'] & online['L'], social['M']))
	rule = np.append(rule,ctrl.Rule(interaction['H'] & online['L'], social['M']))
	rule = np.append(rule,ctrl.Rule(interaction['L'] & online['M'], social['M']))
	rule = np.append(rule,ctrl.Rule(interaction['M'] & online['M'], social['M']))
	rule = np.append(rule,ctrl.Rule(interaction['H'] & online['M'], social['H']))
	rule = np.append(rule,ctrl.Rule(interaction['L'] & online['H'], social['M']))
	rule = np.append(rule,ctrl.Rule(interaction['M'] & online['H'], social['H']))
	rule = np.append(rule,ctrl.Rule(interaction['H'] & online['H'], social['H']))

	social_calc = ctrl.ControlSystem(rule)

	percentage = ctrl.ControlSystemSimulation(social_calc)
	
	ans = get_total_interval(Y[0])
	if ans>720:
		percentage.input['interaction'] = 720
	else:
		percentage.input['interaction'] = ans
	ans = get_total_interval(Y[1])
	if ans>720:
		percentage.input['online'] = 720
	else:
		percentage.input['online'] = ans
	
	percentage.compute()
	z = percentage.output['social']
	
	return z

def calculate_total(Y):

	health = ctrl.Antecedent(np.arange(0, 100, 1), 'health')
	work   = ctrl.Antecedent(np.arange(0, 100, 1),   'work')
	social = ctrl.Antecedent(np.arange(0, 100, 1), 'social')
	total  = ctrl.Consequent(np.arange(0, 100, 1),  'total')

	health['L'] = fuzz.trapmf(health.universe, [  0,  0,  30,  50])
	health['M'] = fuzz.trapmf(health.universe, [  5, 35,  65,  90])
	health['H'] = fuzz.trapmf(health.universe, [ 60, 70, 100, 100])
	work['L']   = fuzz.trapmf(  work.universe, [  0,  0,  30,  50])
	work['M'] 	= fuzz.trapmf(  work.universe, [  5, 35,  65,  90])
	work['H'] 	= fuzz.trapmf(  work.universe, [ 60, 70, 100, 100])
	social['L'] = fuzz.trapmf(social.universe, [  0,  0,  30,  50])
	social['M'] = fuzz.trapmf(social.universe, [  5, 35,  65,  90])
	social['H'] = fuzz.trapmf(social.universe, [ 60, 70, 100, 100])
	total['L']  = fuzz.trapmf( total.universe, [  0,  0,  30,  50])
	total['M']  = fuzz.trapmf( total.universe, [  5, 35,  65,  90])
	total['H']  = fuzz.trapmf( total.universe, [ 60, 70, 100, 100])

	rule = []

	rule = np.append(rule,ctrl.Rule(health['L'] & work['L'] & social['L'], total['L']))
	rule = np.append(rule,ctrl.Rule(health['M'] & work['L'] & social['L'], total['L']))
	rule = np.append(rule,ctrl.Rule(health['H'] & work['L'] & social['L'], total['L']))
	rule = np.append(rule,ctrl.Rule(health['L'] & work['M'] & social['L'], total['L']))
	rule = np.append(rule,ctrl.Rule(health['M'] & work['M'] & social['L'], total['M']))
	rule = np.append(rule,ctrl.Rule(health['H'] & work['M'] & social['L'], total['M']))
	rule = np.append(rule,ctrl.Rule(health['L'] & work['H'] & social['L'], total['M']))
	rule = np.append(rule,ctrl.Rule(health['M'] & work['H'] & social['L'], total['M']))
	rule = np.append(rule,ctrl.Rule(health['H'] & work['H'] & social['L'], total['M']))
	rule = np.append(rule,ctrl.Rule(health['L'] & work['L'] & social['M'], total['L']))
	rule = np.append(rule,ctrl.Rule(health['M'] & work['L'] & social['M'], total['H']))
	rule = np.append(rule,ctrl.Rule(health['H'] & work['L'] & social['M'], total['H']))
	rule = np.append(rule,ctrl.Rule(health['L'] & work['M'] & social['M'], total['H']))
	rule = np.append(rule,ctrl.Rule(health['M'] & work['M'] & social['M'], total['H']))
	rule = np.append(rule,ctrl.Rule(health['H'] & work['M'] & social['M'], total['H']))
	rule = np.append(rule,ctrl.Rule(health['L'] & work['H'] & social['M'], total['H']))
	rule = np.append(rule,ctrl.Rule(health['M'] & work['H'] & social['M'], total['H']))
	rule = np.append(rule,ctrl.Rule(health['H'] & work['H'] & social['M'], total['H']))
	rule = np.append(rule,ctrl.Rule(health['L'] & work['L'] & social['H'], total['M']))
	rule = np.append(rule,ctrl.Rule(health['M'] & work['L'] & social['H'], total['H']))
	rule = np.append(rule,ctrl.Rule(health['H'] & work['L'] & social['H'], total['H']))
	rule = np.append(rule,ctrl.Rule(health['L'] & work['M'] & social['H'], total['M']))
	rule = np.append(rule,ctrl.Rule(health['M'] & work['M'] & social['H'], total['H']))
	rule = np.append(rule,ctrl.Rule(health['H'] & work['M'] & social['H'], total['H']))
	rule = np.append(rule,ctrl.Rule(health['L'] & work['H'] & social['H'], total['H']))
	rule = np.append(rule,ctrl.Rule(health['M'] & work['H'] & social['H'], total['H']))
	rule = np.append(rule,ctrl.Rule(health['H'] & work['H'] & social['H'], total['H']))

	total_calc = ctrl.ControlSystem(rule)

	percentage = ctrl.ControlSystemSimulation(total_calc)
	
	percentage.input['health'] = get_total_sum(Y[0])
	percentage.input['work'] = get_total_sum(Y[1])
	percentage.input['social'] = get_total_sum(Y[2])
	percentage.compute()
	z = percentage.output['total']
	
	return z

def calculate(Y):

	health = calculate_health(Y[0])
	work   = calculate_work(Y[1])
	social = calculate_social(Y[2])
	total  = calculate_total([health, work, social])

	return health, work, social, total

def cummumlative_data(Y):

	data = np.zeros(len(Y))
	for i in range(len(Y)):
		for j in range(len(Y[i])):
			if Y[i,j] == 1:
				data[i] = 1
				break

	return data

def all_data(Y, label_names):

	h = [
		 ['LYING_DOWN', 'SLEEPING'],
		 ['FIX_restaurant', 'EATING'],
		 ['FIX_running', 'FIX_walking', 'BICYCLING', 'AT_THE_GYM','OR_exercise']
		]

	w = [
		 ['IN_CLASS', 'IN_A_MEETING', 'LOC_main_workplace', 'COMPUTER_WORK', 'AT_SCHOOL'], 
		 ['WATCHING_TV', 'SINGING', 'SHOPPING']
		]
	
	s = [
		 ['AT_A_PARTY', 'TALKING', 'WITH_CO-WORKERS', 'WITH_FRIENDS'],
		 ['SURFING_THE_INTERNET','PHONE_IN_HAND']
		]	

	feature = [h, w, s]

	ans = []
	for k in range(len(feature)):
		activity = feature[k]
		for i in range(len(activity)):
			labels = activity[i]
			temp = []
			for j in range(len(labels)):
				ind = label_names.index(labels[j])
				temp.append(Y[:,ind])
			temp = np.array(temp)	
			temp = temp.transpose()
			temp = cummumlative_data(temp)
			ans.append(temp)

	ans = np.array(ans)	
	final_ans = []
	for i in range(len(ans)):
	 	dft = pd.DataFrame(ans[i],columns = ['A'],index=pd.date_range('20170101',periods=1440,freq='T'))
	 	res = sm.tsa.seasonal_decompose(dft.A, freq=60)
	 	a = res.trend
	 	tem = np.isnan(a)
	 	a[tem] = 0
	 	#print a
	 	final_ans.append(a)
		
	#res.plot()
	#plt.show()	
	final_ans = np.array(final_ans)

	return final_ans.transpose()


def runmain():
	bfile = np.array(read_csv('id.csv',sep='\n',header=None)).flatten()

	for i in range(1, 2):
		uuid = bfile[i]
		# print uuid
		(X,Y,M,timestamps,feature_names,label_names) = read_user_data(uuid)
		dat = all_data(Y[0:1440, :], label_names)
		return calculate([[dat[:,0],
						  dat[:,1],
						  dat[:,2]],
						 [dat[:,3],
						  dat[:,4]],
						 [dat[:,5],
						  dat[:,6]]])

if __name__ == '__main__':
	runmain()