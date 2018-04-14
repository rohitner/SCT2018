from abcd import *
import skfuzzy as fuzz

def get_total_interval(data):

	total_interval = 0
	i = 0
	cnt = 0

	while i < len(data):
		if data[i] == 1:
			total_interval += 1
			cnt = 0
			for j in range(i, len(data)):
				if data[j] == 0:
					break
				cnt += 1
		i += cnt	
		
	return total_interval
	
def get_total_sum(data):

	total_hours = np.sum(data)
	return total_hours

def calculate_health(Y):

	sleep = ctrl.Antecedent(np.arange(0, 1440, 1), 'sleep')
	eat = ctrl.Antecedent(np.arange(0, 1440, 1), 'eat')
	exercise = ctrl.Antecedent(np.arange(0, 1440, 1), 'exercise')
	health = ctrl.Consequent(np.arange(0, 100, 1), 'health')

	sleep['low'] = fuzz.trapmf(sleep.universe, [0, 0, 460, 720])
	sleep['medium'] = fuzz.trapmf(sleep.universe, [310,570,870,1130])
	sleep['high'] = fuzz.trapmf(sleep.universe, [720,980,1440,1440])
	eat['low'] = fuzz.trapmf(eat.universe, [0,0,30,45])                              #change the values
	eat['medium'] = fuzz.trapmf(eat.universe, [30,45,75,90])
	eat['high'] = fuzz.trapmf(eat.universe, [80,100,1440,1440])	
	exercise['low'] = fuzz.trapmf(exercise.universe, [0,0,30,45])
	exercise['medium'] = fuzz.trapmf(exercise.universe, [30,45,75,90])
	exercise['high'] = fuzz.trapmf(exercise.universe, [80,100,1440,1440])
	health['low'] = fuzz.trapmf(health.universe, [0,0,30,50])
	health['medium'] = fuzz.trapmf(health.universe, [5,35,65,90])
	health['high'] = fuzz.trapmf(health.universe, [50,70,100, 100])

	rule1 = ctrl.Rule(sleep['high'] & eat['high'] & exercise['high'], health['high'])
	rule2 = ctrl.Rule(sleep['high'] & eat['high'] & exercise['medium'], health['high'])
	rule3 = ctrl.Rule(sleep['high'] & eat['medium'] & exercise['high'], health['high'])
	rule4 = ctrl.Rule(sleep['medium'] & eat['high'] & exercise['high'], health['high'])
	
	rule5 = ctrl.Rule(sleep['medium'] & eat['medium'] & exercise['medium'], health['medium'])
	rule6 = ctrl.Rule(sleep['high'] & eat['medium'] & exercise['medium'], health['medium'])
	rule7 = ctrl.Rule(sleep['medium'] & eat['high'] & exercise['medium'], health['medium'])
	rule8 = ctrl.Rule(sleep['medium'] & eat['medium'] & exercise['high'], health['medium'])
	rule9 = ctrl.Rule(sleep['high'] & eat['high'] & exercise['low'], health['medium'])
	rule10 = ctrl.Rule(sleep['low'] & eat['high'] & exercise['high'], health['medium'])
	rule11 = ctrl.Rule(sleep['high'] & eat['low'] & exercise['high'], health['medium'])
	rule12 = ctrl.Rule(sleep['high'] & eat['low'] & exercise['low'], health['medium'])
	rule13 = ctrl.Rule(sleep['low'] & eat['high'] & exercise['low'], health['medium'])
	rule14 = ctrl.Rule(sleep['low'] & eat['low'] & exercise['high'], health['medium'])
	rule15 = ctrl.Rule(sleep['high'] & eat['medium'] & exercise['low'], health['medium'])
	rule16 = ctrl.Rule(sleep['high'] & eat['low'] & exercise['medium'], health['medium'])
	rule17 = ctrl.Rule(sleep['medium'] & eat['high'] & exercise['low'], health['medium'])
	rule18 = ctrl.Rule(sleep['medium'] & eat['low'] & exercise['high'], health['medium'])
	rule19 = ctrl.Rule(sleep['low'] & eat['high'] & exercise['medium'], health['medium'])
	rule20 = ctrl.Rule(sleep['low'] & eat['medium'] & exercise['high'], health['medium'])
	rule21 = ctrl.Rule(sleep['low'] & eat['medium'] & exercise['medium'], health['medium'])
	rule22 = ctrl.Rule(sleep['medium'] & eat['medium'] & exercise['low'], health['medium'])
	rule23 = ctrl.Rule(sleep['medium'] & eat['low'] & exercise['medium'], health['medium'])

	rule24 = ctrl.Rule(sleep['low'] & eat['low'] & exercise['low'], health['low'])
	rule25 = ctrl.Rule(sleep['low'] & eat['low'] & exercise['medium'], health['low'])
	rule26 = ctrl.Rule(sleep['medium'] & eat['low'] & exercise['low'], health['low'])
	rule27 = ctrl.Rule(sleep['low'] & eat['medium'] & exercise['low'], health['low'])

	health_calc = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9,
					rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19,
					rule20, rule21, rule22, rule23, rule24, rule25, rule26, rule27 ])

	percentage = ctrl.ControlSystemSimulation(health_calc)
	
	percentage.input['sleep'] = get_total_sum(Y[0])
	percentage.input['eat'] = get_total_interval(Y[1])
	percentage.input['exercise'] = get_total_sum(Y[2])
	percentage.compute()
	z = percentage.output['health']
	
	return z

