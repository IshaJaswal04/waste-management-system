from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS
import config

app = Flask(__name__)
CORS(app)


#Load MySQL configuration
app.config['MYSQL_HOST'] = config.MYSQL_HOST
app.config['MYSQL_USER'] = config.MYSQL_USER
app.config['MYSQL_PASSWORD'] = config.MYSQL_PASSWORD
app.config['MYSQL_DB'] = config.MYSQL_DB

mysql = MySQL(app)


#Bins
@app.route('/bins',methods=['GET'])
def get_bins():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM bins")
    rows = cur.fetchall()
    bins = []

    for row in rows:
        bins.append({
            'id':row[0],
            'area':row[1],
            'bin_id':row[2],
            'status':row[3],
            'last_updated':row[4].strftime("%Y-%m-%d %H:%M:%S")
        })

    return jsonify(bins)

#Update bins status
@app.route('/update-bin', methods=['POST'])
def update_bin():
    data = request.json
    bin_id = data.get('bin_id')
    status = data.get('status')

    cur = mysql.connection.cursor()
    cur.execute(
        "UPDATE bins SET status=%s WHERE bin_id=%s",
        (status, bin_id)
    )
    mysql.connection.commit()
    cur.close()

    return jsonify({"message": "Bin updated successfully"})


@app.route('/alerts', methods=['GET'])
def get_full_bins():
    cur = mysql.connection.cursor()
    cur.execute("SELECT bin_id, area FROM bins WHERE status = 'FULL'")
    rows = cur.fetchall()
    cur.close()

    result = []
    for r in rows:
        result.append({
            "bin_id": r[0],
            "area": r[1]
        })

    return jsonify(result)

@app.route('/mark-collected', methods=['POST'])
def mark_collected():
    data = request.json
    bin_id = data.get('bin_id')

    cur = mysql.connection.cursor()
    cur.execute(
        "UPDATE bins SET status='EMPTY' WHERE bin_id=%s",
        (bin_id,)
    )
    mysql.connection.commit()
    cur.close()

    return jsonify({"message": "Bin marked as collected"})


if __name__ == '__main__':
    app.run(debug=True)
   