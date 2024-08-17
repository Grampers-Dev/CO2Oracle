import streamlit as st
import pandas as pd
from sklearn.cluster import KMeans
from yellowbrick.cluster import KElbowVisualizer, SilhouetteVisualizer
import matplotlib.pyplot as plt

def page_cluster_analysis_body():
    st.title("ML: Cluster Analysis")

    # Load the dataset
    df = pd.read_csv('path/to/your/Co2Emissions.csv')
    
    st.header("Cluster Analysis Overview")
    st.write("""
    This section focuses on clustering analysis to segment emission sources based on their characteristics.
    """)

    st.header("Elbow Method for Optimal Number of Clusters")
    
    # Prepare data for clustering
    X = df.drop(columns=['Country', 'Year'])  # Modify as per your dataset structure
    model = KMeans(random_state=0)
    
    # Elbow Method
    visualizer = KElbowVisualizer(model, k=(2,10))
    visualizer.fit(X)
    visualizer.show()
    st.pyplot(plt)
    
    st.header("Silhouette Analysis")
    
    n_clusters = 4  # Choose an appropriate number of clusters based on the elbow method
    model = KMeans(n_clusters=n_clusters, random_state=0)
    visualizer = SilhouetteVisualizer(model)
    visualizer.fit(X)
    visualizer.show()
    st.pyplot(plt)

    st.write(f"""
    The clustering analysis suggests that {n_clusters} clusters are optimal for segmenting the emission sources.
    """)

