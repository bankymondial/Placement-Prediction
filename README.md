### Problem Definition

This project aims to predict the placement of students based on their academic and extracurricular activities. The data source was not explicit on the target variable, `placementstatus` whether a student is placed or not. However, one can infer from variables such as higher and senior secondary marks that the model seeks to predict a student's placement at a higher level of education, maybe college. The data for the modelling can be found on [Kaggle](https://www.kaggle.com/datasets/ruchikakumbhar/placement-prediction-dataset?select=placementdata.csv).

___________________________________________________________________________________________________________________________________________________


### Why the model matters
1. The model can be used by educational institutions, career counsellors, and recruiters to assess student profiles and predict placement outcomes, enabling targeted support and optimized recruitment strategies.
2. The predictive model identifies students at risk of not securing placements, enabling targeted interventions to improve their career outcomes.
3. Data-driven insights help institutions optimize their academic programs and resource allocation, ultimately boosting overall placement rates.


____________________________________________________________________________________________________________________________________________________

### Dataset
The dataset contains 10,000 observations with the following features:
- `CGPA`: (Continuous) Overall grades achieved by the student.
- `Internships`: (Discrete) Number of internships a student has done.
- `Projects`:  (Discrete) Number of projects a student has done
- `Workshops/Certifications`: (Discrete) Number of courses students have taken to upskill themselves.
- `ApptitudeTestScore`: (Discrete) Student's Aptitude test score - a part of the recruitment process to understand the Quant and logical thinking of the student.
- `SoftSkillrating`: (Continuous) Communication is a key role that plays in the placement or in any aspect of life.
- `ExtraCurricularActivities`: (Nominal) Whether a student does extracurricular activities or not.
- `PlacementTraining`: (Nominal) Whether a student underwent one or not. It is provided to students in college to ace the placement process.
- `SSC_Marks`: (Discrete) Senior Secondary score.
- `HSC_Marks`: (Discrete) Higher Secondary score.
- `PlacementStatus` (target): (Nominal) Whether the student  was placed or not (42% for the positive class, `Placed` and 58% for the negative class, `Not Placed`, indicating a fairly balanced dataset).
  
____________________________________________________________________________________________________________________________________________________



### Model Performance Comparison

**Logistic Regression** is the best-performing model overall, with the highest scores across *Validation Accuracy*, *Recall*, *F1 Score*, and *ROC AUC*. It consistently outperforms other models on these key metrics, especially in *recall*, which is crucial for identifying placed students (the minority class). **Gradient Boosting** comes close in test set performance, particularly with its higher Test Accuracy and Test ROC AUC, but Logistic Regression provides a better overall balance between precision and recall.

**Most Important Features Model** also performed well, with high recall (0.7648) and F1 score (0.7483) on the validation set, but it didn't surpass Logistic Regression in key metrics.


| Metric/Model           | **Logistic Regression** | **Gradient Boosting** | **Random Forest** | **Most Important Features** |
|-------------------------|-------------------------|-----------------------|-------------------|-----------------------------|
| **Validation Accuracy**  | 0.7870                  | 0.7755                | 0.7425            | 0.7790                     |
| **Recall**               | 0.7590                  | 0.7322                | 0.7159            | 0.7648                     |
| **F1 Score**             | 0.7538                  | 0.7370                | 0.7049            | 0.7483                     |
| **ROC AUC**              | 0.8716                  | 0.8510                | 0.8021            | 0.8550                     |
| **Test Accuracy**        | 0.7770                  | 0.7830                | N/A               | N/A                        |
| **Test Recall**          | 0.7488                  | 0.6869                | N/A               | N/A                        |
| **Test F1 Score**        | 0.7307                  | 0.7189                | N/A               | N/A                        |
| **Test ROC AUC**         | 0.8572                  | 0.8608                | N/A               | N/A                        |


____________________________________________________________________________________________________________________________________________________

### Instructions for Running the Project
To predict placement using the trained model, follow these chronological steps:

