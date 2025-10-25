from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response_405 import ErrorResponse405
from ...models.error_response_406 import ErrorResponse406
from ...models.error_response_415 import ErrorResponse415
from ...models.error_response_500 import ErrorResponse500
from ...models.parse_error_response import ParseErrorResponse
from ...models.token_refresh import TokenRefresh
from ...models.token_refresh_create_validation_error import TokenRefreshCreateValidationError
from ...models.token_refresh_request import TokenRefreshRequest
from ...types import Response


def _get_kwargs(
    *,
    body: Union[
        TokenRefreshRequest,
        TokenRefreshRequest,
        TokenRefreshRequest,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/core/token/refresh/",
    }

    if isinstance(body, TokenRefreshRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, TokenRefreshRequest):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, TokenRefreshRequest):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        ErrorResponse405,
        ErrorResponse406,
        ErrorResponse415,
        ErrorResponse500,
        TokenRefresh,
        Union["ParseErrorResponse", "TokenRefreshCreateValidationError"],
    ]
]:
    if response.status_code == 400:

        def _parse_response_400(data: object) -> Union["ParseErrorResponse", "TokenRefreshCreateValidationError"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_token_refresh_create_error_response_400_type_0 = (
                    TokenRefreshCreateValidationError.from_dict(data)
                )

                return componentsschemas_token_refresh_create_error_response_400_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_token_refresh_create_error_response_400_type_1 = ParseErrorResponse.from_dict(data)

            return componentsschemas_token_refresh_create_error_response_400_type_1

        response_400 = _parse_response_400(response.json())

        return response_400
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
        response_200 = TokenRefresh.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        ErrorResponse405,
        ErrorResponse406,
        ErrorResponse415,
        ErrorResponse500,
        TokenRefresh,
        Union["ParseErrorResponse", "TokenRefreshCreateValidationError"],
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
    client: Union[AuthenticatedClient, Client],
    body: Union[
        TokenRefreshRequest,
        TokenRefreshRequest,
        TokenRefreshRequest,
    ],
) -> Response[
    Union[
        ErrorResponse405,
        ErrorResponse406,
        ErrorResponse415,
        ErrorResponse500,
        TokenRefresh,
        Union["ParseErrorResponse", "TokenRefreshCreateValidationError"],
    ]
]:
    """Takes a refresh type JSON web token and returns an access type JSON web
    token if the refresh token is valid.

    Args:
        body (TokenRefreshRequest):
        body (TokenRefreshRequest):
        body (TokenRefreshRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse405, ErrorResponse406, ErrorResponse415, ErrorResponse500, TokenRefresh, Union['ParseErrorResponse', 'TokenRefreshCreateValidationError']]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        TokenRefreshRequest,
        TokenRefreshRequest,
        TokenRefreshRequest,
    ],
) -> Optional[
    Union[
        ErrorResponse405,
        ErrorResponse406,
        ErrorResponse415,
        ErrorResponse500,
        TokenRefresh,
        Union["ParseErrorResponse", "TokenRefreshCreateValidationError"],
    ]
]:
    """Takes a refresh type JSON web token and returns an access type JSON web
    token if the refresh token is valid.

    Args:
        body (TokenRefreshRequest):
        body (TokenRefreshRequest):
        body (TokenRefreshRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse405, ErrorResponse406, ErrorResponse415, ErrorResponse500, TokenRefresh, Union['ParseErrorResponse', 'TokenRefreshCreateValidationError']]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        TokenRefreshRequest,
        TokenRefreshRequest,
        TokenRefreshRequest,
    ],
) -> Response[
    Union[
        ErrorResponse405,
        ErrorResponse406,
        ErrorResponse415,
        ErrorResponse500,
        TokenRefresh,
        Union["ParseErrorResponse", "TokenRefreshCreateValidationError"],
    ]
]:
    """Takes a refresh type JSON web token and returns an access type JSON web
    token if the refresh token is valid.

    Args:
        body (TokenRefreshRequest):
        body (TokenRefreshRequest):
        body (TokenRefreshRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse405, ErrorResponse406, ErrorResponse415, ErrorResponse500, TokenRefresh, Union['ParseErrorResponse', 'TokenRefreshCreateValidationError']]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        TokenRefreshRequest,
        TokenRefreshRequest,
        TokenRefreshRequest,
    ],
) -> Optional[
    Union[
        ErrorResponse405,
        ErrorResponse406,
        ErrorResponse415,
        ErrorResponse500,
        TokenRefresh,
        Union["ParseErrorResponse", "TokenRefreshCreateValidationError"],
    ]
]:
    """Takes a refresh type JSON web token and returns an access type JSON web
    token if the refresh token is valid.

    Args:
        body (TokenRefreshRequest):
        body (TokenRefreshRequest):
        body (TokenRefreshRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse405, ErrorResponse406, ErrorResponse415, ErrorResponse500, TokenRefresh, Union['ParseErrorResponse', 'TokenRefreshCreateValidationError']]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
