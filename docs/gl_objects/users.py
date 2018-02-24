# list
users = gl.users.list()
# end list

# search
users = gl.users.list(search='oo')
# end search

# get
# by ID
user = gl.users.get(2)
# by username
user = gl.users.list(username='root')[0]
# end get

# create
user = gl.users.create({'email': 'john@doe.com',
                        'password': 's3cur3s3cr3T',
                        'username': 'jdoe',
                        'name': 'John Doe'})
# end create

# update
user.name = 'Real Name'
user.save()
# end update

# delete
gl.users.delete(2)
user.delete()
# end delete

# block
user.block()
user.unblock()
# end block

# key list
keys = user.keys.list()
# end key list

# key get
key = user.keys.get(1)
# end key get

# key create
k = user.keys.create({'title': 'my_key',
                      'key': open('/home/me/.ssh/id_rsa.pub').read()})
# end key create

# key delete
user.keys.delete(1)
# or
key.delete()
# end key delete

# gpgkey list
gpgkeys = user.gpgkeys.list()
# end gpgkey list

# gpgkey get
gpgkey = user.gpgkeys.get(1)
# end gpgkey get

# gpgkey create
# get the key with `gpg --export -a GPG_KEY_ID`
k = user.gpgkeys.create({'key': public_key_content})
# end gpgkey create

# gpgkey delete
user.gpgkeys.delete(1)
# or
gpgkey.delete()
# end gpgkey delete

# email list
emails = user.emails.list()
# end email list

# email get
email = gl.user_emails.list(1, user_id=1)
# or
email = user.emails.get(1)
# end email get

# email create
k = user.emails.create({'email': 'foo@bar.com'})
# end email create

# email delete
user.emails.delete(1)
# or
email.delete()
# end email delete

# currentuser get
gl.auth()
current_user = gl.user
# end currentuser get

# it list
i_t = user.impersonationtokens.list(state='active')
i_t = user.impersonationtokens.list(state='inactive')
# end it list

# it get
i_t = user.impersonationtokens.get(i_t_id)
# end it get

# it create
i_t = user.impersonationtokens.create({'name': 'token1', 'scopes': ['api']})
# use the token to create a new gitlab connection
user_gl = gitlab.Gitlab(gitlab_url, private_token=i_t.token)
# end it create

# it delete
i_t.delete()
# end it delete
