import psycopg2

# conn_string = "\
# host='localhost' \
# dbname='bd_escuela' \
# user='cthulhu' \
# password='cthulhu'"


host='localhost'
bd_name='bd_escuela'
user='cthulhu'
password='cthulhu'

dict_params = {'host': host, 'dbname': bd_name, 'user': user, 'password': password}
conn_string = ' '.join("{0}='{1}'".format(k, v) for k, v in dict_params.items())

con = psycopg2.connect(conn_string)
cur = con.cursor()
#cur.execute('select eliminar_alumno_por_id((%s))',('08TE0267',))
#cur.execute('select agregar_alumno((%s),(%s),(%s),(%s),(%s),(%s),(%s))',('08TE0266','p','p','p','1','p','12/12/12'))
#cur.execute('select modificar_alumno_por_id((%s),(%s),(%s),(%s),(%s),(%s),(%s))',('08TE0266','azathoth','cthulhu','inuto','666','x','6/6/6'))
cur.execute('select * from consultar_alumno_por_id((%s))',('08TE0266',))
res = cur.fetchall()
con.commit()
for i in res:
    print i
cur.close()
con.close()
