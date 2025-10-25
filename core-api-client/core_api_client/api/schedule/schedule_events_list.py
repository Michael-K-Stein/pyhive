import datetime
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
from ...models.event import Event
from ...models.parse_error_response import ParseErrorResponse
from ...models.schedule_events_list_validation_error import ScheduleEventsListValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    end_lte: Union[Unset, datetime.datetime] = UNSET,
    lesson_id: Union[Unset, int] = UNSET,
    start_gte: Union[Unset, datetime.datetime] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_end_lte: Union[Unset, str] = UNSET
    if not isinstance(end_lte, Unset):
        json_end_lte = end_lte.isoformat()
    params["end__lte"] = json_end_lte

    params["lesson__id"] = lesson_id

    json_start_gte: Union[Unset, str] = UNSET
    if not isinstance(start_gte, Unset):
        json_start_gte = start_gte.isoformat()
    params["start__gte"] = json_start_gte

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/core/schedule/events/",
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
        Union["ParseErrorResponse", "ScheduleEventsListValidationError"],
        list["Event"],
    ]
]:
    if response.status_code == 400:

        def _parse_response_400(data: object) -> Union["ParseErrorResponse", "ScheduleEventsListValidationError"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_schedule_events_list_error_response_400_type_0 = (
                    ScheduleEventsListValidationError.from_dict(data)
                )

                return componentsschemas_schedule_events_list_error_response_400_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_schedule_events_list_error_response_400_type_1 = ParseErrorResponse.from_dict(data)

            return componentsschemas_schedule_events_list_error_response_400_type_1

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
            response_200_item = Event.from_dict(response_200_item_data)

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
        Union["ParseErrorResponse", "ScheduleEventsListValidationError"],
        list["Event"],
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
    end_lte: Union[Unset, datetime.datetime] = UNSET,
    lesson_id: Union[Unset, int] = UNSET,
    start_gte: Union[Unset, datetime.datetime] = UNSET,
) -> Response[
    Union[
        ErrorResponse401,
        ErrorResponse403,
        ErrorResponse405,
        ErrorResponse406,
        ErrorResponse415,
        ErrorResponse500,
        Union["ParseErrorResponse", "ScheduleEventsListValidationError"],
        list["Event"],
    ]
]:
    """Events

    Args:
        end_lte (Union[Unset, datetime.datetime]):
        lesson_id (Union[Unset, int]):
        start_gte (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse401, ErrorResponse403, ErrorResponse405, ErrorResponse406, ErrorResponse415, ErrorResponse500, Union['ParseErrorResponse', 'ScheduleEventsListValidationError'], list['Event']]]
    """

    kwargs = _get_kwargs(
        end_lte=end_lte,
        lesson_id=lesson_id,
        start_gte=start_gte,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    end_lte: Union[Unset, datetime.datetime] = UNSET,
    lesson_id: Union[Unset, int] = UNSET,
    start_gte: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[
    Union[
        ErrorResponse401,
        ErrorResponse403,
        ErrorResponse405,
        ErrorResponse406,
        ErrorResponse415,
        ErrorResponse500,
        Union["ParseErrorResponse", "ScheduleEventsListValidationError"],
        list["Event"],
    ]
]:
    """Events

    Args:
        end_lte (Union[Unset, datetime.datetime]):
        lesson_id (Union[Unset, int]):
        start_gte (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse401, ErrorResponse403, ErrorResponse405, ErrorResponse406, ErrorResponse415, ErrorResponse500, Union['ParseErrorResponse', 'ScheduleEventsListValidationError'], list['Event']]
    """

    return sync_detailed(
        client=client,
        end_lte=end_lte,
        lesson_id=lesson_id,
        start_gte=start_gte,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    end_lte: Union[Unset, datetime.datetime] = UNSET,
    lesson_id: Union[Unset, int] = UNSET,
    start_gte: Union[Unset, datetime.datetime] = UNSET,
) -> Response[
    Union[
        ErrorResponse401,
        ErrorResponse403,
        ErrorResponse405,
        ErrorResponse406,
        ErrorResponse415,
        ErrorResponse500,
        Union["ParseErrorResponse", "ScheduleEventsListValidationError"],
        list["Event"],
    ]
]:
    """Events

    Args:
        end_lte (Union[Unset, datetime.datetime]):
        lesson_id (Union[Unset, int]):
        start_gte (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse401, ErrorResponse403, ErrorResponse405, ErrorResponse406, ErrorResponse415, ErrorResponse500, Union['ParseErrorResponse', 'ScheduleEventsListValidationError'], list['Event']]]
    """

    kwargs = _get_kwargs(
        end_lte=end_lte,
        lesson_id=lesson_id,
        start_gte=start_gte,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    end_lte: Union[Unset, datetime.datetime] = UNSET,
    lesson_id: Union[Unset, int] = UNSET,
    start_gte: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[
    Union[
        ErrorResponse401,
        ErrorResponse403,
        ErrorResponse405,
        ErrorResponse406,
        ErrorResponse415,
        ErrorResponse500,
        Union["ParseErrorResponse", "ScheduleEventsListValidationError"],
        list["Event"],
    ]
]:
    """Events

    Args:
        end_lte (Union[Unset, datetime.datetime]):
        lesson_id (Union[Unset, int]):
        start_gte (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse401, ErrorResponse403, ErrorResponse405, ErrorResponse406, ErrorResponse415, ErrorResponse500, Union['ParseErrorResponse', 'ScheduleEventsListValidationError'], list['Event']]
    """

    return (
        await asyncio_detailed(
            client=client,
            end_lte=end_lte,
            lesson_id=lesson_id,
            start_gte=start_gte,
        )
    ).parsed
