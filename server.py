from flask import Flask, render_template, request, redirect #render_template function allows us to actually send the HTML file
import csv

app = Flask(__name__) #We use Flask class to instantiate an app

@app.route('/')
def my_home():
    return render_template('./index.html')

@app.route('/<string:page_name>') #We can dynamically accept different URL parameters
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database_txt: #mode 'a' - append
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database_txt.write(f'\n {email}, {subject}, {message}')

def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database_csv:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

#Code taken from Flask Request Object
@app.route('/submit_form', methods=['POST', 'GET']) #GET means the browser wants us to send information, while POST wants us to save information
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict() #We are gathering the data in the form of a dictionary
            write_to_csv(data)
            return redirect('/thank_you.html')
        except:
            return 'did not save to the database. Try again!'
    else:
        return 'Something went wrong, try again'



