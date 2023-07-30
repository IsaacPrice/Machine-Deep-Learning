import pandas as pd
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn import linear_model
from sklearn import tree
from sklearn.cluster import KMeans
from sklearn.naive_bayes import GaussianNB

def get_dataframe(x_train, y_train):
    model_params = {
        'linear_reg' : {
            'model' : linear_model.LinearRegression(),
            'params' : {
                'positive' : [False]
            }
        },
        'logistic_regression' : {
            'model' : LogisticRegression(solver='liblinear',multi_class='auto'),
            'params' : {
                'C' : [1, 5, 10]
            }
        },
        'tree' : {
            'model' : tree.DecisionTreeClassifier(),
            'params' : {
                'min_samples_split' : [2]
            }
        },
        'k_means' : {
            'model' : KMeans(),
            'params' : {
                'n_clusters' : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                'random_state' : [1, 2, 3]
            }
        },
        'svm': {
            'model': svm.SVC(gamma='auto'),
            'params' : {
                'C' : [1, 10, 20],
                'kernel' : ['rbf', 'linear']
            }
        },
        'random_forest' : {
            'model' : RandomForestClassifier(),
            'params' : {
                'n_estimators' : [1, 5, 10]
            }
        },
        'naive_gaussianNB' : {
            'model' : GaussianNB(),
            'params' : {
                'var_smoothing' : [1e-9]
            }
        }
    }

    scores = []

    for model_name, mp in model_params.items():
        clf = GridSearchCV(mp['model'], mp['params'], cv=5, return_train_score=False)
        clf.fit(x_train, y_train)
        scores.append({
            'model' : model_name,
            'best_score' : clf.best_score_,
            'best_params' : clf.best_params_
        })
    
    df = pd.DataFrame(scores, columns=['model', 'best_score', 'best_params'])
    return df

from sklearn import datasets
iris = datasets.load_digits()

import pandas as pd
df = pd.DataFrame(iris.data,columns=iris.feature_names)
df['flower'] = iris.target
df['flower'] = df['flower'].apply(lambda x: iris.target_names[x])


df = get_dataframe(iris.data, iris.target)
