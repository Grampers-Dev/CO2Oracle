import streamlit as st

def predict_co2(X_live, co2_features, co2_pipeline_dc_fe, co2_pipeline_model):

    # Subset features related to this pipeline from live data
    X_live_co2 = X_live.filter(co2_features)

    # Apply data cleaning / feature engineering pipeline to live data
    X_live_co2_dc_fe = co2_pipeline_dc_fe.transform(X_live_co2)

    # Predict CO2 emissions
    co2_prediction = co2_pipeline_model.predict(X_live_co2_dc_fe)
    
    # Display the prediction results
    statement = (
        f'### The predicted CO2 emission is **{co2_prediction[0]:.2f}** units.')
    
    st.write(statement)

    return co2_prediction

def predict_sector_co2(X_live, sector_features, sector_pipeline, sector_labels_map):

    # Subset features related to this pipeline from live data
    X_live_sector = X_live.filter(sector_features)

    # Predict the CO2 emission sector
    sector_prediction = sector_pipeline.predict(X_live_sector)
    sector_prediction_proba = sector_pipeline.predict_proba(X_live_sector)
    
    # Create logic to display the results
    sector_prob = sector_prediction_proba[0, sector_prediction][0]*100
    sector_name = sector_labels_map[sector_prediction[0]]

    statement = (
        f"* The model predicts that the sector is **{sector_name}** with a probability of {sector_prob.round(2)}%."
    )
    st.write(statement)

def predict_cluster(X_live, cluster_features, cluster_pipeline, cluster_profile):

    # Subset features related to this pipeline from live data
    X_live_cluster = X_live.filter(cluster_features)

    # Predict the cluster
    cluster_prediction = cluster_pipeline.predict(X_live_cluster)

    statement = (
        f"### The data is expected to belong to **cluster {cluster_prediction[0]}**")
    st.write("---")
    st.write(statement)

    # Assuming clusters represent different CO2 emission profiles, you can provide interpretations:
    statement = (
        f"* Historically, **Cluster 0 represents low CO2 emissions** while "
        f"**Cluster 1 represents moderate emissions** and "
        f"**Cluster 2 represents high CO2 emissions**."
    )
    st.info(statement)

    # Example cluster profile description
    statement = (
        f"* The cluster profiles can be interpreted as follows:\n"
        f"* Cluster 0: Low CO2 emissions, possibly renewable energy sources.\n"
        f"* Cluster 1: Moderate CO2 emissions, mixed energy sources.\n"
        f"* Cluster 2: High CO2 emissions, primarily fossil fuels."
    )
    st.success(statement)

    # Prevent displaying the index in st.table() or st.write()
    cluster_profile.index = [" "] * len(cluster_profile)
    # Display the cluster profile in a table
    st.table(cluster_profile)
