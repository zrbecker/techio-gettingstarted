from double_counted import count_number_words_no_dupes

def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))

def success():
    print("TECHIO> success true")

def fail():
    print("TECHIO> success false")
    
def test_double_counted():
    try:
        # Given
        words1 = ['red', 'blue', 'red', 'green']
        words2 = ['apple', 'blueberry', 'raspberry', 'kiwi']

        # When
        count1 = count_number_words_no_dupes(words1)
        count2 = count_number_words_no_dupes(words2)

        # Then
        assert count1 == 3, 'Expected 3 got {} on list {}'.format(
                count1, words1)
        assert count2 == 4, 'Expected 4 got {} on list {}'.format(
                count2, words2)

        success()
        send_msg('Success!', 'You got it correct!')
    except AssertionError as e:
        fail()
        send_msg('Opps!', e)
        send_msg('Hint', "Don't double count those words!")


if __name__ == '__main__':
    test_double_counted()
