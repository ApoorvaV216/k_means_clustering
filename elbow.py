distortions = []
for j in range(1, 11):
    km = KMeans(
        n_clusters=j, init='random',
        n_init=10, max_iter=300,
        tol=1e-04, random_state=0
    )
    km.fit(X)
    distortions.append(km.inertia_)
pt.plot(range(1, 11), distortions, marker='o')
pt.xlabel('Number of clusters')
pt.ylabel('Distortion')
pt.show()