

def select_post():
    sql = """
    SELECT
        author
        ,title
        ,text
        ,created_date
        ,published_date
        FROM Post
    """
    return sql
