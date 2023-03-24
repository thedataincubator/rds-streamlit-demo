import os
import sqlalchemy

DB_URL = os.getenv('DB_URL')

def query_db(depth, gradient):
    engine = sqlalchemy.create_engine(DB_URL)
    conn = engine.connect()

    query = sqlalchemy.text("""
        SELECT latitude, longitude, depth, gradient FROM wells
        WHERE depth > :depth AND gradient > :gradient;
    """)
    result = conn.execute(query, {"depth": depth, "gradient": gradient})
    
    return result.fetchall()

if __name__ == '__main__':
    import sys

    depth = float(sys.argv[1])
    gradient = float(sys.argv[2])

    print(query_db(depth, gradient))
