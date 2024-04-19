import pandas as pd
from sklearn.impute import SimpleImputer, KNNImputer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.impute import SimpleImputer


# 1. Indlæs datasættet
df = pd.read_csv(r"C:\Users\AliWH\Desktop\AI og data\Lektion 4\recipeData.csv\recipeData.csv", encoding='latin1')

# 2. Udforsk datasættet for at identificere manglende data og mønstre
missing_data_info = df.isnull().sum()
print("Manglende data info:")
print(missing_data_info)

# 4. Anvend relevante imputeringsmetoder

# Identify columns containing string values
# print(df.dtypes)


# Opdel kolonner i numeriske og kategoriske
numerical_columns = ['Size(L)', 'OG', 'FG', 'ABV', 'IBU', 'Color', 'BoilSize', 'BoilTime', 'BoilGravity', 'Efficiency', 'PitchRate', 
'PrimaryTemp', 'UserId']
categorical_columns = ['Name', 'Style', 'SugarScale', 'BrewMethod', 'PrimingMethod', 'PrimingAmount']


# Instantiate imputers with different strategies
imputer_most_frequent = SimpleImputer(strategy='most_frequent')
imputer_mean = SimpleImputer(strategy='mean')
imputer_median = SimpleImputer(strategy='median')

# Fit and transform your DataFrame using each imputer
df_imputed_most_frequent = pd.DataFrame(imputer_most_frequent.fit_transform(df[numerical_columns]), columns=numerical_columns)
df_imputed_mean = pd.DataFrame(imputer_mean.fit_transform(df[numerical_columns]), columns=numerical_columns)
df_imputed_median = pd.DataFrame(imputer_median.fit_transform(df[numerical_columns]), columns=numerical_columns)

# Imputer for kategoriske kolonner med konstant strategi
imputer_categorical = SimpleImputer(strategy='most_frequent')
df_imputed_categorical = pd.DataFrame(imputer_categorical.fit_transform(df[categorical_columns]), columns=categorical_columns)

# Saml de imputerede datasæt igen
df_imputed_mean = pd.concat([df_imputed_mean, df_imputed_categorical], axis=1)
df_imputed_median = pd.concat([df_imputed_median, df_imputed_categorical], axis=1)
df_imputed_most_frequent = pd.concat([df_imputed_most_frequent, df_imputed_categorical], axis=1)
# print("\nSamlet imputeret datasæt:")
# print(df_imputed.isnull().sum())
# print(df_imputed_mean.columns)

# 5. Træn en klassificeringsmodel (KNN)
X = df_imputed_mean.drop(columns=['Name', 'Style', 'SugarScale', 'BrewMethod', 'PrimingMethod', 'PrimingAmount']
)
y = df_imputed_mean['BrewMethod']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Klassificeringsmodel med Simple Imputer
knn_model_mean = KNeighborsClassifier()
knn_model_mean.fit(X_train, y_train)
y_pred_mean = knn_model_mean.predict(X_test)
accuracy_mean = accuracy_score(y_test, y_pred_mean)
print("Accuracy with Simple Imputer (mean strategy):", accuracy_mean)

# # Klassificeringsmodel med KNN Imputer
# X = df_imputed_knn.drop(columns=['Name', 'Style', 'SugarScale', 'BrewMethod', 'PrimingMethod', 'PrimingAmount'])
# y = df_imputed_knn['BrewMethod']
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # knn_model_knn = KNeighborsClassifier()
# # knn_model_knn.fit(X_train, y_train)
# # y_pred_knn = knn_model_knn.predict(X_test)
# # accuracy_knn = accuracy_score(y_test, y_pred_knn)
# # print("Accuracy with KNN Imputer:", accuracy_knn)
