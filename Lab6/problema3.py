import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

def problema3():
    # Încărcăm setul de date despre cancerul de sân
    cancer_data = load_breast_cancer()
    X = cancer_data.data[:, [0, 1]]  # luăm doar raza și textura ca caracteristici
    y = cancer_data.target  # etichetele (0 pentru benign, 1 pentru malign)

    # Divizăm setul de date în set de antrenare și set de testare
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Inițializăm și antrenăm modelul de regresie logistică
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    # Facem predicții pentru setul de testare pentru a evalua performanța modelului
    accuracy = model.score(X_test, y_test)
    print("Precizia modelului pe setul de testare:", accuracy)

    # Facem predicții pentru caracteristicile date
    new_lesion = np.array([[18, 10]])  # caracteristicile leziunii noi (raza, textura)
    predicted_label = model.predict(new_lesion)

    if predicted_label[0] == 0:
        print("Leziunea este etichetată ca fiind benignă.")
    else:
        print("Leziunea este etichetată ca fiind malignă.")
