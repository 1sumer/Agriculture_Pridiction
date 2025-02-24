import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import accuracy_score

# Load Crop Recommendation Dataset
df_crop = pd.read_csv("assets/Data/Crop_recommendation.csv")

# Encode categorical labels
crop_label_encoder = LabelEncoder()
df_crop['label'] = crop_label_encoder.fit_transform(df_crop['label'])

# Split Data for Crop Prediction
X_crop = df_crop.drop(columns=['label'])
y_crop = df_crop['label']
X_crop_train, X_crop_test, y_crop_train, y_crop_test = train_test_split(X_crop, y_crop, test_size=0.2, random_state=42)

# Train Crop Model
crop_model = RandomForestClassifier()
crop_model.fit(X_crop_train, y_crop_train)

# Save Crop Model and Label Encoder
pickle.dump(crop_model, open("models/crop_model.pkl", "wb"))
pickle.dump(crop_label_encoder, open("models/crop_label_encoder.pkl", "wb"))

# Load Fertilizer Prediction Dataset
df_fertilizer = pd.read_csv("assets/Data/Fertilizer_Prediction.csv")

# Encode categorical features before splitting
fertilizer_label_encoder = LabelEncoder()

for col in ['Soil Type', 'Crop Type']:
    df_fertilizer[col] = fertilizer_label_encoder.fit_transform(df_fertilizer[col])  # Fit & transform on full dataset

# Encode Fertilizer Name **before splitting**
fertilizer_name_encoder = LabelEncoder()
df_fertilizer['Fertilizer Name'] = fertilizer_name_encoder.fit_transform(df_fertilizer['Fertilizer Name'])

# Split Data for Fertilizer Prediction
X_fertilizer = df_fertilizer.drop(columns=['Fertilizer Name'])
y_fertilizer = df_fertilizer['Fertilizer Name']

X_fertilizer_train, X_fertilizer_test, y_fertilizer_train, y_fertilizer_test = train_test_split(
    X_fertilizer, y_fertilizer, test_size=0.2, random_state=42, stratify=y_fertilizer
)

# Scale Data
scaler = StandardScaler()
X_fertilizer_train = scaler.fit_transform(X_fertilizer_train)
X_fertilizer_test = scaler.transform(X_fertilizer_test)

# Train Fertilizer Model
fertilizer_model = RandomForestClassifier()
fertilizer_model.fit(X_fertilizer_train, y_fertilizer_train)

# Save Models
pickle.dump(fertilizer_model, open("models/fertilizer_model.pkl", "wb"))
pickle.dump(scaler, open("models/scaler.pkl", "wb"))
pickle.dump(fertilizer_label_encoder, open("models/fertilizer_label_encoder.pkl", "wb"))
pickle.dump(fertilizer_name_encoder, open("models/fertilizer_name_encoder.pkl", "wb"))

print("Models trained and saved successfully!")