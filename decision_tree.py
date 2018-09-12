from sklearn.tree import DecisionTreeClassifier
tree = DecisionTreeClassifier(criterion='entropy', max_depth=3, random_state=0)

input_file = "adult_data.csv"

column_labels = ["age","workclass","fnlwgt","education","education-num","marital-status","occupation","relationship","race","sex",
                 "capital-gain","capital-loss","hours-per-week","native-country"]

# start with page 133 in the python book to read in .csv
#then get one hot encoder to work the categorical data
#might have to split the data into X and Y: where X is the data items and Y is the answer >=50K