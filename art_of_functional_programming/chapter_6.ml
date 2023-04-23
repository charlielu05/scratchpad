
(* Coding challenge 6.3.1: Area of the largest circle *)

(* shape type*)
type shape = Circle of float | Rectangle of float * float;;

(* calculate area of shape *)
let area s = match s with
  | Circle r -> 3.14 *. r *. r
  | Rectangle (w, h) -> w *. h;;

let is_circle x = 
  match x with 
  | Circle r -> true
  | _ -> false;;

(* write a function max_circle that takes list of shape and outputs area of largest circle in the list *)
((* max_circle [] = 0 
    max_circle [Circle 1.; Rectangle (1., 2.); Circle 2.; Rectangle (2., 3.)] *))
let rec max_circle los = 
  match los with 
  | [] -> 0.
  | hd :: tl -> List.fold_left max 0. (List.map area (List.filter is_circle los));;

(* Merge two streams *)
(* stream_take 10 (stream_merge evens odds) = [0;1;2;3;4;5;6;7] *)

(* stream type *)
type 'a stream = Cons of 'a * 'a stream Lazy.t;;

(* head and tail for a stream*)
let stream_hd (Cons (h, _)) = h;;
let stream_tl (Cons (_, t)) = Lazy.force t;;

let rec naturals_from n = Cons (n, lazy (naturals_from (n+1)));;

(* take n from stream *)
let rec stream_take n s =
  if n <= 0 then [] 
  else stream_hd s :: stream_take (n-1) (stream_tl s);;

let rec stream_filter p s = 
  if p (stream_hd s) then Cons (stream_hd s, lazy (stream_filter p (stream_tl s)))
  else stream_filter p (stream_tl s);;

let is_even = fun x -> x mod 2 = 0 ;;
let is_odd = fun x -> x mod 2 != 0 ;;

let rec stream_zipWith f s1 s2 = 
  Cons (f (stream_hd s1) (stream_hd s2), 
    lazy (stream_zipWith f (stream_tl s1) (stream_tl s2)));;

let odd_stream = stream_filter is_odd (naturals_from 0);;
let even_stream = stream_filter is_even (naturals_from 0);;