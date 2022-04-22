# machine_learning_Diabetes_prediction
machine learning diabetes prediction with deployment on flask


### Prerequisites
You must have Scikit Learn, Pandas (for Machine Leraning Model) and Flask installed.

### Project Structure
This project has four major parts :
1. diabetes_model.py - This contains code fot our Machine Learning model to predict if a patient is diabetic based on trainign data in 'diabetes.csv' file.
2. Dpred.py - This contains Flask program linked with HTM file and also the pickle file to load our machine learning file for execution.
3. static.py - This folder contains our css styling.
4. templates - This folder contains the HTML template to allow user to enter a patients necessary detail and displays the predicted diabetic result.

### Running the project
1. Ensure that you are in the project home directory. Create the machine learning model by running below command -
```
python diabetes_model.py
```
This would create a serialized version of our model into a file Diabetes_model.pkl

2. Run Dpred.py using below command to start Flask app
```
python Dpred.py
```
By default, flask will run on port 5000.

3. Navigate to URL http://localhost:5000

Enter valid/appropriate numerical values in all input fields and click the submit button.

If everything goes well, you should  be able to see the predcited diabetes result on the HTML page!
