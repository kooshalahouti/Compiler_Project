class ClusteringCodeGenerator:
    def __init__(self):
        self.non_operands = ['cluster', 'method_name']
        self.operand_stack = []
        self.method = None
        self.params = {}

    def is_operand(self, label):
        return label not in self.non_operands

    def generate_code(self, post_order_list):
        for item in post_order_list:
            label = item['label']
            if '=' in label:
                # Handle parameters like `n_clusters=3`
                key, value = label.split('=')
                self.params[key] = int(value) if value.isdigit() else value
            else:
                # Handle non-parameter labels
                self.handle_node(label)

        return self.finalize_code()

    def handle_node(self, label):
        if label == 'method_name':
            # Set clustering method
            self.method = self.operand_stack.pop()
        elif label == 'cluster':
            pass
        else:
            # Push method name onto the stack
            self.operand_stack.append(label)

    def finalize_code(self):
        lines = [
            "import numpy as np",
            "import pandas as pd",
            "from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering, SpectralClustering",
            "from sklearn.preprocessing import StandardScaler",
            "import matplotlib.pyplot as plt",
            "",
            "# 1) Load dataset",
            'data = pd.read_csv("data.csv")',
            "X = data.values",
            "",
            "# 2) Define model based on DSL instructions",
        ]

        # Generate clustering code
        if self.method == "DBSCAN":
            eps = self.params.get('epsilon', 0.5)
            min_samples = self.params.get('min_sample', 5)
            lines.append(f"model = DBSCAN(eps={eps}, min_samples={min_samples})")
        elif self.method == "KMeans":
            n_clusters = self.params.get('n_clusters', 3)
            random_state = self.params.get('random_state', 42)
            lines.append(f"model = KMeans(n_clusters={n_clusters}, random_state={random_state})")
        else:
            lines.append("# No valid method specified, using default")
            lines.append("model = KMeans(n_clusters=3, random_state=42)")

        lines.extend([
            "",
            "# 3) Fit model & get labels",
            "labels = model.fit_predict(X)",
            'print("Unique cluster labels:", np.unique(labels))',
            "",
            "# 4) Plot the results",
            "plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')",
            f"plt.title('{self.method} Clustering')",
            "plt.show()",
        ])

        return "\n".join(lines)
