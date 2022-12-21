# ASDF

Manage multiple runtime versions with a single CLI tool, extendable via plugins - docs at asdf-vm.com

asdf-vm is a CLI tool that can manage multiple language runtime versions on a per-project basis. It is like gvm, nvm, rbenv & pyenv (and more) all in one! Simply install your language's plugin!

https://asdf-vm.com/#/core-manage-asdf-vm

## Installation

https://asdf-vm.com/#/core-manage-asdf?id=install

mac

```
brew install asdf
echo -e '\n. $HOME/.asdf/asdf.sh' >> ~/.bashrc
echo -e '\n. $HOME/.asdf/completions/asdf.bash' >> ~/.bashrc
```

linux

```
sudo apt install curl git
git clone https://github.com/asdf-vm/asdf.git ~/.asdf --branch v0.8.0
```

Add the following to ~/.bashrc:

```
. $HOME/.asdf/asdf.sh
```

Completions must be configured by adding the following to your .bashrc:

```
. $HOME/.asdf/completions/asdf.bash
```

```
asdf plugin list
```

## Python

https://github.com/danhper/asdf-python

```
brew uninstall python python3 pyenv python@3.8
asdf plugin-add python
asdf list python
asdf install python latest
asdf global python 3.6.2
```

## Ruby

```
asdf plugin-add ruby https://github.com/asdf-vm/asdf-ruby.git
asdf install ruby latest
asdf global ruby 2.7.1
```

## nodejs

https://github.com/asdf-vm/asdf-nodejs

```
GNU Core Utils - brew install coreutils
GnuPG - brew install gpg
brew install gawk
bash -c '${ASDF_DATA_DIR:=$HOME/.asdf}/plugins/nodejs/bin/import-release-team-keyring'
asdf plugin-add nodejs https://github.com/asdf-vm/asdf-nodejs.git
asdf list nodejs
asdf install nodejs latest
asdf install nodejs 12.12.0
asdf global nodejs 12.12.0
```
