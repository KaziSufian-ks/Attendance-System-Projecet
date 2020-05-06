from flask_restful import Resource, reqparse
from models.subject import SubjectstModel

from flask_jwt_extended import jwt_required

parser = reqparse.RequestParser()
parser.add_argument('name', help = 'registration field required', required = True)
parser.add_argument('code', help = 'code field required', required = True)
parser.add_argument('class', help = 'class filed required', required = True)
parser.add_argument('departments', help = 'departments filed required', required = True)

class SubjectRegistration(Resource):
    def post(self):
        data = parser.parse_args()

        if SubjectstModel.find_by_name(data['name']):
            return {'message': 'This department {} already exists '. format(data['name'])}

        if SubjectstModel.find_by_code(data['code']):
            return {'message': 'This code {} already exists '. format(data['code'])}
        
        new_Subject = SubjectstModel(
                        name        = data['name'],
                        code        = data['code'],
                        class_id      = data['class_id'],
                        department  = data['department'],

                    )
        try:
            new_Subject.save_to_db() 
            
            return {
                'message': ' This {} subject data  created successfully'.format(data['name'])
            }, 200   

        except:
            return {'message': 'Something went wrong'}, 500
            

class AllSubject(Resource):
    """this resource for /subject endpoint by this url all classes data can view"""
    def get(self):
        return SubjectstModel.return_all()   

class SubjectBase(Resource):
    """this resource for /Subject/<int:p_id> endpoint by this url classes data can update, delete, single data view """
    def get(self, p_id):
        Subject_data = SubjectstModel.find_by_id(p_id) 
        jsonify_data = Subject_data.to_json(Subject_data)
        return {'Subject': jsonify_data}
    
    def delete(self, p_id):
        subject_data = SubjectstModel.find_by_id(p_id) 
        if subject_data:
           subject_data.db_to_delete()
           return {'message': 'subject data deleted successfully'}, 200
        else:
            return {'message': 'subject not found'}, 500   





        


    




                




