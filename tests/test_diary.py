from lib.diary import *

# def test_make_snippet_over_5():
#     result = make_snippet('Here is a more verbose string, containing more than 5 words.')
#     assert result == 'Here is a more verbose...'

# def test_make_snippet_under_5():
#     result = make_snippet('A few words.')
#     assert result == 'A few words.'

# def test_make_snippet_5_words():
#     result = make_snippet('A string with five words.')
#     assert result == 'A string with five words.'

# def test_make_snippet_empty_string():
#     result = make_snippet('')
#     assert result == ''

# def test_count_words_normal():
#     result = count_words('A string with five words.')
#     assert result == 5

# def test_count_words_empty():
#     result = count_words('')
#     assert result == 0
good_entry_100 = Diary_Entry('Here is some lovely Lorem Ipsum text', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc in ullamcorper tortor, non egestas sapien. Nulla sagittis sodales est, et commodo tellus. Nulla placerat vestibulum efficitur. Nam quis diam ut nibh placerat porta in ac lorem. Sed varius placerat massa a gravida. Phasellus eget justo sollicitudin, pulvinar ligula vitae, pretium diam. Suspendisse suscipit viverra finibus. Proin pretium convallis arcu eu iaculis. In in efficitur nisi. Proin lacinia magna quis turpis fringilla placerat. Curabitur auctor orci orci, eu tincidunt est ultricies at. Fusce pharetra, turpis non sagittis placerat, odio sapien sodales enim, ut placerat velit ex ac purus. In in enim.')

good_entry_200 = Diary_Entry('A day in my life', 'A day in my life is sometimes very boring and requires much typing, so here is some filler text: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus feugiat lacus eget lectus gravida, non dignissim dui bibendum. Nam pulvinar turpis pharetra est rutrum, eu scelerisque magna fermentum. Nulla vulputate congue volutpat. Sed ac turpis a leo pellentesque sollicitudin. Aliquam tortor nulla, vestibulum sed vestibulum et, consequat sed lacus. Quisque fermentum mauris sed laoreet rhoncus. Mauris pretium non leo in convallis. Maecenas eget magna mattis, suscipit erat at, facilisis ante. Suspendisse fermentum magna neque, eget commodo risus rhoncus vitae. Ut tellus augue, interdum et semper id, tempor vitae diam. Ut malesuada, eros in fringilla pulvinar, ipsum elit vulputate tellus, faucibus porta ipsum diam eget velit. Fusce cursus maximus purus blandit faucibus. Suspendisse vel consequat dolor. Maecenas ac neque arcu. Vivamus pretium molestie metus sit amet ornare. In ac nisl sed tortor hendrerit dictum vitae rhoncus nulla. Nunc auctor felis id urna tincidunt, nec dignissim ante semper. Duis viverra, justo ac accumsan iaculis, justo odio mattis nisl, eget porta arcu nisl egestas mi. Proin dui libero, sagittis iaculis ex quis, tincidunt viverra purus. Maecenas pulvinar auctor ipsum, a vulputate libero viverra vel. Quisque convallis ex volutpat enim. Phasellus a porta enim. Suspendisse ullamcorper maximus arcu, ac ultricies turpis pulvinar Fusce congue.')

def test_new_entry_format():
    assert good_entry_200.format() == 'A Day In My Life:  A day in my life is sometimes very boring and requires much typing, so here is some filler text: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus feugiat lacus eget lectus gravida, non dignissim dui bibendum. Nam pulvinar turpis pharetra est rutrum, eu scelerisque magna fermentum. Nulla vulputate congue volutpat. Sed ac turpis a leo pellentesque sollicitudin. Aliquam tortor nulla, vestibulum sed vestibulum et, consequat sed lacus. Quisque fermentum mauris sed laoreet rhoncus. Mauris pretium non leo in convallis. Maecenas eget magna mattis, suscipit erat at, facilisis ante. Suspendisse fermentum magna neque, eget commodo risus rhoncus vitae. Ut tellus augue, interdum et semper id, tempor vitae diam. Ut malesuada, eros in fringilla pulvinar, ipsum elit vulputate tellus, faucibus porta ipsum diam eget velit. Fusce cursus maximus purus blandit faucibus. Suspendisse vel consequat dolor. Maecenas ac neque arcu. Vivamus pretium molestie metus sit amet ornare. In ac nisl sed tortor hendrerit dictum vitae rhoncus nulla. Nunc auctor felis id urna tincidunt, nec dignissim ante semper. Duis viverra, justo ac accumsan iaculis, justo odio mattis nisl, eget porta arcu nisl egestas mi. Proin dui libero, sagittis iaculis ex quis, tincidunt viverra purus. Maecenas pulvinar auctor ipsum, a vulputate libero viverra vel. Quisque convallis ex volutpat enim. Phasellus a porta enim. Suspendisse ullamcorper maximus arcu, ac ultricies turpis pulvinar Fusce congue.'

def test_reading_time():
    assert good_entry_200.reading_time(200) == 1

def test_reading_chunk_short():
    assert good_entry_200.reading_chunk(50, 1) == 'A day in my life is sometimes very boring and requires much typing, so here is some filler text: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus feugiat lacus eget lectus gravida, non dignissim dui bibendum. Nam pulvinar turpis pharetra est rutrum, eu scelerisque magna fermentum. Nulla vulputate congue...'

def test_reading_chunk_long():
    assert good_entry_100.reading_chunk(200, 1) == 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc in ullamcorper tortor, non egestas sapien. Nulla sagittis sodales est, et commodo tellus. Nulla placerat vestibulum efficitur. Nam quis diam ut nibh placerat porta in ac lorem. Sed varius placerat massa a gravida. Phasellus eget justo sollicitudin, pulvinar ligula vitae, pretium diam. Suspendisse suscipit viverra finibus. Proin pretium convallis arcu eu iaculis. In in efficitur nisi. Proin lacinia magna quis turpis fringilla placerat. Curabitur auctor orci orci, eu tincidunt est ultricies at. Fusce pharetra, turpis non sagittis placerat, odio sapien sodales enim, ut placerat velit ex ac purus. In in enim.'

def test_reading_chunk_continuation():
    assert good_entry_200.reading_chunk(10, 1) == 'volutpat. Sed ac turpis a leo pellentesque sollicitudin. Aliquam tortor...'
