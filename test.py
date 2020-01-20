import sftp

c = sftp.Connection(
    host='10.8.15.82',
    port=22022,
    username='admin',
    password='extron',
)

print('c.listdir()=', c.listdir())
