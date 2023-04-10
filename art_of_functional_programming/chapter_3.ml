(* is prime number, only divisible by 1 and itself
starting from number - 1 iterate to 2 *)

let rec prime n = if n < 2 then false else if n = 2 then true else
  let rec aux m = if n mod m = 0 then
    false
  else if m * m > n then 
    true else aux (m + 1) in aux 2;;

(* Naive Fibonacci
write OCAML function for fib: int -> int that returns the n-th fibonacci number *)

let rec fib n = if n <= 0 then 0 else if n <= 2 then 1 else fib (n - 2) + fib (n - 1);;

(* Super Fib, use tail recursive *)

let super_fib n = 
  let rec helper a b m = if m >= n then a 
  else helper b (a + b) (m + 1) in 
  helper 0 1 0;;

(* function twice that applies a function twice *)

let twice func x = func(func x);;

(* filtered accumulate function that takes a predicate p
   filtered_accumulate (+) 0 (fun x -> x) is_prime 1 4 = 5*)

let rec accumulate combiner init term m n = 
  if m > n then init
  else combiner (term m) (accumulate combiner init term (m + 1) n);;

let rec filtered_accumulate combiner init term predicate m n =
  if m > n then init
  else if predicate (term m) then combiner (term m) (filtered_accumulate combiner init term predicate (m + 1) n) 
  else filtered_accumulate combiner init term predicate (m + 1) n;;