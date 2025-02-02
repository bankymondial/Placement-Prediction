#### Problem Definition

This project aims to predict the placement of students based on their academic and extracurricular activities. The data source was not explicit on the target variable, `placementstatus` whether a student is placed or not. However, one can infer from variables such as higher and senior secondary marks that the model seeks to predict a student's placement at a higher level of education, maybe college. The data for the modelling can found at [Kaggle](https://www.kaggle.com/datasets/ruchikakumbhar/placement-prediction-dataset?select=placementdata.csv).

___________________________________________________________________________________________________________________________________________________


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



# Model Performance Comparison

| Metric                  | **Logistic Regression** | **Gradient Boosting** | **Random Forest** | **Most Important Features** | **Best Model**    |
|-------------------------|-------------------------|-----------------------|-------------------|----------------------------|-------------------|
| **Validation Accuracy**  | 0.7870                  | 0.7755                | 0.7425            | 0.7790                     | Logistic Regression |
| **Recall**               | 0.7590                  | 0.7322                | 0.7159            | 0.7648                     | Logistic Regression |
| **F1 Score**             | 0.7538                  | 0.7370                | 0.7049            | 0.7483                     | Logistic Regression |
| **ROC AUC**              | 0.8716                  | 0.8510                | 0.8021            | 0.8550                     | Logistic Regression |
| **Test Accuracy**        | 0.7770                  | 0.7830                | N/A               | N/A                        | Gradient Boosting  |
| **Test Recall**          | 0.7488                  | 0.6869                | N/A               | N/A                        | Logistic Regression |
| **Test F1 Score**        | 0.7307                  | 0.7189                | N/A               | N/A                        | Logistic Regression |
| **Test ROC AUC**         | 0.8572                  | 0.8608                | N/A               | N/A                        | Gradient Boosting  |

## **Best Model Summary**

**Logistic Regression** is the best-performing model overall, with the highest scores across **Validation Accuracy**, **Recall**, **F1 Score**, and **ROC AUC**. It consistently outperforms other models on these key metrics, especially in **recall**, which is crucial for identifying placed students. **Gradient Boosting** comes close in **test set performance**, particularly with its higher **Test Accuracy** and **Test ROC AUC**, but **Logistic Regression** provides a better overall balance between precision and recall.

**Most Important Features Model** also performed well, with **high recall (0.7648)** and **F1 score (0.7483)** on the validation set, but it didn't surpass **Logistic Regression** in key metrics.

**Decision**: Logistic Regression is the preferred model for deployment due to its consistency and ability to identify placed students effectively.



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
  (https://github.com/bankymondial/Placement-Prediction.git)]
    cd Predicting-Gym-Class-Attendance
    
##### 2.2 Install Dependencies
Set up a virtual environment and install the necessary Python packages:
    `pipenv install`
    
##### 2.3 Train the Model (optional)
To retrain the model, run the training script:
   `python train.py`
   
_This generates `model.bin`, which contains the trained model and the DictVectorizer._

____________________________________________________________________________________________________________________________________________________


### 3. Running the Prediction Locally
##### 3.1 Start the Waitress Server
Run the Flask app with Waitress:
    waitress-serve --listen=0.0.0.0:5454 predict:app
_The API will be accessible at `http://localhost:5454/`._

##### 3.2 Make Predictions
    You can test predictions using `curl` or the provided `predict-test.py` script:
###### - Using Curl
    curl -X POST http://localhost:5454/predict \
    -H "Content-Type: application/json" \
    -d '{"months_as_member": 12, "weight": 70, "category": "Cycling"}'
###### - Using the Python script:
    python predict-test.py


____________________________________________________________________________________________________________________________________________________


###### Why This Project Matters
By predicting .........,  can:
- .
- .
- .


____________________________________________________________________________________________________________________________________________________


###### Acknowledgements
Special thanks to the Datatalks Club for offering a free and practical course on Machine Learning. Deep gratitude to Alexey and the team for their hard work and dedication.

____________________________________________________________________________________________________________________________________________________


###### License
This project is distributed under the MIT License. Refer to the [LICENSE](https://opensource.org/license/mit) file for more information.

____________________________________________________________________________________________________________________________________________________


###### Contact
- LinkedIn: [Ọláídé Bánkọ́lé](www.linkedin.com/in/obanky) 


