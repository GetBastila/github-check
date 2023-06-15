### Track and enforce your code quality progression

Bastila is an application that prevents the addition of and tracks the removal of deprecated code patterns, components, and functions using predefined regular expressions.

### How it works

Bastila integrates in two places in your code contribution process.

1. When pull requests are made this extension will search your code for your predefined values and block the pull request from being completed if it adds patterns that you have defined as deprecated. Error messages will be displayed in the build to recommend what developers should use instead.
2. When pull requests are merged and completed, this extension will count the instances found of those predefined code patterns and POST that data to the Bastila app so that you can see the progress you've made in removing old patterns.

### Inputs

1. `BASTILA_KEY`: A secret key for your repository is a required argument from the Bastila app that is used to authenticated this Github action with Bastila.
2. `POST_RESULTS`: A boolean input is required to determine if the results of the search of old patterns should be posted as progress to Bastila. You only want to set this to true when you are merging data into your main/release branch.
