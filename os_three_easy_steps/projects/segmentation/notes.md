ARG address space size 1k
ARG phys mem size 16k

Segment register information:

  Segment 0 base  (grows positive) : 0x00001aea (decimal 6890)
  Segment 0 limit                  : 472

  Segment 1 base  (grows negative) : 0x00001254 (decimal 4692)
  Segment 1 limit                  : 450

VA  0: 0x0000020b (decimal:  523) --> PA or segmentation violation?
VA  1: 0x0000019e (decimal:  414) --> PA or segmentation violation?
VA  2: 0x00000322 (decimal:  802) --> PA or segmentation violation?
VA  3: 0x00000136 (decimal:  310) --> PA or segmentation violation?
VA  4: 0x000001e8 (decimal:  488) --> PA or segmentation violation?

Top bit determines if segment 0 or 1
Address space size is the virtual address

## Solution
All VA are segment 0 and grows positive
VA 0: 523 = violation
VA 1: 414 = 414 + 6890 = 7304
VA 2: 802 = 4692 + (802-1024)
VA 3: 310 = 310 + 6890 = 7200
VA 4: 488 = violation in SEG 0

---
```
ARG seed 0
ARG address space size 128
ARG phys mem size 512

Segment register information:

  Segment 0 base  (grows positive) : 0x00000000 (decimal 0)
  Segment 0 limit                  : 20

  Segment 1 base  (grows negative) : 0x00000200 (decimal 512)
  Segment 1 limit                  : 20

Virtual Address Trace
  VA  0: 0x0000006c (decimal:  108) --> PA or segmentation violation?
  VA  1: 0x00000061 (decimal:   97) --> PA or segmentation violation?
  VA  2: 0x00000035 (decimal:   53) --> PA or segmentation violation?
  VA  3: 0x00000021 (decimal:   33) --> PA or segmentation violation?
  VA  4: 0x00000041 (decimal:   65) --> PA or segmentation violation?
```

