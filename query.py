queries = {
    "controllo": (
        "MATCH (g:Group {{chat_id: {chat_id}}})-[:HAS_USER]->(u:User {{id: {user_id}}}) "
        "WITH u, CASE WHEN u.total + 1 > u.record THEN 1 ELSE 0 END as result "
        "SET u.total = u.total + 1, u.fulltotal = u.fulltotal + 1, u.nome = '{user_full_name}', "
        "u.ultimadata = '{data}', u.record = CASE WHEN u.total + 1 > u.record THEN u.total + 1 ELSE u.record END "
        "WITH u, result "
        "RETURN u.total as total, u.fulltotal as fulltotal, u.record as record, result"
    ),
    "reset all": (
        "MATCH (u:User) "
        "SET u.total = 0"
    ),
    "registrazione": (
        "MERGE (g:Group {{chat_id: {chat_id}}}) "
        "CREATE (u:User {{nome: '{user_full_name}', id: {user_id}, total: 0, fulltotal: 0, record: 0, ultimadata: '{data}'}}) "
        "MERGE (g)-[:HAS_USER]->(u)"
    ),
    "profilo": (
        "MATCH (g:Group {{chat_id: {chat_id}}})-[:HAS_USER]->(u:User {{id: {user_id}}}) "
        "RETURN u.total, u.fulltotal, u.record"
    ),
    "classifica": (
        "MATCH (g:Group {{chat_id: {chat_id}}})-[:HAS_USER]->(u:User) "
        "WHERE u.total <> 0 "
        "RETURN u.nome as nome, u.total as total, u.ultimadata as ultimadata "
        "ORDER BY u.total DESC, u.ultimadata"
    ),
    "classifica totale": (
        "MATCH (g:Group {{chat_id: {chat_id}}})-[:HAS_USER]->(u:User) "
        "WHERE u.fulltotal <> 0 "
        "RETURN u.nome as nome, u.fulltotal as fulltotal, u.ultimadata as ultimadata "
        "ORDER BY u.fulltotal DESC, u.ultimadata"
    ),
    "record": (
        "MATCH (g:Group {{chat_id: {chat_id}}})-[:HAS_USER]->(u:User) "
        "WHERE u.record <> 0 "
        "RETURN u.nome as nome, u.record as record, u.ultimadata as ultimadata "
        "ORDER BY u.record DESC, u.ultimadata"
    ),
    "sorpasso": (
        "MATCH (g:Group {{chat_id: {chat_id}}})-[:HAS_USER]->(u:User) "
        "WHERE u.total = {total} AND u.total <> 0 "
        "RETURN u.nome as nome "
        "ORDER BY u.total DESC, u.ultimadata"
    )
}