## Setup OCaml

```
opam init
eval $(opam env)
opam swtich create 4.12.0
eval $(opam env)

opam install utop
eval $(opam env)
utop
```