def calculate_work(Y):

	tech = ctrl.Antecedent(np.arange(0, 1440, 1), 'tech')
	leisure = ctrl.Antecedent(np.arange(0, 1440, 1), 'leisure')
	work = ctrl.Consequent(np.arange(0, 100, 1), 'work')

	tech['low'] = fuzz.trapmf(tech.universe, [0, 0, 460, 720])                           #change the vlaues
	tech['medium'] = fuzz.trapmf(tech.universe, [310,570,870,1130])
	tech['high'] = fuzz.trapmf(tech.universe, [720,980,1440,1440])
	leisure['low'] = fuzz.trapmf(leisure.universe, [0,0,30,45])                          #change the values
	leisure['medium'] = fuzz.trapmf(leisure.universe, [30,45,75,90])
	leisure['high'] = fuzz.trapmf(leisure.universe, [80,100,1440,1440])	
	work['low'] = fuzz.trapmf(work.universe, [0,0,30,50])
	work['medium'] = fuzz.trapmf(work.universe, [5,35,65,90])
	work['high'] = fuzz.trapmf(work.universe, [50,70,100, 100])

	rule1 = ctrl.Rule(tech['high'] & leisure['high'] , work['high'])
	rule2 = ctrl.Rule(tech['high'] & leisure['medium'] , work['high'])
	rule3 = ctrl.Rule(tech['medium'] & leisure['high']  work['high'])

	rule4 = ctrl.Rule(tech['medium'] & leisure['medium'] , work['medium'])
	rule5 = ctrl.Rule(tech['medium'] & leisure['low'], work['medium'])
	rule6 = ctrl.Rule(tech['high'] & leisure['low'], work['medium'])
	rule7 = ctrl.Rule(tech['low'] & leisure['high'], work['medium'])

	rule8 = ctrl.Rule(tech['low'] & leisure['low'], work['low'])

	work_calc = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8])

	percentage = ctrl.ControlSystemSimulation(work_calc)
	
	percentage.input['tech'] = get_total_sum(Y[0])
	percentage.input['leisure'] = get_total_sum(Y[1])
	percentage.compute()
	z = percentage.output['work']
	
	return z

def calculate_social(Y):

	interaction = ctrl.Antecedent(np.arange(0, 1440, 1), 'interaction')
	online = ctrl.Antecedent(np.arange(0, 1440, 1), 'online')
	social = ctrl.Consequent(np.arange(0, 100, 1), 'work')

	interaction['low'] = fuzz.trapmf(interaction.universe, [0, 0, 460, 720])             #change the vlaues
	interaction['medium'] = fuzz.trapmf(interaction.universe, [310,570,870,1130])
	interaction['high'] = fuzz.trapmf(interaction,universe, [720,980,1440,1440])
	online['low'] = fuzz.trapmf(online.universe, [0,0,30,45])                          #change the values
	online['medium'] = fuzz.trapmf(online.universe, [30,45,75,90])
	online['high'] = fuzz.trapmf(online.universe, [80,100,1440,1440])	
	social['low'] = fuzz.trapmf(social.universe, [0,0,30,50])
	social['medium'] = fuzz.trapmf(social.universe, [5,35,65,90])
	social['high'] = fuzz.trapmf(social.unsiverse, [50,70,100, 100])

	rule1 = ctrl.Rule(interaction['high'] & online['high'] , social['high'])
	rule2 = ctrl.Rule(interaction['high'] & online['medium'] , social['high'])
	rule3 = ctrl.Rule(interaction['medium'] & online['high']  social['high'])

	rule4 = ctrl.Rule(interaction['medium'] & online['medium'] , social['medium'])
	rule5 = ctrl.Rule(interaction['medium'] & online['low'], social['medium'])
	rule6 = ctrl.Rule(interaction['high'] & online['low'], social['medium'])
	rule7 = ctrl.Rule(interaction['low'] & online['high'], social['medium'])

	rule8 = ctrl.Rule(interaction['low'] & online['low'], social['low'])

	social_calc = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8])

	percentage = ctrl.ControlSystemSimulation(social_calc)
	
	percentage.input['tech'] = get_total_sum(Y[0])
	percentage.input['leisure'] = get_total_sum(Y[1])
	percentage.compute()
	z = percentage.output['social']
	
	return z	




def main():
	bfile = np.array(read_csv('id.csv',sep='\n',header=None)).flatten()

	for i in range(1,2):
		uuid = bfile[i]
		print uuid
		(X,Y,M,timestamps,feature_names,label_names) = read_user_data(uuid)

if __name__ == '__main__':
	main()