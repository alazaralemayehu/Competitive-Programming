def longestPeak(array):
    longest_peak_count = 0

    counter = 0
    is_increasing = True
    for i in range(1, len(array)):
        current_number = array[i]
        previous_number = array[i - 1]

        if current_number > previous_number:
            if is_increasing:
                counter += 1
            else:
                if counter > 3 and longest_peak_count < counter:
                    longest_peak_count = counter + 1

                counter = 1
                is_increasing = False

        elif current_number < previous_number:
            if not is_increasing:
                counter += 1
            else:
                if counter > 3:
                    if longest_peak_count < counter:
                        longest_peak_count = counter + 1
                counter = 1
                is_increasing = True

        else:
            counter = 0
            is_increasing = True