#### 1. Prerequisites
Ensure you have the following installed:
- Python: Version >= 3.12
- Pipenv: For dependency management
- curl: For API testing

____________________________________________________________________________________________________________________________________________________


#### 2. Setup and Installation
##### 2.1. Clone the Repository
Clone the project to your local machine and navigate into the directory:
   - git clone https://github.com/bankymondial/Placement-Prediction.git: This command clones the project from GitHub to your local machine into a directory named Placement-Prediction.
   - `cd Placement-Prediction`: After cloning the project, this command moves you into the Placement-Prediction directory so you can work on it locally.

________________________________________________________________________

    
##### 2.2 Install Dependencies
Setting up a virtual environment and installing the necessary dependencies is a crucial step to ensure the right versions of packages are used:
   - `pipenv install` - This command will create a Pipfile (if it doesn’t exist already) and install all the dependencies listed in the Pipfile into a virtual environment. It’s important to activate the virtual environment to ensure you’re using the isolated environment.


________________________________________________________________________


##### 2.3 Train the Model (optional)
If you want to retrain the model and regenerate the model.bin file, you can run the training script: `python train.py`
- This will execute the `train.py` script, which trains the model and saves it as `model.bin`, along with any necessary transformations like the DictVectorizer.
- The `model.bin` file will be used later when making predictions.

____________________________________________________________________________________________________________________________________________________


#### 3. Running the Prediction Locally
##### 3.1 Start the Waitress Server
First, run the Flask app with Waitress:
- Make sure you’re in the project directory.
- In one terminal window, start the Flask app by running `predict.py`
- This will launch the Flask app and Waitress will start serving the model at http://0.0.0.0:9090, meaning it will listen on port 9090 for incoming requests.

________________________________________________________________________

##### 3.2 Open a New Terminal
While the Flask server is running in the first terminal, open a new terminal window to run the prediction.

________________________________________________________________________


##### 3.3 Make Predictions
Once the server is running, you can test the predictions by sending a POST request to the `/predict` endpoint. You can do this either through the provided `predict-test.py` script or using `curl` from the command line.

________________________________________________________________________

###### - Using the Python Script (`predict-test.py`)
The easiest way to test predictions is by using the provided Python script, `predict-test.py`. In the new terminal window, run the following command: `python predict-test.py`. This will send a request to the server and print the prediction result.
- The script will use predefined input data and output the predicted placement status along with the probability of placement.
- You can modify predict-test.py if you want to test with different data.

________________________________________________________________________


###### - Using Curl
Alternatively, repeat steps 3.1 and 3.2, then run `curl` to send a POST request to the server for prediction. 
You can use the example command below or change the feature values:
`curl -X POST http://localhost:9090/predict -H "Content-Type: application/json" -d '{"cgpa": 7, "internships": 2, "projects": 2, "workshopscertifications": 3, "aptitudetestscore": 80, "softskillsrating": 4.6, "extracurricularactivities": "Yes", "placementtraining": "Yes", "ssc_marks": 78, "hsc_marks": 80}'`
- This sends a JSON payload with the student's features to the `/predict` endpoint.
- The response will be in JSON format, showing the predicted placement status and the probability of placement.

____________________________________________________________________________________________________________________________________________________


###### Troubleshooting: Restarting the Server
If the server is already running, and you want to restart it:
1. In the terminal where the server is running, stop the Flask server by pressing Ctrl+C.
2. Then, start the server again with: `python predict.py`
This will restart the server and allow you to continue making predictions.


____________________________________________________________________________________________________________________________________________________


###### Acknowledgements
Special thanks to the Datatalks Club for offering a free and practical course on Machine Learning. Alexey and the team are doing a great service to all learners.

____________________________________________________________________________________________________________________________________________________


###### License
This project is distributed under the MIT License. Refer to the [LICENSE](https://opensource.org/license/mit) file for more information.

____________________________________________________________________________________________________________________________________________________


###### Contact
- LinkedIn: [Ọláídé Bánkọ́lé](www.linkedin.com/in/obanky) 


