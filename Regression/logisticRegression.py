import streamlit as st
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, roc_auc_score, roc_curve
import matplotlib.pyplot as plt
import seaborn as sns


def generate_logistic_regression(df):
    
    st.write("DataFrame:")
    st.write(df)

    # Select features and target
    st.write("Select the feature columns (X) and the target column (y)")

    all_columns = df.columns.tolist()

    features = st.multiselect("Select feature columns (X)", all_columns)
    target = st.selectbox("Select target column (y)", all_columns)

    if st.button("Perform Logistic Regression"):
        if features and target:
            X = df[features]
            y = df[target]

            # Ensure the target variable is binary
            if y.nunique() != 2:
                st.write("The target column must be binary (contain exactly two unique values).")
            else:
                # Split the data into training and testing sets
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

                # Feature scaling
                scaler = StandardScaler()
                X_train_scaled = scaler.fit_transform(X_train)
                X_test_scaled = scaler.transform(X_test)

                # Perform logistic regression
                model = LogisticRegression()
                model.fit(X_train_scaled, y_train)

                # Predicting the target
                y_pred_train = model.predict(X_train_scaled)
                y_pred_test = model.predict(X_test_scaled)

                # Evaluating the model
                st.write("Training Set Performance:")
                st.write("Accuracy:", accuracy_score(y_train, y_pred_train))
                st.write("Precision:", precision_score(y_train, y_pred_train))
                st.write("Recall:", recall_score(y_train, y_pred_train))
                st.write("F1 Score:", f1_score(y_train, y_pred_train))

                st.write("Testing Set Performance:")
                st.write("Accuracy:", accuracy_score(y_test, y_pred_test))
                st.write("Precision:", precision_score(y_test, y_pred_test))
                st.write("Recall:", recall_score(y_test, y_pred_test))
                st.write("F1 Score:", f1_score(y_test, y_pred_test))

                # Confusion matrix
                cm = confusion_matrix(y_test, y_pred_test)
                fig, ax = plt.subplots()
                sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax)
                ax.set_xlabel('Predicted')
                ax.set_ylabel('Actual')
                ax.set_title('Confusion Matrix')
                st.pyplot(fig)

                # ROC curve
                y_pred_prob = model.predict_proba(X_test_scaled)[:,1]
                fpr, tpr, thresholds = roc_curve(y_test, y_pred_prob)
                roc_auc = roc_auc_score(y_test, y_pred_prob)

                fig, ax = plt.subplots()
                ax.plot(fpr, tpr, color='blue', label=f'ROC curve (area = {roc_auc:.2f})')
                ax.plot([0, 1], [0, 1], color='red', linestyle='--')
                ax.set_xlabel('False Positive Rate')
                ax.set_ylabel('True Positive Rate')
                ax.set_title('Receiver Operating Characteristic (ROC) Curve')
                ax.legend(loc='lower right')
                st.pyplot(fig)

        else:
            st.write("Please select the feature columns (X) and the target column (y).")
