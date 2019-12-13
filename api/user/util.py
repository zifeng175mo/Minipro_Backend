from user.models import User, Dynamics, DynamicsPicture, Comment, Gone
from province.models import Province


def get_page(query, page: int, page_size: int = 3) -> (all, int):
    page = int(page)
    total_page = len(query) / page_size
    if total_page % 1 > 0:
        # 如果未填满一页的条, 按一页算
        total_page += 1
    total_page = int(total_page)
    if page + 1 > total_page:
        # 如果页数过多, 返回空的queryset
        return query[0:0], total_page
        # 如果页数正常, 返回结果
    return query[page * page_size: (page + 1) * page_size], total_page


def judge_allgone(user):
    num = Gone.objects.filter(user=user, gone=True).count()
    total_num = Gone.objects.filter(user=user).count()
    if num == total_num:
        return True
    else:
        return False
