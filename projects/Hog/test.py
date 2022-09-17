import hog
always_one = hog.make_test_dice(1)
always_two = hog.make_test_dice(2)
always_three = hog.make_test_dice(3)
always = hog.always_roll
#
# Handle multiple turns with many swaps
s0, s1 = hog.play(always(1), always(1), goal=30, dice=hog.make_test_dice(6, 1, 4, 6, 5, 2, 9))
s0