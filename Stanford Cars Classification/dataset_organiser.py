import numpy as np
import matplotlib.pyplot as plt
import time
import os
import copy

base_path = ''
train_path = os.path.join(base_path, 'cars_train')
test_path = os.path.join(base_path, 'cars_test')
meta_path = os.path.join(base_path, 'meta')

with open(os.path.join(meta_path, 'class_names.txt'), 'r') as class_names:
  lines = class_names.readlines()
  lines = [line.strip() for line in lines]
  classes = [[class_id, line] for class_id, line in enumerate(lines)]
  
classes_names = []

for elem in classes:
  if elem[1].split(' ')[0] in ('Acura',
                               'Audi',
                               'BMW',
                               'Bentley',
                               'Chevrolet',
                               'Chrysler',
                               'Dodge',
                               'Ferrari',
                               'Ford',
                               'Honda',
                               'Hyundai',
                               'Infiniti',
                               'Jeep',
                               'Lamborghini',
                               'Mercedes-Benz',
                               'Rolls-Royce',
                               'Toyota',
                               'Volvo'):

                               elem[1] = elem[1].split(' ')[0]
                               classes_names.append(elem)

with open(os.path.join(meta_path, 'cars_train_classes.txt'), 'r') as train_classes:
  _ = train_classes.readline()
  lines = train_classes.readlines()
  lines = [line.strip('')[:] for line in lines]
  train_classes = [line.split() for line in lines]
  for line in train_classes:
    line[0] = int(line[0])
  
classes_names = dict(classes_names)
  
classes_for_task = []

for elem in train_classes:
  if elem[0] in classes_names:
    classes_for_task.append([elem[1], classes_names[elem[0]]])

dict_classes_for_task = dict(classes_for_task)

classes_mask = []
classes_set = set()

i = 0
for v in classes_names.values():
  if v not in classes_set:
    classes_mask.append([i, v])
    classes_set.add(v)
    i += 1

dataset_final_path = os.path.join(base_path, 'train_data')

for filename in os.listdir(train_path):
  if filename in dict_classes_for_task.keys():
    print(filename)
    os.makedirs(os.path.join(dataset_final_path, dict_classes_for_task[filename].lower()), exist_ok=True)
    os.replace(os.path.join(train_path, filename), os.path.join(dataset_final_path, '{}/{}'.format(dict_classes_for_task[filename].lower(), filename)))

