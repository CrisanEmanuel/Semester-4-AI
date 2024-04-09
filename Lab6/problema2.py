import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

def problema2():
    # Încărcăm setul de date Iris
    iris = load_iris()
    X = iris.data  # caracteristicile (lungimea și lățimea sepalului și petalei)
    y = iris.target  # etichetele (speciile de iris)

    # Divizăm setul de date în set de antrenare și set de testare
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Inițializăm și antrenăm modelul de regresie logistică
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    # Facem predicții pentru setul de testare pentru a evalua performanța modelului
    accuracy = model.score(X_test, y_test)
    print("Precizia modelului pe setul de testare:", accuracy)

    # Facem predicții pentru caracteristicile date
    new_flower = np.array([[5.35, 3.85, 1.25, 0.4]])  # caracteristicile noii flori
    predicted_species = model.predict(new_flower)
    predicted_species_name = iris.target_names[predicted_species[0]]

    print("Specia prezisă pentru noua floare:", predicted_species_name)
