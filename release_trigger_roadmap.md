# Release Trigegr Roadmap

##  Current Features
* Merge to protected main-branch
* Update develop-branch
* next version tag based on latest release + PR labels
* "build" from main - just zips the repo for now
* create release draft
* verify release draft
* Detailed information in workflow annotations

## Planned Features
* Allow optional inputs
* Allow release name/changelog information from milestone/github project
* Enhance feedback through workflow annotations
* implement core features as standalone actions
* Throw error for no existing latest release 
* Implement dedicated workflow for inital release
* Implement automated testing setup

## Gather feedback
* Change requests?
* Logic improvements?
* Feature enhancements?

## Streamlining
* Version number based on text file?
* How to gather changelog information?
* Create pre-releases automatically?

## Research
* Strategy for bugfixes on older releases
* LTS versions
* Cherry-pick chnanges to merge upstream

## Release Branches
* Create when features are implemnted
* Only merge bugfixes
* Automatically create pre-releases after merge
* allows parallel development 
* fully supported bei action automation
