
from flask import Flask,render_template,request,redirect,send_file,send_from_directory
import os
from werkzeug.utils import secure_filename
from main import function

app=Flask(__name__)#object of flask
fn=function()
fname=""

@app.route('/',methods=['GET','POST'])  #it is decorator
def encryption():
     app.config['UPLOAD_FOLDER'] = 'data/encrypteddata'
    #FILE UPLOADING METHOD 
     if request.method == 'POST' and request.form["action"]=="up":
         print("yeah")
         print("Button press=",request.form['action'])

# check if the post request has the file part
         if 'file' not in request.files:
            # flash('No file part')
            return redirect(request.url)
         file = request.files['file']
        # if user does not select file, browser alsode
        # submit a empty part without filename
         if file.filename == '':
            # flash('No selected file')
            return redirect(request.url)
         if file :
            filenames = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filenames))
            print("encryption starts")
            keyenc=fn.encryption1(filenames)

            # uploads = os.path.join(current_app.root_path, app.config['encryptedfile/'])
            # print(current_app.root_rootpath)
            # return send_from_directory(directory=uploads, filename=filenames)

            # return send
            # _file('originaldata/'+filenames,attachment_filename='en_'+filenames)
            downname="/encryptedfile/"+filenames
            print(downname,os.path.exists(downname)) 
            filename1, filext=os.path.splitext(filenames)
            print(filename1,"  ",filext)
            # return send_file(downname)
            fname=filenames
            print("fname=",fname)
            return render_template('encryption.html',data=filenames,keys=keyenc,down=downname,fex=filext)
     if request.method == 'POST' and request.form["action"]=="down":
         print("yeahdown")
         print("Button press=",request.form['action'])
         name=request.form.get('fname')
         print("2nd filename =",name)
         return send_from_directory('encryptedfile','en_'+name, as_attachment=True,)
         

     else :
         return render_template('encryption.html')


@app.route('/decryption',methods=['GET','POST'])
def decryption():
     print("decryption start")
     app.config['UPLOAD_FOLDER'] = 'data/decrypteddata'
    #FILE UPLOADING METHOD 1
     if request.method == 'POST' and request.form["action"]=="up" :
# check if the post request has the file part
         if 'file' not in request.files:
            # flash('No file part')
            return redirect(request.url)
         file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
         if file.filename == '':
            # flash('No selected file')
            return redirect(request.url)
         if file :
            filenames = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filenames))
            print("decryption starts 2")
            key=request.form.get('kname')
            print("decryptionk key=",key)
            fn.decryption1(filenames,key)
            return render_template('decryption.html',data=filenames)

     if request.method == 'POST' and request.form["action"]=="down":
         print("yeahdown")
         print("Button press=",request.form['action'])
         name=request.form.get('fname')
         print("2nd filename =",name)
         return send_from_directory('originaldata',name.replace("en_",""), as_attachment=True,)


     else :
         return render_template('decryption.html')

# @app.route('/downloads',methods=['POST','GET'])
# def download_file():
#    if request.method == "POST":
#       print("Button press=",request.form['action'])
#       name=request.form.get('fname')
#       print("2nd filename =",name)
#       return send_from_directory('encryptedfile',name, as_attachment=True)
#    else:
#       return render_template('encryption.html')



if __name__=="__main__":    #cmds to run flask
   app.run(debug=True)