# tmux
- https://tmuxcheatsheet.com/
- Source: https://gist.github.com/henrik/1967800

## Installation

https://linuxize.com/post/getting-started-with-tmux/#installing-tmux-on-macos

mac

```
brew install tmux
```

## cheatsheet

As configured in [my dotfiles](https://github.com/henrik/dotfiles/blob/master/tmux.conf).

start new:

    tmux

start new with session name:

    tmux new -s myname

attach:

    tmux a  #  (or at, or attach)

attach to named:

    tmux a -t myname

list sessions:

    tmux ls

kill session:

    tmux kill-session -t myname

In tmux, hit the prefix `ctrl+b` and then:

## Sessions

Create session

```
tmux new -s hiiiike
```

List sessions

```
tmux ls
Ctrl + b s
```

## Windows (tabs)

    c           new window
    ,           name window
    w           list windows
    f           find window
    &           kill window
    .           move window - prompted for a new number
    :movew<CR>  move window to the next unused number

```
ctrl + b f
```

## Panes (splits)

ctrl b +
% horizontal split
" vertical split

    o  swap panes
    q  show pane numbers
    x  kill pane
    ⍽  space - toggle between layouts

## Window/pane surgery

    :joinp -s :2<CR>  move window 2 into a new pane in the current window
    :joinp -t :1<CR>  move the current pane into a new pane in window 1

- [Move window to pane](http://unix.stackexchange.com/questions/14300/tmux-move-window-to-pane)
- [How to reorder windows](http://superuser.com/questions/343572/tmux-how-do-i-reorder-my-windows)

## Misc

ctrl b +
d detach
t big clock
? list shortcuts
: prompt

Resources:

- [cheat sheet](http://cheat.errtheblog.com/s/tmux/)

Notes:

- You can cmd+click URLs to open in iTerm.

TODO:

- Conf copy mode to use system clipboard. See PragProg book.

## Search

ctrl b + [
crtl s

```
n - next search match
? - search backward
/ - search forward
```
