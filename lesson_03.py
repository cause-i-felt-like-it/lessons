### LESSON_03: WELCOME TO THE BINARY ###

### THE BYTE(8-bits) ###

# ||128 64 32 16 | 8  4  2  1 ||
# || #  #  #  #  | #  #  #  # ||
#                     X     X               4 + 1 = 5                      ->  0000 0101
#    X        X          X  X    128 + 16 + 2 + 1 = 147                    ->  1001 0011
#       X             X                    64 + 4 = 68                     ->  0100 0100
#          X             X  X          32 + 2 + 1 = 35                     ->  0010 0011
#    x  x  x  x    x  x  x  x    128 + 64 + 32 + 16 + 8 + 4 + 2 + 1 = 255  ->  1111 1111


## inside the computer these are actually lines of electricity:

#        RAM
#     |||| ||||
#     | |    |
#     | |    |
#     | |    |
#     | |    |
#     |||| ||||
#        CPU

# Above, RAM is sending to the CPU, the Byte 162 -> 1010 0010
# 162 can also mean the letter r <--that letter right there, in this file, is literally 162; that's all it is.
# so on your monitor 162 is being drawn like this--> r
# Search 'ascii table' on a search engine to see the full map of characters.
# remember there's a difference between:
a_number = 162
text_aka_a_string = "162"
one = 61
six = 66
two = 62
# So the number 162 is a single byte. but the text "162" is 3 bytes: a "1" character, a "6" character, and a "2" character lined up
# next to eachother in a "string" of bytes. <-- so far we have 1268 characters in this lesson file, so 1268 bytes, or 1.268 kiloBytes,
# or 0.01268 megaBytes.
# So if these things are lines of electricity, how does that get stored in RAM? As tiny dots of electric charge. CPU tells the RAM chip
# the address of the row of 8 charges (byte) it wants to address, and the RAM chip reports back which of those dots have charge in that row.
# And in our case above, we got back 162. And in a smiliar fashion the CPU could tell RAM to overwrite that address with a different 'number'
# so-to-speak (it's just elecricity lines).
# Go Watch a youtube video on the RAM's 'address bus' and 'data bus'. Do it. Not a joke. You need to learn this. Go do it: Just enough to get an idea.
# If we used the leftmost bit, 128, for determining positive or negative, we could communicate a number from -128 to 127. this is called
# a 'signed' interger. the regular byte that gives us 0-255 is called unsigned. the 128-bit is not being used as a 'sign-bit', so the
# number is unsigned.
# Go lookup some youtube videos on signed intergers, and how '1's complement' works.

### MATH ###
# let's just restrict ourselves to 4 bits (a 'nibble'/'nybble'/'nyble'/half-byte)
#  0010  2
# +0101  5
# _____
#  0111  7

#  0111  7
# +0100  4 here we have to carry the 3rd bit from the right to the 4th aka MSb (most significant bit)
# _____
#  1111  15 (max value)

#  1111  15
# +0001  1  !overflow!
# _____
#  0000  0
# The hardware will often have an overflow bit to keep track of when this kind of thing happens in hardware, to take care of this for you,
# but in programming you're out of luck if you violate this python forgvies everything so you don't have to worry (python is a toy language
# with safety mechanism everywhere. We won't be able to commit an interger/math overflow error in python. But when we start programming for real,
# this will become important.

### BITWISE OPERATIONS ###
# This lines of electricity don't have to be used for numbers. We already saw that they can be used for characters in text.
# How else can we use them? We can use them as switches and flags. We can use them as placeholders indicating whatever we want.
# As we just saw a Nybble has 16 possible values (0-15) from the 4 bits. And a Byte (8 bits) doesn't just give us twice that,
# it gives us 256 total possible combinations/states. We don't need to think of these as mathmatical numbers, we can assign whatever we want
# to each one of these states. And by that I mean that 0000_0001 is an identifiably different state of being than 0000_0000. One of those
# states could represent that your character in a game is jumping, and the other running. We already saw that 1010_0010 means the letter 'r'.
# It's whatever-maaan.
# When it comes to working directly with the processor of our wrist-watch, we will often be using these as flags or switches.
# The processor will have some setting we want to tweak in a register (fast memory in the CPU), and so we'll address that set of 8 switches,
# and flip the switches we want. So this is why we need bitwise operations.
# The first one I'll teach you is bitwise-OR:
#
#    0100
# OR 0101
# _______
#    0101   <-- if we had added them, it would have been 1001, not 0101
#
# In bitwise-OR we are treating each digit individually, and asking if either top or bottom row is a 1-- if it is, the answer is a 1.
# Is the least significant bit (far right) of either row a 1?
#
#    010|0|
# OR 010|1| <-- yes
# _________
#    ??? 1
#
# Now just do that for each column.
# Easy enough, but why do this?
# Say I've got a 2 switches i want to hit at address 0xA8003C31
# An address always points to a single Byte. Lets say the register has communication settings for talking to other chips on our circuitboard.
#  @address 0xA8003C31:
#  options   7 6 5 4 3 2 1 0
#            ________________
#            1 1 0 0 0 1 1 1  these switches are already flipped, and let's say i want options 4 and 2 to be turned on, but we haven't checked what's already in there.

address_A8003C31 = (32 + 4)      # which means address_A8003C31 = 0001_0100

# this would be the result:
#
#  @address 0xA8003C31:
#  options   7 6 5 4 3 2 1 0
#            ________________
#            0 0 0 1 0 1 0 0

# Oops... hope those options we just turned off weren't important...
# Okay, well we should add them to what's already there:

address_A8003C31 += (32 + 4)   # which means 'address_A8003C31 = address_A8003C31 + (32 + 4)

#  @address 0xA8003C31:
#  options   7 6 5 4 3 2 1 0
#            ________________
#            1 1 0 1 1 0 1 1
#                      ^ hey! I wanted options 4 and >2<, not 4 and >3<; what happened?
# It did what we asked it to, and we asked for addition, which involves carrying. Option 2 was already flipped on (remember I said we didn't check
# beforehand: checking then adding based on what options are already checked, would be a pain to code)
# Let's bitwise-OR this:
#
address_A8003C31 = address_A8003C31|(32+4)
#also written as:
address_A8003C31 |= (32+4)

#  @address 0xA8003C31:
#  options   7 6 5 4 3 2 1 0
#            ________________
#            1 1 0 1 0 1 1 1
#                     Much better: 2 was already ON, and thus stayed ON, 4 is ON like we wanted, and the rest were left alone.
#
# Go watch some youtube videos on the other bitwise operations like bitwise-AND.
# See you next lesson.
#
#
#
#
#
#
#
#
#
#
# DISCLAIMER: Don't actually type that 'address_A8003C31 =' code. It's psuedo-code. We can't modify memory at >specified addresses< in python. (at
#             least not easily. It's not really what python is for)
#             But we won't be using this toy-language for much longer (however you'll probably always use python for things; it's alot of fun)