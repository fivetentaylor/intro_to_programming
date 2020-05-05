# Intro To Programming

Captures examples and students solutions throughout the course

## Setup pyenv

pyenv is a utility for managing multiple python installations on the same system

```
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bash_profile
```

## Setup SSH Keys

How to generate a new ssh key pair to connect to github

```
ssh-keygen # press enter till success
cat ~/.ssh/id_rsa.pub | pbcopy
```
