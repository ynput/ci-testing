# Changelog


## [3.4.3](https://github.com/ynput/ci-testing/tree/3.4.3)

[Full Changelog](https://github.com/ynput/ci-testing/compare/3.4.3...3.4.2)

### **🚀 Enhancements**


<details>
<summary>not sure what (<i><font color='#367F6C';>3d</font> </i> <i><font style='color:#365E7F';>/ maya</font></i> ) - <a href="https://github.com/ynput/ci-testing/pull/33">#33</a></summary>


___


## Brief description
Use Publisher tool and new creation system in TVPaint integration.

## Description
Using new creation system makes TVPaint integration a little bit easier to maintain for artists. Removed unneeded tools Creator and Subset Manager tools. Goal is to keep the integration work as close as possible to previous integration. Some changes were made but primarilly because they were not right using previous system.All creators create instance with final family instead of changing the family during extraction. Render passes are not related to group id but to render layer instance. Render layer is still related to group. Workfile, review and scene render instances are created using autocreators instead of auto-collection during publishing. Subset names are fully filled during publishing but instance labels are filled on refresh with the last known right value. Implemented basic of legacy convertor which should convert render layers and render passes.




___


</details>

### **🐛 Bug fixes**


<details>
<summary>asdfasdf (<i><font color='#367F6C';>2d</font> </i> <i><font style='color:#365E7F';>/ nuke</font></i> ) - <a href="https://github.com/ynput/ci-testing/pull/32">#32</a></summary>


___


## Brief description
Setting up deadline for 3dsmax

## Description
Setting up deadline for 3dsmax by setting render outputs and viewport camera




___


</details>




## [3.4.1](https://github.com/ynput/ci-testing/tree/3.4.1)

[Full Changelog](https://github.com/ynput/ci-testing/compare/3.4.1...3.4.0)

### **🆕 New features**


<details>
<summary>this is testing pr for changelog generator (<i><font color='#367F6C';>3d</font> </i> <i><font style='color:#365E7F';>/ maya</font></i> ) - <a href="https://github.com/ynput/ci-testing/pull/21">#21</a></summary>


___


## Brief description
Little introduciton of the PR content.

## Description
Here is some text describing the Pr in more details. Here is some text describing the Pr in more details. Here is some text describing the Pr in more details. Here is some text describing the Pr in more details. Here is some text describing the Pr in more details. Here is some text describing the Pr in more details.
- some action points which were taken
- some action points which were taken




___


</details>


<details>
<summary>feature - about this (<i><font color='#367F6C';>2d</font> </i> <i><font style='color:#365E7F';>/ nuke</font></i> ) - <a href="https://github.com/ynput/ci-testing/pull/28">#28</a></summary>


___


this is a description for Pr


___


</details>

### **🚀 Enhancements**


<details>
<summary>stable release with changelog from milestone (<i><font color='#367F6C';>editorial</font> </i> <i><font style='color:#365E7F';>/ flame</font></i> ) - <a href="https://github.com/ynput/ci-testing/pull/27">#27</a></summary>


___





___


</details>

### **🐛 Bug fixes**


<details>
<summary>feature - also this needs to be included (<i><font color='#367F6C';>3d</font> </i> <i><font style='color:#365E7F';>/ nuke,maya</font></i> <i><font style='color:#1E1B7B';>/ ftrack</font></i> ) - <a href="https://github.com/ynput/ci-testing/pull/29">#29</a></summary>


___


## Brief description
This tries to reduce the scattered **hardcoded** values for _renderer_ attribute names, types and tries to clean up the same things on the `RenderSettings` class. I've also refactored the usage of it across the code.

## Description

- Delays getting image prefixes per renderer instead of loading project settings three times on import of `lib_rendersettings`
- Move over missing image prefixes values that existed on validator but not in `lib_rendersettings`
- Move over AOV char logic to `lib_rendersettings`
- Readability cosmetic tweaks on some lines which did more complex formatting than needed.
- Removed `lib.RENDER_ATTRS` in favor of the now added `RenderSettings.get_padding_attr` (other logic of `lib.RENDER_ATTRS` was unused)

```Python
import this
this.use(1)
```




___


</details>


<details>
<summary>fix: this and that (<i><font color='#367F6C';>editorial</font> </i> <i><font style='color:#365E7F';>/ flame</font></i> ) - <a href="https://github.com/ynput/ci-testing/pull/30">#30</a></summary>


___


here is a text


___


</details>




## [3.4.1](https://github.com/ynput/ci-testing/tree/3.4.1)

[Full Changelog](https://github.com/ynput/ci-testing/compare/3.4.0...3.4.1)

### **🆕 New features**


<details>
<summary>this is testing pr for changelog generator (<i><font color='#367F6C';>3d</font> </i> <i><font style='color:#365E7F';>/ maya</font></i> ) - <a href="https://github.com/ynput/ci-testing/pull/21">#21</a></summary>


___


## Brief description
Little introduciton of the PR content.

## Description
Here is some text describing the Pr in more details. Here is some text describing the Pr in more details. Here is some text describing the Pr in more details. Here is some text describing the Pr in more details. Here is some text describing the Pr in more details. Here is some text describing the Pr in more details.
- some action points which were taken
- some action points which were taken




___


</details>


<details>
<summary>feature - about this (<i><font color='#367F6C';>2d</font> </i> <i><font style='color:#365E7F';>/ nuke</font></i> ) - <a href="https://github.com/ynput/ci-testing/pull/28">#28</a></summary>


___


this is a description for Pr


___


</details>

### **🚀 Enhancements**


<details>
<summary>stable release with changelog from milestone (<i><font color='#367F6C';>editorial</font> </i> <i><font style='color:#365E7F';>/ flame</font></i> ) - <a href="https://github.com/ynput/ci-testing/pull/27">#27</a></summary>


___





___


</details>

### **🐛 Bug fixes**


<details>
<summary>feature - also this needs to be included (<i><font color='#367F6C';>3d</font> </i> <i><font style='color:#365E7F';>/ nuke,maya</font></i> <i><font style='color:#1E1B7B';>/ ftrack</font></i> ) - <a href="https://github.com/ynput/ci-testing/pull/29">#29</a></summary>


___


## Brief description
This tries to reduce the scattered **hardcoded** values for _renderer_ attribute names, types and tries to clean up the same things on the `RenderSettings` class. I've also refactored the usage of it across the code.

## Description

- Delays getting image prefixes per renderer instead of loading project settings three times on import of `lib_rendersettings`
- Move over missing image prefixes values that existed on validator but not in `lib_rendersettings`
- Move over AOV char logic to `lib_rendersettings`
- Readability cosmetic tweaks on some lines which did more complex formatting than needed.
- Removed `lib.RENDER_ATTRS` in favor of the now added `RenderSettings.get_padding_attr` (other logic of `lib.RENDER_ATTRS` was unused)

```Python
import this
this.use(1)
```




___


</details>


<details>
<summary>fix: this and that (<i><font color='#367F6C';>editorial</font> </i> <i><font style='color:#365E7F';>/ flame</font></i> ) - <a href="https://github.com/ynput/ci-testing/pull/30">#30</a></summary>


___


here is a text


___


</details>



## [3.2.0](https://github.com/pypeclub/ci-testing/tree/3.2.0) (2021-06-15)

[Full Changelog](https://github.com/pypeclub/ci-testing/compare/CI/3.2.0-nightly.7...3.2.0)

## [CI/3.2.0-nightly.7](https://github.com/pypeclub/ci-testing/tree/CI/3.2.0-nightly.7) (2021-06-15)

[Full Changelog](https://github.com/pypeclub/ci-testing/compare/CI/3.2.0-nightly.6...CI/3.2.0-nightly.7)

## [CI/3.2.0-nightly.6](https://github.com/pypeclub/ci-testing/tree/CI/3.2.0-nightly.6) (2021-06-15)

[Full Changelog](https://github.com/pypeclub/ci-testing/compare/CI/3.2.0-nightly.5...CI/3.2.0-nightly.6)

## [CI/3.2.0-nightly.5](https://github.com/pypeclub/ci-testing/tree/CI/3.2.0-nightly.5) (2021-06-15)

[Full Changelog](https://github.com/pypeclub/ci-testing/compare/CI/3.2.0-nightly.4...CI/3.2.0-nightly.5)

## [CI/3.2.0-nightly.4](https://github.com/pypeclub/ci-testing/tree/CI/3.2.0-nightly.4) (2021-06-15)

[Full Changelog](https://github.com/pypeclub/ci-testing/compare/CI/3.2.0-nightly.3...CI/3.2.0-nightly.4)

## [CI/3.2.0-nightly.3](https://github.com/pypeclub/ci-testing/tree/CI/3.2.0-nightly.3) (2021-06-15)

[Full Changelog](https://github.com/pypeclub/ci-testing/compare/CI/3.2.0-nightly.2...CI/3.2.0-nightly.3)

## [CI/3.2.0-nightly.2](https://github.com/pypeclub/ci-testing/tree/CI/3.2.0-nightly.2) (2021-06-15)

[Full Changelog](https://github.com/pypeclub/ci-testing/compare/3.1.1...CI/3.2.0-nightly.2)

**Implemented enhancements:**

- testing PR in changelog [\#8](https://github.com/pypeclub/ci-testing/pull/8) ([mkolar](https://github.com/mkolar))



\* *This Changelog was automatically generated by [github_changelog_generator](https://github.com/github-changelog-generator/github-changelog-generator)*
