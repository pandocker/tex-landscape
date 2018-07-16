# tex-landscape
Another pandoc filter to force a div to landscape page

Contents in a "LANDSCAPE" class div will be placed in landscape page.

### Sample markdown

```markdown
Portrait contents

::::: LANDSCAPE

Landscape contents with a page break

:::::

Portrait contents with a page break
```

### Usage

```sh
pandoc --filter=pandocker-tex-landscape markdown.md --output html.html
```
