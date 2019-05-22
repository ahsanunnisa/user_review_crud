from flask import Flask, request, jsonify
import pymysql

app = Flask(__name__)


def connect():
    conn = pymysql.connect(
        user="root",
        passwd="XXXX",
        host='127.0.0.1',
        port=3308,
        database="kulinadb"
    )
    return conn


@app.route('/add', methods=['POST'])
def add_rating():
    try:
        db = connect()
        cursor = db.cursor(pymysql.cursors.DictCursor)
        _json = request.json
        _order_id = _json['order_id']
        _product_id = _json['product_id']
        _user_id = _json['user_id']
        _rating = _json['rating']
        _review = _json['review']
        if _order_id and _product_id and _user_id and _rating and _review and request.method == 'POST':
            sql = "INSERT INTO user_review(order_id, product_id, user_id, rating, review) VALUES(%s, %s, %s, %s, %s)"
            data = (_order_id, _product_id, _user_id, _rating, _review)

            cursor.execute(sql, data)
            db.commit()
            print('review added succesfully!')
            return 'OK'
        else:
            return 'Error while adding user review'
    except Exception as e:
        print(e)
        return str(e)
    finally:
        cursor.close()
        db.close()


@app.route('/', methods=['GET'])
def reviews():
    try:
        db = connect()
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM user_review")
        result = []
        for row in cursor:
            print(row)
            result.append(row)
        return jsonify(result)
    except Exception as e:
        print(e)
        return str(e)
    finally:
        cursor.close()
        db.close()


@app.route('/update', methods=['POST'])
def update_review():
    try:
        db = connect()
        cursor = db.cursor(pymysql.cursors.DictCursor)
        _json = request.json
        _order_id = _json['order_id']
        _product_id = _json['product_id']
        _user_id = _json['user_id']
        _rating = _json['rating']
        _review = _json['review']
        _id = _json['id']
        if _order_id and _product_id and _user_id and _rating and _review and _id and request.method == 'POST':
            sql = "UPDATE user_review SET order_id=%s, product_id=%s, user_id=%s, rating=%s, review=%s WHERE id=%s"
            data = (_order_id, _product_id, _user_id, _rating, _review, _id)
            cursor.execute(sql, data)
            db.commit()
            print('review updated succesfully!')
            return 'OK'
        else:
            return 'Error while updating review'
    except Exception as e:
        print(e)
        return str(e)
    finally:
        cursor.close()
        db.close()


@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_review(id):
    try:
        db = connect()
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("DELETE FROM user_review WHERE id=%s", id)
        db.commit()
        print("Review deleted successfully!")
        return 'OK'
    except Exception as e:
        print(e)
        return str(e)
    finally:
        cursor.close()
        db.close()


if __name__ == '__main__':
    app.run(debug=True)
