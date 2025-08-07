def map_to_sql(user_input):
    user_input = user_input.lower()

    if "top customers" in user_input:
        return """
            SELECT customer_id, SUM(amount) AS total_spent
            FROM invoices
            GROUP BY customer_id
            ORDER BY total_spent DESC
        """

    elif "total spent by each customer" in user_input:
        return """
            SELECT customer_id, SUM(amount) AS total_spent
            FROM invoices
            GROUP BY customer_id
        """

    elif "list all customers" in user_input or "show all customers" in user_input:
        return "SELECT * FROM customers"

    elif "total customers" in user_input:
        return "SELECT COUNT(*) AS total_customers FROM customers"

    elif "top customer in mumbai" in user_input:
        return """
            SELECT c.id, c.name, SUM(i.amount) AS total_spent
            FROM customers c
            JOIN invoices i ON c.id = i.customer_id
            WHERE c.city = 'Mumbai'
            GROUP BY c.id, c.name
            ORDER BY total_spent DESC
            LIMIT 1
        """

    elif "show all invoices" in user_input or "list all invoices" in user_input:
        return "SELECT * FROM invoices"

    else:
        return None
