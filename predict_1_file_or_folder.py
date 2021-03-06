import os
import re
from read_data import *
from feature import *
from predict_by_knn import *
import pandas

def predict_1_file(file_path):
	test = []
	with open(file_path, 'r', encoding="utf-16") as f:
		lines = f.readlines()
		lines = ' '.join(lines)
		lines = re.sub(r"[^\w\d\s]"," ",lines,flags=re.UNICODE)
		lines = re.sub("[0-9]"," ",lines,flags=re.UNICODE)
		lines = lines.split()
		lines = ' '.join(lines)
		test.append(lines)
	test_data_tf = tfTranform(test)
	return predict_classification(X_data_tf,test_data_tf[0],5)
def predict_folder(folder_path):
	folder_data = []
	dirs = os.listdir(folder_path)
	for file_path in dirs:
		with open(os.path.join(folder_path, file_path), 'r', encoding="utf-16") as f:
			lines = f.readlines()
			lines = ' '.join(lines)
			lines = lines.lower()
			lines = re.sub(r"[^\w\d\s]"," ",lines,flags=re.UNICODE)
			lines = re.sub("[0-9]"," ",lines,flags=re.UNICODE)
			lines = lines.split()
			lines = ' '.join(lines)
			folder_data.append(lines)
	folder_data_tf = tfTranform(folder_data)
	predict_test = []
	for row in range(len(X_test_tf)):
		predict_test.append(predict_classification(X_data_tf,X_test_tf[row],5))
	print(accuracy_metric(y_test,predict_test))
	return predict_test

# print(predict_1_file('new test - Copy (3)\Duong vao WTO\DVW_TN_T_ (188).txt'))
# print(predict_folder('new test - Copy (3)\My thuat'))

	