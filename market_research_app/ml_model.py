from sklearn.cluster import KMeans

def segment_data(data):
    model = KMeans(n_clusters=3)
    segments = model.fit_predict(data)
    return segments
