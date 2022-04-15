from flask import Flask, make_response, jsonify, abort
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

task_post_args = reqparse.RequestParser()
task_post_args.add_argument("numbers", type=str, required = True, action = 'append')



class Boroplus(Resource):
    def get(self):
        return "Get Successful"

    def post(self):
        args = task_post_args.parse_args()
        A = args["numbers"]
        even, odd = [], []

        outputTrue = { "user": "Boroplus", "status": True,
    "odd": odd,
    "even": even}

        outputFalse = { "user": "Boroplus", "status": False}


        for a in A:

            if not str(a).isdigit():
                return outputFalse

            if int(a)%2:
                odd.append(int(a))
            else:
                even.append(int(a))
        return outputTrue





api.add_resource(Boroplus, '/test')


if __name__ == '__main__':
    app.run(debug= True)
