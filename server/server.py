from flask import Flask 
from model import connect_to_db, db, User
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET-KEY'] = 'super-secret'

@app.route('/api/form', methods=['POST'])
def add_user():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    confirm_password = data.get('confirmPassword')
    existing_user = User.query.filter_by(email=email).all()
    if existing_user:
        error = {'error': 'email already in use'}
        return jsonify(error)
    if password != confirm_password:
        error = {'error': 'passwords do not match'}
    elif not existing_user and password == confirm_password:
        hashed_password = generate_password_hash(password)
        new_user = User(public_id=str(uuid.uuid4()), email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'user added'})

if __name__ == "__main__":
    app.debug = True
    app.jinja_env.auto_reload = app.debug
    connect_to_db(app)
    app.run(port=5000, host='0.0.0.0')