" Vim syntax for Just Text (*.jt) files.
" 
"

if exists("b:current_syntax")
  finish
endif

setlocal iskeyword+=!
syn case match

syn region jtComment start=/^! / end=/$/
syn match jtDef /\![a-zA-Z\-]\+:/
syn match jtCommand /\![a-zA-Z\-]\+/
syn match jtArg / [\~\_\@\*]\+ /

highlight link jtComment Comment
highlight link jtDef Identifier
highlight link jtCommand Identifier
highlight link jtArg Statement

let b:current_syntax = "jt"
