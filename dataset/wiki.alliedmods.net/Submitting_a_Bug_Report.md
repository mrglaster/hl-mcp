# Submitting a Bug Report
From AlliedModders Wiki
Jump to: [navigation](https://wiki.alliedmods.net/Submitting_a_Bug_Report#mw-head), [search](https://wiki.alliedmods.net/Submitting_a_Bug_Report#p-search)
This article goes over some basic rules for reporting bugs at AlliedModders. 
## Contents
  * [1 Getting Started](https://wiki.alliedmods.net/Submitting_a_Bug_Report#Getting_Started)
  * [2 Life cycle of a bug](https://wiki.alliedmods.net/Submitting_a_Bug_Report#Life_cycle_of_a_bug)
  * [3 Etiquette](https://wiki.alliedmods.net/Submitting_a_Bug_Report#Etiquette)
  * [4 Contributing Fixes](https://wiki.alliedmods.net/Submitting_a_Bug_Report#Contributing_Fixes)


# Getting Started
Use a descriptive title and include as much details as possible. What is going wrong? When is it happening? What do you expect to happen instead? 
If you are reporting a problem, such as a bug or crash: 
  * Post the output of "sm version" from your server console.
  * If your server is crashing, post the output of the following commands from your server console: ```
meta list
sm plugins list
plugin_print
```

  * If you have steps to reproduce, give as much detail as you can. For example, if the problem is a scripting or API problem, attach a test script. If there is a bug in parsing admin files, attach a file demonstrating the problem.
  * If your server is crashing and it's Windows, attach minidump (.mdmp) files.
  * If your server is crashing and it's Linux, note whether you have SSH access.


# Life cycle of a bug
Generally bugs follow a simple life cycle: 
  * Bug is reported by user.
  * Developer triages the bug for severity and priority.
  * If the bug is reproducible, or verifiable, or has steps to reproduce, the developer may grant blocking status. This means that particular release is stalled until the bug is fixed.
  * A patch is attached to address the problem.
  * The owner of the patch requests peer review. This is called the review? flag.
  * If the patch looks good, it gets a review+. Once the patch is checked in, the bug is usually closed.
  * If the patch needs work, it stays at review? or goes to review- until it is ready.


# Etiquette
**1. No obligation.** AlliedModders projects are free, open-source projects that are written in developers' spare time. They have no obligation to fix any bug or add any feature you want, no matter how serious or pressing you think it is. **If you nag developers or become impatient, your bug is likely to be ignored.** This includes comments like "status update?" or "is there any progress on this?" 
**2. No support questions.** Use the [forums](https://forums.alliedmods.net/) for support issues. 
**3. No third party requests.** The bug tool is not the place to post questions about, or ask features for, third party software or plugins maintained by the community. 
**4. No private contact.** Don't ask developers to meet you in private on a random instant messaging program. Don't send developers e-mail about a bug unless otherwise requested. 
**5. Do not link to small uploads.** If you have a small file to attach (small being less than 1MB or so), do not link to an external download site, especially free ones like megaupload. No one wants to wait 45 seconds after clearing ads and captchas. Attach small files using the Bugzilla "Add Attachment" link. 
# Contributing Fixes
See the main article [Contributing to SourceMod](https://wiki.alliedmods.net/Contributing_to_SourceMod "Contributing to SourceMod"). The key point is to attach _patches_ , not full files. If you make changes to a file in the source tree, the developers only care about your specific changes, and they won't want to manually diff your file by hunting down what original you might have used. 
