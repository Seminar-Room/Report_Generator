from flask import Flask, render_template, request, send_file ,session
from werkzeug.utils import secure_filename
import os 
from reportlab.lib.units import mm

import report_file_1


app= Flask(__name__,template_folder='templates')
app.secret_key = 'here'

app.config['ALLOWED_EXTENSIONS'] = {'png'}

# Function to check if a file has an allowed extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Define the folder where uploaded files will be stored
app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'Flask_generated')
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# to store in a temporary memory if the input data matches the allowed file type
def file_checker(var):
    if var in request.files:
        file = request.files[var]
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            temp_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(temp_path)
            return temp_path # Return the file path
           

@app.route('/', methods=['GET','POST'])
def cover_index():
    if request.method == 'POST':
        college_name = request.form['college_name']
        event_name = request.form['event_name']
        index1 = request.form['index1']
        index2 = request.form['index2']
        index3 = request.form['index3']
        index4 = request.form['index4']
        index5 = request.form['index5']

        # Store the data in the session
        session['event_name'] = event_name
        session['college_name'] = college_name
        session['index1']=index1
        session['index2']=index2
        session['index3']=index3
        session['index4']=index4
        session['index5']=index5
        

    return render_template('cover_index.html')


@app.route('/about_page', methods=['GET','POST'])
def about_page():
    if request.method == 'POST':
        about_p1 = request.form['about_p1']
        about_p2 = request.form['about_p2']
        about_p3 = request.form['about_p3']
        about_p4 = request.form['about_p4']

        #store in session
        session['about_p1']=about_p1
        session['about_p2']=about_p2
        session['about_p3']=about_p3
        session['about_p4']=about_p4

    return render_template('about_page.html')  # Render the about_page template for the initial GET request

@app.route('/about_sme', methods=['GET','POST'])
def about_sme():
    if request.method == 'POST':
        topic = request.form['topic']
        date = request.form['date']
        timings = request.form['timings']
        sme_name = request.form['sme_name']
        sme_designation = request.form['sme_designation']
        sme_p1 = request.form['sme_p1']
        sme_p2 = request.form['sme_p2']
        sme_p3 = request.form['sme_p3']
        About_the_Session = request.form['About_the_Session']
        learning_outcomes = request.form['learning_outcomes']

        # Store the data in the session
        session['topic'] = topic
        session['date'] = date
        session['timings'] = timings
        session['sme_name'] = sme_name
        session['sme_designation'] = sme_designation
        session['sme_p1'] = sme_p1
        session['sme_p2'] = sme_p2
        session['sme_p3'] = sme_p3
        session['About_the_Session'] = About_the_Session
        session['learning_outcomes'] = learning_outcomes

    
    return render_template('about_sme.html')


@app.route('/feedback', methods=['GET','POST'])
def feedback():
    if request.method == 'POST' :
        happiness_rating = request.form['happiness_rating']
        expectation_rating = request.form['expectation_rating']
        knowledge_rating = request.form['knowledge_rating']
        overall_rating = request.form['overall_rating']
        fb1 = request.form['fb1']
        fb2 = request.form['fb2']
        fb3 = request.form['fb3']
        fb4 = request.form['fb4']
        fb5 = request.form['fb5']
        fb6 = request.form['fb6']

        #store the data in session
        session['happiness_rating']=happiness_rating
        session['expectation_rating']=expectation_rating
        session['knowledge_rating']=knowledge_rating
        session['overall_rating']=overall_rating
        session['fb1']=fb1
        session['fb2']=fb2
        session['fb3']=fb3
        session['fb4']=fb4
        session['fb5']=fb5
        session['fb6']=fb6
        
    
    return render_template('feedback.html')

@app.route('/snapshots', methods=['GET','POST'])
def snapshots():
     # Retrieve data from session variables
        event_name = session.get('event_name')
        college_name = session.get('college_name')
        index1 = session.get('index1')
        index2 = session.get('index2')
        index3 = session.get('index3')
        index4 = session.get('index4')
        index5 = session.get('index5')
        ############################################
        about_p1 = session.get('about_p1')
        about_p2 = session.get('about_p2')
        about_p3 = session.get('about_p3')
        about_p4 = session.get('about_p4')
        ###########################################
        topic = session.get('topic')
        sme_photo = session.get('sme_photo')
        date = session.get('date')
        timings = session.get('timings')
        sme_name = session.get('sme_name')
        sme_designation = session.get('sme_designation')
        sme_p1 = session.get('sme_p1')
        sme_p2 = session.get('sme_p2')
        sme_p3 = session.get('sme_p3')
        About_the_Session = session.get('About_the_Session')
        learning_outcomes = session.get('learning_outcomes')
        #######################################################  
        happiness_rating=session.get('happiness_rating')      
        expectation_rating = session.get('expectation_rating')
        knowledge_rating = session.get('knowledge_rating')
        overall_rating = session.get('overall_rating')
        fb1 = session.get('fb1')
        fb2 = session.get('fb2')
        fb3 = session.get('fb3')
        fb4 = session.get('fb4')
        fb5 = session.get('fb5')
        fb6 = session.get('fb6')
        ##########################################################
        # Handle uploaded snapshots
        if request.method == 'POST':
            college_logo = request.files['college_logo']
            sme_photo = request.files['sme_photo']
            snap1 = request.files["snap1"]
            snap2 = request.files["snap2"]
            #converting text to a list of numbers
            happiness_rating = [float(rating.strip()) for rating in happiness_rating.split(',')]
            expectation_rating = [float(rating.strip()) for rating in expectation_rating.split(',')]
            knowledge_rating = [float(rating.strip()) for rating in knowledge_rating.split(',')]
            overall_rating = [float(rating.strip()) for rating in overall_rating.split(',')]

            college_logo=file_checker('college_logo')
            sme_photo=file_checker('sme_photo')
            snap1=file_checker('snap1')
            snap2=file_checker('snap2')

            pdf_file=report_file_1.iip_report_generator(
                                        event_name, college_name, college_logo, #coverpage 
                                        index1,index2,index3,index4,index5, #index 
                                        about_p1,about_p2,about_p3,about_p4, # about page   
                                        sme_photo,sme_name,sme_designation,sme_p1, sme_p2, sme_p3,# about the speaker
                                        topic, date, timings,About_the_Session,learning_outcomes, # SME and session  details   
                                        happiness_rating, expectation_rating, knowledge_rating, overall_rating,#Feedback graph inputs
                                        fb1,fb2,fb3,fb4,fb5,fb6, #feedback 
                                        snap1,snap2 #snapshots
                                        )
            report_file_1.delete_temporary_directory(f'{college_name}_IIP_report')
            return send_file(pdf_file, as_attachment=True, download_name=f"{college_name}_IIP_Report.pdf")

        return render_template('snapshots.html')




if __name__ == '__main__':
    app.run(debug=True)
