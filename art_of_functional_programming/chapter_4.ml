(* sum of list*)
let rec total l =
  match l with
  | [] -> 0
  | h :: t -> h + total t;;

(* 4.5.1 *)
(* find longest string in a list*)
let longest_string l = 
  (let rec helper l current_max = 
    match l with 
    | [] -> current_max
    | hd :: tl -> helper tl (max (String.length hd) current_max) 
  in helper l (0));;

(* 4.5.2 *)
(* function to concat: string -> string list -> string *)
(* to add a string s and a list of string l and then concatenate all the strings in the list delimited by s *)
let concat delimiter los =
  (let rec helper l = 
    match l with
    | [] -> ""
    | hd :: [] -> hd
    | hd :: tl -> hd ^ delimiter ^ helper tl
  in helper los);;

(* 4.5.3 *)
(* function to return the height of the binary tree *)
(* height of binary tree is the longest path from the root node to any leaf in the tree *)
type 'a bin_tree = 
  | Leaf
  | Node of 'a bin_tree * 'a * 'a bin_tree;;

let rec height t = 
  match t with 
  | Leaf -> 0
  | Node (l, _, r) -> 1 + max (height l) (height r);;

(* 4.5.4 *)
(* find the predecessor of natural number *)
(* function that takes n of nat and returns its predecessor *)
type nat = Zero | Succ of nat;;

let rec pred nats = 
  match nats with 
  | Zero -> None
  | Succ x -> Some x;; 

(* 4.5.5 *)
(* add two natural numbers *)
(* add two nat types, example: add Zero Zero = Zero, add Zero (Succ Zero) = Succ Zero, add (Succ Zero) (Succ Zero) = Succ(Succ Zero) *)
let rec add l r = 
  match r with 
  | Zero -> l
  | Succ x -> add (Succ l) x;;
