# <a name="top"></a>Classification Project
![]()

by: Michael Haerle

<p>
  <a href="https://github.com/michael-haerle" target="_blank">
    <img alt="Michael" src="https://img.shields.io/github/followers/michael-haerle?label=Follow_Michael&style=social" />
  </a>
</p>


***
[[Project Description](#project_description)]
[[Project Planning](#planning)]
[[Key Findings](#findings)]
[[Data Dictionary](#dictionary)]
[[Data Acquire and Prep](#wrangle)]
[[Data Exploration](#explore)]
[[Statistical Analysis](#stats)]
[[Modeling](#model)]
[[Conclusion](#conclusion)]
___


## <a name="project_description"></a>Project Description:
Using the data science pipeline to practice with classification. In this repository you will find everything you need to replicate this project. This project uses the Telco dataset to find key drivers of churn. 

[[Back to top](#top)]

***
## <a name="planning"></a>Project Planning: 
[[Back to top](#top)]

### Project Outline:


        
### Hypothesis



### Target variable
- The target variable for this project is Churn.

### Need to haves (Deliverables):



### Nice to haves (With more time):
 - If I had more time with the project I would like to explore more combinations of features on my models and I would also implement more feature engineering.
 - I would also like to explore more why females that don't have phone service are less likely to churn.

***

## <a name="findings"></a>Key Findings:
[[Back to top](#top)]




***

## <a name="dictionary"></a>Data Dictionary  
[[Back to top](#top)]

### Data Used
---
| Attribute | Definition | Data Type |
| ----- | ----- | ----- |
| | | |
| | | |
| | | |
| | | |
| | | |
| | | |

***

## <a name="wrangle"></a>Data Acquisition and Preparation
[[Back to top](#top)]

![]()


### Wrangle steps: 


*********************

## <a name="explore"></a>Data Exploration:
[[Back to top](#top)]
- Python files used for exploration:
    - prepare.py 
    - acquire.py
    - modeling.py


### Takeaways from exploration:


***

## <a name="stats"></a>Statistical Analysis
[[Back to top](#top)]

### Stats Test 1: Chi Square


#### Hypothesis:
- The null hypothesis (H<sub>0</sub>) is
- The alternate hypothesis (H<sub>1</sub>) is 

#### Confidence level and alpha value:
- I established a 95% confidence level
- alpha = 1 - confidence, therefore alpha is 0.05

#### Results:


#### Summary:


### Stats Test 2: Chi Square


#### Hypothesis:
- The null hypothesis (H<sub>0</sub>) is 
- The alternate hypothesis (H<sub>1</sub>) is 

#### Confidence level and alpha value:
- I established a 95% confidence level
- alpha = 1 - confidence, therefore alpha is 0.05


#### Results:


#### Summary:


### Stats Test 3: Chi Square


#### Hypothesis:
- The null hypothesis (H<sub>0</sub>) is 
- The alternate hypothesis (H<sub>1</sub>) is 

#### Confidence level and alpha value:
- I established a 95% confidence level
- alpha = 1 - confidence, therefore alpha is 0.05


#### Results:


#### Summary:

***

## <a name="model"></a>Modeling:
[[Back to top](#top)]

### Model Preparation:

### Baseline
    
- Baseline Results: Accuracy 73%
    

- Selected features to input into models:
    - features = ['bel_avg_ten_abv_avg_mon_chrg', 'internet_service_type_None', 'internet_service_type_Fiber_optic', 'contract_type_Two_year', 'contract_type_One_year', 'gender_Male', 'monthly_charges', 'paperless_billing', 'tenure', 'dependents', 'partner', 'senior_citizen']

***

### Models:


#### Model 1: Random Forest


Model 1 results:
- RandomForestClassifier min_samples_leaf=12, max_depth=8, random_state=123
- Model stats:
- Accuracy: 0.81
- True Positive Rate: 0.51
- False Positive Rate: 0.08
- True Negative Rate: 0.92
- Flase Negative Rate: 0.49
- Precision: 0.71
- Recall: 0.51
- f1 score: 0.59
- Positive support: 1121
- Negative support: 3104
- Accuracy of random forest classifier on training set: 0.81



### Model 2 : K-Nearest Neighbor


Model 2 results:
- KNeighborsClassifier n_neighbors=15
- Model stats:
- Accuracy: 0.81
- True Positive Rate: 0.51
- False Positive Rate: 0.08
- True Negative Rate: 0.92
- Flase Negative Rate: 0.49
- Precision: 0.69
- Recall: 0.51
- f1 score: 0.58
- Positive support: 1121
- Negative support: 3104
- Accuracy of KNN classifier on training set: 0.81

### Model 3 : Logistic Regression

Model 3 results:
- LogisticRegression C=.01, random_state=123, intercept_scaling=1, solver=lbfgs
- Model stats:
- Accuracy: 0.80
- True Positive Rate: 0.46
- False Positive Rate: 0.09
- True Negative Rate: 0.91
- Flase Negative Rate: 0.54
- Precision: 0.66
- Recall: 0.46
- f1 score: 0.55
- Positive support: 1121
- Negative support: 3104
- Accuracy of Logistic Regression classifier on training set: 0.80


## Selecting the Best Model:

### Use Table below as a template for all Modeling results for easy comparison:

| Model | Validation |
| ---- | ----|
| Baseline | 0.73 |
| Random Forest | 0.80 |
| K-Nearest Neighbor | 0.79 | 
| Logistic Regression | 0.80 |


- {Random Forest} model performed the best


## Testing the Model

- Model Testing Results: 81% Accuracy

***

## <a name="conclusion"></a>Conclusion:
[[Back to top](#top)]
