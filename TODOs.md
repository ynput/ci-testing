# Release Trigger development
* Fix input value issues in testing repo
* Test full workflow to block releases > 0.1.0 when no PR labels where found
* implement PR templates
* research and implement PR data fetching logic
* Create filtering method to assign data to releases
* Move inital release creation to its own job
* Test creation of inital version
* Implement develop-to-main-merge using gh command
* Speed up merge-to-main (slowest job right now taking 25s)
* Create PR templates
* fetch data from PRs (accordign to templates) to create release changelog
* according to [chart](https://miro.com/welcomeonboard/aE5aMU04QWFJcUJZeE1YRzVkeGFMT01rMTZhYk9DU2VsdWRVV05qVzlhU1pGQTJ1c2pGYkN6NnVCNHp1N044QXwzNDU4NzY0NTIzMjczNzc1NTY2fDI=?share_link_id=167155028336)

# Implement release branches
* Fully controlled by actions anyway
* Whenever pralalel workign is required it can be done without any hassle

# Build local test environment
* Running every test run on github runners task lots of time
* Local testing using [act](https://nektosact.com/)
* Check out provided dockers
* Potentially create custom docker to behave identical to github runners
* Mock repo varibales like GH_TOKEN locally

# Implement shell commands as stand alone github actions
* Shell commands are long and often difficult to read
* Wrapping them [into actions to be more user friendly](https://docs.github.com/en/actions/creating-actions)
* Ynput should maintain a bunch own own github actions
* Utilize Annotations to output helpfull error messages including data causing the error
* (test also for windows runners - utilize powershell)

# Implement Standard for workflows
* Workflow implementations should follow a standardized scheme
* Every developer working with them should be able to easily adjust
* Add naming conventions and key word orders
* enforce modular implementations

# Set up security standards
* Using external actions can be a potential security risk
* Check how they use provided data
* Implement checks for untrusted inputs
* Read actions code before using them
* check which workflows are accessable to forks

# Unit + Integration Tests for Actions and Workflows
* Research [how to test github workflows](https://dev.to/cicirello/how-to-test-a-github-action-with-github-actions-2hag#integration-test)
* Test common use-cases
* Test faulty labels
* Test release creation if release already exists
* [Another guidline](https://github.com/Azure/actions/blob/main/docs/Testing-docs/Testing-GitHub-Actions.md)
* [test summary](https://github.blog/2022-05-09-supercharging-github-actions-with-job-summaries/)
