from python import Python

fn set_fire(borrowed text: String) -> String:
    # text += "🔥"
    return text +"🔥" 

struct MyPair:
    var first: Int
    var second: Int

    fn __init__(inout self, first: Int, second: Int):
        self.first = first
        self.second = second
    
    fn dump(self):
        print(self.first, self.second)

fn mojo():
    let a: String = "mojo"
    let b = set_fire(a)
    print(a)
    print(b)

fn main() raises:
	mojo()
	let a = MyPair(first=1,second=2)
	a.dump()
	let np = Python.import_module("numpy")
	let ar = np.arange(15).reshape(3, 5)
	print(ar)
	print(ar.shape)



