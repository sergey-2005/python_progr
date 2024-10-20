# TODO Найдите количество книг, которое можно разместить на дискете
full_V = 1.44 * (1024 ** 2)
pages_in_book = 100
strings_in_page = 50
sim_in_string = 25
bytes_for_sim = 4
print("Количество книг, помещающихся на дискету:", int((full_V//(pages_in_book * strings_in_page * sim_in_string * bytes_for_sim))))
