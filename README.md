# CO2Oracle

## Dataset Content

The dataset is sourced from [Kaggle](https://www.kaggle.com/datasets/thedevastator/global-fossil-co2-emissions-by-country-2002-2022/data). I have created a fictitious scenario to demonstrate how predictive analytics can be applied in a real-world project.

### Dataset Structure

- **Rows:** Each row represents a data record.
- **Columns:** Each column contains an attribute related to CO2 emissions.

### Included Information

- **Emission Sources:** Data on CO2 emissions from various sources such as cement production, coal combustion, gas combustion, oil combustion, gas flaring, and other sources.
- **Temporal Data:** Yearly data capturing the changes in CO2 emissions over time.
- **Geographical Data:** Information on the country where the emissions were recorded.

| Variable          | Meaning                                                        | Units                                                                               |
|-------------------|----------------------------------------------------------------|-------------------------------------------------------------------------------------|
| Country           | Country where CO2 emissions are recorded                       | Country name                                                                        |
| Year              | Year of the CO2 emission data                                  | Year (e.g., 1990, 2000)                                                             |
| Cement            | CO2 emissions from cement production                           | Metric tons (t)                                                                     |
| Coal              | CO2 emissions from coal combustion                             | Metric tons (t)                                                                     |
| Gas               | CO2 emissions from natural gas combustion                      | Metric tons (t)                                                                     |
| Oil               | CO2 emissions from oil combustion                              | Metric tons (t)                                                                     |
| Flaring           | CO2 emissions from gas flaring                                 | Metric tons (t)                                                                     |
| Other             | CO2 emissions from other sources                               | Metric tons (t)                                                                     |

## Project Terminology & Jargon

In the CO2 Oracle project, specific terms and definitions pertinent to the analysis of CO2 emissions data include:

- **Emission Sources:** Various sources contributing to CO2 emissions such as cement production, coal combustion, gas combustion, oil combustion, gas flaring, and other sources.
- **Temporal Data:** Yearly data capturing changes in CO2 emissions over time.
- **Geographical Data:** Information on the country where CO2 emissions were recorded.

## Business Requirements

As a Data Analyst at CO2 Oracle, I have been engaged by a Goverment Agency to provide actionable insights and data-driven recommendations. The objective is to manage CO2 emissions effectively and understand how different sources contribute to the overall emissions. The client has shared the data spanning multiple years and various emission sources.

### Understanding Emission Patterns

The client aims to comprehend the patterns in CO2 emissions from different sources. They are particularly interested in identifying the most relevant variables that correlate with changes in emissions over time.

### Predictive Modeling for Emissions

The client wants to determine whether certain factors can predict changes in CO2 emissions accurately. Specifically, they are interested in:

- Identifying which factors can move a source with moderate predictive power, like 'Flaring', to a more predictable category.

## 1 - Understanding Emission Patterns

### Objective

To analyze the dataset to reveal significant patterns and correlations among different CO2 emission sources. The goal is to understand how each source contributes to the total emissions and identify key variables that influence these emissions.

### Approach

- **Correlation Analysis**: Use Spearman and Pearson correlation coefficients to determine the relationships between 'Year', 'Country', and various emission sources (Coal, Oil, Gas, Cement, Flaring, Other).

### Deliverables

- **Correlation Heatmaps**: Visual representations of the Spearman and Pearson correlations to highlight the strength and nature of relationships between variables.

## 2 - Predictive Modeling for Emissions

### Objective

To develop models that can predict future CO2 emissions based on historical data. The focus will be on leveraging the strong predictive relationships identified in the data analysis phase.

### Approach

- **Time Series Analysis**: Utilize historical 'Year' data to forecast future emissions for key emission sources.
- **Clustering Analysis**: Segment emission sources into clusters based on their characteristics and predictive factors. Identify key factors that influence a source's membership in a cluster.
- **Predictive Modeling**: Build models to predict emissions and understand what factors could maintain or move sources into more stable emission clusters.

### Deliverables

- **Forecast Models**: Time series models predicting emissions based on historical 'Year' data.
- **Cluster Analysis Report**: Identification of clusters and the factors influencing cluster membership.
- **Predictive Insights**: Recommendations on how to manage and reduce CO2 emissions by targeting key predictive factors.

## Conclusion

By understanding the patterns in CO2 emissions and developing robust predictive models, the Goverment Agencie can make data-driven decisions to manage emissions effectively. The insights derived from correlation analyses will enable the client to forecast future emissions accurately and identify actionable strategies to reduce the environmental impact.

### Next Steps

- **Data Preparation**: Ensure the dataset is clean and preprocessed for analysis.
- **Analysis Phase**: Conduct correlation analyses to uncover key insights.
- **Model Development**: Develop predictive models and validate their accuracy.
- **Reporting**: Present findings and recommendations to the client, emphasizing actionable strategies to manage CO2 emissions.

## Hypothesis and Validation Approach

### 1 - Hypothesis: CO2 Emissions are Increasing Over Time

I suspect that CO2 emissions from various sources have been increasing over the years.

- **Validation Approach**: Conduct a correlation study (Spearman and Pearson) to investigate the relationship between 'Year' and CO2 emissions from different sources (Coal, Oil, Gas, Cement, Flaring, Other).

### 2 - Hypothesis: Cement Production is a Major Contributor to CO2 Emissions

My analysis suggests that emissions from cement production are significantly correlated with the year.

- **Validation Approach**: Use a correlation study and PPS (Predictive Power Score) to validate this hypothesis. This will help determine the strength and nature of the relationship between 'Year' and 'Cement' emissions.

## Mapping Business Requirements to Data Visualizations and ML Tasks

### Business Requirement 1: Data Visualization and Correlation Study

- **Objective**: Analyze the data to uncover significant patterns and correlations among different CO2 emission sources.

- **Approach**:
  - Inspect the data related to CO2 emissions from different sources.
  - Conduct a correlation study (Spearman and Pearson) to understand how variables like 'Year' and 'Country' correlate with different emission sources.
  - Visualize the main variables against CO2 emissions to derive insights.

- **Deliverables**:
  - Correlation Heatmaps: Visual representations of the Spearman and Pearson correlations.
  - Detailed analysis of how each source contributes to the total emissions and identification of key variables influencing these emissions.

### Business Requirement 2: Predictive Modeling and Cluster Analysis

- **Objective**: Develop predictive models to forecast future CO2 emissions and understand the characteristics of different emission sources.

- **Approach**:
  - **Time Series Analysis**: Build models using historical 'Year' data to predict future emissions for key sources.
  - **Classification and Regression**: Develop models to predict whether certain sources will have higher emissions in the future and to forecast specific emission levels.
  - **Cluster Analysis**: Segment emission sources into clusters based on their characteristics and predictive factors. Identify key factors that influence a source's membership in a cluster.
  - **Cluster Profiling**: Analyze the clusters to present potential strategies to manage emissions and reduce environmental impact.

- **Deliverables**:
  - **Forecast Models**: Time series models predicting future emissions based on historical data.
  - **Cluster Analysis Report**: Identification of clusters and the factors influencing their membership.
  - **Predictive Insights**: Recommendations on how to manage and reduce CO2 emissions by targeting key predictive factors.

## Conclusion

By conducting a thorough analysis of CO2 emissions and developing predictive models, I can provide actionable insights to the Goverment Agencie. These insights will enable the client to forecast future emissions accurately and implement strategies to manage and reduce the environmental impact effectively.

### Next Steps

- **Data Preparation**: Clean and preprocess the dataset for analysis.
- **Analysis Phase**: Conduct correlation and PPS score analyses to uncover key insights.
- **Model Development**: Develop and validate predictive models.
- **Reporting**: Present findings and recommendations to the client, with a focus on actionable strategies to manage CO2 emissions.

## ML Business Case

### Predicting CO2 Emissions

#### Classification Model

I aim to develop an ML model to predict whether CO2 emissions from specific sources will increase or decrease based on historical data. The target variable is categorical, representing the two classes: increase (1) or decrease (0). This model will be a supervised, binary classification model.

- **Objective**: Provide insights to environmental analysts to manage and mitigate CO2 emissions effectively.
- **Success Metrics**:
  - Achieve at least 80% recall for predicting increases in emissions on both the training and test sets.
  - The model will be considered a failure if:
    - After three months of deployment, more than 30% of predicted increases in emissions are incorrect.
    - The precision for predicting decreases in emissions is lower than 80% on both the training and test sets.
- **Model Output**: A flag indicating whether CO2 emissions will increase or decrease, along with the associated probability. Predictions will be made in real-time, based on input data provided by environmental analysts.
- **Current Approach**: No existing method to predict changes in CO2 emissions.
- **Training Data**: Historical data on CO2 emissions, excluding non-predictive variables like unique identifiers.

#### Predicting Emission Levels

#### Regression Model

I want to develop an ML model to predict future emission levels for sources expected to increase in emissions. The target variable is continuous, representing emission levels.

- **Objective**: Provide insights to environmental analysts to manage and mitigate CO2 emissions effectively.
- **Success Metrics**:
  - Achieve an R2 score of at least 0.7 on both the training and test sets.
  - The model will be considered a failure if:
    - After 12 months of deployment, more than 30% of predictions are off by more than 50%.
- **Model Output**: A continuous value representing predicted emission levels. Predictions will be made in real-time.
- **Current Approach**: No existing method to predict emission levels.
- **Training Data**: Historical data on CO2 emissions, filtered to include only instances where emissions increased, excluding non-predictive variables like unique identifiers.

#### Classification Model for Emission Duration

Before finalizing MY approach, i considered a regression model to predict the duration of emission increases but did not meet the performance requirements (at least 0.7 R2 score). Instead, i converted this task to a classification problem by discretizing the target into three ranges: <4 months, 4-20 months, and >20 months.

- **Objective**: Provide insights to environmental analysts on the duration of emission increases.
- **Success Metrics**:
  - Achieve at least 0.8 recall for predicting increases lasting <4 months on both the training and test sets.
  - The model will be considered a failure if:
    - After three months of deployment, more than 30% of predictions for <4 months are incorrect.
- **Model Output**: A class representing the range of emission increase duration. Predictions will be made in real-time.
- **Current Approach**: No existing method to predict emission increase duration.
- **Training Data**: Historical data on CO2 emissions, filtered to include only instances where emissions increased, excluding non-predictive variables like unique identifiers.

### Cluster Analysis

#### Clustering Model

I aim to develop an ML model to cluster similar emission sources based on their characteristics. This is an unsupervised learning task.

- **Objective**: Provide insights to environmental analysts for better management of CO2 emissions.
- **Success Metrics**:
  - Achieve an average silhouette score of at least 0.45.
  - The model will be considered a failure if it suggests more than 15 clusters, making it impractical to interpret.
- **Model Output**: A categorical variable representing cluster membership, appended to the dataset.
- **Current Approach**: No existing method to group similar emission sources.
- **Training Data**: Historical data on CO2 emissions, excluding non-predictive variables like unique identifiers and emissions totals.

## Deployment

This project was deployed to [Heroku](https://heroku.com/) using the following steps:

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.

### Heroku

- The App live link is: `https://YOUR_APP_NAME.herokuapp.com/`
- Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
- The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App on the top of the page to access your App.

## Main Data Analysis and Machine Learning Libraries

- Numpy:
For efficient calculations on large datasets, particularly pixel data.
Normalizing pixel data.
Calculating means and standard deviations.
Serving as a foundation for other data analysis and machine learning libraries.

- Pandas:
Utilized mainly for managing data with pandas DataFrames.

- Matplotlib & Seaborn:
Used for data visualization, including plotting and displaying images from pixel data.
Generating metric plots and histograms.

- Main Machine Learning libraries used:

- Scikit Learn:
Utilized for hyperparameter optimization through GridSearchCV.

## Run locally

This repo covers the entire process of creating a ML model. From collecting and processing the data, to conducting hyperparameter optimization, data augmentation, defining and training the model on the data.

__To use this repo, follow these steps:__

1. Fork or clone this repository
2. Install dependencies by running:
	```bash
	pip install -r "requirements-dev.txt"
	```
3. Register an account with [Kaggle](https://www.kaggle.com/) and create a new API token, download the kaggle.json and place it in the projects root directory.
4. Run the notebooks in the jupyter_notebooks folder in the specified order.
	- __DataCollection.ipynb:__ Downloads the dataset and extracts specified number of images.
	- __DataVisualization.ipynb:__ Conducts studies on the data and saves insightful plots.
	- __Model.ipynb:__ Prepares data, performs data augmentation and hyperparameter optimization, defines model architecture, trains, evaluates and saves a ML model.
5. Start the web app by running:
	```bash
	streamlit run Home.py
	```
