import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from category_encoders.target_encoder import TargetEncoder

# Load and preprocess data
train = pd.read_csv('data/train.csv')
X = train.drop(['class'], axis=1)
y = train['class']

# Data preprocessing
encoder = TargetEncoder()
cat_features = [val for val in X.select_dtypes(exclude='number').columns]
for feature in cat_features:
    X[feature] = encoder.fit_transform(X[feature], y)

# Train model
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.05, random_state=5)

clf = xgb.XGBClassifier(
    max_depth=8,
    min_child_weight=1,
    gamma=0.1,
    subsample=0.8,
    colsample_bytree=0.8,
    reg_alpha=0.1,
    reg_lambda=1,
    learning_rate=0.1,    
    n_estimators=2000,    
    random_state=5,
    device="cuda", 
    tree_method="gpu_hist",
    eval_metric="logloss",      
    early_stopping_rounds=10,  
)

clf.fit(X_train, y_train, eval_set=[(X_val, y_val)], verbose=True)

# Save model
clf.save_model('backend/xgboost_model.json')
