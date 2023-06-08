# Есть маркер @pytest.mark.id_check(1, 2, 3), нужно вывести на печать, то что в него передано
#
# >>> 1, 2, 3

import pytest


@pytest.mark.id_check(1, 2, 3)
def test(request):
    # Здесь пишем код
    my_mark = request.node.get_closest_marker("id_check")
    args = my_mark.args
    print(args)
