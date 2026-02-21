from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.metrics import r2_score, mean_absolute_error,mean_squared_error


# split du data

def split_data(df_clean, target='salary_clean', test_size=0.2):

    x = df_clean.drop(columns=[target])
    y = df_clean[target]

    x_train, y_train, x_test, y_test = train_test_split(x, y, test_size=test_size, random_state=42)

    return x_train, y_train, x_test, y_test


# realisation du pipeline sklearn

def pipeline(numerical_cols, categorical_cols, model):

    numeric_transform = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler())
    ])

    categorical_transform = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore"))
    ])

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_transform, numerical_cols),
            ("cat", categorical_transform, categorical_cols)
        ]
    )

    return Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("model", model)
        ]
    )


# metriques d'evaluation

def metric_model(y_test, y_pred):

    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_absolute_error(y_test, y_pred)

    return r2, mae, mse










