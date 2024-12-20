########################################################
# Sample alumnus blueprint of endpoints
########################################################
from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

#------------------------------------------------------------
# Create a new Blueprint object, which is a collection of 
# routes.
alumnus = Blueprint('alumnus', __name__)

alumnus_id = 289


#------------------------------------------------------------
# gets a list of students in a specific major
@alumnus.route('/student_major/<major>', methods=['GET'])
def get_students_in_major(major):

    query = '''
    SELECT id, firstName, lastName,
             FROM student
             WHERE student.major = major;
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)

    theData = cursor.fetchall()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

#------------------------------------------------------------
# gets a specific alumn's job title
@alumnus.route('/alumnJobTitle/<id>', methods=['GET'])
def get_alumnus_job(id):
    query = '''
    SELECT p.comment 
             FROM position p JOIN alumnus a ON a.jobID = p.id
             WHERE a.id =%s;
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query, id)

    theData = cursor.fetchall()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

#------------------------------------------------------------
# gets a job id by the name
@alumnus.route('/positionByComment/<comment>', methods=['GET'])
def get_job_by_comment(comment):
    query = '''
    SELECT id
             FROM position
             WHERE comment =%s;
    '''

    cursor = db.get_db().cursor()
    data = (comment)
    cursor.execute(query, data)

    theData = cursor.fetchall()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

#------------------------------------------------------------
# updates a job from a user given their id, probably
@alumnus.route('/update_job', methods=['PUT'])
def update_alumni_job():

    alumn_info = request.json
    alumnus_id = alumn_info['id']
    job_id = alumn_info['job_id']

    query = '''
    UPDATE alumnus
    SET jobID = %s
    WHERE id = %s;
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query, (job_id, alumnus_id))
    db.get_db().commit()
    response = make_response("job updated")
    response.status_code = 200
    return response

#------------------------------------------------------------
# creates a new chat with a student, hopefully
@alumnus.route('/create_chatroom/<userID>', methods=['POST'])
def create_new_chat(id):

    data = request.json
    student_id = data['userID']

    query = '''
    INSERT INTO chatroom (recieverID, senderID) VALUES (%s, %s);
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query, (student_id, id))
    db.get_db().commit()
    response = make_response("chat created!")
    response.status_code = 200
    return response


# ------------------------------------------------------------
# Deletes a chat 
@alumnus.route('/delete_chatroom/<senderID>', methods=['DELETE'])
def delete_chat(id):

    query = '''
        DELETE FROM chatroom 
        WHERE
        sender.id = id;
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    response = make_response("chat deleted!")
    response.status_code = 200
    return response

#------------------------------------------------------------
# gets a specific alumn's email
@alumnus.route('/alumnusEmail/<id>', methods=['GET'])
def get_alumnus_email(id):
    query = '''
    SELECT email 
             FROM alumnus
             WHERE id =%s;
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query, id)

    theData = cursor.fetchall()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response



 # updates a job from a user given their id, probably
@alumnus.route('/update_email', methods=['PUT'])
def update_alumni_email():

    alumn_info = request.json
    alumnus_id = alumn_info['id']
    email = alumn_info['email']

    query = '''
    UPDATE alumnus
    SET email = %s
    WHERE id = %s;
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query, (email, alumnus_id))
    db.get_db().commit()
    response = make_response("email updated")
    response.status_code = 200
    return response


