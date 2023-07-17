### Track and enforce your code quality progression

[Bastila](https://bastila.app/) is a tool for removing deprecated code. You define deprecated patterns using regex in the app and then prevent additional usages of those deprecated patterns from being used. The tool can also be used to track the removal of these patterns as well.

### How it works

This github action can be integrated in two places in your continuous integration pipeline.

1. When pull requests are made this extension will search your code for your predefined values and, if `PREVENT_REGRESSION=true`, block the pull request from being completed if it adds patterns that you have defined as deprecated. Error messages will be displayed in the build to recommend what developers should use instead.
2. When pull requests are merged and completed, this extension will count the instances found of those predefined code patterns and POST that data to the Bastila app so that you can see the progress you've made in removing old patterns. `POST_RESULTS` should be 'true' for step 2.

### Inputs

1. `BASTILA_KEY`: A secret key for your repository is a required argument from the Bastila app that is used to authenticated this Github action with Bastila.
2. `POST_RESULTS`: An optional (default false) boolean input used to determine if the results of the search of old patterns should be posted as progress to Bastila. You only want to set this to true when you are merging data into your main/release branch.
3. `PREVENT_REGRESSION`: An optional (default false) boolean input used to determine if changes that add deprecated code should be blocked.

Support: hello@bastila.app