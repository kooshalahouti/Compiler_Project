class ClusteringCodeGenerator:
    def __init__(self):
        self.non_operands = [
            'SET_DATASET',
            'METHOD',
            'CLUSTERS',
            'EPS',
            'MIN_SAMPLES',
            'SCALE',
            'FIT',
            'PLOT',
            'SPECTRAL_CLUSTERS',
            'KMEANS', 'DBSCAN', 'AGGLOMERATIVE', 'SPECTRAL'
        ]
        self.operand_stack = []

        # DSL data
        self.dataset_path = None
        self.method = None     # KMEANS, DBSCAN, AGGLOMERATIVE, SPECTRAL
        self.n_clusters = None
        self.eps = 0.5
        self.min_samples = 5
        self.scale_data = False
        self.spectral_n_clusters = None
        self.do_fit = False
        self.do_plot = False

    def is_operand(self, label):
        return label not in self.non_operands

    def generate_code(self, post_order_list):
        for item in post_order_list:
            label = item['label']
            if self.is_operand(label):
                # It's an operand (string, int, float, bool)
                self.operand_stack.append(label)
            else:
                # It's a DSL node
                self.handle_node(label)
        return self.finalize_code()

    def handle_node(self, label):
        if label == 'SET_DATASET':
            self.handle_set_dataset()
        elif label == 'METHOD':
            self.handle_method()
        elif label == 'CLUSTERS':
            self.handle_clusters()
        elif label == 'EPS':
            self.handle_eps()
        elif label == 'MIN_SAMPLES':
            self.handle_min_samples()
        elif label == 'SCALE':
            self.handle_scale()
        elif label == 'FIT':
            self.do_fit = True
        elif label == 'PLOT':
            self.do_plot = True
        elif label == 'SPECTRAL_CLUSTERS':
            self.handle_spectral_clusters()
        elif label in ['KMEANS','DBSCAN','AGGLOMERATIVE','SPECTRAL']:
            # might push it on operand stack or handle in handle_method
            self.operand_stack.append(label)

    def handle_set_dataset(self):
        path_token = self.operand_stack.pop()  # e.g. '"data.csv"'
        self.dataset_path = path_token.strip('"')

    def handle_method(self):
        # we expect the method name on top of the stack
        method_label = self.operand_stack.pop()  # KMEANS, DBSCAN, ...
        self.method = method_label

    def handle_clusters(self):
        num = self.operand_stack.pop()
        self.n_clusters = int(num)

    def handle_eps(self):
        val = self.operand_stack.pop()
        self.eps = float(val)

    def handle_min_samples(self):
        val = self.operand_stack.pop()
        self.min_samples = int(val)

    def handle_scale(self):
        boolval = self.operand_stack.pop()
        if boolval.lower() == 'true':
            self.scale_data = True
        else:
            self.scale_data = False

    def handle_spectral_clusters(self):
        num = self.operand_stack.pop()
        self.spectral_n_clusters = int(num)

    def finalize_code(self):
        lines = []
        lines.append("import numpy as np")
        lines.append("import pandas as pd")
        lines.append("from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering")
        lines.append("from sklearn.preprocessing import StandardScaler")
        lines.append("import matplotlib.pyplot as plt")
        lines.append("")

        lines.append("# 1) Load dataset")
        if not self.dataset_path:
            self.dataset_path = "data.csv"
        lines.append(f'data = pd.read_csv("{self.dataset_path}")')
        lines.append("")

        lines.append("# 2) Optionally scale data")
        if self.scale_data:
            lines.append("scaler = StandardScaler()")
            lines.append("data_scaled = scaler.fit_transform(data)")
            lines.append("X = data_scaled")
        else:
            lines.append("X = data.values")
        lines.append("")

        lines.append("# 3) Define model based on DSL instructions")
        if not self.method:
            self.method = "KMEANS"  # default
        if self.method == "KMEANS":
            n_clusters = self.n_clusters if self.n_clusters else 3
            lines.append(f'model = KMeans(n_clusters={n_clusters}, random_state=42)')
        elif self.method == "DBSCAN":
            lines.append(f'model = DBSCAN(eps={self.eps}, min_samples={self.min_samples})')
        elif self.method == "AGGLOMERATIVE":
            n_clusters = self.n_clusters if self.n_clusters else 3
            lines.append(f'model = AgglomerativeClustering(n_clusters={n_clusters})')
        elif self.method == "SPECTRAL":
            # For spectral, we might or might not have n_clusters
            n_clusters = self.spectral_n_clusters if self.spectral_n_clusters else 3
            lines.append(f'# Example: from sklearn.cluster import SpectralClustering (not imported above but could be)')
            lines.append(f'# model = SpectralClustering(n_clusters={n_clusters}, affinity="nearest_neighbors")')
            lines.append('model = KMeans(n_clusters=2, random_state=42)  # Placeholder: DSL says SPECTRAL, but we need import')
        lines.append("")

        lines.append("# 4) Fit model & get labels")
        lines.append("labels = None")
        if self.do_fit:
            lines.append("labels = model.fit_predict(X)")
            lines.append('print("Unique cluster labels:", np.unique(labels))')
        else:
            lines.append("# DSL did not specify FIT, so no fitting done.")
        lines.append("")

        if self.do_plot:
            lines.append("# 5) Plot if user said PLOT, (only if 2D data?)")
            lines.append("plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')")
            lines.append(f"plt.title('{self.method} Clustering')")
            lines.append("plt.show()")
        else:
            lines.append("# No plotting done.")
        lines.append("")

        return "\n".join(lines)
