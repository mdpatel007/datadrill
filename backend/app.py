from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

# Dummy translator for now
def translate_to_sql(query):
    q = query.lower().strip()

    if "all customers" in q:
        return "SELECT * FROM customers;"
    
    elif "all invoices" in q:
        return "SELECT * FROM invoices;"
    
    elif "total spent" in q or "each customer spent" in q or "how much each customer" in q or "customer spent" in q:
        return """
        SELECT c.id AS customer_id, c.name, SUM(i.amount) AS total_spent
        FROM customers c
        JOIN invoices i ON c.id = i.customer_id
        GROUP BY c.id
        ORDER BY total_spent DESC;
        """
    
    elif "top customer" in q:
        return """
        SELECT c.id AS customer_id, c.name, SUM(i.amount) AS total_spent
        FROM customers c
        JOIN invoices i ON c.id = i.customer_id
        GROUP BY c.id
        ORDER BY total_spent DESC
        LIMIT 1;
        """
    
    elif "total customers" in q or "how many customers" in q:
        return "SELECT COUNT(*) AS total_customers FROM customers;"
    
    else:
        return None



@app.route("/query", methods=["POST"])
def query():
    try:
        data = request.get_json()
        user_query = data.get("query", "")

        sql = translate_to_sql(user_query)
        if not sql:
            return jsonify({"error": "❌ Could not understand your query."}), 400

        conn = sqlite3.connect("datadrill.db")
        cursor = conn.cursor()

        cursor.execute(sql)
        columns = [col[0] for col in cursor.description]
        rows = cursor.fetchall()

        results = [dict(zip(columns, row)) for row in rows]

        return jsonify({"results": results})

    except Exception as e:
        return jsonify({"error": f"❌ SQL execution failed: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
