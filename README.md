# Gaël Close's personal website

Personal website of [Gaël Close](https://orcid.org/0000-0002-5140-7789).

The CLI tasks mentionned below are all defined in the [Taskfile](Taskfile.yml).
Invoke with `task <task-name>`. 

## Render

The website, ready to be distributed, is built in the [dist/ folder](dist/index.html).

```bash
# Temporary server for preview
quarto preview site
# Full render
quarto render site
```

## Publication on Github pages

Committing and pushing to the [remote repo](https://github.com/gael-close/gael-close.github.io),
invokes the publication to <https://gael-close.github.io/>.
The dist/ folder is deployed as a Github Pages site via a Github action.

```bash
task pub
```

## Dependencies

- [Quarto](https://quarto.org/)
- [Task](https://taskfile.dev/)

## References

Additional info in second brain at `$BR2/Personal/Blog`.
Blog contents also exported there with `task export` via symlinks for broad accessibility.

