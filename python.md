# Python

https://docs.python.org/3/tutorial/venv.html#creating-virtual-environments

```
asdf install python 3.9.0
asdf global python 3.9.0
python -m venv myenv
<!-- python -m virtualenv myenv -->
source myenv/bin/activate
pip install -r requirements.txt
```

## Formatter

Proposed Solution

- Formatter: yapf
- VSCode Extension: ms-python
  -- Config: `.vscode/settings.json` and `.style.yapf`
  -- Keyboard Shortcuts: `shift + alt + f`

```
// .vscode/settings.json
{
  "python.pythonPath": "env/bin/python2.7"
}
```

```
// .style.yapf
[style]
based_on_style = google
ALLOW_SPLIT_BEFORE_DICT_VALUE = False
INDENT_DICTIONARY_VALUE = True
SPLIT_BEFORE_FIRST_ARGUMENT = True
```

## Virtualenv

https://virtualenv.pypa.io/en/latest/cli_interface.html

```
virtualenv env
virtualenv -p /Users/yes/.asdf/shims/python env
source env/bin/active
python --version
pip install -r requirements.txt
```
