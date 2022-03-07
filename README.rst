Requests-REST: A RESTful client based on requests
=================================================

This library intends to provide an elegant RESTful client.


Installation
============

.. code-block:: shell

    pip install requests-rest


Usage example
=============
.. code-block:: shell

    base_url = 'https://httpbin.org/'

    new_name = 'aponder'
    new_email = 'i@aponder.top'
    new_user = {
        'name': new_name,
        'email': new_email,
    }
    update_user = new_user.copy()
    update_user.update({'name': f'new {new_name}'})

    # print(resource_user.list().json())
    # print(resource_user.create(new_user).json())
    # print(resource_user.update(1, new_user).json())
    # print(resource_user.patch(1, new_name).json())
    # print(resource_user.patch(1, new_email).json())
    # print(resource_user.delete(1).json())

    resource_client = Client(base_url, debug=True)
    Users = resource_client('users')

    users_creating = Users.create(new_user)
    print(users_creating.response)

    users_listing = Users.list(page=1, page_size=10)
    print(users_listing.response)

    users_detailing = Users.detail(1)
    print(users_detailing.response)

    users_updating = Users.update(2, update_user)
    print(users_updating.response)

    users_partial_updating = Users.partial_update(3, update_user)
    print(users_partial_updating.response)

    users_deleting = Users.delete(4)
    print(users_deleting.response)

    # extra actions
    Users.login = Users.make_plural_action('login')
    credentials = {'username': 'root', 'password': 'root'}
    print(Users.login(credentials).response)

    Users.disable = Users.make_single_action('disable')
    print(Users.disable(2).response)

    # resource combination
    Blogs = resource_client('blogs')
    UsersBlogs = users_detailing(Blogs)

    new_blog = {'title': 'hello'}
    print(UsersBlogs.create(new_blog).response)
    print(UsersBlogs.list(page=2, page_size=20).response)
    print(UsersBlogs.delete(10).response)
    print(UsersBlogs.update(10, new_blog).response)
    print(UsersBlogs.partial_update(10, new_blog).response)
    print(UsersBlogs.delete(10).response)


