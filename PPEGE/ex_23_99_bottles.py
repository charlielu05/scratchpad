
# 99 bottles on the wall song
def ninety_nine_bottles(bottles=99)->str:
    # recursive solutions requires counting down from 99
    if bottles == 0:
        print("No more bottles of beer on the wall!")
    else:
        print(f"""{bottles} bottles of beer on the wall,\n
                {bottles} bottles of beer,\n
                Take one down,\n
                Pass it around,\n
                {bottles - 1} bottles of beer on the wall.""")
        ninety_nine_bottles(bottles - 1)

if __name__ == "__main__":
    ninety_nine_bottles()