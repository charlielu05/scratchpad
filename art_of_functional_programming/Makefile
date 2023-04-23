
init-ocaml:
	opam init
	eval $(opam env)
	opam switch create 4.12.0
	eval $(opam env)

	opam install utop
	opam install ocaml-lsp-server
	eval $(opam env)