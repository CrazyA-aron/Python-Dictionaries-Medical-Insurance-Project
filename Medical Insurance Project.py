# Add your code here
medical_costs = {}
medical_costs['Marina'] = 6607.0
medical_costs['Vinay'] = 3225.0

medical_costs.update({'Connie': 8886.0, 
'Isaac': 16444.0, 'Valentina': 6420.0})
medical_costs.update({'Vinay': 3325.0})

total_cost = 0
for cost in medical_costs.values():
  total_cost += cost

average_cost = total_cost / len(medical_costs)


names = ['Marina', 'Vinay', 'Connie', 'Isaac', 'Valentina']
ages = [27, 24, 43, 35, 52]

zipped_ages = zip(names, ages)

names_to_ages = {name: age for name, age in zipped_ages}

marina_age = names_to_ages.get('Marina', None)

medical_records = {}

medical_records['Marina'] = {"Age": 27, "Sex": "Female", "BMI": 31.1, "Children": 2, "Smoker": "Non-smoker", "Insurance_cost": 6607.0}

medical_records['Vinay'] = {"Age": 24, "Sex": "Male", "BMI": 26.9, "Children": 0, "Smoker": "Non-smoker", "Insurance_cost": 3225.0}

medical_records['Connie'] = {"Age": 43, "Sex": "Female", "BMI": 25.3, "Children": 3, "Smoker": "Non-smoker", "Insurance_cost": 8886.0}

medical_records['Isaac'] = {"Age": 35, "Sex": "Male", "BMI": 20.6, "Children": 4, "Smoker": "Smoker", "Insurance_cost": 16444.0}

medical_records['Valentina'] = {"Age": 52, "Sex": "Female", "BMI": 18.7, "Children": 1, "Smoker": "Non-smoker", "Insurance_cost": 6420.0}


connie_insurance = medical_records['Connie']['Insurance_cost']

medical_records.pop('Vinay')


for name, record in medical_records.items():
  print(name + " is a " + str(record['Age']) + " year old " + record['Sex'] + ' ' + record['Smoker'] + " with a BMI of " + str(record['BMI']) + " and insurance cost of " + str(record['Insurance_cost']))


def update_medical_records(name, age, sex, bmi,       children, smoker, insurance_cost):
  medical_records_dict = {}
  medical_records_dict[name] = {"Age": age, "Sex": sex,"BMI": bmi, "Children": children, "Smoker": smoker, "Insurance_cost": insurance_cost}
  medical_records.update(medical_records_dict)

update_medical_records('Aaron', 13, 'Male', 20.3, 0, 'Non-smoker', 1000)
print(medical_records)
