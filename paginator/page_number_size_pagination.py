from rest_framework.pagination import PageNumberPagination

class PageNumberSizePagination( PageNumberPagination ):
    page_size_query_param = 'size'
    max_page_size = 100