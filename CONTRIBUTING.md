# CONTRIBUTING

## Code Style

- For each important variable, add a single comment line using #.
- For each function, add a `multiline docstring` at the start of the body describing the use of the function, the parameters and the return value.
- For each class, describe the use of the class, each field of the class and the constructor parameters in a `multiline docstring`.
- Always have a `newline` at the end of the file.
- If you add a new dependency, update the `requirements.txt` in the correct format.
  
## Example functions following code style

```python
def func(a):
    """
    func(a) increments the value of a returns it.
    @params:
        a: int
    @return:
        int
    """
    a = a + 1
    return a
```

## Contributing code

1. Clone the repository.
2. Checkout a new branch : `git checkout -b <name>_<feature>`.
3. Make changes.
4. Stage only required files to commit : `git add <Files_Changed>`. Don't add files you did not intentionally changed.
5. Commit with a proper message `git commit -m "message"`.
6. Push the branch : `git push origin <name>_<feature>`. Remember NOT to push `main` branch.
7. Create a Pull Request.
8. After the PR is merged, delete the local branch : `git checkout main && git branch -D <name>_<feature>`.
9. Pull the latest main branch : `git pull`.
10. Repeat Steps 2 to 6 for further contributions.

NOTE: Don't delete the branch unless the PR is merged.
