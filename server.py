from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    strawberry_count = request.form['strawberry']
    raspberry_count = request.form['raspberry']
    apple_count = request.form ['apple']
    total_count = int(strawberry_count)+ int(raspberry_count)+ int(apple_count)
    firstname = request.form['first_name']
    lastname = request.form['last_name']
    studentid = request.form['student_id']
    print(f'Charging {firstname} {lastname} for  {total_count} fruits.')
    return render_template("checkout.html",strawberry_count=strawberry_count, raspberry_count=raspberry_count, apple_count=apple_count, total_count=total_count, firstname=firstname, lastname=lastname, studentid=studentid)

@app.route('/fruits')         
def fruits():
    fruits_images = ["img/apple.png", "img/blackberry.png", "img/raspberry.png", "img/strawberry.png"] #added images to create a for loop
    return render_template("fruits.html", fruits_images=fruits_images) #since we created for loop, pass the name of array

if __name__=="__main__":   
    app.run(debug=True)    