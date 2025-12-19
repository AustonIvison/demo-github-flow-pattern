# GitHub Flow Pattern Demo

This repository demonstrates the **GitHub Flow** branching strategy.

## Philosophy
GitHub Flow is a lightweight, branch-based workflow that supports teams and projects where deployments are made regularly.

## Key Concepts
- **main**: The default branch where the code is always deployable.
- **Feature Branches**: Created from `main` for new work.

## How to Interact
1. **Create a Branch**: Create a descriptively named branch off of `main`.
   `git checkout -b new-feature`
2. **Make Changes**: Commit changes to your branch.
3. **Open a Pull Request**: Open a PR to merge your branch into `main`.
4. **Discuss and Review**: Review code and discuss changes.
5. **Merge and Deploy**: Merge the PR into `main` and deploy immediately.
