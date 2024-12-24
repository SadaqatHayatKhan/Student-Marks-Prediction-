from flask import Flask ,render_template,request
import joblib
app= Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/display",methods=['GET','POST'])

def uploader():
    if request.method=='POST':
        model=joblib.load('student_mark_prediction.pkl')
        study_hours=request.form["study_hours"]
        study_hours=int(study_hours)
        marks=model.predict([[study_hours]])[0]
        marks="{:.2f}".format(marks)
        return render_template("index.html",prediction=marks)

if __name__ =='__main__':
    app.run(debug=True)