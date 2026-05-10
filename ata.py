from flask import Flask, render_template, request
import pandas as pd
from sklearn import tree

app = Flask(__name__)

# ---------------- DATA ---------------- #

sml1 = [
    'Crackling of nails ',
    'Crackling of foot',
    'pain in foot',
    'numbness in foot',
    'sciatica',
    'stiffness',
    'paraplegia',
    'diarrehea',
    'bloating',
    'lameness',
    'groin tension',
    'voice hoarseness',
    'loss of taste',
    'loss of smell',
    'ear ache',
    'deafness',
    'dandruff',
    'Excessive irrelevant talk',
    'depression and weakness',
    'unstable mind',
    'excessive thirst or hunger',
    'Acidity',
    'fever',
    'skin rashes'
]

doshas = ['vata', 'pitta', 'kapha']

# ---------------- TRAIN MODEL ---------------- #

df = pd.read_csv("d1.csv")

df.replace({
    'Prog': {
        'vata': 0,
        'pitta': 1,
        'kapha': 2
    }
}, inplace=True)

X = df[sml1]
y = df["Prog"]

clf = tree.DecisionTreeClassifier()
clf.fit(X, y)

@app.route("/", methods=["GET", "POST"])
def home():

    prediction = ""
    error = ""

    if request.method == "POST":

        selected_symptoms = request.form.getlist("symptoms")

        # validation
        if len(selected_symptoms) == 0:
            error = "Please select at least 1 symptom."

        elif len(selected_symptoms) > 3:
            error = "You can select at most 3 symptoms."

        else:

            l2 = [0] * len(sml1)

            for i in range(len(sml1)):
                if sml1[i] in selected_symptoms:
                    l2[i] = 1

            prediction_index = clf.predict([l2])[0]

            prediction = doshas[prediction_index]

    return render_template(
        "index.html",
        symptoms=sml1,
        prediction=prediction,
        error=error
    )
if __name__ == "__main__":
     app.run(host="0.0.0.0", port=5000)
