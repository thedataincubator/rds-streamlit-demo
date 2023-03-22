import sqlalchemy

def query_db():
    engine = sqlalchemy.create_engine('postgresql://tdi:qKmd8s5ze7WAYV@adventureworks.tditrain.com:5431/wells')
    conn = engine.connect()

    depth = 1000
    gradient = 0.01

    query = sqlalchemy.text("""
        SELECT latitude, longitude, depth, gradient FROM wells
        WHERE depth > :depth AND gradient > :gradient;
    """)
    result = conn.execute(query, {"depth": depth, "gradient": gradient})
    
    return result.fetchall()

if __name__ == '__main__':
    print(query_db())
