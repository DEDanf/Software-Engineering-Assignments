from github import Github

print("Username: ")
username = input()

print("Password: ")
password = input()

g = Github(username, password)

print("You are logged in as" + g.get_user().name)

print("Repositories: ")
for repo in g.get_user().get_repos():
    print(repo.name)

while True:

    print("Select a repository or type 'exit'")

    inputA = input()
    if inputA == "exit":
        print("You have been logged out")
        break

    found = False
    for repo in g.get_user().get_repos():
        if inputA == repo.name:
            print("Commit dates and authors:")
            for commit in repo.get_commits():
                print(commit.commit.author.date)
                print(commit.commit.author.name)

            print("Contributors:")
            for contributor in repo.get_contributors():
                print(contributor.name)

            found = True

    if not found:
        print("Repository not found")