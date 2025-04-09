from lib.time_estimation import *
import pytest

# test output for empty string
# test less than a minute
# test for minutes
# test for seconds
# test for hours
# test output for int


text_100 = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc in ullamcorper tortor, non egestas sapien. Nulla sagittis sodales est, et commodo tellus. Nulla placerat vestibulum efficitur. Nam quis diam ut nibh placerat porta in ac lorem. Sed varius placerat massa a gravida. Phasellus eget justo sollicitudin, pulvinar ligula vitae, pretium diam. Suspendisse suscipit viverra finibus. Proin pretium convallis arcu eu iaculis. In in efficitur nisi. Proin lacinia magna quis turpis fringilla placerat. Curabitur auctor orci orci, eu tincidunt est ultricies at. Fusce pharetra, turpis non sagittis placerat, odio sapien sodales enim, ut placerat velit ex ac purus. In in enim.'
text_200 = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus feugiat lacus eget lectus gravida, non dignissim dui bibendum. Nam pulvinar turpis pharetra est rutrum, eu scelerisque magna fermentum. Nulla vulputate congue volutpat. Sed ac turpis a leo pellentesque sollicitudin. Aliquam tortor nulla, vestibulum sed vestibulum et, consequat sed lacus. Quisque fermentum mauris sed laoreet rhoncus. Mauris pretium non leo in convallis. Maecenas eget magna mattis, suscipit erat at, facilisis ante. Suspendisse fermentum magna neque, eget commodo risus rhoncus vitae. Ut tellus augue, interdum et semper id, tempor vitae diam. Ut malesuada, eros in fringilla pulvinar, ipsum elit vulputate tellus, faucibus porta ipsum diam eget velit. Fusce cursus maximus purus blandit faucibus. Suspendisse vel consequat dolor. Maecenas ac neque arcu. Vivamus pretium molestie metus sit amet ornare. In ac nisl sed tortor hendrerit dictum vitae rhoncus nulla. Nunc auctor felis id urna tincidunt, nec dignissim ante semper. Duis viverra, justo ac accumsan iaculis, justo odio mattis nisl, eget porta arcu nisl egestas mi. Proin dui libero, sagittis iaculis ex quis, tincidunt viverra purus. Maecenas pulvinar auctor ipsum, a vulputate libero viverra vel. Quisque convallis ex volutpat enim. Phasellus a porta enim. Suspendisse ullamcorper maximus arcu, ac ultricies turpis pulvinar a. Fusce congue.'

def test_empty():
    assert time_estimation('') == 'This text will take you less than 1 minute to read.'

def test_less_than_a_minute():
    assert time_estimation(text_100) == 'This text will take you less than 1 minute to read.'

def test_one_minute():
    assert time_estimation(text_200) == 'This text will take you approximately 1 minute to read.'

def test_minutes():
    assert time_estimation(text_200*2) == 'This text will take you approximately 2 minutes to read.'

def test_minutes_round_up():
    assert time_estimation(text_200*58) == "This text will take you approximately 1 hour to read."

def test_hour():
    assert time_estimation(text_200*60) == "This text will take you approximately 1 hour to read."

def test_hour_and_minutes():
    assert time_estimation(text_200*110) == "This text will take you approximately 1 hour and 50 minutes to read."

def test_hour_round_up():
    assert time_estimation(text_200*118) == "This text will take you approximately 2 hours to read."

def test_hours_few_mins():
    assert time_estimation(text_200*122) == "This text will take you approximately 2 hours to read."

def test_hours_and_mins():
    assert time_estimation(text_200*221) == "This text will take you approximately 3 hours and 41 minutes to read."

def test_hours_round_up():
    assert time_estimation(text_200*298) == "This text will take you approximately 5 hours to read."

def test_wrong_input():
    with pytest.raises(Exception) as e:
        time_estimation(823.9) #should throw exception
    error_message = str(e.value)
    assert error_message == "I can only check strings, sorry!"