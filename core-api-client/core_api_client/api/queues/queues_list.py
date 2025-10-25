from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response_401 import ErrorResponse401
from ...models.error_response_403 import ErrorResponse403
from ...models.error_response_405 import ErrorResponse405
from ...models.error_response_406 import ErrorResponse406
from ...models.error_response_415 import ErrorResponse415
from ...models.error_response_500 import ErrorResponse500
from ...models.parse_error_response import ParseErrorResponse
from ...models.queue import Queue
from ...models.queues_list_validation_error import QueuesListValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    class_id: Union[Unset, int] = UNSET,
    mentor_id: Union[Unset, int] = UNSET,
    module: Union[Unset, int] = UNSET,
    module_isnull: Union[Unset, bool] = UNSET,
    program_id_in: Union[Unset, list[int]] = UNSET,
    user: Union[Unset, int] = UNSET,
    user_isnull: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["class__id"] = class_id

    params["mentor__id"] = mentor_id

    params["module"] = module

    params["module__isnull"] = module_isnull

    json_program_id_in: Union[Unset, list[int]] = UNSET
    if not isinstance(program_id_in, Unset):
        json_program_id_in = program_id_in

    params["program__id__in"] = json_program_id_in

    params["user"] = user

    params["user__isnull"] = user_isnull

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/core/queues/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        ErrorResponse401,
        ErrorResponse403,
        ErrorResponse405,
        ErrorResponse406,
        ErrorResponse415,
        ErrorResponse500,
        Union["ParseErrorResponse", "QueuesListValidationError"],
        list["Queue"],
    ]
]:
    if response.status_code == 400:

        def _parse_response_400(data: object) -> Union["ParseErrorResponse", "QueuesListValidationError"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_queues_list_error_response_400_type_0 = QueuesListValidationError.from_dict(data)

                return componentsschemas_queues_list_error_response_400_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_queues_list_error_response_400_type_1 = ParseErrorResponse.from_dict(data)

            return componentsschemas_queues_list_error_response_400_type_1

        response_400 = _parse_response_400(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = ErrorResponse401.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = ErrorResponse403.from_dict(response.json())

        return response_403
    if response.status_code == 405:
        response_405 = ErrorResponse405.from_dict(response.json())

        return response_405
    if response.status_code == 406:
        response_406 = ErrorResponse406.from_dict(response.json())

        return response_406
    if response.status_code == 415:
        response_415 = ErrorResponse415.from_dict(response.json())

        return response_415
    if response.status_code == 500:
        response_500 = ErrorResponse500.from_dict(response.json())

        return response_500
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Queue.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        ErrorResponse401,
        ErrorResponse403,
        ErrorResponse405,
        ErrorResponse406,
        ErrorResponse415,
        ErrorResponse500,
        Union["ParseErrorResponse", "QueuesListValidationError"],
        list["Queue"],
    ]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    class_id: Union[Unset, int] = UNSET,
    mentor_id: Union[Unset, int] = UNSET,
    module: Union[Unset, int] = UNSET,
    module_isnull: Union[Unset, bool] = UNSET,
    program_id_in: Union[Unset, list[int]] = UNSET,
    user: Union[Unset, int] = UNSET,
    user_isnull: Union[Unset, bool] = UNSET,
) -> Response[
    Union[
        ErrorResponse401,
        ErrorResponse403,
        ErrorResponse405,
        ErrorResponse406,
        ErrorResponse415,
        ErrorResponse500,
        Union["ParseErrorResponse", "QueuesListValidationError"],
        list["Queue"],
    ]
]:
    """Queues.

    Args:
        class_id (Union[Unset, int]):
        mentor_id (Union[Unset, int]):
        module (Union[Unset, int]):
        module_isnull (Union[Unset, bool]):
        program_id_in (Union[Unset, list[int]]):
        user (Union[Unset, int]):
        user_isnull (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse401, ErrorResponse403, ErrorResponse405, ErrorResponse406, ErrorResponse415, ErrorResponse500, Union['ParseErrorResponse', 'QueuesListValidationError'], list['Queue']]]
    """

    kwargs = _get_kwargs(
        class_id=class_id,
        mentor_id=mentor_id,
        module=module,
        module_isnull=module_isnull,
        program_id_in=program_id_in,
        user=user,
        user_isnull=user_isnull,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    class_id: Union[Unset, int] = UNSET,
    mentor_id: Union[Unset, int] = UNSET,
    module: Union[Unset, int] = UNSET,
    module_isnull: Union[Unset, bool] = UNSET,
    program_id_in: Union[Unset, list[int]] = UNSET,
    user: Union[Unset, int] = UNSET,
    user_isnull: Union[Unset, bool] = UNSET,
) -> Optional[
    Union[
        ErrorResponse401,
        ErrorResponse403,
        ErrorResponse405,
        ErrorResponse406,
        ErrorResponse415,
        ErrorResponse500,
        Union["ParseErrorResponse", "QueuesListValidationError"],
        list["Queue"],
    ]
]:
    """Queues.

    Args:
        class_id (Union[Unset, int]):
        mentor_id (Union[Unset, int]):
        module (Union[Unset, int]):
        module_isnull (Union[Unset, bool]):
        program_id_in (Union[Unset, list[int]]):
        user (Union[Unset, int]):
        user_isnull (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse401, ErrorResponse403, ErrorResponse405, ErrorResponse406, ErrorResponse415, ErrorResponse500, Union['ParseErrorResponse', 'QueuesListValidationError'], list['Queue']]
    """

    return sync_detailed(
        client=client,
        class_id=class_id,
        mentor_id=mentor_id,
        module=module,
        module_isnull=module_isnull,
        program_id_in=program_id_in,
        user=user,
        user_isnull=user_isnull,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    class_id: Union[Unset, int] = UNSET,
    mentor_id: Union[Unset, int] = UNSET,
    module: Union[Unset, int] = UNSET,
    module_isnull: Union[Unset, bool] = UNSET,
    program_id_in: Union[Unset, list[int]] = UNSET,
    user: Union[Unset, int] = UNSET,
    user_isnull: Union[Unset, bool] = UNSET,
) -> Response[
    Union[
        ErrorResponse401,
        ErrorResponse403,
        ErrorResponse405,
        ErrorResponse406,
        ErrorResponse415,
        ErrorResponse500,
        Union["ParseErrorResponse", "QueuesListValidationError"],
        list["Queue"],
    ]
]:
    """Queues.

    Args:
        class_id (Union[Unset, int]):
        mentor_id (Union[Unset, int]):
        module (Union[Unset, int]):
        module_isnull (Union[Unset, bool]):
        program_id_in (Union[Unset, list[int]]):
        user (Union[Unset, int]):
        user_isnull (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse401, ErrorResponse403, ErrorResponse405, ErrorResponse406, ErrorResponse415, ErrorResponse500, Union['ParseErrorResponse', 'QueuesListValidationError'], list['Queue']]]
    """

    kwargs = _get_kwargs(
        class_id=class_id,
        mentor_id=mentor_id,
        module=module,
        module_isnull=module_isnull,
        program_id_in=program_id_in,
        user=user,
        user_isnull=user_isnull,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    class_id: Union[Unset, int] = UNSET,
    mentor_id: Union[Unset, int] = UNSET,
    module: Union[Unset, int] = UNSET,
    module_isnull: Union[Unset, bool] = UNSET,
    program_id_in: Union[Unset, list[int]] = UNSET,
    user: Union[Unset, int] = UNSET,
    user_isnull: Union[Unset, bool] = UNSET,
) -> Optional[
    Union[
        ErrorResponse401,
        ErrorResponse403,
        ErrorResponse405,
        ErrorResponse406,
        ErrorResponse415,
        ErrorResponse500,
        Union["ParseErrorResponse", "QueuesListValidationError"],
        list["Queue"],
    ]
]:
    """Queues.

    Args:
        class_id (Union[Unset, int]):
        mentor_id (Union[Unset, int]):
        module (Union[Unset, int]):
        module_isnull (Union[Unset, bool]):
        program_id_in (Union[Unset, list[int]]):
        user (Union[Unset, int]):
        user_isnull (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse401, ErrorResponse403, ErrorResponse405, ErrorResponse406, ErrorResponse415, ErrorResponse500, Union['ParseErrorResponse', 'QueuesListValidationError'], list['Queue']]
    """

    return (
        await asyncio_detailed(
            client=client,
            class_id=class_id,
            mentor_id=mentor_id,
            module=module,
            module_isnull=module_isnull,
            program_id_in=program_id_in,
            user=user,
            user_isnull=user_isnull,
        )
    ).parsed
