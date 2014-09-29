
mysql = require \mysql

conn = mysql.createConnection do
    host: \192.168.1.113
    user: \root
    database: \test
    password: \root

conn.connect!

(err, rows) <- conn.query "select 1 + 1 as solution"
console.dir rows

conn.end!


