# app/api.py
from flask import jsonify
from flask import request
from flask_restful import Resource

from app import api, app
from app.image_processing import generate_frames
from app.models import ImageData


# Resource for the frames API
class FramesResource(Resource):
    def get(self):
        depth_min = float(request.args.get('depth_min'))
        depth_max = float(request.args.get('depth_max'))
        image_data = ImageData.query.filter(ImageData.depth.between(depth_min, depth_max)).all()
        frames = []
        for image in image_data:
            frames.append(generate_frames(image))

        # Convert frames to JSON or any other suitable format
        return jsonify(frames)


# API resources
api.add_resource(FramesResource, '/get_frames')

if __name__ == '__main__':
    app.run(debug=True)
