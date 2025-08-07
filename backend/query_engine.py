from db import run_sql
from nlp_mapper import map_to_sql

def process_query(prompt):
    sql = map_to_sql(prompt)
    if sql is None:
        return {"error": "Could not understand the query."}
    try:
        columns, rows = run_sql(sql)
        return {"columns": columns, "rows": rows}
    except Exception as e:
        return {"error": str(e)}
