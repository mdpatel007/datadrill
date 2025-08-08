### Prompt Experiments

1. Prompt: "Show me top customers"
   → SQL: SELECT customer_id, total_spent FROM customers ORDER BY total_spent DESC LIMIT 5

2. Prompt: "List all customers"
   → SQL: SELECT \* FROM customers

3. Prompt: "Show me all sales"
   → SQL: SELECT \* FROM sales

4. Prompt: "Show all customers"
   → SQL: SELECT \* FROM customers;

5. Prompt: "Show all invoices"
   → SQL: SELECT \* FROM invoices;

6. Prompt: "Total customers"
   → SQL: SELECT COUNT(\*) FROM customers;

7. Prompt: "How much did each customer spend"
   → SQL: SELECT c.id, c.name, SUM(i.amount) FROM customers c JOIN invoices i ON c.id = i.customer_id GROUP BY c.id;

8. Prompt: "Top customer in Mumbai"
   → SQL: SELECT c.id, c.name, SUM(i.amount) FROM customers c JOIN invoices i ON c.id = i.customer_id WHERE c.city = 'Mumbai' GROUP BY c.id ORDER BY SUM(i.amount) DESC LIMIT 1;

9. Prompt: "Customers from Delhi"
   → SQL: SELECT \* FROM customers WHERE city = 'Delhi';

10. Prompt: "Show invoice for customer ID 3"
    → SQL: SELECT \* FROM invoices WHERE customer_id = 3;

11. Prompt: "Invalid query"
    → SQL: ❌ No SQL matched
