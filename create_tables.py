import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def create_database():
    '''Creates and connects to sparkifydb database. Returns cursor and connection to DB'''
    # connect to default database
    conn = psycopg2.connect(host="172.19.0.3" , dbname="postgres" ,user="postgres", password="Mohamed")

    conn.autocommit = True
    cur = conn.cursor()
    
    # create sparkify database with UTF8 encoding
    cur.execute("DROP DATABASE IF EXISTS sparkifydb")
    cur.execute("CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0")

    # close connection to default database
    conn.close()    
    
    # connect to sparkify database
    conn = psycopg2.connect(host="172.19.0.3" , dbname="sparkifydb" ,user="postgres", password="Mohamed")
    cur = conn.cursor()
    
    return cur, conn


def drop_tables(cur, conn):
    '''Drops all tables created on the database'''
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    '''Created tables defined on the sql_queries script: [songplays, users, songs, artists, time]'''
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """ Function to drop and re create sparkifydb database and all related tables.
        Usage: python create_tables.py
    """
    cur, conn = create_database()
    
    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()