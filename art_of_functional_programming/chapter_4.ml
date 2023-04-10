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