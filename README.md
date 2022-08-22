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
| customer_id | | object |
| senior_citizen | | int64 |
| partner | | int64 |
| dependents | | int64 |
| tenure | | int64 |
| phone_service | | int64 |
| multiple_lines | | object |
| online_security | | object |
| online_backup | | object |
| device_protection | | object |
| tech_support | | object |
| streaming_tv | | object |
| streaming_movies | | object |
| paperless_billing | | int64 |
| monthly_charges | | float64 |
| total_charges | | float64 |
| churn | | int64 |
| contract_type | | object |
| internet_service_type | | object |
| gender_Male | | uint8 |
| contract_type_One_year | | uint8 |
| contract_type_Two_year | | uint8 |
| internet_service_type_Fiber_optic | | uint8 |
| internet_service_type_None | | uint8 |
| bel_avg_ten_abv_avg_mon_chrg | | int64 |
| baseline | | int64 |
| gender_Male_str | | object |
| churn_str | | object|
***

## <a name="wrangle"></a>Data Acquisition and Preparation
[[Back to top](#top)]

![]()


### Prepare steps: 
- Droped duplicate columns
- Created dummy variables
- Concatenated the dummy dataframe
- Changed the type for senior_citizen, tenure, and monthly_charges
- Mapped the yes and no to 1 and 0 for columns partner, dependents, phone_service, paperless_billing, and churn
- Dropped columns not needed
- Changed the type of total_charges by replacing the white space with a 0
- Set variables for the mean of tenure and monthly charges
- Used those variables to feature engineer a new column where it returned a true if they were above the average monthly charge and below the average tenure
- Mapped the true and false of that columns to 1 and 0
- Split into the train, validate, and test sets

*********************

## <a name="explore"></a>Data Exploration:
[[Back to top](#top)]
- Python files used for exploration:
    - prepare.py 
    - acquire.py
    - modeling.py


### Takeaways from exploration:
- The new column I made for people above the Avg Monthly Charge and Below the Avg Tenure seems to be a good column to use in the modeling phase.
- Most of the numeric columns will be used for the modeling phase.

***

## <a name="stats"></a>Statistical Analysis
[[Back to top](#top)]

### Stats Test 1: Chi Square


#### Hypothesis:
- The null hypothesis (H<sub>0</sub>) is: Contract Type and churn are independent
- The alternate hypothesis (H<sub>1</sub>) is: There is a relationship between churn and Contract Type

#### Confidence level and alpha value:
- I established a 95% confidence level
- alpha = 1 - confidence, therefore alpha is 0.05

#### Results:
- We reject the null hypothesis that Contract Type and churn are independent
- There is a relationship between churn and Contract Type
- P-Value 3.2053427834370596e-153
- Chi2 702.26
- Degrees of Freedom 2


### Stats Test 2: Chi Square


#### Hypothesis(First Plot):
- The null hypothesis (H<sub>0</sub>) is: Phone Service and churn are independent
- The alternate hypothesis (H<sub>1</sub>) is: There is a relationship between churn and Phone Service

#### Confidence level and alpha value(First Plot):
- I established a 95% confidence level
- alpha = 1 - confidence, therefore alpha is 0.05


#### Results(First Plot):
- We fail to reject the null hypothesis that Phone Service and churn are independent
- There appears to be no relationship between churn and Phone Service
- P-Value 0.11104986402814591
- Chi2 2.54
- Degrees of Freedom 1

#### Hypothesis(Second Plot):
- The null hypothesis (H<sub>0</sub>) is: Females who have Phone Service and churn are independent
- The alternate hypothesis (H<sub>1</sub>) is: There is a relationship between churn and Females with Phone Service

#### Confidence level and alpha value(Second Plot):
- I established a 95% confidence level
- alpha = 1 - confidence, therefore alpha is 0.05


#### Results(Second Plot):
- We reject the null hypothesis that Females who have Phone Service and churn are independent
- There is a relationship between churn and Females with Phone Service
- P-Value 0.0298505787547087
- Chi2 4.72
- Degrees of Freedom 1


### Stats Test 3: Chi Square


#### Hypothesis:
- The null hypothesis (H<sub>0</sub>) is: People who are above the Avg Monthly Charge and Below the Avg Tenure are independent with churn
- The alternate hypothesis (H<sub>1</sub>) is: There is a relationship between churn and people who are above the Avg Monthly Charge and Below the Avg Tenure

#### Confidence level and alpha value:
- I established a 95% confidence level
- alpha = 1 - confidence, therefore alpha is 0.05


#### Results:
- We reject the null hypothesis that People who are above the Avg Monthly Charge and Below the Avg Tenure are independent with churn
- There is a relationship between churn and people who are above the Avg Monthly Charge and Below the Avg Tenure
- P-Value 5.788583939458989e-132
- Chi2 597.52
- Degrees of Freedom 1


***

## <a name="model"></a>Modeling:
[[Back to top](#top)]

### Baseline
    
- Baseline Results: Accuracy 73%
    

- Selected features to input into models:
    - features = ['bel_avg_ten_abv_avg_mon_chrg', 'internet_service_type_None', 'internet_service_type_Fiber_optic', 'contract_type_Two_year', 'contract_type_One_year', 'gender_Male', 'monthly_charges', 'paperless_billing', 'tenure', 'dependents', 'partner', 'senior_citizen']

***

## Models:


### Model 1: Random Forest


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

- There are positive correlations with churn and monthly charges, papperless billing, fiber optic, phone service, senior citizen, and those who are above the average monthly charges and below the average tenure.
- There are negative correlations with churn and tenure, total charges, no internet service, and a two year contract.
- There is a relationship between churn and contract type.
- There was not a relationship between both genders who churn and phone service, however there was a relationship between females who churn and phone service.
- There was a relationship between churn and people who are above the average monthly charge and below the average tenure.

#### Idealy we would like to find a way to incentivise more people to sign a one or two year contract as opposed to a month-to-month contract. It would also be benificial to get more people to stay past the average tenure and keep their cost at or below the average monthly charge. 

[[Back to top](#top)]
