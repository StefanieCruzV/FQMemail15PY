from flask_app import app
from flask import render_template,redirect,request,session
from flask_app.models.email import Email

@app.route("/")
def index():
    # users = User.get_all() # regresa los valores del metodo get all y almacena todos los datos de lbd
    # print(users)
    return render_template("email.html") 


 

@app.route('/create_user', methods=["POST"])
def create_user():
    data = {
        "uname": request.form["uname"],
        "ulastname": request.form["ulastname"],
        "uemail": request.form["uemail"]
        # guarda los valores del formulario
        }
   
    id=User.save(data) # manda llamar al metodo para guardar
    print(id)
   
    return redirect(f"/show_user/{id}")# lo que me regreso de la base al html
        # si es otra pagina 

@app.route('/delete_user/<int:id>')
def delete_user(id):
    print(id)
    data = {
        "id": id
        }
    User.delete(data)
    users = User.get_all()
    return render_template("users.html",users=users)
   

@app.route("/email",methods=["POST"])
def update_user():
    if not Email.validate_email(request.form):
        return redirect('/')
    data = {
        "email": request.form["email"]
        }
    Email.update(data)
    emails = Email.get_all()
    return render_template("response.html", emails=emails)