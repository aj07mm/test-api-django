from rest_framework import pagination, response


class BasePaginator(pagination.PageNumberPagination):
    page_query_param = 'page'
    page_size_query_param = 'page_size'
    page_size = 50
    max_page_size = 1000

    def get_paginated_response(self, data):
        return response.Response(
            {
                'results': data,
                'page': self.page.number,
                'per_page': self.page.paginator.per_page,
                'num_pages': self.page.paginator.num_pages,
                'count': self.page.paginator.count,
                'has_previous': self.page.has_previous(),
                'has_next': self.page.has_next(),
            }
        )
