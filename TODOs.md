# Release Trigger development
* Move inital release creation to its own job
* Test creation of inital version
* Add inputs for external data source (milestones, github projects, ...)
* Handle already existing release-draft-tag
* Create PR templates
* fetch data from PRs (accordign to templates) to create release changelog

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
