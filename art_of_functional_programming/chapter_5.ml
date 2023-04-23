let rec square_list l =
  match l with
  | [] -> []
  | hd :: tl -> (hd * hd) :: square_list tl;;

let map_square_list = List.map (fun x -> x * x);;

let even i =
  match i with
  | i when i mod 2 = 0 -> true
  | _ -> false;;

let rec evens l = 
  match l with
  | [] -> []
  | hd :: tl -> if even hd then hd :: evens tl 
     else evens tl;;

let positive i = 
  match i with 
  | i when i > 0 = true -> true
  | _ -> false;;

let rec positives l = 
  match l with
  | [] -> []
  | hd :: tl -> if positive hd then hd :: positives tl
    else positives tl;; 

(* Coding challenge 5.5.1*)
(* right of 'b holds the correct value while left of 'a represents an error value *)
type ('a, 'b) either = Left of 'a | Right of 'b;;

(* mapping function for either called map_either : ('a -> 'b)-> ('c, 'a)either -> ('c, 'b)either. *)
let map_either f x = 
  match x with
  | Right x -> Right (f x)
  | Left x -> Left x;;

(* Coding challenge 5.5.2 *)
(* fold_left *)
(* applies function and reduce from left side of list to right *)
(* example: fold_left (-) 0 [1; 2; 3] = -6 *)
let rec fold_left f acc loi = 
  match loi with 
  | [] -> acc
  | hd :: tl -> fold_left f (f acc hd) tl;;

(* Coding challenge 5.5.3 *)
(* tree elements to list with fold_tree *)
(* apply fold over a tree type *)
type 'a bin_tree = Leaf | Node of 'a bin_tree * 'a * 'a bin_tree;;

(* function tree_to_list: 'a bin_tree -> 'a list that collects all elements of the tree, reusing fold_tree *)
let rec fold_tree f init t = 
  match t with 
  | Leaf -> init
  | Node (l, x, r) -> f (fold_tree f init l)
    x (fold_tree f init r);;

let tree_to_list t = fold_tree (fun l x r -> [x] @ l @ r) [] t;;

(* Coding challenge 5.5.4 *)
(* use zip_with to construct function to check if list is in ascending order *)
let rec zipWith f l1 l2 = 
  match l1, l2 with 
  | [], _ -> []
  | _, [] -> []
  | x :: xs , y :: ys -> f x y :: zipWith f xs ys;;

let all_true l = List.fold_right (&&) l true ;;

let is_ascending_sorted l = if l = [] then true
                            else all_true(zipWith (<=) l (List.tl l));;