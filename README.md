# GitHub Flow Pattern Demo

This repository demonstrates the **GitHub Flow** branching strategy.

## Philosophy & In-Depth Explanation
GitHub Flow is a lightweight, branch-based workflow that supports teams and projects where deployments are made regularly. It is significantly simpler than Gitflow.

The core rule is that anything in the `main` branch is always deployable. To work on something new, you create a descriptively named branch off of `main` (e.g., `new-oauth-flow`), commit to that branch locally, and regularly push to the server. When you need feedback or help, or you think the branch is ready for merging, you open a **Pull Request**. Once reviewed and approved, it is merged into `main` and deployed immediately.

## Comparison with Other Patterns

| Pattern | Best For | Key Difference |
| :--- | :--- | :--- |
| [**Gitflow**](https://github.com/AustonIvison/demo-gitflow-pattern) | Scheduled releases, strict control. | More complex structure with `develop` and `release` branches. |
| **GitHub Flow** (This Repo) | Continuous deployment, web apps. | Simple cycle: Branch -> PR -> Merge -> Deploy. `main` is always production-ready. |
| [**Trunk-Based**](https://github.com/AustonIvison/demo-trunk-based-pattern) | High-velocity teams, CI/CD. | Focuses on avoiding "merge hell" by merging to `main` extremely frequently, often without PRs for every single commit, using feature flags. |

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
