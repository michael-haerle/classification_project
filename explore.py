import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

def scatter_plot(train_telco):
    # Setting the variables for the average monthly charge and average tenure
    avg_monthly_charges = train_telco.monthly_charges.mean()
    avg_tenure = train_telco.tenure.mean()
    # Setting alpha
    alpha = 0.5
    # Setting the figure size
    plt.figure(figsize = (12, 10))

    # Plotting the figure
    sns.scatterplot(data=train_telco, x='tenure', y='monthly_charges', hue='churn_str', alpha=.7)

    # Plotting the lines for the average tenure and average monthly charge
    plt.axhline(avg_monthly_charges, color='lime')
    plt.axvline(avg_tenure, color='red')

    # Setting the limit for the x axis, this makes room for my annotation
    plt.xlim(0, 90)

    # Adding annotations to lable the lines for the average tenure and average monthly charge
    plt.annotate('Avg Monthly Charge', xy=(72,64), xytext=(74,72), arrowprops={'facecolor':'lime'})
    plt.annotate('Avg Tenure', xy=(32,118), xytext=(20,120), arrowprops={'facecolor':'red'})

    # Setting the legend, xlabel, ylabel, title, and making it look nice
    plt.legend(fancybox=True, shadow=True, prop={'size': 15})
    plt.xlabel('Tenure')
    plt.ylabel('Monthly Charges')
    plt.title('People who are above the Avg Monthly Charge and Below the Avg Tenure are more likely to Churn')
    plt.show()

    # Setting the null and alternate hypothesis 
    null_hyp = 'People who are above the Avg Monthly Charge and Below the Avg Tenure are independent with churn'
    alt_hyp = 'There is a relationship between churn and people who are above the Avg Monthly Charge and Below the Avg Tenure'

    # Creating the observed dataframe
    observed = pd.crosstab(train_telco.churn, train_telco.bel_avg_ten_abv_avg_mon_chrg)

    # Running the chi square test and running a if statement for the null hypothesis to be rejected or failed to reject
    chi2, p, degf, expected = stats.chi2_contingency(observed)
    if p < alpha:
        print('We reject the null hypothesis that', null_hyp)
        print(alt_hyp)
    else:
        print('We fail to reject the null hypothesis that', null_hyp)
        print('There appears to be no relationship between churn and people who are above the Avg Monthly Charge and Below the Avg Tenure')

    print('P-Value', p)
    print('Chi2', round(chi2, 2))
    print('Degrees of Freedom', degf)


def bar_plot(train_telco):
    # Setting the variables needed for the upcoming plot
    females = train_telco[train_telco.gender_Male == 0]
    males = train_telco[train_telco.gender_Male == 1]

    # Making a new column so the upcoming legend makes sense
    train_telco['gender_Male_str'] = train_telco.gender_Male.replace(0, 'Female')
    train_telco.gender_Male_str = train_telco.gender_Male_str.replace(1, 'Male')

    # Increasing the figure size and setting the title
    plt.figure(figsize = (7, 7))
    plt.title('Relationship of Churn and Phone Service')

    # Plotting the bar plot
    sns.barplot(x='phone_service', y='churn', hue='gender_Male_str', data=train_telco)

    # Setting the variable for the average churn
    churn_rate = train_telco.churn.mean()
    
    # Plotting the average churn line
    plt.axhline(churn_rate, label='Churn Rate')

    # Setting the x and y labels, and setting the legend
    plt.xlabel('Phone Service')
    plt.ylabel('Churn')
    plt.legend()
    plt.show()

    # Setting the alpha
    alpha = 0.05

    # Setting the null and alternative hypothesis
    null_hyp = 'Phone Service and churn are independent'
    alt_hyp = 'There is a relationship between churn and Phone Service'

    # Making the observed dataframe
    observed = pd.crosstab(train_telco.churn, train_telco.phone_service)

    # Running the chi square test and running a if statement for the null hypothesis to be rejected or failed to reject
    chi2, p, degf, expected = stats.chi2_contingency(observed)
    if p < alpha:
        print('We reject the null hypothesis that', null_hyp)
        print(alt_hyp)
    else:
        print('We fail to reject the null hypothesis that', null_hyp)
        print('There appears to be no relationship between churn and Phone Service')
        
    print('P-Value', p)
    print('Chi2', round(chi2, 2))
    print('Degrees of Freedom', degf)

    # Increasing the figure size and setting the title
    plt.figure(figsize = (7, 7))
    plt.title('Relationship of Females who Churned and Phone Service')

    # Plotting the bar plot
    sns.barplot(x='phone_service', y='churn', data=females)

    # Plotting the average churn line
    plt.axhline(churn_rate, label='Churn Rate')

    # Setting the x and y labels, and setting the legend
    plt.xlabel('Phone Service')
    plt.ylabel('Churn')
    plt.legend()
    plt.show()

    # Setting the null and alternative hypothesis
    null_hyp = 'Females who have Phone Service and churn are independent'
    alt_hyp = 'There is a relationship between churn and Females with Phone Service'

    # Making the observed dataframe
    observed = pd.crosstab(females.churn, females.phone_service)

    # Running the chi square test and running a if statement for the null hypothesis to be rejected or failed to reject
    chi2, p, degf, expected = stats.chi2_contingency(observed)
    if p < alpha:
        print('We reject the null hypothesis that', null_hyp)
        print(alt_hyp)
    else:
        print('We fail to reject the null hypothesis that', null_hyp)
        print('There appears to be no relationship between churn and Females with Phone Service')
        
    print('P-Value', p)
    print('Chi2', round(chi2, 2))
    print('Degrees of Freedom', degf)