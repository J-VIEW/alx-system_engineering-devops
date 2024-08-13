![alt text](../../../AppData/Local/Temp/technology-humor-memes-9iw7dun6u8ffz3mt.jpg)

# Postmortem: Bcrypt Gem Version Issue

## Issue Summary

We had just released a new feature to our recently launched Ruby on Rails site when we encountered our first wave of user complaints. Five minutes after performing a feature update, we started receiving emails from users stating that they couldn't sign in or sign up on our platform. This was surprising as the feature had worked on our machines and had functioned correctly before. In total, we received about 127 emails, creating an avalanche of complaints. Given the importance of user retention, we couldn't afford to lose 127 users and immediately began investigating the problem.

We cloned our site's repository from GitBug and followed the installation instructions in the README file, only to find that the site couldn't start up. It quickly became apparent that the issue was due to failing to update the project's requirements. The site malfunctioned from 9:55 AM GMT+1 to 11:20 AM GMT+1.

## Timeline

- **05-02-2022 9:55 AM GMT+1:** A customer complained that they couldn't sign in to the site.
- **05-02-2022 10:20 AM GMT+1:** Winus, one of our backend developers, experienced the same issues our customers reported.
- **05-02-2022 10:35 AM GMT+1:** We investigated the controllers and the views for inconsistencies.
- **05-02-2022 10:40 AM GMT+1:** We assumed the bcrypt (one of our site's dependencies) gem being used was either at fault or used incorrectly because the error message on the site showed that the bcrypt gem was raising an error over an invalid hash.
- **05-02-2022 10:42 AM GMT+1:** We checked that the views might not be binding the form fields to the right model fields, which later turned out to be false.
- **05-02-2022 10:45 AM GMT+1:** We were misled by thinking that our controllers might be creating a different hash for a valid password of the site's admin.
- **05-02-2022 10:50 AM GMT+1:** Winus thought the issue might have been that the password was not properly hashed.
- **05-02-2022 11:00 AM GMT+1:** The incident was escalated to the backend development team.
- **05-02-2022 11:20 AM GMT+1:** The incident was resolved by updating the requirements (the bcrypt gem version) for the backend server.

## Root Cause and Resolution

The version of the bcrypt gem we used was outdated. It raised an error over a hash that was valid and matched what was stored in the database. The hash we were creating might not have been supported by the installed version of bcrypt. Winus fixed the issue by manually updating the version of bcrypt in the `Gemfile.lock` file to a more recent version and reinstalling the required gems. The fix worked successfully.

## Corrective and Preventative Measures

- **Setup a continuous integration pipeline** to run a build on each pull request branch. This will ensure that builds are passing in the pull request branch before it is merged with the deployment branch.
- **Setup a monitoring system** for the database and application servers to keep track of any issues that may occur.
- **Develop tests** that must be passed for each new feature. These tests should pass before they are merged with the deployment branch.

## Additional Notes

- **Engagement Strategy:**  
  Consider adding humor, a diagram, or a catchy visual to make the postmortem more engaging.

  _Keep your postmortem brief, straight to the point, and between 400 to 600 words._
