##########
Search API
##########

You can search for resources at the top level, in a project or in a group.
Searches are based on a scope (issues, merge requests, and so on) and a search
string.

Reference
---------

* v4 API:

  + :attr:`gitlab.Gitlab.search`
  + :attr:`gitlab.v4.objects.Group.search`
  + :attr:`gitlab.v4.objects.Project.search`

* GitLab API: https://docs.gitlab.com/ce/api/search.html

Examples
--------

Search for issues matching a specific string::

    # global search
    gl.search('issues', 'regression')

    # group search
    group = gl.groups.get('mygroup')
    group.search('issues', 'regression')

    # project search
    project = gl.projects.get('myproject')
    project.search('issues', 'regression')

The ``search()`` methods implement the pagination support::

    # get lists of 10 items, and start at page 2
    gl.search('issues', search_str, page=2, per_page=10)

    # get a generator that will automatically make required API calls for
    # pagination
    for item in gl.search('issues', search_str, as_list=False):
        do_something(item)

The search API doesn't return objects, but dicts. If you need to act on
objects, you need to create them explicitly::

    for item in gl.search('issues', search_str, as_list=False):
        issue_project = gl.projects.get(item['project_id'], lazy=True)
        issue = issue_project.issues.get(item['iid'])
        issue.state = 'closed'
        issue.save()
