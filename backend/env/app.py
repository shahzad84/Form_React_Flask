# from flask import Flask, request, jsonify
# from flask_sqlalchemy import SQLAlchemy
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)  # Allow cross-origin requests
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contacts.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)

# class Contact(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     email = db.Column(db.String(100), nullable=False)
#     message = db.Column(db.Text, nullable=False)

#     def __init__(self, name, email, message):
#         self.name = name
#         self.email = email
#         self.message = message

# @app.route('/init-db', methods=['GET'])
# def init_db():
#     try:
#         db.create_all()
#         return "Database initialized successfully!", 200
#     except Exception as e:
#         return f"An error occurred: {str(e)}", 500

# @app.route('/contact', methods=['POST'])
# def contact():
#     data = request.json
#     name = data.get('name')
#     email = data.get('email')
#     message = data.get('message')

#     if not name or not email or not message:
#         return jsonify({'error': 'Invalid input'}), 400

#     new_contact = Contact(name=name, email=email, message=message)
    
#     try:
#         db.session.add(new_contact)
#         db.session.commit()
#         return jsonify({'message': 'Contact submitted successfully'}), 200
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

# if __name__ == '__main__':
#     with app.app_context():
#         try:
#             db.create_all() 
#         except Exception as e:
#             print(f"An error occurred during table creation: {str(e)}")
#     app.run(debug=True)
