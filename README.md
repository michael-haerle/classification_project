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


- Model 1 results:



### Model 2 : K-Nearest Neighbor


- Model 2 results:


### Model 3 : Logistic Regression

- Model 3 results:



## Selecting the Best Model:

### Use Table below as a template for all Modeling results for easy comparison:

| Model | Validation |
| ---- | ----|
| Baseline | 0.167366 |
| Random Forest | 0.166731 |
| K-Nearest Neighbor | 0.155186 | 
| Logistic Regression | 0.166731 |


- {} model performed the best


## Testing the Model

- Model Testing Results

***

## <a name="conclusion"></a>Conclusion:
[[Back to top](#top)]
