# app/models.py
from app import db,app


class ImageData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    depth = db.Column(db.Float, nullable=False)
    pixel_data = db.Column(db.LargeBinary, nullable=False)

    def __repr__(self):
        return f"<Image id={self.id} depth={self.depth}>"


def save_to_database(depth, pixel_data):
    image_data = ImageData(depth=depth, pixel_data=pixel_data)
    with app.app_context():
        db.session.add(image_data)
        db.session.commit()
