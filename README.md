## Predicting Placement

This project aims to predict ...

### Problem Definition


____________________________________________________________________________________________________________________________________________________


### Repository Overview
This repository contains:

1. Training Scripts: 
2. Prediction Scripts: 
3. Deployment Scripts: 
4. API Documentation: 
5. This repository also contains the dataset, `placementdata.csv` which can also be found on [Kaggle](https://www.kaggle.com/datasets/ruchikakumbhar/placement-prediction-dataset?select=placementdata.csv).
6. Deployment to the cloud: 

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


### Model Comparison: Validation and Test Set Performance

| **Model**               | **Validation Accuracy** | **Test Accuracy** | **Recall** | **F1 Score** | **ROC AUC** |
|-------------------------|-------------------------|-------------------|------------|--------------|-------------|
| **Baseline Model**       | 0.7825                  | 0.8045            | 0.7772     | 0.7626       | 0.8720      |
| **Important Features Model** | 0.7750                | N/A               | 0.7532     | 0.7420       | 0.8652      |
| **Random Forest**        | 0.7390                  | N/A               | 0.6799     | 0.6911       | 0.8124      |
| **Gradient Boosting (Tuned)** | 0.7843             | 0.7945            | 0.7017     | 0.7340       | 0.8655      |

Summary:
This table compares the performance of different models—Baseline, Important Features Model, Random Forest, and Gradient Boosting—on both the validation and test sets. Metrics like Accuracy, Recall, F1 Score, and ROC AUC were evaluated to assess the models' generalization and ability to predict outcomes. The Baseline model performed the best overall in terms of test accuracy, while Gradient Boosting showed the highest validation accuracy after tuning.

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


