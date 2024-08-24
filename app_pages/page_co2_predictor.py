import streamlit as st
import pandas as pd
from src.data_management import load_co2_data, load_pkl_file
from src.machine_learning.predictive_analysis_ui import (
    predict_co2_emission,
    predict_cluster)

def page_co2_predictor():

    # load CO2 prediction files
    version = 'v1'
    co2_pipe_dc_fe = load_pkl_file(
        f'outputs/ml_pipeline/predict_co2/{version}/reg_pipeline_data_cleaning_feat_eng.pkl')
    co2_pipe_model = load_pkl_file(
        f"outputs/ml_pipeline/predict_co2/{version}/reg_pipeline_model.pkl")
    co2_features = (pd.read_csv(f"outputs/ml_pipeline/predict_co2/{version}/X_train.csv")
                      .columns
                      .to_list()
                      )

#    # load cluster analysis files
#    version = 'v1'
#    cluster_pipe = load_pkl_file(
#        f"outputs/ml_pipeline/cluster_analysis/{version}/cluster_pipeline.pkl")
#    cluster_features = (pd.read_csv(f"outputs/ml_pipeline/cluster_analysis/{version}/TrainSet.csv")
#                        .columns
#                        .to_list()
#                        )
#    cluster_profile = pd.read_csv(
#        f"outputs/ml_pipeline/cluster_analysis/{version}/clusters_profile.csv")

    st.write("### CO2 Emissions Predictor Interface")
    st.info(
        f"* This interface allows you to predict CO2 emissions based on various input factors. "
        f"You can also determine which cluster the input data falls into and make informed decisions based on the results."
    )
    st.write("---")

    # Generate Live Data
    X_live = draw_co2_input_widgets(co2_features)

    # predict on live data
    if st.button("Run Predictive Analysis"):
        co2_prediction = predict_co2_emission(
            X_live, co2_features, co2_pipe_dc_fe, co2_pipe_model)

        predict_cluster(X_live, cluster_features,
                        cluster_pipe, cluster_profile)

def draw_co2_input_widgets(co2_features):
    # load dataset
    df = load_co2_data()
    percentageMin, percentageMax = 0.4, 2.0

    col1, col2, col3, col4 = st.columns(4)

    # create an empty DataFrame, which will be the live data
    X_live = pd.DataFrame([], index=[0])

    # Define widgets for each feature (example features, adjust based on your data)
    with col1:
        feature = "Coal"
        st_widget = st.number_input(
            label=feature,
            min_value=df[feature].min() * percentageMin,
            max_value=df[feature].max() * percentageMax,
            value=df[feature].median()
        )
    X_live[feature] = st_widget

    with col2:
        feature = "Oil"
        st_widget = st.number_input(
            label=feature,
            min_value=df[feature].min() * percentageMin,
            max_value=df[feature].max() * percentageMax,
            value=df[feature].median()
        )
    X_live[feature] = st_widget

    with col3:
        feature = "Gas"
        st_widget = st.number_input(
            label=feature,
            min_value=df[feature].min() * percentageMin,
            max_value=df[feature].max() * percentageMax,
            value=df[feature].median()
        )
    X_live[feature] = st_widget

    with col4:
        feature = "Cement"
        st_widget = st.number_input(
            label=feature,
            min_value=df[feature].min() * percentageMin,
            max_value=df[feature].max() * percentageMax,
            value=df[feature].median()
        )
    X_live[feature] = st_widget

    # You can add more features as necessary

    return X_live

