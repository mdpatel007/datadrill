### Prompt Experiments

1. Prompt: "Show me top customers"
   → SQL: SELECT customer_id, total_spent FROM customers ORDER BY total_spent DESC LIMIT 5

2. Prompt: "List all customers"
   → SQL: SELECT \* FROM customers

3. Prompt: "Show me all sales"
   → SQL: SELECT \* FROM sales
