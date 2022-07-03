from copy import copy


def params(request):
    get_params = request.GET
    if 'page' in get_params:
        get_params = copy(get_params)
        del get_params['page']

    return {'params': f'&{get_params.urlencode()}' if get_params else ''}
