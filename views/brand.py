from .app import app
from db import tables, session_scope


@app.route('/orm/brands', methods=['GET'])
def all_brands():
    with session_scope() as session:
        brand_list = session.query(tables.Brand).all()
        result = {
            'brands': [brand.to_dict() for brand in brand_list]
        }
        return result


@app.route('/orm/brands/<title>', methods=['GET'])
def certain_brand(title):
    with session_scope() as session:
        brand = session.query(tables.Brand).filter_by(title=title).first()
        brand_dict = brand.to_dict()
        return {'brand': brand_dict}
